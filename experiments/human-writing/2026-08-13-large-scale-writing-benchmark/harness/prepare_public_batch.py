#!/usr/bin/env python3
"""Convert isolated Markdown outputs into one blind, public-benchmark batch."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "harness"))

from blind import build_blind_bundle  # noqa: E402
from common import read_jsonl, sha256_value, write_json  # noqa: E402


SECTION = re.compile(r"^## (F\d{2}-D\d{2})\n(.*?)(?=^## (?:F\d{2}-D\d{2}|Run metadata)\n|\Z)", re.M | re.S)


def parse_markdown(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    sections = {match.group(1): match.group(2).strip() for match in SECTION.finditer(text)}
    if not sections or any(not value for value in sections.values()):
        raise ValueError(f"missing or empty output section in {path}")
    return sections


def prompt_sha(case: dict) -> str:
    return hashlib.sha256(case["prompt"].encode()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", type=Path, required=True)
    parser.add_argument("--skill-output", action="append", nargs=3,
                        metavar=("SKILL_ID", "REVISION", "MARKDOWN"), required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--batch-id", required=True)
    args = parser.parse_args()

    cases = read_jsonl([args.cases])
    case_ids = {case["case_id"] for case in cases}
    skills = [row[0] for row in args.skill_output]
    if len(skills) != 4 or len(set(skills)) != 4:
        raise ValueError("exactly four distinct Skills are required")

    generator_contract = {
        "model_provider": "current-entitlement",
        "model_family": "current-model",
        "model_revision": "unknown",
        "system_prompt_sha256": "0" * 64,
        "decoding": {"temperature": "unknown"},
        "tool_access": "isolated-filesystem",
        "token_limit": "unknown",
        "retry_policy": "none",
    }
    contract_sha = sha256_value(generator_contract)
    tasks = []
    outputs = []
    for skill_id, revision, markdown in args.skill_output:
        sections = parse_markdown(Path(markdown))
        if set(sections) != case_ids:
            raise ValueError(f"case set mismatch for {skill_id}: {sorted(set(sections) ^ case_ids)}")
        for case in cases:
            body = {
                "split": case["split"], "batch": case["batch"],
                "case_id": case["case_id"], "case_sha256": case["case_sha256"],
                "prompt_sha256": prompt_sha(case), "skill_id": skill_id,
                "skill_revision": revision, "replicate": 1,
                "generator_contract_sha256": contract_sha,
            }
            task_id = sha256_value(body)
            task = dict(body, task_id=task_id)
            task["task_sha256"] = sha256_value(task)
            tasks.append(task)
            output_text = sections[case["case_id"]]
            outputs.append({
                **{key: task[key] for key in ("task_id", "task_sha256", "case_id", "case_sha256",
                                                "prompt_sha256", "skill_id", "skill_revision",
                                                "generator_contract_sha256")},
                "text": output_text,
                "output_sha256": hashlib.sha256(output_text.encode()).hexdigest(),
            })

    plan = {"schema_version": "generation-plan/v1", "experiment_id": "human-writing-large-scale-benchmark-2026-08-13",
            "split": "development", "wave": 1, "generator_contract": generator_contract,
            "generator_contract_sha256": contract_sha, "tasks": tasks}
    plan["plan_sha256"] = sha256_value(plan)
    packets, mapping = build_blind_bundle(cases, outputs, skills, plan["experiment_id"], args.batch_id, plan=plan)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.output_dir / "plan.json", plan)
    with (args.output_dir / "outputs.jsonl").open("w", encoding="utf-8") as handle:
        for row in outputs:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    for packet in packets:
        write_json(args.output_dir / f"packet-{packet['judge_id']}.json", packet)
    write_json(args.output_dir / "mapping.json", mapping)
    print(json.dumps({"cases": len(cases), "outputs": len(outputs), "packets": len(packets),
                      "mapping_sha256": mapping["mapping_sha256"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
