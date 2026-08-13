#!/usr/bin/env python3
"""Build deterministic round-robin generation tasks and resume views."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from common import ROOT, ValidationError, load_manifest, read_json, read_jsonl, sha256_value, skill_revisions, write_json
from validate_corpus import discover, validate_cases
from holdout import require_unlocked


def load_revision_schedule(path: Path | None, defaults: dict[str, str]) -> dict[str, Any]:
    if path is None:
        return {"development": {}, "holdout": defaults}
    value = read_json(path)
    if not isinstance(value, dict) or set(value) != {"development", "holdout"}:
        raise ValidationError("revision schedule must contain only development and holdout")
    return value


def revisions_for(schedule: dict[str, Any], split: str, wave: int, defaults: dict[str, str]) -> dict[str, str]:
    value = schedule["holdout"] if split == "holdout" else schedule["development"].get(str(wave), defaults)
    if set(value) != set(defaults):
        raise ValidationError(f"revision schedule skill set mismatch for {split} wave {wave}")
    for skill_id, revision in value.items():
        if not isinstance(revision, str) or len(revision) != 40 or any(ch not in "0123456789abcdef" for ch in revision):
            raise ValidationError(f"invalid revision for {skill_id} in {split} wave {wave}")
        if skill_id != "human-writing" and revision != defaults[skill_id]:
            raise ValidationError(f"fixed comparator revision changed for {skill_id}")
    return value


def build_plan(cases: list[dict[str, Any]], root: Path = ROOT, schedule: dict[str, Any] | None = None,
               completed: list[dict[str, Any]] | None = None,
               generator_contract: dict[str, Any] | None = None,
               holdout_state: dict[str, Any] | None = None) -> dict[str, Any]:
    validate_cases(cases, root, complete=False, enforce_partial_manifest=False)
    splits = {case["split"] for case in cases}
    if len(splits) != 1:
        raise ValidationError("one plan must contain exactly one split")
    split = splits.pop()
    case_ids = {case["case_id"] for case in cases}
    if split == "development":
        waves = {case["batch"] for case in cases}
        if len(waves) != 1 or len(cases) != 120:
            raise ValidationError("development plan requires one complete 120-case round-robin wave")
        wave = waves.pop()
        expected = {f"F{family:02d}-D{index:02d}" for family in range(1, 13) for index in range((wave-1)*10+1, wave*10+1)}
    else:
        if len(cases) != 240:
            raise ValidationError("holdout plan requires the complete 240-case sealed split")
        expected = {f"F{family:02d}-H{index:02d}" for family in range(1, 13) for index in range(1, 21)}
    if case_ids != expected:
        raise ValidationError(f"{split} plan case set is incomplete or unexpected")
    manifest = load_manifest(root)
    defaults = skill_revisions(manifest)
    schedule = schedule or {"development": {}, "holdout": defaults}
    required_generator = {"model_provider", "model_family", "model_revision", "system_prompt_sha256", "decoding", "tool_access", "token_limit", "retry_policy"}
    if generator_contract is None or set(generator_contract) != required_generator:
        raise ValidationError("explicit frozen generator contract is required")
    if any(generator_contract[key] is None or generator_contract[key] == "" or generator_contract[key] == "fixed_before_first_batch" for key in required_generator):
        raise ValidationError("generator contract contains unresolved values")
    generator_contract_sha256 = sha256_value(generator_contract)
    if split == "holdout":
        if holdout_state is None:
            raise ValidationError("holdout tasks require an unlocked holdout state")
        require_unlocked(holdout_state, revisions_for(schedule, "holdout", 1, defaults)["human-writing"])
    tasks = []
    for case in sorted(cases, key=lambda item: (item["split"], item["batch"], item["family_id"], item["case_id"])):
        revisions = revisions_for(schedule, case["split"], case["batch"], defaults)
        for skill_id in sorted(defaults):
            body = {
                "schema_version": "generation-task/v1",
                "experiment_id": manifest["experiment_id"],
                "split": case["split"],
                "wave": case["batch"],
                "case_id": case["case_id"],
                "family_id": case["family_id"],
                "case_sha256": case["case_sha256"],
                "prompt_sha256": sha256_value(case["prompt"]),
                "skill_id": skill_id,
                "skill_revision": revisions[skill_id],
                "generator_contract_sha256": generator_contract_sha256,
                "replicate": 1,
            }
            body["task_id"] = sha256_value(body)
            body["task_sha256"] = sha256_value(body)
            tasks.append(body)
    completed_ids = set()
    expected_pairs = {(task["task_id"], task["task_sha256"]) for task in tasks}
    seen_receipts: set[str] = set()
    for receipt in completed or []:
        if set(receipt) != {"task_id", "task_sha256", "status"} or receipt["status"] != "success":
            raise ValidationError("completed receipt must contain task_id, task_sha256, status=success")
        if receipt["task_id"] in seen_receipts:
            raise ValidationError(f"duplicate completed receipt: {receipt['task_id']}")
        seen_receipts.add(receipt["task_id"])
        pair = (receipt["task_id"], receipt["task_sha256"])
        if pair not in expected_pairs:
            raise ValidationError(f"completed receipt does not match this plan: {receipt['task_id']}")
        completed_ids.add(pair)
    pending = [task["task_id"] for task in tasks if (task["task_id"], task["task_sha256"]) not in completed_ids]
    plan = {
        "schema_version": "generation-plan/v1",
        "experiment_id": manifest["experiment_id"],
        "task_count": len(tasks),
        "pending_count": len(pending),
        "tasks": tasks,
        "pending_task_ids": pending,
        "generator_contract": generator_contract,
        "generator_contract_sha256": generator_contract_sha256,
    }
    plan["plan_sha256"] = sha256_value(plan)
    return plan


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--corpus", type=Path, action="append")
    parser.add_argument("--revisions", type=Path)
    parser.add_argument("--completed", type=Path, action="append")
    parser.add_argument("--generator-contract", type=Path, required=True)
    parser.add_argument("--holdout-state", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cases = read_jsonl(args.corpus or discover(args.root))
    defaults = skill_revisions(load_manifest(args.root))
    schedule = load_revision_schedule(args.revisions, defaults)
    receipts = read_jsonl(args.completed) if args.completed else []
    state = read_json(args.holdout_state) if args.holdout_state else None
    write_json(args.output, build_plan(cases, args.root, schedule, receipts, read_json(args.generator_contract), state))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
