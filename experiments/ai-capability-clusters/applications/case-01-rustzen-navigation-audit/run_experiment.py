#!/usr/bin/env python3
"""Fixed-target, source-led RustZen navigation audit with a frozen oracle."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from pathlib import Path

CASE = Path(__file__).resolve().parent
COMMIT = "4e0189b52b5b6904a4b4082361a893a6f66e6797"
PRIOR = "2f6c6b35c644871f82cc1e35005580852468f362"
PATHS = ["apps/web/src/components/base-layout/routes.tsx", "docs/architecture.md", "docs/reference/capability-map.md"]
FIXTURES_SHA256 = "8c9cc01b749a8bf5e2976b9fc96d080b63692dad56876c92d04f5e802be05178"
ORACLE_SHA256 = "4522c7fce0a3ceb9be97eeadd88403795563becfd6d328e7f69de9b299601685"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(repo: Path, *args: str) -> tuple[int, str, str]:
    p = subprocess.run(["git", "-C", str(repo), *args], text=True, capture_output=True)
    return p.returncode, p.stdout, p.stderr.strip()


def metrics(expected: set[str], predicted: set[str]) -> dict[str, float | int]:
    tp, fp, fn = len(expected & predicted), len(predicted - expected), len(expected - predicted)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"TP": tp, "FP": fp, "FN": fn, "precision": precision, "recall": recall, "F1": f1}


def load_frozen_json(name: str, expected_sha256: str) -> tuple[dict[str, object] | None, str, str | None]:
    data = CASE.joinpath(name).read_bytes()
    actual = sha256_bytes(data)
    if actual != expected_sha256:
        return None, actual, f"frozen {name} SHA-256 mismatch"
    try:
        value = json.loads(data)
    except json.JSONDecodeError as error:
        return None, actual, f"invalid frozen {name}: {error}"
    if not isinstance(value, dict):
        return None, actual, f"frozen {name} must be an object"
    return value, actual, None


def parse_route_groups(routes_text: str) -> dict[str, str]:
    """Parse named route-group objects without knowing the audit routes in advance."""
    groups: dict[str, str] = {}
    for match in re.finditer(r"const\s+(\w+)Routes\s*:\s*AppRouteItem\s*=\s*\{(.*?)\n\};", routes_text, re.DOTALL):
        body = match.group(2)
        name = re.search(r'\bname:\s*"([^"]+)"', body)
        children = re.search(r"\bchildren:\s*\[(.*)\]", body, re.DOTALL)
        if not name or not children:
            continue
        for route in re.finditer(r'\bpath:\s*"(/[^"]+)"', children.group(1)):
            groups[route.group(1)] = name.group(1)
    return groups


def parse_capability_map(capmap: str) -> dict[str, dict[str, str]]:
    """Parse every capability table row into exact frontend-route ownership."""
    by_route: dict[str, dict[str, str]] = {}
    for line in capmap.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 3 or cells[0] in {"Capability", "---"} or set(cells[0]) == {"-"}:
            continue
        capability = cells[0]
        backend_paths = re.findall(r"`([^`]+)`", cells[1])
        frontend_paths = re.findall(r"`([^`]+)`", cells[2])
        for frontend in frontend_paths:
            exact = re.fullmatch(r"apps/web/src/routes/(.+)\.tsx", frontend)
            if not exact or not backend_paths:
                continue
            route = "/" + exact.group(1).replace("/index", "")
            by_route[route] = {"capability": capability, "backend_owner": backend_paths[0], "frontend_owner": frontend}
    return by_route


def candidate_id(route: str) -> str:
    return route.strip("/").replace("/", "-") + "-owner-capability-gap"


def enumerate_candidates(targets: list[str], groups: dict[str, str], capability_by_route: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    """Enumerate candidates only from frozen targets and source-derived exact mappings."""
    candidates: list[dict[str, str]] = []
    for route in targets:
        mapping = capability_by_route.get(route)
        if route not in groups or mapping is None:
            continue
        candidates.append({"id": candidate_id(route), "path": route, "kind": "owner_capability_gap", **mapping, "evidence": "routes.tsx + capability-map.md"})
    return candidates


def check_negative_routes(negative_routes: dict[str, str], audit_targets: list[str], groups: dict[str, str], capability_by_route: dict[str, dict[str, str]], candidates: list[dict[str, str]]) -> dict[str, bool]:
    """Prove distinct missing-mapping and scope-external negative conditions."""
    decoy = negative_routes["missing_mapping_decoy"]
    scope_external = negative_routes["scope_external"]
    finding_paths = {candidate["path"] for candidate in candidates}
    return {
        "missing_mapping_decoy": decoy in groups and decoy not in capability_by_route and decoy not in finding_paths,
        "scope_external": scope_external in groups and scope_external in capability_by_route and scope_external not in audit_targets and scope_external not in finding_paths,
    }


def main() -> int:
    repo_value = os.environ.get("RUSTZEN_ADMIN_REPO")
    if not repo_value:
        print("RUSTZEN_ADMIN_REPO is required and must point to a RustZen Admin Git repository")
        return 1
    repo = Path(repo_value).expanduser()
    if not repo.is_dir():
        print("RUSTZEN_ADMIN_REPO does not name an existing directory")
        return 1
    fixtures, fixtures_before, fixtures_error = load_frozen_json("fixtures.json", FIXTURES_SHA256)
    if fixtures_error:
        print(fixtures_error)
        return 1
    assert fixtures is not None
    audit_targets = fixtures.get("audit_targets")
    negative_routes = fixtures.get("negative_routes")
    if not (isinstance(audit_targets, list) and all(isinstance(route, str) for route in audit_targets) and isinstance(negative_routes, dict) and set(negative_routes) == {"missing_mapping_decoy", "scope_external"} and all(isinstance(route, str) for route in negative_routes.values())):
        print("invalid frozen fixture route scope")
        return 1

    CASE.joinpath("runs").mkdir(exist_ok=True)
    repo_label = "$RUSTZEN_ADMIN_REPO"
    basis: dict[str, object] = {"repo": repo_label, "commit": COMMIT, "prior_commit": PRIOR, "working_tree_used": False, "files": {}, "commands": [f"git -C {repo_label} rev-parse --verify {COMMIT}", f"git -C {repo_label} rev-parse --verify {PRIOR}"], "fixtures_sha256_before": fixtures_before}
    rc, _, err = git(repo, "rev-parse", "--verify", COMMIT)
    basis["commit_available"] = rc == 0
    rc_prior, _, _ = git(repo, "rev-parse", "--verify", PRIOR)
    basis["prior_commit_available"] = rc_prior == 0
    contents: dict[str, str] = {}
    for path in PATHS:
        rc, out, show_error = git(repo, "show", f"{COMMIT}:{path}")
        rc_hash, blob, _ = git(repo, "rev-parse", f"{COMMIT}:{path}")
        record: dict[str, object] = {"path": path, "available": rc == 0, "git_blob_sha": blob.strip() if rc_hash == 0 else None, "command": f"git -C {repo_label} show {COMMIT}:{path}"}
        if rc == 0:
            contents[path] = out
            record["sha256"] = sha256_bytes(out.encode())
        else:
            record["not_verified"] = f"Not verified: {show_error}"
        basis["files"][path] = record  # type: ignore[index]
    if rc:
        basis["not_verified"] = f"Not verified: frozen commit unavailable ({err})"
    CASE.joinpath("basis.json").write_text(json.dumps(basis, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if len(contents) != len(PATHS):
        return 1

    routes_text, architecture, capmap = (contents[path] for path in PATHS)
    groups = parse_route_groups(routes_text)
    capability_by_route = parse_capability_map(capmap)
    candidates = enumerate_candidates(audit_targets, groups, capability_by_route)
    candidate_ids = {candidate["id"] for candidate in candidates}
    negative_evidence = check_negative_routes(negative_routes, audit_targets, groups, capability_by_route, candidates)
    injected_decoy_map = dict(capability_by_route)
    injected_decoy_map[negative_routes["missing_mapping_decoy"]] = {"capability": "synthetic decoy", "backend_owner": "synthetic/backend", "frontend_owner": "apps/web/src/routes/system/status.tsx"}
    injected_decoy = check_negative_routes(negative_routes, audit_targets, groups, injected_decoy_map, candidates)
    removed_scope_map = dict(capability_by_route)
    removed_scope_map.pop(negative_routes["scope_external"], None)
    removed_scope = check_negative_routes(negative_routes, audit_targets, groups, removed_scope_map, candidates)
    synthetic_parser_negative_pass = not injected_decoy["missing_mapping_decoy"] and not removed_scope["scope_external"]
    negative_pass = all(negative_evidence.values()) and synthetic_parser_negative_pass
    # Candidate derivation is complete before the oracle is loaded for scoring.
    oracle, oracle_before, oracle_error = load_frozen_json("oracle.json", ORACLE_SHA256)
    if oracle_error:
        print(oracle_error)
        return 1
    assert oracle is not None
    basis["oracle_sha256_before"] = oracle_before
    baseline = {"strategy": "route-prefix-only", "groups": {route: groups.get(route) for route in audit_targets}, "findings": [], "metrics": metrics(set(oracle.get("expected_candidate_ids", [])), set()), "visual_browser_verified": False}
    treatment = {"strategy": "fixed-target-scope+exact-capability-map", "groups": {route: groups.get(route) for route in audit_targets}, "findings": candidates, "negative_routes": negative_evidence, "synthetic_parser_negative": {"injected_decoy_mapping_fails": not injected_decoy["missing_mapping_decoy"], "removed_scope_mapping_fails": not removed_scope["scope_external"]}, "negative_route_pass": negative_pass, "metrics": metrics(set(oracle.get("expected_candidate_ids", [])), candidate_ids), "visual_browser_verified": False, "architecture_read": bool(architecture)}
    CASE.joinpath("runs/baseline.json").write_text(json.dumps(baseline, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    CASE.joinpath("runs/treatment.json").write_text(json.dumps(treatment, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    oracle_after = sha256_bytes(CASE.joinpath("oracle.json").read_bytes())
    expected_ids = oracle.get("expected_candidate_ids")
    expected_findings = oracle.get("expected_findings")
    expected_routes = oracle.get("routes")
    passed = (oracle_after == oracle_before and isinstance(expected_ids, list) and candidate_ids == set(expected_ids) and candidates == expected_findings and {route: groups.get(route) for route in audit_targets} == expected_routes and negative_evidence == oracle.get("expected_negative_routes") and negative_pass)
    adjudication = {"oracle_pass": passed, "expected_candidate_ids": expected_ids, "baseline": baseline["metrics"], "treatment": treatment["metrics"], "oracle_sha256_before": oracle_before, "oracle_sha256_after": oracle_after, "oracle_hash_unchanged": oracle_before == oracle_after, "fixture_sha256": fixtures_before, "independent_checks": {"frozen_commit": bool(basis["commit_available"]), "all_paths_read": len(contents) == len(PATHS), "negative_routes": negative_evidence, "synthetic_parser_negative": treatment["synthetic_parser_negative"], "negative_routes_no_false_positives": negative_pass, "browser_visual": "not_verified"}}
    CASE.joinpath("adjudication.json").write_text(json.dumps(adjudication, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    CASE.joinpath("summary.md").write_text("\n".join(["# Case 01 result", "", f"- Fixed target scope: `{audit_targets}`; classified negative routes: `{negative_routes}`.", "- Treatment never loads oracle or expected answers while deriving candidates; it parses route groups and exact capability-map rows from frozen source.", f"- Baseline metrics: `{json.dumps(baseline['metrics'], sort_keys=True)}`.", f"- Treatment metrics: `{json.dumps(treatment['metrics'], sort_keys=True)}`; frozen-oracle pass: `{passed}`.", f"- Frozen oracle SHA-256 unchanged: `{oracle_before == oracle_after}` (`{oracle_before}`).", "- Missing-mapping decoy and scope-external routes both have no finding; injected decoy mapping and removed external mapping each fail their synthetic parser check.", "- Not verified: browser/visual behavior, permission service runtime, provider/agent behavior, and production deployment safety.", ""]), encoding="utf-8")
    print(json.dumps(adjudication, ensure_ascii=False, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
