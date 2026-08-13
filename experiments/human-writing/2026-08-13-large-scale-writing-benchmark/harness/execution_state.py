#!/usr/bin/env python3
"""Fail-closed development-wave review and revision state machine."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from aggregate import aggregate_bundles, load_bundle
from blind import validate_outputs
from common import ValidationError, ROOT, hash_without, load_manifest, read_json, read_jsonl, sha256_value, skill_revisions, write_json
from deterministic_gates import validate_gate_report
from evidence import base_evidence_digest
from validate_review import validate_wave_reviews


def initialize(root=None) -> dict[str, Any]:
    manifest = load_manifest() if root is None else load_manifest(root)
    revisions = skill_revisions(manifest)
    state = {
        "schema_version": "benchmark-execution-state/v1",
        "experiment_id": manifest["experiment_id"],
        "phase": "development",
        "next_wave": 1,
        "current_revisions": revisions,
        "completed_waves": [],
        "candidate_revision": None,
        "state_sha256": "",
    }
    state["state_sha256"] = hash_without(state, "state_sha256")
    return state


def _validate_state(state: dict[str, Any]) -> None:
    allowed = {"schema_version", "experiment_id", "phase", "next_wave", "current_revisions", "completed_waves", "candidate_revision", "state_sha256"}
    if set(state) != allowed or state["schema_version"] != "benchmark-execution-state/v1" or hash_without(state, "state_sha256") != state["state_sha256"]:
        raise ValidationError("benchmark execution state contract/hash invalid")
    if state["phase"] not in {"development", "candidate_frozen", "holdout_complete"}:
        raise ValidationError("benchmark execution phase invalid")


def complete_development_wave(state: dict[str, Any], wave: int, cases: list[dict[str, Any]], plan: dict[str, Any],
                              outputs: list[dict[str, Any]], gate_report: dict[str, Any], aggregate: dict[str, Any],
                              reviews: list[dict[str, Any]], bundles: list[tuple[dict[str,Any],dict[str,dict[str,Any]],dict[str,dict[str,Any]]]]) -> dict[str, Any]:
    _validate_state(state)
    if state["phase"] != "development" or wave != state["next_wave"] or not 1 <= wave <= 8:
        raise ValidationError("development wave is not currently open")
    expected_case_ids = {f"F{family:02d}-D{index:02d}" for family in range(1, 13)
                         for index in range((wave-1)*10+1, wave*10+1)}
    if {case["case_id"] for case in cases} != expected_case_ids:
        raise ValidationError("wave case set is incomplete")
    skills = sorted(state["current_revisions"])
    if len(plan.get("tasks", [])) != 480:
        raise ValidationError("development wave requires exactly 480 planned tasks")
    planned_revisions = {skill: {task["skill_revision"] for task in plan["tasks"] if task["skill_id"] == skill} for skill in skills}
    if any(planned_revisions[skill] != {state["current_revisions"][skill]} for skill in skills):
        raise ValidationError("generation plan revisions differ from the open-wave state")
    if "plan_sha256" in plan and hash_without(plan, "plan_sha256") != plan["plan_sha256"]:
        raise ValidationError("generation plan hash invalid")
    indexed = validate_outputs(outputs, cases, skills, plan)
    expected_outputs = {row["task_id"]: {"output_sha256": row["output_sha256"]} for row in indexed.values()}
    validate_gate_report(gate_report, expected_outputs, {case["case_id"]: case for case in cases})
    if (aggregate.get("schema_version") != "aggregate/v2" or aggregate.get("mode") != "development_partial"
            or aggregate.get("experiment_id") != plan.get("experiment_id", aggregate.get("experiment_id"))
            or aggregate.get("cases") != 120 or hash_without(aggregate, "aggregate_sha256") != aggregate.get("aggregate_sha256")):
        raise ValidationError("validated 120-case development aggregate is required")
    if len(bundles) != 1:
        raise ValidationError("one complete blind/judge artifact bundle is required for a development wave")
    recomputed = aggregate_bundles(bundles, [gate_report])
    if aggregate != recomputed or aggregate.get("input_evidence_sha256") != base_evidence_digest(bundles, [gate_report]):
        raise ValidationError("aggregate does not match the complete blind/judge input commitment")
    summaries = list(aggregate.get("summary", {}).values())
    observed = {(item.get("skill_id"), item.get("skill_revision"), item.get("split"), item.get("cases")) for item in summaries}
    expected_summaries = {(skill, state["current_revisions"][skill], "development", 120) for skill in skills}
    if observed != expected_summaries or len(summaries) != len(skills):
        raise ValidationError("development aggregate revision/skill coverage differs from the open wave")
    previous = state["current_revisions"]["human-writing"]
    decision = validate_wave_reviews(reviews, previous, expected_case_ids)
    global_review = next(review for review in reviews if review["scope"] == "global_wave")
    updated = {key: value for key, value in state.items() if key != "state_sha256"}
    execution_input_sha256 = sha256_value({
        "plan_sha256": plan.get("plan_sha256", sha256_value(plan)),
        "outputs_sha256": sha256_value(sorted((row["task_id"], row["output_sha256"]) for row in outputs)),
        "gate_report_sha256": gate_report["report_sha256"],
        "blind_judge_evidence_sha256": aggregate["input_evidence_sha256"],
    })
    updated["completed_waves"] = state["completed_waves"] + [{
        "wave": wave,
        "human_writing_revision": previous,
        "plan_sha256": plan.get("plan_sha256", sha256_value(plan)),
        "outputs_sha256": sha256_value(sorted((row["task_id"], row["output_sha256"]) for row in outputs)),
        "gate_report_sha256": gate_report["report_sha256"],
        "aggregate_sha256": aggregate["aggregate_sha256"],
        "execution_input_sha256": execution_input_sha256,
        "reviews_sha256": sha256_value(sorted(review["review_sha256"] for review in reviews)),
        "decision": decision["global_decision"],
    }]
    if global_review["decision"] == "accepted":
        updated["current_revisions"] = dict(state["current_revisions"])
        updated["current_revisions"]["human-writing"] = global_review["next_revision"]
    updated["next_wave"] = wave + 1
    if wave == 8:
        updated["phase"] = "candidate_frozen"
        updated["candidate_revision"] = updated["current_revisions"]["human-writing"]
    updated["state_sha256"] = sha256_value(updated)
    return updated


def revisions_for_next_wave(state: dict[str, Any]) -> dict[str, str]:
    _validate_state(state)
    if state["phase"] != "development" or not 1 <= state["next_wave"] <= 8:
        raise ValidationError("no development wave is open")
    return dict(state["current_revisions"])


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init"); init.add_argument("--root", type=Path, default=ROOT); init.add_argument("--output", type=Path, required=True)
    complete = sub.add_parser("complete-dev")
    complete.add_argument("--state", type=Path, required=True); complete.add_argument("--wave", type=int, required=True)
    complete.add_argument("--cases", type=Path, required=True); complete.add_argument("--plan", type=Path, required=True)
    complete.add_argument("--outputs", type=Path, required=True); complete.add_argument("--gate-report", type=Path, required=True)
    complete.add_argument("--aggregate", type=Path, required=True); complete.add_argument("--review", type=Path, action="append", required=True)
    complete.add_argument("--bundle", type=Path, action="append", required=True)
    complete.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "init":
        result = initialize(args.root)
    else:
        reviews = []
        for path in args.review:
            if path.suffix == ".jsonl": reviews.extend(read_jsonl([path]))
            else: reviews.append(read_json(path))
        result = complete_development_wave(read_json(args.state), args.wave, read_jsonl([args.cases]), read_json(args.plan),
                                           read_jsonl([args.outputs]), read_json(args.gate_report), read_json(args.aggregate), reviews,
                                           [load_bundle(path) for path in args.bundle])
    write_json(args.output, result)
    print(json.dumps({"phase": result["phase"], "next_wave": result["next_wave"], "state_sha256": result["state_sha256"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
