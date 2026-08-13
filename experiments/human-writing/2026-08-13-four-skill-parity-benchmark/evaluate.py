#!/usr/bin/env python3
"""Deterministic checks and blind-packet builder for the four-skill writing pilot."""

from __future__ import annotations

import hashlib
import json
import random
import re
import subprocess
import sys
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS = ["human-writing", "humanizer", "humanizer-zh", "stop-slop"]
CASE_IDS = ["C01", "C02", "C03", "C04", "C05", "C06", "N01", "N02", "N03", "N04"]
OUTPUT_IDS = dict(zip(CASE_IDS, [f"T{i:02d}" for i in range(1, 11)]))
NEGATIVE = {"N01", "N02", "N03", "N04"}
SOURCE_COMMIT = "325c9daeb34df0abaee8f4efa8e715a6f0547887"
PROTECTED = {
    "C01": ["GitHub", "Google Drive", "ChatGPT Library", "Google Sheets", "生产 Skill"],
    "C02": ["Awesome List", "Output", "来源卡", "知识图谱", "实验/应用证据"],
    "C03": ["checkpoint", "agent", "function tools", "Apache-2.0", "LiveKit", "MODEL_LICENSE"],
    "C04": ["typed graph execution", "run identity/history", "approval/deferred flows", "Agent", "provider/native-tool", "CI", "runtime_validated"],
    "C05": ["`--verify-remote`", "`gh api`", "path/tree blob SHA", "Git blob SHA", "locator", "Markdown", "`SECURITY.md#security`", "`Not verified`", "token"],
    "C06": ["Activepieces", "Trigger.dev", "Hexabot", "exactly-once", "LLM", "“Workflow”", "five malformed", "three multi-root JSON files", "SSH", "`active=true`", "Golutra"],
    "N01": ["Global AGENTS", "45 行", "UserPromptSubmit", "`240000`", "4", "`adaptive-collaboration`", "`spawn_agent`", "2026-08-11", "57", "15", "208", "100"],
    "N02": ["Star", "Awesome List", "GitHub Stars", "description", "README", "Skill", "Agent"],
    "N03": ["canonical", "Eval", "许可证", "安全边界", "固定版本"],
    "N04": ["canonical index", "run report", "retrospective", "shard", "`owner/name`", "repository identity", "fork", "archive", "mirror", "empty", "adjacent", "unclear", "reconciliation", "canonical totals", "deep-analysis queue", "`snapshot_id`", "`source_commit`", "`status=ready`", "commit"],
}
CASE_CRITERIA = {
    "C01": "Keep the five storage/automation responsibilities distinct and preserve normative modality, especially automatic-only limits.",
    "C02": "Keep each preference, counter-limit, before/after action, and stopping condition paired with the claim it qualifies.",
    "C03": "Preserve the difference between design focus, authorization, and licensing; do not turn an interpretation boundary into categorical unusability.",
    "C04": "Preserve the four explicit arguments and every evidence ceiling, including that durability is not automatic for every Agent run.",
    "C05": "Preserve the complete verification chain, locator matching modalities, counterexample, and fail-closed behavior.",
    "C06": "Preserve all five findings, counts, examples, and especially the scope word automatically in the exactly-once limitation.",
    "N01": "The input is already compact; evaluate exact preservation under the explicit conditional no-op instruction.",
    "N02": "The input is already compact; evaluate exact preservation under the explicit conditional no-op instruction.",
    "N03": "The input is already compact; evaluate exact preservation under the explicit conditional no-op instruction.",
    "N04": "The input is already compact; evaluate exact preservation under the explicit conditional no-op instruction.",
}
RUBRIC = """## Scoring rubric

Score each dimension independently from 1 to 5. Use 2 and 4 for cases between anchors.

- **Fidelity:** 5 = every fact, actor, relation, scope, modality and uncertainty is preserved; 3 = a localized omission/strength change is present but the main conclusion remains usable; 1 = invented facts or a material reversal. Record every factual omission/addition or modality/claim-strength change as `hard_issue`. A localized hard issue caps Fidelity at 3; a material reversal caps it at 1.
- **Instruction/structure:** 5 = all explicit format and scope requirements are met and claims are grouped by coherent semantic unit; 3 = compliant but noticeably fragmented, merged, or structurally awkward; 1 = required format/scope is ignored.
- **Clarity:** 5 = immediately understandable with precise referents and relationships; 3 = understandable after rereading or scanning avoidable density; 1 = ambiguous or internally confusing.
- **Naturalness:** 5 = direct, idiomatic professional prose without staged transitions or mechanical cadence; 3 = noticeable checklist/template rhythm or awkward phrasing; 1 = strongly formulaic or unidiomatic.
- **Restraint:** 5 = removes only reader-visible problems and keeps already-effective wording; 3 = needless splitting, polishing, or normalization without factual damage; 1 = extensive unnecessary rewriting or voice flattening.

The reference is a style and fidelity aid, not the only valid wording. Do not reward literal similarity by itself. A protected-span pass does not prove semantic fidelity.
"""


def sections(text: str) -> dict[str, str]:
    hits = list(re.finditer(r"^## ([CNT]\d\d)(?:\s.*)?$", text, re.M))
    result = {}
    for idx, hit in enumerate(hits):
        end = hits[idx + 1].start() if idx + 1 < len(hits) else len(text)
        result[hit.group(1)] = text[hit.end():end].strip()
    return result


def case_fields(body: str) -> tuple[str, str]:
    if "Reference and input are identical:" in body:
        value = body.split("Reference and input are identical:", 1)[1].strip()
        return value, value
    reference, rest = body.split("Reference:", 1)[1].split("Input:", 1)
    return reference.strip(), rest.strip()


def source_path(body: str) -> str:
    return re.search(r"^Source: `([^`]+)`$", body, re.M).group(1)


def clean_output(body: str) -> str:
    return body.split("## Run metadata", 1)[0].strip()


def sha256(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


cases = sections((ROOT / "cases.md").read_text())
outputs = {
    skill: sections((ROOT / "outputs" / f"{skill}.md").read_text())
    for skill in SKILLS
}

rows = []
for case_id in CASE_IDS:
    reference, input_text = case_fields(cases[case_id])
    source = source_path(cases[case_id])
    source_text = subprocess.run(
        ["git", "show", f"{SOURCE_COMMIT}:{source}"],
        cwd=ROOT.parents[2], check=True, capture_output=True, text=True,
    ).stdout
    reference_exact = reference in source_text
    for skill in SKILLS:
        output = clean_output(outputs[skill][OUTPUT_IDS[case_id]])
        missing = [span for span in PROTECTED[case_id] if span not in output]
        rows.append({
            "case_id": case_id,
            "skill": skill,
            "negative_control": case_id in NEGATIVE,
            "source_path": source,
            "source_reference_exact": reference_exact,
            "protected_pass": not missing,
            "missing_protected": missing,
            "negative_exact": output == reference if case_id in NEGATIVE else None,
            "reference_similarity": round(SequenceMatcher(None, reference, output).ratio(), 4),
            "input_similarity": round(SequenceMatcher(None, input_text, output).ratio(), 4),
            "input_chars": len(input_text),
            "output_chars": len(output),
            "output_sha256": sha256(output),
        })

summary = {}
for skill in SKILLS:
    own = [row for row in rows if row["skill"] == skill]
    summary[skill] = {
        "protected_pass_cases": sum(row["protected_pass"] for row in own),
        "protected_total_cases": len(own),
        "negative_exact_cases": sum(row["negative_exact"] is True for row in own),
        "negative_total_cases": len(NEGATIVE),
        "mean_reference_similarity": round(sum(row["reference_similarity"] for row in own) / len(own), 4),
        "mean_input_similarity": round(sum(row["input_similarity"] for row in own) / len(own), 4),
    }

(ROOT / "results").mkdir(exist_ok=True)
(ROOT / "results" / "automatic.json").write_text(json.dumps({"rows": rows, "summary": summary}, ensure_ascii=False, indent=2) + "\n")
if not all(row["source_reference_exact"] and row["protected_pass"] for row in rows):
    print("deterministic source/protected gate failed", file=sys.stderr)
    raise SystemExit(1)
if not all(row["negative_exact"] is True for row in rows if row["negative_control"]):
    print("conditional no-op gate failed", file=sys.stderr)
    raise SystemExit(1)

rng = random.Random(20260813)
mappings = {}
labels = ["A", "B", "C", "D"]
initial_order = SKILLS[:]
rng.shuffle(initial_order)
base_orders = {
    case_id: initial_order[index % 4:] + initial_order[:index % 4]
    for index, case_id in enumerate(CASE_IDS)
}
for judge_no in (1, 2, 3):
    mapping = {}
    packet = ["# Blind review packet", "", f"Judge packet {judge_no}; skill identities are withheld.", "", RUBRIC]
    for case_index, case_id in enumerate(CASE_IDS):
        reference, input_text = case_fields(cases[case_id])
        # Base permutation varies by case; each judge then receives a Latin rotation.
        base = base_orders[case_id]
        rotated = base[judge_no - 1:] + base[:judge_no - 1]
        case_mapping = dict(zip(labels, rotated))
        mapping[case_id] = case_mapping
        packet += [f"## {case_id}", "", f"Case-specific criterion: {CASE_CRITERIA[case_id]}", "", "### Input", "", input_text, "", "### Reference", "", reference, ""]
        for label, skill in case_mapping.items():
            packet += [f"### Candidate {label}", "", clean_output(outputs[skill][OUTPUT_IDS[case_id]]), ""]
    mappings[str(judge_no)] = mapping
    (ROOT / "results" / f"blind-review-{judge_no}.md").write_text("\n".join(packet).rstrip() + "\n")

(ROOT / "results" / "blind-mappings.json").write_text(json.dumps(mappings, ensure_ascii=False, indent=2) + "\n")

print(json.dumps(summary, ensure_ascii=False, indent=2))
