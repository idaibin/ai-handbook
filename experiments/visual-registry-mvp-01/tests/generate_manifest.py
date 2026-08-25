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
    "evidence/compiler-output.json",
    "evidence/query-index.json",
    "evidence/image-case-prompts.json",
    "evidence/determinism-rerun.json",
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
paths.extend(ROOT / name for name in EVIDENCE_FILES)
paths = sorted(set(paths), key=lambda path: path.relative_to(ROOT).as_posix())

manifest = {
    "experiment": "visual-registry-mvp-01",
    "unit": "UNIT_03_QUERY_AND_IMAGE_CASES",
    "status": "passed_query_and_prompt_case_validation",
    "validation_level": "static_unit_and_clean_copy_tests",
    "basis": {
        "repository": "idaibin/ai-handbook",
        "commit_before_implementation": "44cb4312a34e4082a79e67829a3047a822477794",
        "design_path": "research/visual-registry/2026-08-24-visual-registry-mvp-01.md",
    },
    "environment": {
        "node": version(["node", "--version"]),
        "typescript": version(["tsc", "--version"]),
        "python": platform.python_version(),
        "jsonschema": version(["python3", "-c", "from importlib.metadata import version; print(version('jsonschema'))"]),
    },
    "trial": {
        "contracts": 3,
        "consumer_cases": 3,
        "image_comparison_cases": 2,
        "prompt_variants_per_image_case": 3,
        "planned_images": 6,
        "catalog_records": 5,
        "adapters": ["gemini", "flux", "midjourney"],
        "compiler_compilations": 9,
        "command": "./run-tests.sh",
    },
    "verified": [
        "draft_2020_12_schema_validation",
        "provider_fields_rejected_by_visual_contract_schema",
        "image_case_schema_validation",
        "abc_prompt_variant_contract",
        "provider_syntax_absent_from_visual_contracts",
        "typescript_strict_compilation",
        "deterministic_compilation_objects",
        "byte_identical_cross_process_compiler_output",
        "byte_identical_cross_process_query_index",
        "byte_identical_cross_process_image_prompt_sets",
        "semantic_trace_preserved_across_adapters",
        "positive_and_negative_constraints_preserved_in_text_output",
        "adapter_specific_syntax_isolated",
        "invalid_target_rejected",
        "empty_subject_rejected",
        "consumer_identity_separated_from_visual_category",
        "query_by_id_text_unicode_and_filters",
        "machine_readable_query_cli",
        "image_case_status_does_not_overstate_generation",
    ],
    "not_verified": [
        "real_provider_image_generation",
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
