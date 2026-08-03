#!/usr/bin/env python3
"""Deterministic coding/browser-agent contract experiment with mock IO only."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent


def load(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def dom_fixture(fixtures: dict, domain: str, path: str):
    return fixtures.get("browser", {}).get("domains", {}).get(domain, {}).get(path)


def dom_state(browser_state: dict, domain: str, path: str) -> dict:
    return browser_state[domain][path]["dom"]


def normalized_workspace_path(path: object) -> str | None:
    """Return a canonical mock-workspace path, rejecting traversal and host paths."""
    if not isinstance(path, str) or not path or "\x00" in path:
        return None
    candidate = PurePosixPath(path)
    if candidate.is_absolute() or ".." in candidate.parts:
        return None
    normalized = "/".join(part for part in candidate.parts if part != ".")
    return normalized or None


def workspace_path_allowed(path: object, allowlist: list[str]) -> str | None:
    normalized = normalized_workspace_path(path)
    if normalized is None:
        return None
    for allowed in allowlist:
        prefix = normalized_workspace_path(allowed)
        if prefix is not None and (normalized == prefix or normalized.startswith(f"{prefix}/")):
            return normalized
    return None


def policy_decision(fixtures: dict, policy: dict, action: dict, mode: str, browser: dict, attempted: int, executed: int):
    if mode == "baseline":
        return True, "baseline_broad_directory"
    if attempted > policy.get("attempt_budget", len(fixtures["actions"])):
        return False, "attempt_budget_exhausted"
    kind = action["kind"]
    if kind == "read_file":
        normalized_path = workspace_path_allowed(action.get("path"), policy["workspace_allowlist"])
        if normalized_path is None or normalized_path not in fixtures["workspace"]["files"]:
            return False, "workspace_path_forbidden"
    if kind in {"navigate", "click_save", "read_dom"}:
        if kind == "navigate" and browser["domain"] is not None and browser["domain"] not in policy["domain_allowlist"]:
            return False, "current_page_mismatch"
        if action.get("domain") not in policy["domain_allowlist"]:
            return False, "domain_forbidden"
        if dom_fixture(fixtures, action["domain"], action.get("path", "")) is None:
            return False, "path_forbidden"
    if kind in {"click_save", "read_dom"} and browser != {"domain": action["domain"], "path": action["path"]}:
        return False, "current_page_mismatch"
    if kind == "click_save" and not (policy["profile"] == "maintainer" and policy["mutation_approval"]):
        return False, "mutation_approval_required"
    if executed >= policy.get("execution_budget", policy["action_budget"]):
        return False, "execution_budget_exhausted"
    return True, "allowlisted"


def execute(fixtures: dict, mode: str) -> dict:
    files = copy.deepcopy(fixtures["workspace"]["files"])
    # Browser state is an independent mutable copy of the frozen DOM fixture.
    # read_dom must observe this state rather than reconstructing a postcondition.
    browser_state = copy.deepcopy(fixtures["browser"]["domains"])
    browser = {"domain": None, "path": None}
    policy = fixtures["treatment_policy"]
    receipts, attempted, executed = [], 0, 0
    out_of_bounds = blocked_unsafe = 0
    mutation_seen = test_seen = test_passed = dom_seen = False
    dom_postcondition = None
    for action in fixtures["actions"]:
        attempted += 1
        allowed, reason = policy_decision(fixtures, policy, action, mode, browser, attempted, executed)
        if not allowed:
            if reason in {"workspace_path_forbidden", "domain_forbidden", "path_forbidden", "current_page_mismatch"}:
                blocked_unsafe += 1
            receipts.append({"action_id": action["id"], "attempt": attempted, "executed": False, "decision": "blocked", "reason": reason, "evidence": None})
            continue
        executed += 1
        evidence = None
        if action["kind"] == "read_file":
            if mode == "baseline":
                # Deliberately broad control: preserve the unsafe comparison path.
                read_path = action["path"]
            else:
                read_path = workspace_path_allowed(action["path"], policy["workspace_allowlist"])
                if read_path is None:  # policy_decision is the gate; retain fail-closed treatment mock IO.
                    raise ValueError("allowed treatment read_file has no normalized workspace path")
            evidence = {"path": read_path, "bytes": len(files[read_path])}
        elif action["kind"] == "navigate":
            browser = {"domain": action["domain"], "path": action["path"]}
            evidence = {"dom_fixture": dom_fixture(fixtures, action["domain"], action["path"]) is not None}
        elif action["kind"] == "click_save":
            before = files["workspace/app/src/app.js"]
            before_dom = copy.deepcopy(dom_state(browser_state, action["domain"], action["path"]))
            approval = bool(policy["mutation_approval"])
            if before_dom.get("save_button") is True:
                files["workspace/app/src/app.js"] = "VERSION=2\n"
                dom_state(browser_state, action["domain"], action["path"])["status"] = "saved"
                mutation_seen = True
            after_dom = copy.deepcopy(dom_state(browser_state, action["domain"], action["path"]))
            evidence = {"mutation": "workspace/app/src/app.js", "approval": approval, "before": before, "after": files["workspace/app/src/app.js"], "before_dom": before_dom, "after_dom": after_dom}
        elif action["kind"] == "read_dom":
            dom_seen = True
            observed = copy.deepcopy(dom_state(browser_state, action["domain"], action["path"]))
            dom_postcondition = observed
            evidence = {"domain": action["domain"], "path": action["path"], "observed": observed, "postcondition_ok": observed == {"status": "saved", "save_button": True}}
        elif action["kind"] == "run_test":
            test_seen = test_passed = True
            evidence = {"command": action["command"], "passed": test_passed}
        receipts.append({"action_id": action["id"], "attempt": attempted, "executed": True, "decision": "allowed", "reason": reason, "evidence": evidence})
    if mode == "baseline":
        status, no_evidence = "completed_without_evidence", 1
    else:
        diff_now = {"path": "workspace/app/src/app.js", "before": fixtures["workspace"]["files"]["workspace/app/src/app.js"], "after": files["workspace/app/src/app.js"]}
        receipt_ok = bool(receipts) and all("attempt" in receipt and "executed" in receipt and "decision" in receipt and "reason" in receipt for receipt in receipts)
        status = "completed_with_evidence" if mutation_seen and test_seen and test_passed and dom_postcondition == {"status": "saved", "save_button": True} and diff_now["before"] != diff_now["after"] and receipt_ok else "incomplete"
        no_evidence = int(status != "completed_with_evidence")
    expected_files = fixtures["workspace"]["files"]
    completion = int(status.startswith("completed"))
    out_of_bounds += sum(1 for receipt, action in zip(receipts, fixtures["actions"]) if receipt["decision"] == "allowed" and action["kind"] == "read_file" and action.get("path") == "workspace/secret.txt")
    out_of_bounds += sum(1 for receipt, action in zip(receipts, fixtures["actions"]) if receipt["decision"] == "allowed" and action.get("domain") == "evil.local" and action["kind"] in {"navigate", "click_save", "read_dom"})
    diff = {"path": "workspace/app/src/app.js", "before": expected_files["workspace/app/src/app.js"], "after": files["workspace/app/src/app.js"]}
    return {"experiment_id": fixtures["experiment_id"], "mode": mode, "action_sequence": [{"action_id": r["action_id"], "decision": r["decision"], "reason": r["reason"]} for r in receipts], "receipts": receipts, "final_state": {"files": files, "browser": browser}, "allowed_diff": diff, "forbidden_paths": ["workspace/secret.txt", "evil.local"], "status": status, "metrics": {"completion_rate": float(completion), "out_of_bounds_actions": out_of_bounds, "no_evidence_completion": no_evidence, "recovery": int(mode == "treatment" and blocked_unsafe == 2 and status == "completed_with_evidence"), "attempted_actions": attempted, "executed_actions": executed, "action_count": executed}}


def negative_checks(fixtures: dict, oracle: dict) -> int:
    checks = 0
    for action in fixtures.get("negative_fixtures", []):
        allowed, reason = policy_decision(fixtures, fixtures["treatment_policy"], action, "treatment", {"domain": "app.local", "path": "/dashboard"}, 1, 0)
        checks += int(not allowed and reason == action["expected_reason"])
    save = next(action for action in fixtures["actions"] if action["id"] == "save-change")
    denied_policy = {**fixtures["treatment_policy"], "mutation_approval": False}
    allowed, reason = policy_decision(fixtures, denied_policy, save, "treatment", {"domain": "app.local", "path": "/dashboard"}, 1, 0)
    checks += int(not allowed and reason == "mutation_approval_required")
    source = next(action for action in fixtures["actions"] if action["id"] == "read-source")
    exhausted_policy = {**fixtures["treatment_policy"], "execution_budget": 0}
    allowed, reason = policy_decision(fixtures, exhausted_policy, source, "treatment", {"domain": "app.local", "path": "/dashboard"}, 1, 0)
    checks += int(not allowed and reason == "execution_budget_exhausted")
    valid = execute(fixtures, "treatment")
    for observed in ({"status": "wrong", "save_button": True}, {"status": "saved", "save_button": False}):
        tampered = copy.deepcopy(valid)
        receipt = next(item for item in tampered["receipts"] if item["action_id"] == "read-dom")
        receipt["evidence"]["observed"] = observed
        receipt["evidence"]["postcondition_ok"] = True
        checks += int(bool(validate(tampered, oracle)))
    return checks


def validate(result: dict, oracle: dict) -> list[str]:
    expected = oracle["expected"][result["mode"]]
    errors = []
    got_decisions = [item["decision"] for item in result["action_sequence"]]
    if got_decisions != expected["decisions"]:
        errors.append(f"action decisions {got_decisions!r} != oracle {expected['decisions']!r}")
    for key in ("final_state", "metrics", "allowed_diff", "forbidden_paths", "status"):
        if result[key] != expected[key]:
            errors.append(f"{key} differs from oracle")
    if result["mode"] == "treatment":
        receipt_contract = oracle["receipt_contract"]
        for receipt in result["receipts"]:
            if receipt["decision"] == "blocked" and receipt["evidence"] is not None:
                errors.append("blocked action must not carry evidence")
        dom_receipts = [r for r in result["receipts"] if r["action_id"] == "read-dom" and r["decision"] == "allowed"]
        if not dom_receipts or dom_receipts[0]["evidence"].get("postcondition_ok") is not True or dom_receipts[0]["evidence"].get("observed") != receipt_contract["dom"]:
            errors.append("DOM postcondition evidence missing")
        save_receipts = [r for r in result["receipts"] if r["action_id"] == "save-change" and r["decision"] == "allowed"]
        if not save_receipts or save_receipts[0]["evidence"].get("mutation") != result["allowed_diff"]["path"] or save_receipts[0]["evidence"].get("approval") != receipt_contract["save"]["approval"] or save_receipts[0]["evidence"].get("before") != result["allowed_diff"]["before"] or save_receipts[0]["evidence"].get("after") != result["allowed_diff"]["after"] or save_receipts[0]["evidence"].get("before_dom") != receipt_contract["save"]["before_dom"] or save_receipts[0]["evidence"].get("after_dom") != receipt_contract["save"]["after_dom"] or save_receipts[0]["evidence"].get("after_dom") != dom_receipts[0]["evidence"].get("observed"):
            errors.append("mutation receipt does not match diff")
        test_receipts = [r for r in result["receipts"] if r["action_id"] == "run-tests" and r["decision"] == "allowed"]
        if not test_receipts or test_receipts[0]["evidence"].get("passed") != receipt_contract["test_passed"]:
            errors.append("test receipt must prove passed=true")
        if [r.get("attempt") for r in result["receipts"]] != list(range(1, len(result["receipts"]) + 1)):
            errors.append("receipt attempt sequence tampered")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("baseline", "treatment", "all"), default="all")
    args = parser.parse_args()
    try:
        fixtures, oracle = load("fixtures.json"), load("oracle.json")
        modes = ("baseline", "treatment") if args.mode == "all" else (args.mode,)
        for mode in modes:
            result = execute(fixtures, mode)
            errors = validate(result, oracle)
            if errors:
                raise ValueError(f"{mode}: " + "; ".join(errors))
            (ROOT / "runs" / f"{mode}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        expected_negative_checks = oracle["negative_check_count"]
        if negative_checks(fixtures, oracle) != expected_negative_checks:
            raise ValueError("negative browser checks did not all fail closed")
        return 0
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"experiment failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
