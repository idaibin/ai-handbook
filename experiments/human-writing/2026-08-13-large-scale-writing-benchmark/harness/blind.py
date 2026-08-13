#!/usr/bin/env python3
"""Build deterministic, position-balanced anonymous judge packets."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
from collections import Counter
from pathlib import Path
from typing import Any

from common import LABELS, ROOT, ValidationError, load_manifest, read_jsonl, sha256_value, write_json


def _output_hash(output: dict[str, Any]) -> str:
    return hashlib.sha256(output["text"].encode()).hexdigest()


def validate_outputs(outputs: list[dict[str, Any]], cases: list[dict[str, Any]], skills: list[str],
                     plan: dict[str, Any]) -> dict[str, dict[str, Any]]:
    allowed = {"task_id", "task_sha256", "case_id", "case_sha256", "prompt_sha256", "skill_id", "skill_revision", "generator_contract_sha256", "text", "output_sha256"}
    case_ids = {case["case_id"] for case in cases}
    indexed: dict[str, dict[str, Any]] = {}
    for output in outputs:
        if set(output) != allowed:
            raise ValidationError(f"output keys invalid for {output.get('case_id', '<unknown>')}")
        if output["case_id"] not in case_ids or output["skill_id"] not in skills:
            raise ValidationError("output references an unknown case or skill")
        if not all(isinstance(output[key], str) and output[key] for key in allowed):
            raise ValidationError("all output fields must be non-empty strings")
        if re.fullmatch(r"[0-9a-f]{64}", output["task_id"]) is None:
            raise ValidationError("output task_id must be a SHA-256 identifier")
        if re.fullmatch(r"[0-9a-f]{40}", output["skill_revision"]) is None:
            raise ValidationError("output skill_revision must be a full Git SHA")
        if _output_hash(output) != output["output_sha256"]:
            raise ValidationError(f"output hash mismatch: {output['case_id']} {output['skill_id']}")
        key = f"{output['case_id']}\0{output['skill_id']}"
        if key in indexed:
            raise ValidationError(f"duplicate output: {output['case_id']} {output['skill_id']}")
        indexed[key] = output
    plan_tasks = {task["task_id"]: task for task in plan.get("tasks", [])}
    if len(plan_tasks) != len(plan.get("tasks", [])):
        raise ValidationError("generation plan contains duplicate task_id")
    for task in plan_tasks.values():
        task_body = {key: value for key, value in task.items() if key not in {"task_id", "task_sha256"}}
        if sha256_value(task_body) != task["task_id"]:
            raise ValidationError("generation plan task_id is not bound to its task contract")
        with_id = dict(task_body, task_id=task["task_id"])
        if sha256_value(with_id) != task["task_sha256"]:
            raise ValidationError("generation plan task_sha256 is invalid")
    case_index = {case["case_id"]: case for case in cases}
    for output in outputs:
        task = plan_tasks.get(output["task_id"])
        if task is None:
            raise ValidationError("output task_id is absent from the generation plan")
        bound = {key: output[key] for key in ("task_id", "task_sha256", "case_id", "case_sha256", "prompt_sha256", "skill_id", "skill_revision", "generator_contract_sha256")}
        expected = {key: task[key] for key in bound}
        if bound != expected or output["case_sha256"] != case_index[output["case_id"]]["case_sha256"]:
            raise ValidationError("output identity does not match plan/case/prompt/revision/generator contract")
    expected = len(cases) * len(skills)
    if len(indexed) != expected:
        raise ValidationError(f"expected {expected} outputs, got {len(indexed)}")
    for case in cases:
        if {indexed[f"{case['case_id']}\0{skill}"]["skill_id"] for skill in skills} != set(skills):
            raise ValidationError(f"incomplete skill set for {case['case_id']}")
    return indexed


def verify_position_balance(mapping: dict[str, Any], paired: dict[str, Any] | None = None) -> None:
    skills = [item["skill_id"] for item in mapping["skills"]]
    counts: Counter[tuple[str, str]] = Counter()
    for packet in mapping["packets"]:
        if set(packet) != {"judge_id", "packet_sha256", "cases"}:
            raise ValidationError("blind mapping packet keys invalid")
        for case_id, labels in packet["cases"].items():
            if set(labels) != set(LABELS):
                raise ValidationError(f"mapping labels are not A-D for {case_id}")
            assigned = [entry["skill_id"] for entry in labels.values()]
            if set(assigned) != set(skills) or len(assigned) != len(set(assigned)):
                raise ValidationError(f"mapping is not bijective for {case_id}")
            for label, entry in labels.items():
                counts[(entry["skill_id"], label)] += 1
    for skill in skills:
        values = [counts[(skill, label)] for label in LABELS]
        if max(values) - min(values) > 1:
            raise ValidationError(f"position imbalance for {skill}: {values}")
    slices = mapping.get("slice_values", {})
    for slice_name, values_by_case in slices.items():
        if set(values_by_case) != {case_id for packet in mapping["packets"] for case_id in packet["cases"]}:
            raise ValidationError(f"position slice {slice_name} does not cover every case")
        grouped: dict[str, Counter[tuple[str, str]]] = {}
        for slice_value in set(values_by_case.values()):
            grouped[slice_value] = Counter()
        for packet in mapping["packets"]:
            for case_id, labels in packet["cases"].items():
                counter = grouped[values_by_case[case_id]]
                for label, entry in labels.items():
                    counter[(entry["skill_id"], label)] += 1
        for slice_value, counter in grouped.items():
            case_count = sum(value == slice_value for value in values_by_case.values())
            if case_count < 2:
                continue
            for skill in skills:
                position_counts = [counter[(skill, label)] for label in LABELS]
                if max(position_counts) - min(position_counts) > 1:
                    raise ValidationError(f"position imbalance in {slice_name}={slice_value} for {skill}: {position_counts}")
    if paired is not None:
        verify_position_balance(paired)
        combined = counts.copy()
        for packet in paired["packets"]:
            for labels in packet["cases"].values():
                for label, entry in labels.items():
                    combined[(entry["skill_id"], label)] += 1
        totals = {combined[(skill, label)] for skill in skills for label in LABELS}
        if len(totals) != 1:
            raise ValidationError(f"paired batches are not exactly balanced: {sorted(totals)}")


def build_blind_bundle(cases: list[dict[str, Any]], outputs: list[dict[str, Any]], skill_ids: list[str],
                       experiment_id: str, batch_id: str, case_offset: int = 0,
                       judges: int = 3, plan: dict[str, Any] | None = None,
                       slice_values: dict[str, dict[str, str]] | None = None,
                       order_contract: str = "base") -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if judges != 3 or len(skill_ids) != 4:
        raise ValidationError("v1 balanced mapping requires exactly four skills and three judges")
    if len(cases) % 2 or not cases:
        raise ValidationError("blind batch must contain a positive even number of cases")
    case_ids = [case["case_id"] for case in cases]
    if len(case_ids) != len(set(case_ids)):
        raise ValidationError("duplicate cases in blind batch")
    if plan is None:
        raise ValidationError("generation plan is required to bind outputs")
    if order_contract not in {"base", "swapped"}:
        raise ValidationError("order_contract must be base or swapped")
    indexed = validate_outputs(outputs, cases, skill_ids, plan)
    seed = int(hashlib.sha256(f"{experiment_id}|blind-mapping/v1".encode()).hexdigest(), 16)
    skill_order = sorted(skill_ids)
    random.Random(seed).shuffle(skill_order)
    packets = []
    mapping_packets = []
    mapping_skills = []
    derived_slices = slice_values or {
        "family": {case["case_id"]: case["family_id"] for case in cases},
        "language": {case["case_id"]: case["language"] for case in cases},
        "output_form": {case["case_id"]: case["output_form"] for case in cases},
    }
    # Assign a base rotation by balancing the one omitted Latin-square position in
    # every registered slice. Deterministic greedy minimization is sufficient for
    # valid 10-case slices and is verified independently below.
    omission_counts: Counter[tuple[str, str, int]] = Counter()
    global_omissions: Counter[int] = Counter()
    case_rotations = {}
    for local_index, case in enumerate(cases):
        candidates = []
        for rotation in range(4):
            omitted = (rotation + 3) % 4
            penalty = (global_omissions[omitted] + 1) ** 2
            for slice_name, values in derived_slices.items():
                penalty += (omission_counts[(slice_name, values[case["case_id"]], omitted)] + 1) ** 2
            candidates.append((penalty, (rotation - case_offset) % 4, rotation))
        rotation = min(candidates)[2]
        case_rotations[case["case_id"]] = rotation
        omitted = (rotation + 3) % 4
        global_omissions[omitted] += 1
        for slice_name, values in derived_slices.items():
            omission_counts[(slice_name, values[case["case_id"]], omitted)] += 1
    for skill in sorted(skill_ids):
        revisions = {indexed[f"{case_id}\0{skill}"]["skill_revision"] for case_id in case_ids}
        if len(revisions) != 1:
            raise ValidationError(f"batch mixes revisions for {skill}")
        mapping_skills.append({"skill_id": skill, "revision": revisions.pop()})
    for judge_index in range(judges):
        judge_id = f"J{judge_index + 1:02d}"
        packet_cases = []
        case_mapping: dict[str, Any] = {}
        for local_index, case in enumerate(cases):
            rotation = (case_rotations[case["case_id"]] + judge_index) % 4
            ordered = skill_order[rotation:] + skill_order[:rotation]
            if order_contract == "swapped":
                ordered = list(reversed(ordered))
            labels = dict(zip(LABELS, ordered))
            candidates = []
            case_mapping[case["case_id"]] = {}
            for label in LABELS:
                output = indexed[f"{case['case_id']}\0{labels[label]}"]
                candidates.append({"label": label, "text": output["text"], "output_sha256": output["output_sha256"]})
                case_mapping[case["case_id"]][label] = {
                    "skill_id": output["skill_id"],
                    "skill_revision": output["skill_revision"],
                    "task_id": output["task_id"],
                    "output_sha256": output["output_sha256"],
                }
            packet_cases.append({
                "case_id": case["case_id"],
                "family_id": case["family_id"],
                "language": case["language"],
                "length_contract": case["length_contract"],
                "no_op_policy": case["no_op_policy"],
                "prompt": case["prompt"],
                "source": case["source"],
                "constraints": case["constraints"],
                "gates": case["gates"],
                "criteria": case["criteria"],
                "candidates": candidates,
            })
        packet = {"schema_version": "blind-packet/v1", "experiment_id": experiment_id,
                  "batch_id": batch_id, "judge_id": judge_id, "cases": packet_cases}
        packet_sha = sha256_value(packet)
        packets.append(packet)
        mapping_packets.append({"judge_id": judge_id, "packet_sha256": packet_sha, "cases": case_mapping})
    mapping = {
        "schema_version": "blind-mapping/v1",
        "experiment_id": experiment_id,
        "batch_id": batch_id,
        "case_offset": case_offset,
        "order_contract": order_contract,
        "slice_values": derived_slices,
        "skills": mapping_skills,
        "packets": mapping_packets,
    }
    mapping["mapping_sha256"] = sha256_value(mapping)
    verify_position_balance(mapping)
    return packets, mapping


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--cases", type=Path, required=True)
    parser.add_argument("--outputs", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--case-offset", type=int, default=0)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    manifest = load_manifest(args.root)
    cases = read_jsonl([args.cases])
    outputs = read_jsonl([args.outputs])
    packets, mapping = build_blind_bundle(cases, outputs, sorted(manifest["skills"]),
                                          manifest["experiment_id"], args.batch_id, args.case_offset,
                                          plan=read_json(args.plan))
    for packet in packets:
        write_json(args.output_dir / f"packet-{packet['judge_id']}.json", packet)
    write_json(args.output_dir / "mapping.json", mapping)
    print(json.dumps({"batch_id": args.batch_id, "packets": len(packets), "mapping_sha256": mapping["mapping_sha256"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
