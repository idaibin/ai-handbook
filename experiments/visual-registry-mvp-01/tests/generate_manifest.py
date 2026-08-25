#!/usr/bin/env python3
import hashlib
import json
import platform
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACKED_DIRS = [
    "schema",
    "contracts",
    "cases",
    "image-cases",
    "prompt-cases",
    "prototype",
    "tests",
    "sources",
]
TRACKED_FILES = [
    ".gitignore",
    "README.md",
    "SOURCES.md",
    "EXECUTION.md",
    "package.json",
    "tsconfig.json",
    "run-tests.sh",
    "requirements.txt",
]
EVIDENCE_FILES = [
    "evidence/schema-validation.json",
    "evidence/compiler-test.json",
    "evidence/query-test.json",
    "evidence/image-case-test.json",
    "evidence/prompt-case-test.json",
    "evidence/compiler-output.json",
    "evidence/query-index.json",
    "evidence/image-case-prompts.json",
    "evidence/determinism-rerun.json",
    "evidence/clean-copy-validation.json",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def version(command: list[str]) -> str:
    return subprocess.check_output(command, text=True).strip()


paths: list[Path] = []
for directory in TRACKED_DIRS:
    paths.extend(
        path
        for path in (ROOT / directory).rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    )
paths.extend(ROOT / name for name in TRACKED_FILES)
paths.extend(ROOT / name for name in EVIDENCE_FILES if (ROOT / name).exists())
paths = sorted(set(paths), key=lambda path: path.relative_to(ROOT).as_posix())

manifest = {
    "experiment": "visual-registry-mvp-01",
    "unit": "UNIT_04_GENERATION_BATCH_QUERY_CONTRACT",
    "status": "passed_contract_and_query_validation_generation_blocked",
    "validation_level": "static_unit_and_clean_copy_tests",
    "basis": {
        "repository": "idaibin/ai-handbook",
        "commit_before_implementation": "ee0969c45407380a3d8a343b655dae22c8b5cfdb",
        "design_path": "research/visual-registry/2026-08-24-visual-registry-mvp-01.md",
        "drive_contract": "visual-registry-prompt-1vn-contract-v0.1.json",
    },
    "environment": {
        "node": version(["node", "--version"]),
        "typescript": version(["tsc", "--version"]),
        "python": platform.python_version(),
        "jsonschema": version(
            ["python3", "-c", "from importlib.metadata import version; print(version('jsonschema'))"]
        ),
    },
    "trial": {
        "contracts": 3,
        "consumer_cases": 3,
        "image_comparison_cases": 2,
        "prompt_cases": 1,
        "generation_batches": 1,
        "independent_result_identities": 4,
        "provider_native_images": 0,
        "invalid_generation_attempt_evidence_entries": 4,
        "catalog_records": 11,
        "adapters": ["gemini", "flux", "midjourney"],
        "compiler_compilations": 9,
        "query_modes": ["exact_results", "related_results"],
        "command": "./run-tests.sh",
    },
    "verified": [
        "draft_2020_12_visual_contract_schema_validation",
        "draft_2020_12_image_case_schema_validation",
        "draft_2020_12_prompt_case_schema_validation",
        "provider_fields_rejected_by_visual_contract_schema",
        "abc_prompt_variant_contract",
        "prompt_sha256_matches_prompt_text",
        "generation_batch_prompt_sha_matches_prompt_case",
        "requested_count_matches_independent_result_identities",
        "contiguous_result_sequence",
        "provider_native_evidence_required_for_counted_results",
        "derived_composite_never_counted",
        "blocked_batch_requires_failure_evidence",
        "typescript_strict_compilation",
        "deterministic_compilation_objects",
        "byte_identical_cross_process_compiler_output",
        "byte_identical_cross_process_query_index",
        "byte_identical_cross_process_image_prompt_sets",
        "semantic_trace_preserved_across_adapters",
        "query_by_id_text_unicode_and_structured_filters",
        "query_expression_fields",
        "exact_and_related_results_are_separate",
        "prompt_generation_batch_and_result_records_are_queryable",
        "machine_readable_query_cli",
        "invalid_generation_outputs_not_saved_as_results",
        "generation_blocked_status_matches_available_evidence",
    ],
    "not_verified": [
        "four_provider_native_independent_images",
        "provider_receipts_for_image_results",
        "image_sha256_and_dimensions",
        "different_prompt_image_output_examples",
        "cross_provider_visual_similarity",
        "quality_against_manually_authored_prompt_baseline",
        "story_studio_runtime_integration",
        "ui_spec_runtime_integration",
        "skills_promotion_readiness",
        "public_web_query_interface",
    ],
    "files": {
        path.relative_to(ROOT).as_posix(): {
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
        }
        for path in paths
    },
}

print(json.dumps(manifest, indent=2, sort_keys=True))
