#!/usr/bin/env python3
"""Unblind and aggregate the three markdown judge sheets."""

from __future__ import annotations

import json
import re
import argparse
from collections import defaultdict
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
ROOT = parser.parse_args().root.resolve()
mapping = json.loads((ROOT / "results/blind-mappings.json").read_text())
dimensions = ["fidelity", "instruction_structure", "clarity", "naturalness", "restraint"]
scores: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
repair_scores: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
hard_counts = defaultdict(int)
first_share = defaultdict(float)
case_first = defaultdict(float)
records = []
rankings_seen = set()
expected_cases = {"C01", "C02", "C03", "C04", "C05", "C06", "N01", "N02", "N03", "N04"}
expected_labels = {"A", "B", "C", "D"}
expected_skills = {"human-writing", "humanizer", "humanizer-zh", "stop-slop"}
if set(mapping) != {"1", "2", "3"}:
    raise ValueError("mapping must contain judges 1, 2, and 3")
for judge_no, judge_mapping in mapping.items():
    if set(judge_mapping) != expected_cases:
        raise ValueError(f"mapping cases invalid for judge {judge_no}")
    for case_id, case_mapping in judge_mapping.items():
        if set(case_mapping) != expected_labels or set(case_mapping.values()) != expected_skills:
            raise ValueError(f"mapping is not a bijection for judge {judge_no} case {case_id}")

for judge_no in (1, 2, 3):
    text = (ROOT / f"results/judge-{judge_no}.md").read_text()
    sections = re.split(r"^## (C\d\d|N\d\d)\s*$", text, flags=re.M)
    for idx in range(1, len(sections), 2):
        case_id, body = sections[idx], sections[idx + 1]
        for line in body.splitlines():
            match = re.match(r"^\|\s*([A-D])\s*\|\s*(\d)\s*\|\s*(\d)\s*\|\s*(\d)\s*\|\s*(\d)\s*\|\s*(\d)\s*\|\s*(.*?)\s*\|", line)
            if not match:
                continue
            label = match.group(1)
            skill = mapping[str(judge_no)][case_id][label]
            vals = list(map(int, match.groups()[1:6]))
            hard = match.group(7).strip() not in {"无", "无。", "none", "None"}
            for dimension, value in zip(dimensions, vals):
                scores[skill][dimension].append(value)
                if case_id.startswith("C"):
                    repair_scores[skill][dimension].append(value)
            hard_counts[skill] += int(hard)
            records.append({"judge": judge_no, "case_id": case_id, "label": label, "skill": skill, "scores": dict(zip(dimensions, vals)), "hard_issue": hard})

        ranks = re.findall(r"^Ranking:\s*([^\n]+?)\s*$", body, flags=re.M)
        if len(ranks) != 1:
            raise ValueError(f"expected one ranking for judge {judge_no} case {case_id}")
        expression = ranks[0].strip()
        if not re.fullmatch(r"[A-D](?:\s*=\s*[A-D])*(?:\s*>\s*[A-D](?:\s*=\s*[A-D])*)*", expression):
            raise ValueError(f"invalid ranking syntax for judge {judge_no} case {case_id}: {expression}")
        rank_labels = re.findall(r"[A-D]", expression)
        if len(rank_labels) != 4 or set(rank_labels) != expected_labels:
            raise ValueError(f"ranking must contain A-D exactly once for judge {judge_no} case {case_id}")
        rankings_seen.add((judge_no, case_id))
        leaders = re.split(r"\s*=\s*", re.split(r"\s*>\s*", expression)[0])
        for label in leaders:
            share = 1 / len(leaders)
            skill = mapping[str(judge_no)][case_id][label]
            first_share[skill] += share
            case_first[(skill, case_id)] += share

expected_records = 3 * 10 * 4
if len(records) != expected_records:
    raise ValueError(f"expected {expected_records} score rows, got {len(records)}")
if len(rankings_seen) != 3 * 10:
    raise ValueError(f"expected 30 rankings, got {len(rankings_seen)}")
if abs(sum(first_share.values()) - 30) > 1e-9:
    raise ValueError("first-place shares do not sum to 30")
repair_share = sum(value for (skill, case), value in case_first.items() if case.startswith("C"))
if abs(repair_share - 18) > 1e-9:
    raise ValueError("repair first-place shares do not sum to 18")
for judge_no in (1, 2, 3):
    for case_id in ("C01", "C02", "C03", "C04", "C05", "C06", "N01", "N02", "N03", "N04"):
        subset = [r for r in records if r["judge"] == judge_no and r["case_id"] == case_id]
        if {r["label"] for r in subset} != {"A", "B", "C", "D"}:
            raise ValueError(f"incomplete labels for judge {judge_no} case {case_id}")
        if any(not 1 <= value <= 5 for r in subset for value in r["scores"].values()):
            raise ValueError(f"score out of range for judge {judge_no} case {case_id}")

summary = {}
for skill in sorted(scores):
    summary[skill] = {
        "overall_mean": round(sum(sum(v) for v in scores[skill].values()) / sum(len(v) for v in scores[skill].values()), 3),
        "repair_mean": round(sum(sum(v) for v in repair_scores[skill].values()) / sum(len(v) for v in repair_scores[skill].values()), 3),
        "repair_dimensions": {k: round(sum(v) / len(v), 3) for k, v in repair_scores[skill].items()},
        "hard_issue_flags_of_30_all_cases": hard_counts[skill],
        "hard_issue_flags_of_18_repair_cases": sum(
            record["hard_issue"] for record in records
            if record["skill"] == skill and record["case_id"].startswith("C")
        ),
        "first_place_share_of_30": round(first_share[skill], 3),
        "repair_first_place_share_of_18": round(sum(value for (name, case), value in case_first.items() if name == skill and case.startswith("C")), 3),
    }

(ROOT / "results/aggregate.json").write_text(json.dumps({"summary": summary, "records": records}, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(summary, ensure_ascii=False, indent=2))
