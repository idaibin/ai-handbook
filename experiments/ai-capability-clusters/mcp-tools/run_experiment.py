#!/usr/bin/env python3
"""Deterministic local MCP authorization experiment; no network or model calls."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def execute(fixtures: dict, mode: str) -> dict:
    state = copy.deepcopy(fixtures["initial_state"])
    actions = fixtures["actions"]
    receipts = []
    decisions = []
    approvals = 0
    postcondition_checks = 0
    postcondition_correct = 0
    unauthorized_blocked = 0
    legitimate_completed = 0
    false_reject = 0
    grant_registry = {} if mode == "treatment" else {"connection-grant": {"action_id": "connection", "state": "active", "used": False, "transitions": ["active"]}}
    grant_uses = set()

    for seq, action in enumerate(actions, 1):
        allowed = mode == "baseline"
        reason = "connection_grant" if allowed else "policy"
        grant_id = None
        revoke = None
        approval = bool(action.get("approval", False))
        if mode == "treatment":
            principal_ok = fixtures["principal"] == "alice"
            session_ok = fixtures["session"] == "session-1"
            account_ok = fixtures["account"] == "acct-1"
            target_ok = action["target"] in fixtures["target_allowlist"]
            kind_ok = action["kind"] in {"read_profile", "transfer"}
            allowed = principal_ok and session_ok and account_ok and target_ok and kind_ok
            if allowed and action["kind"] == "transfer":
                approvals += 1 if approval else 0
                allowed = approval
                reason = "approved_temporary_grant" if allowed else "approval_required"
                if allowed:
                    grant_id = f"grant-{seq}"
                    grant_registry[grant_id] = {"action_id": action["id"], "state": "active", "used": False, "transitions": ["active"]}
            elif not allowed:
                reason = "target_or_action_not_allowlisted"

        before = copy.deepcopy(state)
        if allowed:
            if action["kind"] == "transfer":
                if mode == "treatment" and (not grant_id or grant_id in grant_uses or grant_registry[grant_id]["state"] != "active"):
                    raise ValueError(f"invalid grant transition for {action['id']}")
                state["balances"][action["target"]] -= action["amount"]
                if mode == "treatment":
                    grant_registry[grant_id]["used"] = True
                    grant_uses.add(grant_id)
                legitimate_completed += 1 if action["authorized"] else 0
            elif action["kind"] == "delete_record":
                state["records"][action["target"]] = "deleted"
            elif action["kind"] == "read_profile":
                legitimate_completed += 1
        elif action["authorized"]:
            false_reject += 1
        if not action["authorized"] and not allowed:
            unauthorized_blocked += 1

        postcondition = None
        if mode == "treatment" and allowed and action["kind"] == "transfer":
            observed = state["balances"][action["target"]]
            expected = before["balances"][action["target"]] - action["amount"]
            postcondition = {"expected": expected, "observed": observed, "ok": observed == expected}
            postcondition_checks += 1
            postcondition_correct += int(postcondition["ok"])
            grant_registry[grant_id]["state"] = "revoked"
            grant_registry[grant_id]["transitions"].append("revoked")
            revoke = {"grant_id": grant_id, "performed": True, "state_before": "active", "state_after": "revoked"}
        receipts.append({
            "seq": seq,
            "action_id": action["id"],
            "decision": "allowed" if allowed else "blocked",
            "reason": reason,
            "approval": approval,
            "grant_id": grant_id,
            "postcondition_readback": postcondition,
            "revoke": revoke,
        })
    residual_permission = sum(1 for grant in grant_registry.values() if grant["state"] == "active")
    metrics = {
        "unauthorized_blocked": unauthorized_blocked,
        "legitimate_completed": legitimate_completed,
        "postcondition_accuracy": (postcondition_correct / postcondition_checks) if postcondition_checks else 0.0,
        "false_reject": false_reject,
        "residual_permission": residual_permission,
    }
    return {
        "experiment_id": fixtures["experiment_id"],
        "mode": mode,
        "decision_table": [{"action_id": r["action_id"], "decision": r["decision"], "reason": r["reason"]} for r in receipts],
        "final_state": state,
        "receipts": receipts,
        "grant_registry": grant_registry,
        "metrics": metrics,
    }


def receipt_integrity_errors(result: dict, fixtures: dict) -> list[str]:
    """Independently replay ordered receipts and bind grants/readbacks to state."""
    errors = []
    seen = set()
    registry = result.get("grant_registry", {})
    table = {item.get("action_id"): item for item in result.get("decision_table", [])}
    actions = fixtures.get("actions", [])
    receipts = result.get("receipts", [])
    replay_state = copy.deepcopy(fixtures["initial_state"])
    if len(receipts) != len(actions):
        errors.append("receipt count must equal fixture action count")
    for seq, receipt in enumerate(receipts, 1):
        action_id = receipt.get("action_id")
        fixture = actions[seq - 1] if seq <= len(actions) else None
        if not fixture or receipt.get("seq") != seq or action_id != fixture.get("id"):
            errors.append(f"{action_id}: receipt sequence/action differs from fixture")
            continue
        if table.get(action_id, {}).get("decision") != receipt.get("decision") or table.get(action_id, {}).get("reason") != receipt.get("reason"):
            errors.append(f"{action_id}: receipt decision tampered")
        before = copy.deepcopy(replay_state)
        allowed = receipt.get("decision") == "allowed"
        if allowed and fixture.get("kind") == "transfer":
            replay_state["balances"][fixture["target"]] -= fixture["amount"]
        elif allowed and fixture.get("kind") == "delete_record":
            replay_state["records"][fixture["target"]] = "deleted"
        grant_id = receipt.get("grant_id")
        if grant_id is None:
            if receipt.get("revoke") is not None:
                errors.append(f"{action_id}: revoke without grant")
            if receipt.get("postcondition_readback") is not None:
                errors.append(f"{action_id}: postcondition without grant")
            continue
        if grant_id in seen:
            errors.append(f"{action_id}: grant reused")
        seen.add(grant_id)
        if fixture.get("kind") != "transfer" or receipt.get("decision") != "allowed":
            errors.append(f"{action_id}: grant attached to a non-allowed transfer")
            continue
        grant = registry.get(grant_id)
        if not grant or grant.get("action_id") != action_id:
            errors.append(f"{action_id}: grant registry mismatch")
        if grant and grant.get("used") is not True:
            errors.append(f"{action_id}: registry grant not marked used")
        if receipt.get("approval") is not True:
            errors.append(f"{action_id}: grant missing approval")
        revoke = receipt.get("revoke")
        if not isinstance(revoke, dict) or revoke.get("performed") is not True or revoke.get("grant_id") != grant_id or revoke.get("state_before") != "active" or revoke.get("state_after") != "revoked":
            errors.append(f"{action_id}: grant revoke missing")
        if grant and grant.get("state") != "revoked":
            errors.append(f"{action_id}: registry grant not revoked")
        if grant and grant.get("transitions") != ["active", "revoked"]:
            errors.append(f"{action_id}: invalid grant transition history")
        postcondition = receipt.get("postcondition_readback")
        expected_balance = before["balances"][fixture["target"]] - fixture["amount"]
        observed_balance = replay_state["balances"][fixture["target"]]
        if (
            not isinstance(postcondition, dict)
            or postcondition.get("expected") != expected_balance
            or postcondition.get("observed") != observed_balance
            or postcondition.get("ok") is not True
        ):
            errors.append(f"{action_id}: postcondition receipt tampered")
    if set(registry) != seen:
        errors.append("registry grants must exactly equal non-empty receipt grants")
    if replay_state != result.get("final_state"):
        errors.append("receipt replay final state differs from result final_state")
    if result.get("metrics", {}).get("residual_permission") != sum(1 for grant in registry.values() if grant.get("state") == "active"):
        errors.append("residual_permission is not derived from registry")
    return errors


def negative_checks(fixtures: dict) -> int:
    """Return number of intentionally corrupted receipt cases detected."""
    result = execute(fixtures, "treatment")
    cases = 0
    if "skip_revoke" in fixtures.get("negative_cases", []):
        corrupted = copy.deepcopy(result)
        corrupted["receipts"][1]["revoke"]["performed"] = False
        cases += int(bool(receipt_integrity_errors(corrupted, fixtures)))
    if "reuse_grant" in fixtures.get("negative_cases", []):
        corrupted = copy.deepcopy(result)
        corrupted["receipts"][0]["grant_id"] = corrupted["receipts"][1]["grant_id"]
        cases += int(bool(receipt_integrity_errors(corrupted, fixtures)))
    if "tamper_receipt" in fixtures.get("negative_cases", []):
        corrupted = copy.deepcopy(result)
        corrupted["receipts"][1]["postcondition_readback"]["observed"] += 1
        cases += int(bool(receipt_integrity_errors(corrupted, fixtures)) or corrupted["receipts"][1]["postcondition_readback"]["observed"] != corrupted["receipts"][1]["postcondition_readback"]["expected"])
    if "tamper_registry_used" in fixtures.get("negative_cases", []):
        corrupted = copy.deepcopy(result)
        corrupted["grant_registry"]["grant-2"]["used"] = False
        cases += int(bool(receipt_integrity_errors(corrupted, fixtures)))
    if "tamper_revoke_before" in fixtures.get("negative_cases", []):
        corrupted = copy.deepcopy(result)
        corrupted["receipts"][1]["revoke"]["state_before"] = "revoked"
        cases += int(bool(receipt_integrity_errors(corrupted, fixtures)))
    if "joint_postcondition_tamper" in fixtures.get("negative_cases", []):
        corrupted = copy.deepcopy(result)
        corrupted["receipts"][1]["postcondition_readback"].update({"expected": 999, "observed": 999, "ok": True})
        cases += int(bool(receipt_integrity_errors(corrupted, fixtures)))
    if "ghost_grant" in fixtures.get("negative_cases", []):
        corrupted = copy.deepcopy(result)
        corrupted["grant_registry"]["ghost-revoked-grant"] = {"action_id": "ghost", "state": "revoked", "used": True, "transitions": ["active", "revoked"]}
        cases += int(bool(receipt_integrity_errors(corrupted, fixtures)))
    return cases


def validate(result: dict, oracle: dict) -> list[str]:
    expected = oracle["expected"][result["mode"]]
    errors = []
    got_decisions = [item["decision"] for item in result["decision_table"]]
    if got_decisions != expected["decisions"]:
        errors.append(f"decisions {got_decisions!r} != oracle {expected['decisions']!r}")
    if result["final_state"] != expected["final_state"]:
        errors.append("final_state differs from oracle")
    if result["metrics"] != expected["metrics"]:
        errors.append(f"metrics {result['metrics']!r} != oracle {expected['metrics']!r}")
    if len(result["receipts"]) != 4:
        errors.append("receipt count must equal action count")
    if result["mode"] == "treatment":
        errors.extend(receipt_integrity_errors(result, load("fixtures.json")))
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
        if negative_checks(fixtures) != len(fixtures.get("negative_cases", [])):
            raise ValueError("negative receipt checks did not all fail closed")
        return 0
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"experiment failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
