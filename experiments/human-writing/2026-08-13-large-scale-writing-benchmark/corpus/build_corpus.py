#!/usr/bin/env python3
"""Build the deterministic first corpus wave and the 1,200-slot allocation plan.

Only sources whose locked bytes are locally available and hash-verified may emit cases.
The current implementation materializes WritingBench development candidates D01-D10
only for families that pass the initial feasibility filter. This is a smoke test, not
a construct-validity claim. Other slots are plans, not fabricated case commitments.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import unicodedata
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError as exc:  # pragma: no cover - explicit dependency failure
    raise SystemExit("PyYAML is required: python -m pip install pyyaml") from exc


SCRIPT_DIR = Path(__file__).resolve().parent
EXPERIMENT_DIR = SCRIPT_DIR.parent
DEFAULT_LOCKS = EXPERIMENT_DIR / "locks" / "sources.yaml"
DEFAULT_FAMILIES = SCRIPT_DIR / "families.yaml"
DEFAULT_SCHEMA = EXPERIMENT_DIR / "schemas" / "case.schema.json"
WRITINGBENCH_RAW = (
    "https://raw.githubusercontent.com/X-PLUG/WritingBench/"
    "ae2d5176449b7b769815482641d35926f26793eb/"
    "benchmark_query/benchmark_all.jsonl"
)
CASE_ID_RE = re.compile(r"^F(?:0[1-9]|1[0-2])-(?:D(?:0[1-9]|[1-7][0-9]|80)|H(?:0[1-9]|1[0-9]|20))$")


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    value = re.sub(r"\s+", " ", value).strip()
    return value


def tokens(value: str) -> list[str]:
    normalized = normalize_text(value)
    return re.findall(r"[a-z0-9]+|[\u3400-\u9fff]", normalized)


def shingles(value: str, width: int = 5) -> set[str]:
    items = tokens(value)
    if len(items) < width:
        return {" ".join(items)} if items else set()
    return {" ".join(items[i : i + width]) for i in range(len(items) - width + 1)}


def jaccard(left: set[str], right: set[str]) -> float:
    if not left and not right:
        return 1.0
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def read_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = yaml.safe_load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"expected mapping in {path}")
    return value


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def materialize_writingbench(source_path: Path | None, cache_dir: Path, lock: dict[str, Any]) -> Path:
    if source_path is None:
        source_path = cache_dir / "writingbench" / lock["revision"] / lock["path"]
        if not source_path.exists():
            source_path.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(WRITINGBENCH_RAW, timeout=90) as response:
                payload = response.read()
            temporary = source_path.with_suffix(".download")
            temporary.write_bytes(payload)
            os.replace(temporary, source_path)
    payload = source_path.read_bytes()
    actual = sha256_bytes(payload)
    expected = lock.get("content_sha256")
    if not expected:
        raise ValueError("WritingBench lock is missing content_sha256")
    if actual != expected:
        raise ValueError(f"WritingBench SHA-256 mismatch: expected {expected}, got {actual}")
    return source_path


def load_writingbench(path: Path, lock: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    required = set(lock["fields"])
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            row = json.loads(line)
            missing = required - row.keys()
            if missing:
                raise ValueError(f"WritingBench row {line_number} missing {sorted(missing)}")
            if row["lang"] not in {"zh", "en"}:
                raise ValueError(f"WritingBench row {line_number} has unsupported lang")
            rows.append(row)
    if len(rows) != lock["expected_rows"]:
        raise ValueError(f"WritingBench expected {lock['expected_rows']} rows, got {len(rows)}")
    if len({row["index"] for row in rows}) != len(rows):
        raise ValueError("WritingBench index is not unique")
    return rows


def matches(row: dict[str, Any], rule: dict[str, Any]) -> bool:
    if rule.get("domain1") and row["domain1"] not in rule["domain1"]:
        return False
    if rule.get("domain2") and row["domain2"] not in rule["domain2"]:
        return False
    if len(row["query"]) < int(rule.get("min_query_chars", 0)):
        return False
    if rule.get("query_regex") and not re.search(rule["query_regex"], row["query"], re.I):
        return False
    return True


def rank_key(seed: str, family_id: str, row: dict[str, Any]) -> str:
    return sha256_text(f"{seed}\0{family_id}\0writingbench\0{row['index']}")


def select_first_wave(
    rows: list[dict[str, Any]], families: dict[str, Any], seed: str, threshold: float
) -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]]]:
    selected: dict[str, list[dict[str, Any]]] = {}
    used_indexes: set[int] = set()
    accepted: list[tuple[str, set[str]]] = []
    rejected_near: list[dict[str, Any]] = []

    for family_id, family in families.items():
        if family.get("first_wave_status") == "deferred_no_fit":
            selected[family_id] = []
            continue
        rule = family["writingbench"]
        family_rows: list[dict[str, Any]] = []
        for language in ("zh", "en"):
            candidates = [
                row
                for row in rows
                if row["lang"] == language
                and row["index"] not in used_indexes
                and matches(row, rule)
            ]
            candidates.sort(key=lambda row: rank_key(seed, family_id, row))
            language_rows: list[dict[str, Any]] = []
            for row in candidates:
                normalized_hash = sha256_text(normalize_text(row["query"]))
                row_shingles = shingles(row["query"])
                collision: tuple[str, float] | None = None
                for other_hash, other_shingles in accepted:
                    similarity = jaccard(row_shingles, other_shingles)
                    if normalized_hash == other_hash or similarity >= threshold:
                        collision = (other_hash, similarity)
                        break
                if collision:
                    rejected_near.append(
                        {
                            "family_id": family_id,
                            "source_index": row["index"],
                            "similarity": round(collision[1], 6),
                        }
                    )
                    continue
                language_rows.append(row)
                used_indexes.add(row["index"])
                accepted.append((normalized_hash, row_shingles))
                if len(language_rows) == 5:
                    break
            if len(language_rows) != 5:
                raise ValueError(
                    f"{family_id} has only {len(language_rows)} usable {language} WritingBench rows"
                )
            family_rows.extend(language_rows)
        family_rows.sort(key=lambda row: (row["lang"], rank_key(seed, family_id, row)))
        selected[family_id] = family_rows
    return selected, rejected_near


def slug(value: str, fallback: str) -> str:
    result = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return result or fallback


def criteria_from_checklist(checklist: list[dict[str, Any]]) -> list[dict[str, Any]]:
    criteria: list[dict[str, Any]] = []
    seen: set[str] = set()
    for position, item in enumerate(checklist[:5], 1):
        criterion_id = slug(str(item.get("name", "")), f"source-{position}")
        if criterion_id in seen:
            criterion_id = f"{criterion_id}-{position}"
        seen.add(criterion_id)
        text = str(item.get("criteria_description", "")).strip()
        if not text:
            continue
        criteria.append({"criterion_id": criterion_id, "text": text, "weight": 1.0})
    if not criteria:
        criteria.append(
            {
                "criterion_id": "task-fit",
                "text": "Satisfy the requested content, audience, and output form without invention.",
                "weight": 1.0,
            }
        )
    return criteria


def source_row_hash(row: dict[str, Any]) -> str:
    return sha256_text(canonical_json(row))


def parse_length_contract(prompt: str, language: str) -> dict[str, Any]:
    patterns = [
        ("words", r"(?:between\s+)?(\d[\d,]*)\s*(?:-|to|and)\s*(\d[\d,]*)\s*words?"),
        ("words", r"(?:at least|minimum of)\s+(\d[\d,]*)\s*words?"),
        ("words", r"(?:no more than|at most|under)\s+(\d[\d,]*)\s*words?"),
        ("chars", r"(\d+)\s*(?:-|到|至)\s*(\d+)\s*(?:字|字符)"),
        ("chars", r"(?:不少于|至少)(\d+)\s*(?:字|字符)"),
        ("chars", r"(?:不超过|最多|控制在)(\d+)\s*(?:字|字符)"),
    ]
    for unit, pattern in patterns:
        match = re.search(pattern, prompt, re.I)
        if not match:
            continue
        values = [int(item.replace(",", "")) for item in match.groups() if item]
        lower = upper = None
        token = match.group(0).casefold()
        if len(values) == 2:
            lower, upper = values
        elif any(term in token for term in ("at least", "minimum", "不少于", "至少")):
            lower = values[0]
        else:
            upper = values[0]
        return {
            "unit": unit, "minimum": lower, "maximum": upper, "source": "explicit",
            "_matched_text": match.group(0),
        }
    return {"unit": "unspecified", "minimum": None, "maximum": None, "source": "unspecified"}


def infer_audience(prompt: str, family_id: str) -> str:
    patterns = [
        r"(?:written|suitable|intended)\s+for\s+([^,.\n]{3,80})",
        r"(?:aimed at|target(?:ing|ed at)?|target audience(?: is|:))\s+([^,.\n]{3,80})",
        r"(?:面向|目标受众(?:是|为)?)[：:]?\s*([^，。\n]{2,40})",
        r"适合([^，。\n]{2,40})(?:阅读|使用|人群|受众)",
    ]
    for pattern in patterns:
        match = re.search(pattern, prompt, re.I)
        if match:
            return match.group(1).strip()
    defaults = {
        "F01": "readers seeking an AI or technical explanation",
        "F02": "software engineering stakeholders",
        "F04": "general blog readers",
        "F05": "the requested social-platform audience",
        "F06": "readers who need a faithful summary",
        "F08": "product or business stakeholders",
        "F09": "the named collaboration recipients",
        "F10": "learners at the level stated in the task",
        "F12": "the product's stated target audience",
    }
    return defaults[family_id]


def infer_operation(prompt: str, fallback: str) -> str:
    """Use the task's explicit verb instead of assigning a family-wide operation."""
    normalized = normalize_text(prompt)
    # WritingBench prompts can embed long source passages. Search the likely instruction
    # edges, not the full passage, so words such as "translation" in a cited paper do not
    # silently relabel a drafting task.
    windows = [normalized[:800]]
    if len(normalized) > 800:
        tail = normalized[-800:]
        if re.search(r"\b(?:please|help me|your task)\b|(?:请|帮我|要求|任务)", tail, re.I):
            windows.append(tail)
    rules = [
        ("summarize", r"\b(?:please\s+)?summari[sz]e\b|(?:请|帮我|需要).{0,16}(?:总结|归纳|概括)"),
        ("rewrite", r"\b(?:rewrite|revise|edit|proofread|polish)\b|(?:改写|修改|润色|校对|修订)"),
        ("adapt", r"\b(?:adapt|convert|translate|locali[sz]e)\b|(?:适配|改编|转换|翻译|本地化)"),
        ("structure", r"\b(?:organize|structure|outline)\b|(?:整理|结构化|列出大纲|提纲)"),
    ]
    for operation, pattern in rules:
        for window in windows:
            if re.search(pattern, window, re.I):
                return operation
    # Most WritingBench records ask the model to create an artifact from a brief.
    # Falling back to draft is safer than forcing a family label such as adapt.
    return "draft" if fallback in {"adapt", "structure"} else fallback


def extract_contract(prompt: str, family_id: str, language: str) -> dict[str, Any]:
    protected = []
    protected_patterns = [
        r"(?:must|should|required to)\s+(?:include|contain|use|preserve)\s+(?:the\s+)?(?:exact\s+)?(?:phrase|string|text|term|title)?\s*[`\"“]([^`\"”\n]{1,120})[`\"”]",
        r"(?:必须|务必|需要)(?:包含|保留|使用|写出)(?:原样|准确)?[：:]?\s*[`\"“]([^`\"”\n]{1,120})[`\"”]",
    ]
    for pattern in protected_patterns:
        for item in re.findall(pattern, prompt, re.I):
            item = item.strip()
            if item and item not in protected:
                protected.append(item)
            if len(protected) == 12:
                break
    length = parse_length_contract(prompt, language)
    length_evidence = length.pop("_matched_text", None)
    evidence_id = "E-task-brief"
    evidence = [{
        "evidence_id": evidence_id,
        "kind": "task_brief",
        "text": prompt,
        "source_span_sha256": sha256_text(prompt),
    }]
    claims = []
    for position, value in enumerate(protected[:8], 1):
        claims.append({
            "claim_id": f"C-protected-{position:02d}",
            "text": f"Preserve the supplied literal or named item: {value}",
            "evidence_ids": [evidence_id],
            "required": True,
        })
    gates = [{
        "gate_id": "G-grounding",
        "gate_type": "grounding",
        "target": "all factual claims",
        "expected": True,
    }]
    for position, value in enumerate(protected[:8], 1):
        gates.append({
            "gate_id": f"G-protected-{position:02d}",
            "gate_type": "contains",
            "target": value,
            "expected": True,
        })
    if length["source"] == "explicit":
        evidence.append({
            "evidence_id": "E-explicit-length",
            "kind": "explicit_constraint",
            "text": length_evidence,
            "source_span_sha256": sha256_text(length_evidence),
        })
        gates.append({
            "gate_id": "G-length",
            "gate_type": "length",
            "target": length["unit"],
            "expected": canonical_json({"minimum": length["minimum"], "maximum": length["maximum"]}),
        })
    omission_patterns = [
        r"(?:may|can)\s+(?:omit|leave out|exclude)\s+([^.;\n]{1,120})",
        r"(?:可以|可)(?:省略|不写|排除)([^。；\n]{1,60})",
    ]
    permitted_omissions = []
    for pattern in omission_patterns:
        match = re.search(pattern, prompt, re.I)
        if match:
            permitted_omissions.append(match.group(1).strip())
    no_op_required = bool(re.search(
        r"(?:if (?:no|there are no) changes? (?:are )?needed.{0,40}(?:return|preserve).{0,20}(?:original|unchanged|verbatim))|"
        r"(?:无需修改|不需要修改).{0,20}(?:原样返回|保持不变)",
        prompt, re.I | re.S,
    ))
    if no_op_required:
        gates.append({
            "gate_id": "G-no-op",
            "gate_type": "no_op",
            "target": "return the supplied artifact unchanged when no edit is needed",
            "expected": True,
        })
    risk_level = "medium" if family_id in {"F01", "F02", "F06", "F08", "F12"} else "low"
    if re.search(r"\b(?:medical|diagnosis|legal advice|investment advice)\b|(?:医疗|诊断|法律意见|投资建议)", prompt, re.I):
        risk_level = "high"
    return {
        "audience": infer_audience(prompt, family_id),
        "length_contract": length,
        "risk_level": risk_level,
        "atomic_claims": claims,
        "evidence": evidence,
        "permitted_omissions": permitted_omissions,
        "gates": gates,
        "no_op_policy": "required" if no_op_required else "forbidden",
        "protected": protected,
    }


def build_case(
    family_id: str,
    ordinal: int,
    family: dict[str, Any],
    row: dict[str, Any],
    lock: dict[str, Any],
) -> dict[str, Any]:
    case_id = f"{family_id}-D{ordinal:02d}"
    content_hash = source_row_hash(row)
    contract = extract_contract(row["query"], family_id, row["lang"])
    source_lock_hash = sha256_text(canonical_json(lock))
    case: dict[str, Any] = {
        "schema_version": "case/v2",
        "case_id": case_id,
        "family_id": family_id,
        "split": "development",
        "batch": 1,
        "language": row["lang"],
        "operation": infer_operation(row["query"], family["operation"]),
        "output_form": row["domain2"],
        "audience": contract["audience"],
        "length_contract": contract["length_contract"],
        "risk_level": contract["risk_level"],
        "prompt": row["query"],
        "source": None,
        "atomic_claims": contract["atomic_claims"],
        "evidence": contract["evidence"],
        "permitted_omissions": contract["permitted_omissions"],
        "gates": contract["gates"],
        "no_op_policy": contract["no_op_policy"],
        "constraints": {
            "protected": contract["protected"],
            "required_fields": [],
            "forbidden_additions": [
                "unsupported facts",
                "invented personal experience",
                "invented measurements or results",
            ],
            "min_chars": contract["length_contract"]["minimum"]
            if contract["length_contract"]["unit"] == "chars" else None,
            "max_chars": contract["length_contract"]["maximum"]
            if contract["length_contract"]["unit"] == "chars" else None,
            "exact_noop": contract["no_op_policy"] == "required",
        },
        "criteria": criteria_from_checklist(row["checklist"]),
        "provenance": {
            "source_id": "writingbench",
            "revision": lock["revision"],
            "license": lock["license"],
            "locator": (
                "https://github.com/X-PLUG/WritingBench/blob/"
                f"{lock['revision']}/{lock['path']}#index-{row['index']}"
            ),
            "content_sha256": content_hash,
            "redistribution": lock["redistribution"],
            "source_lock_sha256": source_lock_hash,
        },
    }
    case["case_sha256"] = sha256_text(canonical_json(case))
    return case


def smooth_schedule(counts: dict[str, int], seed: str) -> list[str]:
    total = sum(counts.values())
    used = Counter()
    result = []
    for position in range(total):
        candidates = [source_id for source_id, count in counts.items() if used[source_id] < count]
        source_id = max(
            candidates,
            key=lambda item: (
                counts[item] * (position + 1) / total - used[item],
                sha256_text(f"{seed}\0{position}\0{item}"),
            ),
        )
        result.append(source_id)
        used[source_id] += 1
    return result


def planned_sources(family_id: str, family: dict[str, Any], seed: str) -> list[str]:
    counts = {source_id: int(count) for source_id, count in family["source_plan"].items()}
    if sum(counts.values()) != 100:
        raise ValueError(f"{family_id} source_plan does not sum to 100")
    materialized_first_wave = family.get("first_wave_status") != "deferred_no_fit"
    prefix: list[str] = []
    if materialized_first_wave:
        if counts.get("writingbench", 0) < 10:
            raise ValueError(f"{family_id} first wave requires ten WritingBench slots")
        prefix = ["writingbench"] * 10
        counts["writingbench"] -= 10
    return prefix + smooth_schedule(counts, f"{seed}\0{family_id}\0remaining")


def build_artifact_indexes(
    families_doc: dict[str, Any],
    source_locks: dict[str, Any],
    locks_path: Path,
    families_path: Path,
    materialized_cases: list[dict[str, Any]],
    seed: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    locks_hash = sha256_bytes(locks_path.read_bytes())
    families_hash = sha256_bytes(families_path.read_bytes())
    policy = {
        "seed": seed,
        "locks_sha256": locks_hash,
        "families_sha256": families_hash,
        "selector": "sha256-ranked-with-global-source-index-uniqueness/v1",
        "near_duplicate": "normalized-token-5gram-jaccard/v1",
    }
    policy_hash = sha256_text(canonical_json(policy))
    materialized = {case["case_id"]: case for case in materialized_cases}
    plan_slots: list[dict[str, Any]] = []
    case_commitments: list[dict[str, Any]] = []
    for family_id, family in families_doc["families"].items():
        source_slots = planned_sources(family_id, family, seed)
        for position in range(1, 101):
            split = "development" if position <= 80 else "holdout"
            ordinal = position if split == "development" else position - 80
            case_id = f"{family_id}-{'D' if split == 'development' else 'H'}{ordinal:02d}"
            source_id = source_slots[position - 1]
            case = materialized.get(case_id)
            source_lock = source_locks[source_id]
            source_revision = source_lock.get("revision")
            if not source_revision:
                raise ValueError(f"planned source {source_id} has no locked revision")
            planned_language = (
                case["language"] if case
                else ("zh" if (position + int(family_id[1:])) % 2 else "en")
            )
            if case:
                commitment_payload = {
                    "case_id": case_id,
                    "source_id": source_id,
                    "source_revision": source_revision,
                    "content_sha256": case["provenance"]["content_sha256"],
                    "case_sha256": case["case_sha256"],
                    "policy_sha256": policy_hash,
                }
                case_commitments.append({
                    "case_id": case_id,
                    "family_id": family_id,
                    "split": split,
                    "source_id": source_id,
                    "source_revision": source_revision,
                    "content_sha256": case["provenance"]["content_sha256"],
                    "case_sha256": case["case_sha256"],
                    "commitment_sha256": sha256_text(canonical_json(commitment_payload)),
                })
            plan_slots.append(
                {
                    "slot_kind": "plan_not_case_commitment",
                    "case_id": case_id,
                    "family_id": family_id,
                    "split": split,
                    "sealed": split == "holdout",
                    "planned_source": source_id,
                    "planned_source_revision": source_revision,
                    "planned_source_status": source_lock["status"],
                    "planned_language": planned_language,
                    "materialized": case is not None,
                    "selector_status": "bound_by_case_commitment" if case else "pending_source_specific_selector",
                }
            )
    plan_document = {
        "schema_version": "corpus-plan-slots/v1",
        "warning": "Unmaterialized entries are allocation plans, not case commitments.",
        "selection_policy": policy,
        "selection_policy_sha256": policy_hash,
        "holdout_policy": {
            "sealed": True,
            "prompt_in_commitments": False,
            "source_locator_in_commitments": False,
            "materialize_after_final_skill_freeze": True,
        },
        "slots": plan_slots,
    }
    commitment_document = {
        "schema_version": "case-commitments/v1",
        "selection_policy_sha256": policy_hash,
        "commitments": case_commitments,
    }
    return plan_document, commitment_document


def validate_case_shape(case: dict[str, Any]) -> None:
    required = {
        "schema_version", "case_id", "family_id", "split", "batch", "language",
        "operation", "output_form", "audience", "length_contract", "risk_level",
        "prompt", "source", "atomic_claims", "evidence", "permitted_omissions",
        "gates", "no_op_policy", "constraints", "criteria",
        "provenance", "case_sha256",
    }
    if set(case) != required:
        raise ValueError(f"{case.get('case_id')} case keys do not match schema")
    if not CASE_ID_RE.fullmatch(case["case_id"]):
        raise ValueError(f"invalid case ID {case['case_id']}")
    copied = dict(case)
    actual = copied.pop("case_sha256")
    expected = sha256_text(canonical_json(copied))
    if actual != expected:
        raise ValueError(f"case hash mismatch for {case['case_id']}")


def validate_no_duplicates(cases: list[dict[str, Any]], threshold: float) -> dict[str, Any]:
    normalized: dict[str, str] = {}
    shingle_sets: list[tuple[str, set[str]]] = []
    comparisons = 0
    maximum = 0.0
    for case in cases:
        digest = sha256_text(normalize_text(case["prompt"]))
        if digest in normalized:
            raise ValueError(f"exact prompt duplicate: {normalized[digest]} and {case['case_id']}")
        normalized[digest] = case["case_id"]
        current = shingles(case["prompt"])
        for other_id, other in shingle_sets:
            comparisons += 1
            similarity = jaccard(current, other)
            maximum = max(maximum, similarity)
            if similarity >= threshold:
                raise ValueError(
                    f"near duplicate >= {threshold}: {other_id} and {case['case_id']} ({similarity:.6f})"
                )
        shingle_sets.append((case["case_id"], current))
    return {
        "status": "pass",
        "algorithm": "normalized-token-5gram-jaccard/v1",
        "threshold": threshold,
        "comparisons": comparisons,
        "maximum_similarity": round(maximum, 6),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locks", type=Path, default=DEFAULT_LOCKS)
    parser.add_argument("--families", type=Path, default=DEFAULT_FAMILIES)
    parser.add_argument("--writingbench-path", type=Path)
    parser.add_argument("--cache-dir", type=Path, default=SCRIPT_DIR / ".cache")
    parser.add_argument("--output-dir", type=Path, default=SCRIPT_DIR)
    parser.add_argument("--print-report", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    locks_doc = read_yaml(args.locks)
    families_doc = read_yaml(args.families)
    source_locks = locks_doc["sources"]
    families = families_doc["families"]
    if len(families) != 12:
        raise ValueError(f"expected 12 families, got {len(families)}")
    threshold = float(families_doc["near_duplicate_threshold"])
    seed = str(locks_doc["selection_seed"])

    writingbench_path = materialize_writingbench(
        args.writingbench_path, args.cache_dir, source_locks["writingbench"]
    )
    rows = load_writingbench(writingbench_path, source_locks["writingbench"])
    selected, rejected_near = select_first_wave(rows, families, seed, threshold)

    cases: list[dict[str, Any]] = []
    for family_id, family_rows in selected.items():
        family = families[family_id]
        # IDs deliberately alternate language so every ten-case review is balanced.
        zh_rows = [row for row in family_rows if row["lang"] == "zh"]
        en_rows = [row for row in family_rows if row["lang"] == "en"]
        interleaved = [item for pair in zip(zh_rows, en_rows) for item in pair]
        for ordinal, row in enumerate(interleaved, 1):
            case = build_case(
                family_id, ordinal, family, row, source_locks["writingbench"]
            )
            validate_case_shape(case)
            cases.append(case)

    expected_first_wave = 10 * sum(
        family.get("first_wave_status") != "deferred_no_fit" for family in families.values()
    )
    if len(cases) != expected_first_wave:
        raise ValueError(f"expected {expected_first_wave} first-wave cases, got {len(cases)}")
    duplicate_gate = validate_no_duplicates(cases, threshold)
    plan_slots, case_commitments = build_artifact_indexes(
        families_doc, source_locks, args.locks, args.families, cases, seed
    )
    if len(plan_slots["slots"]) != 1200:
        raise ValueError("plan must contain exactly 1,200 slots")
    if len(case_commitments["commitments"]) != len(cases):
        raise ValueError("every materialized case must have exactly one commitment")
    for slot in plan_slots["slots"]:
        if slot["sealed"] and any(key in slot for key in ("prompt", "query", "locator", "source_index")):
            raise ValueError(f"sealed holdout metadata leak in {slot['case_id']}")
    for family_id in families:
        family_slots = [slot for slot in plan_slots["slots"] if slot["family_id"] == family_id]
        planned_counts = Counter(slot["planned_source"] for slot in family_slots)
        expected_counts = Counter({key: int(value) for key, value in families[family_id]["source_plan"].items()})
        if planned_counts != expected_counts:
            raise ValueError(f"{family_id} source-plan quota mismatch: {planned_counts} != {expected_counts}")
        if any(slot["materialized"] and slot["planned_language"] != next(
            case["language"] for case in cases if case["case_id"] == slot["case_id"]
        ) for slot in family_slots):
            raise ValueError(f"{family_id} materialized language disagrees with plan slot")
        holdout = [slot for slot in plan_slots["slots"] if slot["family_id"] == family_id and slot["sealed"]]
        if Counter(slot["planned_language"] for slot in holdout) != {"zh": 10, "en": 10}:
            raise ValueError(f"{family_id} holdout language plan is not balanced")
        if len(families[family_id]["source_plan"]) > 1 and len({slot["planned_source"] for slot in holdout}) < 2:
            raise ValueError(f"{family_id} holdout source plan is not diversified")

    family_counts = Counter(case["family_id"] for case in cases)
    language_counts = Counter(case["language"] for case in cases)
    source_state = {source_id: lock["status"] for source_id, lock in source_locks.items()}
    report = {
        "schema_version": "corpus-report/v1",
        "status": "candidate_smoke_test_materialized",
        "target_cases": 1200,
        "materialized_cases": len(cases),
        "pending_cases": 1200 - len(cases),
        "materialized_wave": "local candidate smoke test; no family validity claim",
        "case_file": "cases.wave-01.jsonl",
        "case_file_distribution": "local_only_untracked_pending_third_party_review",
        "rebuild_command": "WRITINGBENCH_PATH=/absolute/path/benchmark_all.jsonl python corpus/build_corpus.py --writingbench-path $WRITINGBENCH_PATH",
        "case_commitments_file": "case-commitments.json",
        "plan_slots_file": "plan-slots.json",
        "case_file_sha256": sha256_text("".join(canonical_json(case) + "\n" for case in cases)),
        "family_counts": dict(sorted(family_counts.items())),
        "language_counts": dict(sorted(language_counts.items())),
        "source_states": source_state,
        "gates": {
            "writingbench_hash": "pass",
            "required_fields": "pass",
            "case_schema_shape": "pass",
            "materialized_exact_and_near_duplicate": duplicate_gate,
            "cross_split_duplicate": "pending_holdout_not_materialized",
            "holdout_prompt_exposure": "pass",
            "source_lock_binding": "pass",
            "plan_source_quotas": "pass",
            "holdout_source_and_language_plan": "pass",
            "third_party_redistribution_review": "pending_blocking_publication",
        },
        "selection_rejections": {
            "near_duplicates_before_final_selection": len(rejected_near),
            "details": rejected_near,
        },
        "limitations": [
            f"Only {len(cases)} WritingBench candidate smoke-test cases are materialized; construct validity is not claimed.",
            "Deferred families: " + ", ".join(
                family_id for family_id, family in families.items()
                if family.get("first_wave_status") == "deferred_no_fit"
            ) + ".",
            f"The {1200 - len(cases)} remaining entries are plan slots, not case commitments.",
            "Cross-split near-duplicate validation cannot complete until sealed holdout materialization.",
            "Non-WritingBench sources remain locked but byte-level hashing and selection are pending.",
        ],
    }

    case_text = "".join(canonical_json(case) + "\n" for case in cases)
    atomic_write(args.output_dir / "cases.wave-01.jsonl", case_text)
    atomic_write(args.output_dir / "case-commitments.json", json.dumps(case_commitments, ensure_ascii=False, indent=2) + "\n")
    atomic_write(args.output_dir / "plan-slots.json", json.dumps(plan_slots, ensure_ascii=False, indent=2) + "\n")
    atomic_write(args.output_dir / "corpus-report.json", json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    if args.print_report:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError, KeyError) as exc:
        print(f"build_corpus.py: error: {exc}", file=sys.stderr)
        raise SystemExit(1)
