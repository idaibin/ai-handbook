#!/usr/bin/env python3
"""Shared, dependency-free validation and hashing helpers."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
LABELS = ("A", "B", "C", "D")
DIMENSIONS = (
    "fidelity",
    "instruction_structure",
    "clarity",
    "naturalness",
    "restraint",
)


class ValidationError(ValueError):
    """Raised when an evidence contract fails closed."""


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def sha256_value(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def hash_without(value: dict[str, Any], field: str) -> str:
    return sha256_value({key: item for key, item in value.items() if key != field})


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"cannot read JSON {path}: {exc}") from exc


def read_jsonl(paths: list[Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in paths:
        try:
            lines = path.read_text().splitlines()
        except OSError as exc:
            raise ValidationError(f"cannot read JSONL {path}: {exc}") from exc
        for line_no, line in enumerate(lines, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValidationError(f"invalid JSONL {path}:{line_no}: {exc}") from exc
            if not isinstance(row, dict):
                raise ValidationError(f"JSONL row must be an object: {path}:{line_no}")
            rows.append(row)
    return rows


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if path.exists() and path.read_text() != data:
        raise ValidationError(f"refusing to overwrite immutable artifact: {path}")
    path.write_text(data)


def _scalar(value: str) -> Any:
    value = value.strip()
    if value in {"null", "~"}:
        return None
    if value in {"true", "false"}:
        return value == "true"
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if re.fullmatch(r"-?(?:\d+\.\d*|\d*\.\d+)", value):
        return float(value)
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def read_simple_yaml(path: Path) -> dict[str, Any]:
    """Parse the mapping/list subset used by this experiment's manifest."""
    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]
    lines = path.read_text().splitlines()
    for number, raw in enumerate(lines, 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if indent % 2:
            raise ValidationError(f"unsupported YAML indentation at {path}:{number}")
        text = raw.strip()
        while stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        if text.startswith("- "):
            if not isinstance(parent, list):
                raise ValidationError(f"YAML list without list parent at {path}:{number}")
            parent.append(_scalar(text[2:]))
            continue
        if ":" not in text or not isinstance(parent, dict):
            raise ValidationError(f"unsupported YAML at {path}:{number}")
        key, raw_value = text.split(":", 1)
        key, raw_value = key.strip(), raw_value.strip()
        if raw_value:
            parent[key] = _scalar(raw_value)
            continue
        # Detect whether the next meaningful indented line is a list item.
        child: Any = {}
        for following in lines[number:]:
            if not following.strip() or following.lstrip().startswith("#"):
                continue
            next_indent = len(following) - len(following.lstrip(" "))
            if next_indent <= indent:
                break
            child = [] if following.strip().startswith("- ") else {}
            break
        parent[key] = child
        stack.append((indent, child))
    return root


def load_manifest(root: Path = ROOT) -> dict[str, Any]:
    path = root / "manifest.yaml"
    if not path.is_file():
        raise ValidationError(f"missing root manifest: {path}")
    manifest = read_simple_yaml(path)
    required = {"experiment_id", "design", "skills"}
    if set(manifest) < required:
        raise ValidationError(f"manifest missing keys: {sorted(required - set(manifest))}")
    return manifest


def load_schema(name: str, root: Path = ROOT) -> dict[str, Any]:
    return read_json(root / "schemas" / f"{name}.schema.json")


def _is_type(value: Any, expected: str) -> bool:
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
        "null": value is None,
    }[expected]


def validate_schema(value: Any, schema: dict[str, Any], path: str = "$") -> None:
    """Validate the strict JSON-Schema subset used by the repository contracts."""
    expected = schema.get("type")
    if expected is not None:
        types = expected if isinstance(expected, list) else [expected]
        if not any(_is_type(value, item) for item in types):
            raise ValidationError(f"{path}: expected type {types}, got {type(value).__name__}")
    if "const" in schema and value != schema["const"]:
        raise ValidationError(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        raise ValidationError(f"{path}: value is not in enum")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            raise ValidationError(f"{path}: string is too short")
        if "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
            raise ValidationError(f"{path}: string does not match {schema['pattern']}")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            raise ValidationError(f"{path}: value below minimum")
        if "maximum" in schema and value > schema["maximum"]:
            raise ValidationError(f"{path}: value above maximum")
        if "exclusiveMinimum" in schema and value <= schema["exclusiveMinimum"]:
            raise ValidationError(f"{path}: value below exclusive minimum")
    if isinstance(value, dict):
        required = set(schema.get("required", []))
        missing = required - set(value)
        if missing:
            raise ValidationError(f"{path}: missing keys {sorted(missing)}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = set(value) - set(properties)
            if extra:
                raise ValidationError(f"{path}: unexpected keys {sorted(extra)}")
        for key, item in value.items():
            if key in properties:
                validate_schema(item, properties[key], f"{path}.{key}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            raise ValidationError(f"{path}: too few items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            raise ValidationError(f"{path}: too many items")
        if schema.get("uniqueItems") and len({canonical_bytes(item) for item in value}) != len(value):
            raise ValidationError(f"{path}: duplicate items")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                validate_schema(item, item_schema, f"{path}[{index}]")


def skill_revisions(manifest: dict[str, Any]) -> dict[str, str]:
    result = {}
    for skill_id, entry in manifest["skills"].items():
        revision = entry.get("commit")
        if not isinstance(revision, str) or re.fullmatch(r"[0-9a-f]{40}", revision) is None:
            raise ValidationError(f"invalid skill revision for {skill_id}")
        result[skill_id] = revision
    if len(result) != int(manifest["design"]["skills"]):
        raise ValidationError("skill count does not match manifest design")
    return result
