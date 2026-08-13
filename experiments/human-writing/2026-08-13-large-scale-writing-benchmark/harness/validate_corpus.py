#!/usr/bin/env python3
"""Validate corpus schemas, hashes, split allocation, and round-robin batches."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any

from common import ROOT, ValidationError, hash_without, load_manifest, load_schema, read_jsonl, sha256_value, validate_schema

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("PyYAML is required for source-lock validation") from exc


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", value).casefold()).strip()


def prompt_shingles(value: str, width: int = 5) -> set[str]:
    words = re.findall(r"[a-z0-9]+|[\u3400-\u9fff]", normalize(value))
    if len(words) < width:
        return {" ".join(words)} if words else set()
    return {" ".join(words[i:i + width]) for i in range(len(words) - width + 1)}


def load_source_locks(root: Path) -> dict[str, Any]:
    path = root / "locks" / "sources.yaml"
    try:
        document = yaml.safe_load(path.read_text())
    except (OSError, yaml.YAMLError) as exc:
        raise ValidationError(f"cannot read source locks: {exc}") from exc
    return document["sources"]


def discover(root: Path) -> list[Path]:
    return sorted((root / "corpus").rglob("*.jsonl"))


def validate_cases(
    cases: list[dict[str, Any]], root: Path = ROOT, complete: bool = True,
    strict_source_locks: bool = False, enforce_partial_manifest: bool = True,
) -> dict[str, Any]:
    manifest = load_manifest(root)
    schema = load_schema("case", root)
    seen: set[str] = set()
    counts: Counter[tuple[str, str]] = Counter()
    wave_counts: Counter[tuple[str, int]] = Counter()
    languages: Counter[tuple[str, str]] = Counter()
    locators: dict[str, str] = {}
    prompt_hashes: dict[str, str] = {}
    shingle_sets: list[tuple[str, set[str]]] = []
    source_locks = load_source_locks(root)
    for case in cases:
        validate_schema(case, schema)
        criterion_ids = [criterion["criterion_id"] for criterion in case["criteria"]]
        if len(criterion_ids) != len(set(criterion_ids)):
            raise ValidationError(f"duplicate criterion_id: {case['case_id']}")
        case_id = case["case_id"]
        if case_id in seen:
            raise ValidationError(f"duplicate case_id: {case_id}")
        seen.add(case_id)
        if hash_without(case, "case_sha256") != case["case_sha256"]:
            raise ValidationError(f"case hash mismatch: {case_id}")
        match = re.fullmatch(r"(F\d\d)-(D|H)(\d\d)", case_id)
        assert match
        family, marker, raw_index = match.groups()
        index = int(raw_index)
        expected_split = "development" if marker == "D" else "holdout"
        expected_batch = (index - 1) // 10 + 1
        if case["family_id"] != family or case["split"] != expected_split or case["batch"] != expected_batch:
            raise ValidationError(f"case identity/split/batch mismatch: {case_id}")
        counts[(family, expected_split)] += 1
        wave_counts[(expected_split, expected_batch)] += 1
        languages[(family, case["language"])] += 1
        locator = case["provenance"]["locator"]
        if locator in locators:
            raise ValidationError(f"duplicate provenance locator: {locators[locator]} and {case_id}")
        locators[locator] = case_id
        digest = hashlib.sha256(normalize(case["prompt"]).encode()).hexdigest()
        if digest in prompt_hashes:
            raise ValidationError(f"cross-split or corpus prompt duplicate: {prompt_hashes[digest]} and {case_id}")
        prompt_hashes[digest] = case_id
        current = prompt_shingles(case["prompt"])
        for other_id, other in shingle_sets:
            similarity = len(current & other) / len(current | other) if current | other else 1.0
            if similarity >= 0.92:
                raise ValidationError(f"cross-split or corpus near duplicate: {other_id} and {case_id}")
        shingle_sets.append((case_id, current))
        evidence_ids = {item["evidence_id"] for item in case["evidence"]}
        if len(evidence_ids) != len(case["evidence"]):
            raise ValidationError(f"duplicate evidence ID: {case_id}")
        for item in case["evidence"]:
            if hashlib.sha256(item["text"].encode()).hexdigest() != item["source_span_sha256"]:
                raise ValidationError(f"evidence hash mismatch: {case_id}")
        claim_ids = {item["claim_id"] for item in case["atomic_claims"]}
        if len(claim_ids) != len(case["atomic_claims"]):
            raise ValidationError(f"duplicate atomic claim ID: {case_id}")
        for claim in case["atomic_claims"]:
            if not set(claim["evidence_ids"]) <= evidence_ids:
                raise ValidationError(f"claim references unknown evidence: {case_id}")
        gate_ids = {item["gate_id"] for item in case["gates"]}
        if len(gate_ids) != len(case["gates"]):
            raise ValidationError(f"duplicate gate ID: {case_id}")
        contains_targets = {item["target"] for item in case["gates"] if item["gate_type"] == "contains"}
        if not set(case["constraints"]["protected"]) <= contains_targets:
            raise ValidationError(f"protected text has no contains gate: {case_id}")
        length = case["length_contract"]
        if length["unit"] == "chars":
            if case["constraints"].get("min_chars") != length["minimum"] or case["constraints"].get("max_chars") != length["maximum"]:
                raise ValidationError(f"character length contract disagrees with constraints: {case_id}")
        if length["source"] == "explicit" and not any(item["gate_type"] == "length" for item in case["gates"]):
            raise ValidationError(f"explicit length contract has no gate: {case_id}")
        if case["no_op_policy"] == "required" and not case["constraints"].get("exact_noop"):
            raise ValidationError(f"required no-op is not backed by exact_noop: {case_id}")
        provenance = case["provenance"]
        source_id = provenance["source_id"]
        if source_id not in source_locks:
            if strict_source_locks:
                raise ValidationError(f"unknown provenance source lock: {case_id}")
        else:
            lock = source_locks[source_id]
            if provenance["revision"] != lock["revision"] or provenance["license"] != lock["license"] or provenance["redistribution"] != lock["redistribution"]:
                raise ValidationError(f"provenance disagrees with source lock: {case_id}")
            if provenance["source_lock_sha256"] != sha256_value(lock):
                raise ValidationError(f"source lock hash mismatch: {case_id}")

    design = manifest["design"]
    expected_families = int(design["families"])
    expected_dev = int(design["development_cases_per_family"])
    expected_holdout = int(design["sealed_holdout_cases_per_family"])
    if complete:
        if len(cases) != expected_families * int(design["cases_per_family"]):
            raise ValidationError(f"expected {expected_families * int(design['cases_per_family'])} cases, got {len(cases)}")
        for family_no in range(1, expected_families + 1):
            family = f"F{family_no:02d}"
            if counts[(family, "development")] != expected_dev:
                raise ValidationError(f"development count mismatch for {family}")
            if counts[(family, "holdout")] != expected_holdout:
                raise ValidationError(f"holdout count mismatch for {family}")
            if languages[(family, "zh")] != 50 or languages[(family, "en")] != 50:
                raise ValidationError(f"language quota mismatch for {family}")
        expected_wave = expected_families * int(design["development_batch_size"])
        for batch in range(1, expected_dev // int(design["development_batch_size"]) + 1):
            if wave_counts[("development", batch)] != expected_wave:
                raise ValidationError(f"development wave {batch} is incomplete")
        for batch in range(1, expected_holdout // int(design["development_batch_size"]) + 1):
            if wave_counts[("holdout", batch)] != expected_wave:
                raise ValidationError(f"holdout wave {batch} is incomplete")
    elif enforce_partial_manifest:
        corpus_state = manifest.get("corpus", {})
        expected_partial = int(corpus_state.get("materialized_cases", 0))
        if expected_partial and len(cases) != expected_partial:
            raise ValidationError(f"partial corpus count mismatch: expected {expected_partial}, got {len(cases)}")
        deferred = set(corpus_state.get("deferred_families", []))
        active = {f"F{number:02d}" for number in range(1, expected_families + 1)} - deferred
        if {case["family_id"] for case in cases} != active:
            raise ValidationError("partial corpus family allocation disagrees with manifest")
        for family in active:
            if counts[(family, "development")] != int(design["development_batch_size"]):
                raise ValidationError(f"partial development batch mismatch for {family}")
            if languages[(family, "zh")] != 5 or languages[(family, "en")] != 5:
                raise ValidationError(f"partial language quota mismatch for {family}")
    return {
        "schema_version": "corpus-report/v1",
        "experiment_id": manifest["experiment_id"],
        "cases": len(cases),
        "families": len({case["family_id"] for case in cases}),
        "splits": {split: sum(value for (family, name), value in counts.items() if name == split) for split in ("development", "holdout")},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--corpus", type=Path, action="append")
    parser.add_argument("--allow-incomplete", action="store_true")
    args = parser.parse_args()
    paths = args.corpus or discover(args.root)
    if not paths:
        raise ValidationError("no corpus JSONL files found")
    print(json.dumps(validate_cases(
        read_jsonl(paths), args.root, not args.allow_incomplete, strict_source_locks=True
    ), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
