#!/usr/bin/env python3
"""Strictly validate anonymous JSON judgments against their exact packets."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from common import LABELS, ROOT, ValidationError, load_schema, read_json, sha256_value, validate_schema


def validate_packet(packet: dict[str, Any]) -> None:
    allowed = {"schema_version", "experiment_id", "batch_id", "judge_id", "cases"}
    if set(packet) != allowed or packet["schema_version"] != "blind-packet/v1":
        raise ValidationError("blind packet contract invalid")
    if not all(isinstance(packet[key], str) and packet[key] for key in ("experiment_id", "batch_id", "judge_id")):
        raise ValidationError("blind packet identity fields must be non-empty strings")
    if not isinstance(packet["cases"], list) or not packet["cases"]:
        raise ValidationError("blind packet cases must be a non-empty array")
    seen_cases = set()
    for case in packet["cases"]:
        expected = {"case_id", "family_id", "language", "length_contract", "no_op_policy", "prompt", "source", "constraints", "gates", "criteria", "candidates"}
        if set(case) != expected:
            raise ValidationError("blind packet case keys invalid")
        if case["case_id"] in seen_cases:
            raise ValidationError("duplicate case in blind packet")
        seen_cases.add(case["case_id"])
        if not isinstance(case["prompt"], str) or not case["prompt"]:
            raise ValidationError("blind packet prompt must be non-empty")
        if not isinstance(case["candidates"], list) or len(case["candidates"]) != 4:
            raise ValidationError("blind packet must contain four candidates")
        labels = []
        for candidate in case["candidates"]:
            if set(candidate) != {"label", "text", "output_sha256"}:
                raise ValidationError("blind packet candidate keys invalid")
            labels.append(candidate["label"])
            if not isinstance(candidate["text"], str) or not candidate["text"]:
                raise ValidationError("blind packet candidate text must be non-empty")
            import hashlib
            if hashlib.sha256(candidate["text"].encode()).hexdigest() != candidate["output_sha256"]:
                raise ValidationError("blind packet candidate hash mismatch")
        if len(set(labels)) != 4 or set(labels) != set(LABELS):
            raise ValidationError("blind packet labels must be A-D exactly once")


def validate_judgment(judgment: dict[str, Any], packet: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    validate_packet(packet)
    validate_schema(judgment, load_schema("judgment", root))
    if judgment["judge_id"] != packet.get("judge_id"):
        raise ValidationError("judge_id does not match packet")
    packet_sha = sha256_value(packet)
    if judgment["packet_sha256"] != packet_sha:
        raise ValidationError("packet hash mismatch")
    packet_cases = {case["case_id"]: case for case in packet.get("cases", [])}
    judged_cases = {case["case_id"]: case for case in judgment["cases"]}
    if len(judged_cases) != len(judgment["cases"]):
        raise ValidationError("duplicate case_id in judgment")
    if set(judged_cases) != set(packet_cases):
        raise ValidationError("judgment case set does not match packet")
    for case_id, review in judged_cases.items():
        expected_labels = {candidate["label"] for candidate in packet_cases[case_id]["candidates"]}
        candidates = review["candidates"]
        labels = [candidate["label"] for candidate in candidates]
        if len(set(labels)) != 4 or set(labels) != expected_labels or set(labels) != set(LABELS):
            raise ValidationError(f"candidate labels invalid for {case_id}")
        flattened = [label for group in review["ranking"] for label in group]
        if len(flattened) != 4 or len(set(flattened)) != 4 or set(flattened) != set(LABELS):
            raise ValidationError(f"ranking must partition A-D exactly once for {case_id}")
        for candidate in candidates:
            expected_criteria = {criterion["criterion_id"] for criterion in packet_cases[case_id]["criteria"]}
            actual_criteria = [item["criterion_id"] for item in candidate["task_specific"]]
            if len(actual_criteria) != len(set(actual_criteria)) or set(actual_criteria) != expected_criteria:
                raise ValidationError(f"task-specific criteria must match packet exactly for {case_id}/{candidate['label']}")
            hard_issues = candidate["hard_issues"]
            fidelity = candidate["scores"]["fidelity"]
            if hard_issues and fidelity > 3:
                raise ValidationError(f"hard issue must cap fidelity at 3 for {case_id}/{candidate['label']}")
            if any(issue["material"] for issue in hard_issues) and fidelity > 1:
                raise ValidationError(f"material hard issue must cap fidelity at 1 for {case_id}/{candidate['label']}")
    return {"judge_id": judgment["judge_id"], "packet_sha256": packet_sha, "cases": len(judged_cases), "valid": True}


def validate_judge_diversity(judgments: list[dict[str, Any]]) -> None:
    if len(judgments) != 3 or len({item["judge_id"] for item in judgments}) != 3:
        raise ValidationError("exactly three distinct judges are required")
    if len({item["context_id"] for item in judgments}) != 3:
        raise ValidationError("judges must use three distinct contexts")
    if len({item["model_family"] for item in judgments}) != 3:
        raise ValidationError("judges must use three distinct model families")
    if len({item["provider"] for item in judgments}) < 2:
        raise ValidationError("judges must span at least two providers")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--judgment", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(validate_judgment(read_json(args.judgment), read_json(args.packet), args.root), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
