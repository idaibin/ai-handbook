#!/usr/bin/env python3
"""Audit the fixed coverage manifest and batches with a frozen oracle."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

CASE = Path(__file__).resolve().parent
HANDBOOK_ROOT = CASE.parents[3]
ROOT = HANDBOOK_ROOT / "sources/coverage"
MANIFEST = ROOT / "manifest.yaml"
BATCHES = sorted(ROOT.glob("batch-*.yaml"))
VALIDATOR = ROOT / "validate_coverage.py"
ROLES = ["readme", "core", "security_or_boundary", "evaluation_or_testing", "code_or_test"]
ORACLE_SHA256 = "44535d5ad633a4cdd1b15673d71ee1c4c2c1a2ff49fc187233b5ede21d23f125"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def metrics(expected: set[str], predicted: set[str]) -> dict[str, float | int]:
    tp, fp, fn = len(expected & predicted), len(predicted - expected), len(expected - predicted)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"TP": tp, "FP": fp, "FN": fn, "precision": precision, "recall": recall, "F1": f1}


def load_oracle() -> tuple[dict[str, object] | None, str, str | None]:
    data = CASE.joinpath("oracle.json").read_bytes()
    before = hashlib.sha256(data).hexdigest()
    if before != ORACLE_SHA256:
        return None, before, "frozen oracle SHA-256 mismatch"
    try:
        oracle = json.loads(data)
    except json.JSONDecodeError as error:
        return None, before, f"invalid frozen oracle: {error}"
    return (oracle if isinstance(oracle, dict) else None), before, None if isinstance(oracle, dict) else "frozen oracle must be an object"


def main() -> int:
    CASE.joinpath("runs").mkdir(exist_ok=True)
    oracle, oracle_before, oracle_error = load_oracle()
    if oracle_error:
        oracle_after = digest(CASE / "oracle.json")
        CASE.joinpath("adjudication.json").write_text(json.dumps({"oracle_pass": False, "oracle_error": oracle_error, "oracle_sha256_before": oracle_before, "oracle_sha256_after": oracle_after, "oracle_hash_unchanged": oracle_before == oracle_after}, indent=2) + "\n", encoding="utf-8")
        return 1
    source_ids = re.findall(r"^\s{2}([a-z0-9][a-z0-9-]*):\s*\{repo:", MANIFEST.read_text(encoding="utf-8"), flags=re.M)
    raw_expected = {f"{source_id}|{role}" for source_id in source_ids for role in ROLES}
    relative = lambda path: path.relative_to(HANDBOOK_ROOT).as_posix()
    basis = {"manifest": relative(MANIFEST), "batches": [relative(p) for p in BATCHES], "validator": relative(VALIDATOR), "sha256": {relative(p): digest(p) for p in [MANIFEST, *BATCHES, VALIDATOR]}, "remote_verify": False, "oracle_sha256_before": oracle_before}
    CASE.joinpath("basis.json").write_text(json.dumps(basis, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    baseline_keys = {f"{source_id}|summary" for source_id in source_ids}
    baseline = {"strategy": "README+manifest-summary-only", "source_summaries": source_ids, "records": [], "metrics": metrics(raw_expected, baseline_keys), "completion_claim": "coverage summarized; role evidence omitted", "remote_runtime_effect": "Not verified"}
    CASE.joinpath("runs/baseline.json").write_text(json.dumps(baseline, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    command = ["python3", str(VALIDATOR), *map(str, BATCHES)]
    command_display = ["python3", relative(VALIDATOR), *map(relative, BATCHES)]
    proc = subprocess.run(command, text=True, capture_output=True)
    summary_match = re.search(r"coverage: batches=(\d+) sources=(\d+) records=(\d+) read=(\d+) not_found=(\d+) incomplete=(\d+)", proc.stdout)
    summary_counts = {"batches": int(summary_match.group(1)), "sources": int(summary_match.group(2)), "records": int(summary_match.group(3)), "read": int(summary_match.group(4)), "not_found": int(summary_match.group(5)), "incomplete": int(summary_match.group(6))} if summary_match else {}
    error_match = re.search(r"errors=(\d+)", proc.stdout)
    errors = [] if error_match and int(error_match.group(1)) == 0 else [proc.stdout.strip() or proc.stderr.strip()]
    records: list[dict[str, str]] = []
    for path in BATCHES:
        current_source = None
        roles_by_source: dict[str, list[str]] = {}
        statuses_by_source: dict[str, list[str]] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            source_match = re.match(r'^  -\s+source_id:\s*["\']?([A-Za-z0-9_-]+)', line)
            if source_match:
                current_source = source_match.group(1)
                roles_by_source.setdefault(current_source, [])
                statuses_by_source.setdefault(current_source, [])
            status_match = re.match(r'^\s*(?:-\s*)?status:\s*["\']?([A-Za-z0-9_]+)', line)
            if status_match and current_source:
                statuses_by_source[current_source].append("read_at_fixed_commit" if status_match.group(1) == "read" else status_match.group(1))
            role_match = re.match(r'^\s*(?:-\s*)?role:\s*["\']?([A-Za-z0-9_]+)', line)
            if role_match and current_source:
                roles_by_source[current_source].append(role_match.group(1))
        for source_id, roles in roles_by_source.items():
            for index, role in enumerate(roles):
                records.append({"source_id": source_id, "role": role, "status": statuses_by_source[source_id][index] if index < len(statuses_by_source[source_id]) else ""})
    treatment_keys = {f"{record['source_id']}|{record['role']}" for record in records}
    treatment = {"strategy": "validator+normalized-records", "validator_command": " ".join(command_display), "validator_stdout": proc.stdout.strip(), "validator_exit": proc.returncode, "summary": summary_counts, "errors": errors, "records": records, "metrics": metrics(raw_expected, treatment_keys), "remote_verify": "Not verified", "runtime_effect": "Not verified"}
    CASE.joinpath("runs/treatment.json").write_text(json.dumps(treatment, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    oracle_after = digest(CASE / "oracle.json")
    statuses = {record["status"] for record in records}
    roles = {record["role"] for record in records}
    passed = (oracle_after == oracle_before and proc.returncode == 0 and len(errors) == oracle.get("errors") and len(source_ids) == oracle.get("source_count") and len(records) == oracle.get("record_count") and roles == set(oracle.get("roles", [])) and statuses == {oracle.get("status")} and treatment_keys == set(oracle.get("expected_record_keys", [])))
    adjudication = {"oracle_pass": passed, "baseline_metrics": baseline["metrics"], "treatment_metrics": treatment["metrics"], "oracle_sha256_before": oracle_before, "oracle_sha256_after": oracle_after, "oracle_hash_unchanged": oracle_before == oracle_after, "independent_checks": {"validator_exit_0": proc.returncode == 0, "errors_zero": not errors, "source_count_matches_oracle": len(source_ids) == oracle.get("source_count"), "record_count_matches_oracle": len(records) == oracle.get("record_count"), "record_keys_match_oracle": treatment_keys == set(oracle.get("expected_record_keys", [])), "remote": "Not verified"}}
    CASE.joinpath("adjudication.json").write_text(json.dumps(adjudication, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    CASE.joinpath("summary.md").write_text("\n".join(["# Case 02 result", "", f"- Validator: `{' '.join(command_display)}` exit `{proc.returncode}`; errors `{len(errors)}`.", f"- Counts: `{json.dumps(summary_counts, sort_keys=True)}`; treatment frozen-oracle pass `{passed}`.", f"- Baseline metrics: `{json.dumps(baseline['metrics'], sort_keys=True)}`; treatment metrics: `{json.dumps(treatment['metrics'], sort_keys=True)}`.", f"- Frozen oracle SHA-256 unchanged: `{oracle_before == oracle_after}` (`{oracle_before}`).", "- Fixed-commit structure/coverage is verified locally; remote GitHub path/blob and upstream runtime/provider effects remain `Not verified`.", ""]), encoding="utf-8")
    print(json.dumps(adjudication, ensure_ascii=False, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
