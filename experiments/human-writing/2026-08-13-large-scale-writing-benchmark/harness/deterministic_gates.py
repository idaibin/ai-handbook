#!/usr/bin/env python3
"""Validate deterministic gate reports and compute preference eligibility."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from common import ValidationError, hash_without, read_json, sha256_value, write_json

SEVERITIES = {"major", "critical"}


def execute_gates(batch_id: str, cases: list[dict[str, Any]], outputs: list[dict[str, Any]]) -> dict[str, Any]:
    """Execute only objectively decidable frozen gates; unsupported gates block."""
    case_index = {case["case_id"]: case for case in cases}
    rows = []
    for output in outputs:
        case = case_index.get(output["case_id"])
        if case is None:
            raise ValidationError("gate executor received output for unknown case")
        checks = []
        for gate in case["gates"]:
            kind, target, expected = gate["gate_type"], gate["target"], gate["expected"]
            if kind == "contains":
                passed = (target in output["text"]) is bool(expected)
            elif kind == "not_contains":
                passed = (target not in output["text"]) is bool(expected)
            elif kind == "no_op":
                passed = (output["text"] == (case["source"] or "")) is bool(expected)
            elif kind == "length":
                if not isinstance(expected, int):
                    raise ValidationError("length gate expected must be integer")
                passed = len(output["text"]) <= expected
            else:
                raise ValidationError(f"gate type requires a dedicated verified executor: {kind}")
            checks.append({"check_id": gate["gate_id"], "gate_type": kind, "target": target, "expected": expected,
                           "passed": passed, "severity": "critical",
                           "evidence": f"executed frozen {kind} gate against output bytes"})
        critical = any(not check["passed"] and check["severity"] == "critical" for check in checks)
        rows.append({"task_id": output["task_id"], "case_id": output["case_id"], "output_sha256": output["output_sha256"],
                     "checks": checks, "critical_failure": critical})
    report = {"schema_version": "deterministic-gates/v1", "batch_id": batch_id, "outputs": rows}
    report["report_sha256"] = sha256_value(report)
    return report


def validate_gate_report(report: dict[str, Any], expected: dict[str, dict[str, Any]], cases: dict[str, dict[str, Any]] | None = None) -> dict[str, dict[str, Any]]:
    if cases is None:
        raise ValidationError("case contracts are required to validate deterministic gates")
    allowed = {"schema_version", "batch_id", "outputs", "report_sha256"}
    if set(report) != allowed or report["schema_version"] != "deterministic-gates/v1":
        raise ValidationError("deterministic gate report contract invalid")
    if hash_without(report, "report_sha256") != report["report_sha256"]:
        raise ValidationError("deterministic gate report hash mismatch")
    if not isinstance(report["outputs"], list):
        raise ValidationError("deterministic gate outputs must be an array")
    indexed = {}
    for row in report["outputs"]:
        if set(row) != {"task_id", "case_id", "output_sha256", "checks", "critical_failure"}:
            raise ValidationError("deterministic gate row keys invalid")
        if row["task_id"] in indexed or row["task_id"] not in expected:
            raise ValidationError("duplicate or unknown deterministic gate task")
        target = expected[row["task_id"]]
        if row["output_sha256"] != target["output_sha256"]:
            raise ValidationError("deterministic gate output hash mismatch")
        if not isinstance(row["checks"], list):
            raise ValidationError("deterministic checks must be an array")
        computed_critical = False
        check_ids = set()
        if row["case_id"] not in cases:
            raise ValidationError("deterministic gate row references unknown case")
        expected_gates = {gate["gate_id"]: gate for gate in cases[row["case_id"]]["gates"]}
        for check in row["checks"]:
            if set(check) != {"check_id", "gate_type", "target", "expected", "passed", "severity", "evidence"}:
                raise ValidationError("deterministic check keys invalid")
            if check["check_id"] in check_ids or check["severity"] not in SEVERITIES:
                raise ValidationError("duplicate check or invalid severity")
            check_ids.add(check["check_id"])
            frozen = expected_gates.get(check["check_id"])
            if frozen is None or any(check[key] != frozen[key] for key in ("gate_type", "target", "expected")):
                raise ValidationError("deterministic check does not match frozen case gate")
            if not isinstance(check["passed"], bool) or not isinstance(check["evidence"], str) or not check["evidence"]:
                raise ValidationError("deterministic check result invalid")
            computed_critical |= not check["passed"] and check["severity"] == "critical"
        if row["critical_failure"] is not computed_critical:
            raise ValidationError("critical_failure does not match checks")
        if check_ids != set(expected_gates):
            raise ValidationError("deterministic checks do not cover every frozen case gate exactly once")
        indexed[row["task_id"]] = row
    if set(indexed) != set(expected):
        raise ValidationError("deterministic gate report is incomplete")
    return indexed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--outputs", type=Path, required=True)
    parser.add_argument("--cases", type=Path, required=True)
    args = parser.parse_args()
    outputs = read_json(args.outputs)
    expected = {row["task_id"]: row for row in outputs}
    case_rows = read_json(args.cases)
    if not isinstance(case_rows, list):
        raise ValidationError("--cases must be a JSON array")
    result = validate_gate_report(read_json(args.report), expected, {row["case_id"]: row for row in case_rows})
    print(json.dumps({"outputs": len(result), "critical_failures": sum(row["critical_failure"] for row in result.values())}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
