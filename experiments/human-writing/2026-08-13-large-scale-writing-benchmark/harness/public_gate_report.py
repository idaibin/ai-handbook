#!/usr/bin/env python3
"""Build gate evidence for a public batch from objective checks and blind consensus."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from common import read_json, read_jsonl, sha256_value, write_json


def word_count(text: str) -> int:
    return len(text.split())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", type=Path, required=True)
    parser.add_argument("--outputs", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--judgment", type=Path, action="append", required=True)
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    cases = {row["case_id"]: row for row in read_jsonl([args.cases])}
    outputs = read_jsonl([args.outputs])
    mapping = read_json(args.mapping)
    judgments = {row["judge_id"]: row for row in (read_json(path) for path in args.judgment)}
    mapped = {packet["judge_id"]: packet["cases"] for packet in mapping["packets"]}
    reviews = {judge_id: {row["case_id"]: row for row in judgment["cases"]}
               for judge_id, judgment in judgments.items()}
    issue_votes: Counter[str] = Counter()
    issue_evidence: dict[str, list[str]] = {}
    for judge_id, case_map in mapped.items():
        for case_id, labels in case_map.items():
            candidate_map = {row["label"]: row for row in reviews[judge_id][case_id]["candidates"]}
            for label, identity in labels.items():
                relevant = [issue for issue in candidate_map[label]["hard_issues"]
                            if issue["material"] and issue["type"] in {"addition", "scope", "actor", "status"}]
                if relevant:
                    issue_votes[identity["task_id"]] += 1
                    issue_evidence.setdefault(identity["task_id"], []).extend(issue["evidence"] for issue in relevant)

    rows = []
    for output in outputs:
        case = cases[output["case_id"]]
        checks = []
        for gate in case["gates"]:
            if gate["gate_type"] == "length":
                contract = case["length_contract"]
                measured = word_count(output["text"]) if contract["unit"] == "words" else len(output["text"])
                passed = ((contract["minimum"] is None or measured >= contract["minimum"])
                          and (contract["maximum"] is None or measured <= contract["maximum"]))
                evidence = f"objective {contract['unit']} count={measured}; contract={contract['minimum']}..{contract['maximum']}"
            elif gate["gate_type"] == "grounding":
                votes = issue_votes[output["task_id"]]
                passed = votes < 2
                details = " | ".join(issue_evidence.get(output["task_id"], []))
                evidence = f"blind semantic material-issue votes={votes}/3" + (f": {details}" if details else "")
            else:
                raise ValueError(f"unsupported public gate type: {gate['gate_type']}")
            checks.append({"check_id": gate["gate_id"], "gate_type": gate["gate_type"],
                           "target": gate["target"], "expected": gate["expected"], "passed": passed,
                           "severity": "critical", "evidence": evidence})
        rows.append({"task_id": output["task_id"], "case_id": output["case_id"],
                     "output_sha256": output["output_sha256"], "checks": checks,
                     "critical_failure": any(not check["passed"] for check in checks)})
    report = {"schema_version": "deterministic-gates/v1", "batch_id": args.batch_id, "outputs": rows}
    report["report_sha256"] = sha256_value(report)
    write_json(args.output, report)
    print(json.dumps({"outputs": len(rows), "critical_failures": sum(row["critical_failure"] for row in rows)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
