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
    "evidence/compiler-output.json",
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
    "unit": "UNIT_02_STATIC_COMPILER",
    "status": "passed_static_validation",
    "validation_level": "static_and_unit_tests",
    "basis": {
        "repository": "idaibin/ai-handbook",
        "commit_before_implementation": "dc8925bd7b5760a1a591c77e8e9e69abcbacb722",
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
        "adapters": ["gemini", "flux", "midjourney"],
        "compilations": 9,
        "command": "./run-tests.sh",
    },
    "verified": [
        "draft_2020_12_schema_validation",
        "provider_fields_rejected_by_schema",
        "provider_syntax_absent_from_contracts",
        "typescript_strict_compilation",
        "deterministic_compilation_objects",
        "byte_identical_cross_process_output",
        "semantic_trace_preserved_across_adapters",
        "positive_and_negative_constraints_preserved_in_text_output",
        "adapter_specific_syntax_isolated",
        "invalid_target_rejected",
        "empty_subject_rejected",
        "consumer_identity_separated_from_visual_category",
    ],
    "not_verified": [
        "real_provider_image_generation",
        "cross_provider_visual_similarity",
        "quality_against_manually_authored_prompt_baseline",
        "story_studio_runtime_integration",
        "ui_spec_runtime_integration",
        "skills_promotion_readiness",
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
