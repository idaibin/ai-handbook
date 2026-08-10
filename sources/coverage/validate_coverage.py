#!/usr/bin/env python3
"""Validate fixed-commit reading coverage, with optional GitHub verification."""
from __future__ import annotations

import argparse
import ast
import base64
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Callable

import yaml

ROOT = Path(__file__).resolve().parent
SHA = re.compile(r"^[0-9a-f]{40}$")
PLACEHOLDER = re.compile(r"^(?:x+|tbd|todo|n/?a|unknown|none|placeholder)$", re.I)
DEFAULT_ROLES = {"readme", "core", "security_or_boundary", "evaluation_or_testing", "code_or_test"}


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text())
    except (OSError, yaml.YAMLError) as exc:
        raise ValueError(f"cannot parse {path}: {exc}") from exc


def err(errors: list[str], where: str, message: str) -> None:
    errors.append(f"{where}: {message}")


def non_placeholder(value: Any, minimum: int = 1) -> bool:
    return isinstance(value, str) and len(value.strip()) >= minimum and not PLACEHOLDER.fullmatch(value.strip())


def _schema_error_parts(error: str) -> tuple[str, str] | None:
    if not error.startswith("schema:"):
        return None
    where, separator, message = error.removeprefix("schema:").partition(": ")
    return (where.strip(), message) if separator else None


def _schema_field(path: str) -> str:
    return re.sub(r"\[\d+\]$", "", path.rsplit(".", 1)[-1])


def _schema_path_covers(parent: str, child: str) -> bool:
    return parent == child or child.startswith(f"{parent}.") or child.startswith(f"{parent}[")


def _jsonschema_error_is_covered(error: str, semantic_errors: list[str]) -> bool:
    parts = _schema_error_parts(error)
    if parts is None:
        return False
    path, message = parts
    field = _schema_field(path)
    for semantic in semantic_errors:
        semantic_parts = _schema_error_parts(semantic)
        if semantic_parts is None:
            continue
        semantic_path, semantic_message = semantic_parts
        if "Additional properties are not allowed" in message:
            if semantic_path == path and ("unknown field" in semantic_message or "is not allowed" in semantic_message):
                return True
            continue
        if "is a required property" in message:
            required = re.search(r"'([^']+)' is a required property", message)
            if required and semantic_path == path and (
                f"missing required field {required.group(1)!r}" in semantic_message
                or f"requires {required.group(1)}" in semantic_message
            ):
                return True
            continue
        if not _schema_path_covers(semantic_path, path):
            continue
        if field and re.search(rf"(?<!\w){re.escape(field)}(?!\w)", semantic_message):
            return True
    return False


def _schema_problem_leaves(problem: Any) -> list[Any]:
    """Use the smallest oneOf/anyOf branch for stable, useful diagnostics."""
    if not problem.context:
        return [problem]
    branches = [_schema_problem_leaves(child) for child in problem.context]
    return min(branches, key=len)


def _merge_schema_errors(semantic_errors: list[str], structural_errors: list[str]) -> list[str]:
    """Keep fallback semantics and append independent structural findings once."""
    merged: list[str] = []
    seen: set[str] = set()
    for error in semantic_errors:
        if error in seen:
            continue
        seen.add(error)
        merged.append(error)
    for error in structural_errors:
        if error in seen or _jsonschema_error_is_covered(error, semantic_errors):
            continue
        seen.add(error)
        merged.append(error)
    return merged


def schema_errors(data: Any, schema_path: Path, legacy_allowed: bool) -> list[str]:
    """Run the shared semantic contract and safely merge structural findings.

    The fallback deliberately covers the conditional status requirements and closed
    fields. It is kept in this file so CLI behavior remains deterministic on hosts
    without the optional jsonschema dependency. Its messages remain canonical;
    jsonschema findings are appended only when they are not the same finding in
    different wording. This preserves independent structural errors even when a
    batch also has a fallback semantic error.
    """
    semantic_errors = fallback_schema_errors(data, legacy_allowed)
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return semantic_errors
    schema = load_yaml(schema_path)
    result = []
    for problem in jsonschema.Draft202012Validator(schema).iter_errors(data):
        for leaf in _schema_problem_leaves(problem):
            result.append(f"schema: {leaf.json_path or '$'}: {leaf.message}")
    if isinstance(data, dict) and data.get("format_version") == "legacy-v1" and not legacy_allowed:
        result.append("schema: $: legacy-v1 batch is not in manifest legacy allowlist at coverage ROOT")
    return _merge_schema_errors(semantic_errors, result)


def fallback_schema_errors(data: Any, legacy_allowed: bool) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["schema: $: batch must be an object"]
    top = {"format_version", "batch_id", "checked_at", "evidence_policy", "sources"}
    for key in set(data) - top:
        err(errors, "schema:$", f"unknown field {key!r}")
    for key in top:
        if key not in data:
            err(errors, "schema:$", f"missing required field {key!r}")
    version = data.get("format_version")
    if version not in {"canonical-v2", "legacy-v1"}:
        err(errors, "schema:$", "format_version must be canonical-v2 or legacy-v1")
    if version == "legacy-v1" and not legacy_allowed:
        err(errors, "schema:$", "legacy-v1 batch is not in manifest legacy allowlist at coverage ROOT")
    for field in ("batch_id", "checked_at"):
        if not non_placeholder(data.get(field)):
            err(errors, "schema:$", f"{field} must be a non-empty string")
    if not isinstance(data.get("evidence_policy"), dict) or not data["evidence_policy"]:
        err(errors, "schema:$", "evidence_policy must be a non-empty object")
    entries = data.get("sources")
    if not isinstance(entries, list) or not entries:
        err(errors, "schema:$", "sources must be a non-empty array")
        return errors
    for i, entry in enumerate(entries):
        where = f"schema:$.sources[{i}]"
        if not isinstance(entry, dict):
            err(errors, where, "source must be an object")
            continue
        nested = "records" in entry
        allowed = {"source_id", "repo", "commit_sha", "records"}
        if nested and version == "legacy-v1":
            allowed.add("document_identity")
        record_entries = entry.get("records") if nested else [entry]
        if nested and (not isinstance(record_entries, list) or not record_entries):
            err(errors, where, "records must be a non-empty array")
            continue
        if not nested and version != "legacy-v1":
            err(errors, where, "canonical-v2 requires nested records")
        unknown = set(entry) - (allowed if nested else record_allowed_fields())
        if nested and version == "canonical-v2" and "document_identity" in unknown:
            unknown.remove("document_identity")
            err(errors, where, "document_identity is not allowed in canonical-v2")
        for key in unknown:
            err(errors, where, f"unknown field {key!r}")
        if "document_identity" in entry and nested:
            validate_schema_identity(entry["document_identity"], f"{where}.document_identity", errors, "document_identity")
        for field in ("source_id", "repo", "commit_sha"):
            if not non_placeholder(entry.get(field)):
                err(errors, where, f"missing {field}")
        if not isinstance(entry.get("repo"), str) or not re.fullmatch(r"[^/\s]+/[^/\s]+", entry["repo"]):
            err(errors, where, "repo must be owner/name")
        if not isinstance(entry.get("commit_sha"), str) or not SHA.fullmatch(entry["commit_sha"]):
            err(errors, where, "commit_sha must be 40 lowercase hex characters")
        for j, record in enumerate(record_entries):
            validate_schema_record(record, f"{where}.records[{j}]", errors, version == "canonical-v2")
    return errors


def record_allowed_fields() -> set[str]:
    return {"source_id", "repo", "commit_sha", "role", "status", "path", "git_blob_sha", "locator", "coverage", "atomic_claims", "boundaries_or_counterexamples", "not_verified", "search_evidence"}


def validate_schema_identity(identity: Any, where: str, errors: list[str], label: str) -> None:
    if not isinstance(identity, dict):
        err(errors, where, f"{label} must be an identity object")
        return
    expected_fields = ("source_id", "repo", "commit_sha")
    expected = set(expected_fields)
    for key in set(identity) - expected:
        err(errors, where, f"unknown field {key!r}")
    for field in expected_fields:
        if field not in identity:
            err(errors, where, f"{label} missing required field {field!r}")
    if "source_id" in identity and not non_placeholder(identity["source_id"]):
        err(errors, where, f"{label}.source_id must be a non-empty string")
    if "repo" in identity and (not isinstance(identity["repo"], str) or not re.fullmatch(r"[^/\s]+/[^/\s]+", identity["repo"])):
        err(errors, where, f"{label}.repo must be owner/name")
    if "commit_sha" in identity and (not isinstance(identity["commit_sha"], str) or not SHA.fullmatch(identity["commit_sha"])):
        err(errors, where, f"{label}.commit_sha must be 40 lowercase hex characters")


def validate_schema_search_evidence(evidence: Any, where: str, errors: list[str]) -> None:
    if not isinstance(evidence, dict):
        err(errors, where, "search_evidence must be an object")
        return
    expected_fields = ("commit", "method_or_query", "searched_paths_or_tree", "result", "gap")
    expected = set(expected_fields)
    for key in set(evidence) - expected:
        err(errors, where, f"unknown field {key!r}")
    for field in expected_fields:
        if field not in evidence:
            err(errors, where, f"search_evidence missing required field {field!r}")
    if "commit" in evidence and (not isinstance(evidence["commit"], str) or not SHA.fullmatch(evidence["commit"])):
        err(errors, where, "search_evidence.commit must be 40 lowercase hex characters")
    for field in ("method_or_query", "result", "gap"):
        if field in evidence and not non_placeholder(evidence[field], 8):
            err(errors, where, f"search_evidence.{field} must be a specific string")
    paths = evidence.get("searched_paths_or_tree")
    if "searched_paths_or_tree" in evidence and (not isinstance(paths, list) or not paths or not all(non_placeholder(item, 2) for item in paths)):
        err(errors, where, "search_evidence.searched_paths_or_tree must be a non-empty string array")


def validate_schema_record(record: Any, where: str, errors: list[str], require_identity: bool) -> None:
    if not isinstance(record, dict):
        err(errors, where, "record must be an object")
        return
    for key in set(record) - record_allowed_fields():
        err(errors, where, f"unknown field {key!r}")
    for field in ("role", "status") + (("source_id", "repo", "commit_sha") if require_identity else ()):
        if field not in record:
            err(errors, where, f"missing required field {field!r}")
    if not isinstance(record.get("role"), str) or not record["role"]:
        err(errors, where, "role must be a non-empty string")
    for field in ("source_id", "repo", "commit_sha"):
        if field not in record:
            continue
        if field == "source_id" and not non_placeholder(record[field]):
            err(errors, where, "source_id must be a non-empty string")
        elif field == "repo" and (not isinstance(record[field], str) or not re.fullmatch(r"[^/\s]+/[^/\s]+", record[field])):
            err(errors, where, "repo must be owner/name")
        elif field == "commit_sha" and (not isinstance(record[field], str) or not SHA.fullmatch(record[field])):
            err(errors, where, "commit_sha must be 40 lowercase hex characters")
    for field in ("path", "locator", "coverage"):
        if field in record and not non_placeholder(record[field]):
            err(errors, where, f"{field} must be a non-empty string")
    if "git_blob_sha" in record and (not isinstance(record["git_blob_sha"], str) or not SHA.fullmatch(record["git_blob_sha"])):
        err(errors, where, "git_blob_sha must be 40 lowercase hex characters")
    for field in ("atomic_claims", "boundaries_or_counterexamples", "not_verified"):
        if field in record:
            value = record[field]
            if not isinstance(value, list) or not value or not all(non_placeholder(item) for item in value):
                err(errors, where, f"{field} must be a non-empty string array")
    if "search_evidence" in record:
        validate_schema_search_evidence(record["search_evidence"], f"{where}.search_evidence", errors)
    status = record.get("status")
    if not isinstance(status, str):
        err(errors, where, "status must be a string")
        return
    if status == "read_at_fixed_commit":
        for field in ("path", "git_blob_sha", "locator", "coverage", "atomic_claims", "boundaries_or_counterexamples", "not_verified"):
            if field not in record:
                err(errors, where, f"status read_at_fixed_commit requires {field}")
    elif status == "not_found" and "search_evidence" not in record:
        err(errors, where, "status not_found requires search_evidence")
    elif status not in {"read_at_fixed_commit", "not_found", "read"}:
        err(errors, where, "unknown status")


def normalize_batch(data: Any, name: str, errors: list[str], *, legacy_allowed: bool = False) -> list[dict[str, Any]]:
    """Return logical sources; parent inheritance exists only for allowlisted legacy batches."""
    if not isinstance(data, dict):
        err(errors, name, "batch must be a mapping")
        return []
    version = data.get("format_version")
    if version not in {"canonical-v2", "legacy-v1"}:
        err(errors, name, "missing or unsupported format_version")
        return []
    if version == "legacy-v1" and not legacy_allowed:
        err(errors, name, "legacy-v1 is not in manifest legacy allowlist at coverage ROOT")
        return []
    entries = data.get("sources")
    if not isinstance(entries, list) or not entries:
        return []
    sources: dict[tuple[str, str, str], dict[str, Any]] = {}
    for index, entry in enumerate(entries):
        where = f"{name}.sources[{index}]"
        if not isinstance(entry, dict):
            continue
        identity = {key: entry.get(key) for key in ("source_id", "repo", "commit_sha")}
        if not all(non_placeholder(value) for value in identity.values()):
            continue
        key = (identity["source_id"], identity["repo"], identity["commit_sha"])
        source = sources.setdefault(key, {**identity, "records": []})
        nested = "records" in entry
        records = entry.get("records") if nested else [{k: v for k, v in entry.items() if k not in identity}]
        if not isinstance(records, list):
            continue
        for record_index, raw in enumerate(records):
            record_where = f"{where}.records[{record_index}]"
            if not isinstance(raw, dict):
                continue
            record = dict(raw)
            for field, expected in identity.items():
                actual = record.get(field)
                if version == "canonical-v2" and actual is None:
                    err(errors, record_where, f"canonical-v2 requires repeated {field}")
                if actual is not None and actual != expected:
                    err(errors, record_where, f"{field} conflicts with parent ({actual!r} != {expected!r})")
                record[field] = expected
            if record.get("status") == "read":
                record["status"] = "read_at_fixed_commit"
            source["records"].append(record)
    return list(sources.values())


def validate_not_found(record: dict[str, Any], where: str, commit: str, errors: list[str]) -> None:
    evidence = record.get("search_evidence")
    if not isinstance(evidence, dict):
        err(errors, where, "not_found requires structured search_evidence")
        return
    expected = {"commit", "method_or_query", "searched_paths_or_tree", "result", "gap"}
    if set(evidence) != expected:
        err(errors, where, "search_evidence must contain exactly commit, method_or_query, searched_paths_or_tree, result, gap")
    if evidence.get("commit") != commit or not SHA.fullmatch(str(evidence.get("commit", ""))):
        err(errors, where, "search_evidence.commit must equal source commit_sha")
    for field in ("method_or_query", "result", "gap"):
        if not non_placeholder(evidence.get(field), 8):
            err(errors, where, f"search_evidence.{field} must be specific, not a placeholder")
    paths = evidence.get("searched_paths_or_tree")
    if not isinstance(paths, list) or not paths or not all(non_placeholder(item, 2) for item in paths):
        err(errors, where, "search_evidence.searched_paths_or_tree must be non-empty specific paths/tree")


def validate_logical_sources(sources: list[dict[str, Any]], label: str, errors: list[str], required_roles: set[str] = DEFAULT_ROLES, *, complete: bool = True) -> Counter:
    blobs: Counter = Counter()
    for source in sources:
        source_name = f"{label}:{source['source_id']}"
        roles = []
        for record in source["records"]:
            role = record.get("role")
            if not isinstance(role, str):
                err(errors, source_name, "role must be a string")
                continue
            roles.append(role)
        counts = Counter(roles)
        missing, extras = sorted(required_roles - set(roles)), sorted(set(roles) - required_roles)
        if missing: err(errors, source_name, f"missing roles: {', '.join(missing)}")
        if extras: err(errors, source_name, f"unknown roles: {', '.join(extras)}")
        for role, count in sorted(counts.items()):
            if count != 1: err(errors, source_name, f"role {role!r} occurs {count} times (must be exactly once)")
        for index, record in enumerate(source["records"]):
            where = f"{source_name}.records[{index}]"
            status = record.get("status")
            if status == "not_found":
                validate_not_found(record, where, source["commit_sha"], errors)
                if complete: err(errors, where, "coverage_complete forbids required role status not_found")
                continue
            if status != "read_at_fixed_commit":
                err(errors, where, "status must be read_at_fixed_commit or not_found")
                continue
            for field in ("path", "locator", "coverage"):
                if not non_placeholder(record.get(field)):
                    err(errors, where, f"read_at_fixed_commit requires non-placeholder {field}")
            blob = record.get("git_blob_sha")
            if not isinstance(blob, str) or not SHA.fullmatch(blob): err(errors, where, "read_at_fixed_commit requires 40 lowercase hex git_blob_sha")
            else: blobs[(record.get("path"), blob)] += 1
            for field in ("atomic_claims", "boundaries_or_counterexamples", "not_verified"):
                value = record.get(field)
                if not isinstance(value, list) or not value or not all(non_placeholder(item) for item in value): err(errors, where, f"read_at_fixed_commit requires non-placeholder {field}")
    return blobs


def repository_index(catalog: dict[str, Any]) -> dict[str, str]:
    return {item.get("repo"): str(item.get("commit_sha")) for item in catalog.get("repositories", []) if isinstance(item, dict)}


def validate_global(sources: list[dict[str, Any]], manifest: dict[str, Any], catalog: dict[str, Any], errors: list[str]) -> set[str]:
    required = manifest.get("required_roles")
    if not isinstance(required, list) or not required or not all(isinstance(role, str) for role in required):
        err(errors, "global", "manifest required_roles must be a non-empty string list")
        required_roles = DEFAULT_ROLES
    else:
        required_roles = set(required)
        if required_roles != DEFAULT_ROLES: err(errors, "global", "manifest required_roles must equal supported role set")
    expected = manifest.get("sources", {}) if isinstance(manifest, dict) else {}
    actual = {source["source_id"]: source for source in sources}
    if set(actual) != set(expected): err(errors, "global", f"expected exactly manifest sources; missing={sorted(set(expected)-set(actual))}; extra={sorted(set(actual)-set(expected))}")
    catalog_by_repo = repository_index(catalog)
    for source_id, source in actual.items():
        wanted = expected.get(source_id, {})
        if source["repo"] != wanted.get("repo") or source["commit_sha"] != str(wanted.get("commit_sha")): err(errors, f"global:{source_id}", "repo/commit differs from manifest")
        if catalog_by_repo.get(source["repo"]) != source["commit_sha"]: err(errors, f"global:{source_id}", "repo/commit differs from github-ai-repositories.yaml")
    return required_roles


def gh_api(endpoint: str) -> Any:
    run = subprocess.run(["gh", "api", endpoint], text=True, capture_output=True, check=False)
    if run.returncode:
        raise RuntimeError(run.stderr.strip() or "gh api failed (authenticate with gh auth login)")
    return json.loads(run.stdout)


def _heading_key(value: str) -> str:
    return re.sub(r"[^\w]+", "", value.casefold(), flags=re.UNICODE)


def _text_key(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def locator_piece_matches(text: str, piece: str) -> bool:
    """Match one auditable locator fragment using its declared syntax.

    `# heading` and `path.md#heading` are Markdown-heading locators, never a
    free-text search. Symbol-looking fragments match literal identifiers; other
    fragments are exact case/whitespace-normalized text phrases.
    """
    piece = piece.strip()
    if piece.startswith("symbol:"):
        return symbol_matches(text, piece.removeprefix("symbol:").strip())
    anchor = piece.rsplit("#", 1)[-1] if "#" in piece else None
    is_markdown_anchor = bool(re.search(r"\.(?:md|mdx)#", piece, re.I))
    if piece.startswith("#") or is_markdown_anchor:
        wanted = _heading_key(anchor if anchor is not None else piece.lstrip("#"))
        if not wanted:
            return False
        headings = re.findall(r"(?m)^\s{0,3}#{1,6}\s*(.+?)\s*#*\s*$", text)
        return any(_heading_key(heading) == wanted for heading in headings)
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_./]*\(?\)?", piece):
        return re.search(rf"(?<![A-Za-z0-9_]){re.escape(piece)}(?![A-Za-z0-9_])", text) is not None
    wanted = _text_key(anchor if anchor is not None else piece)
    return len(re.sub(r"\W", "", wanted, flags=re.UNICODE)) >= 8 and wanted in _text_key(text)


def symbol_matches(text: str, symbol: str) -> bool:
    """Audit a code symbol by declaration/member identity, not call syntax."""
    parts = symbol.split(".")
    if not all(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", part) for part in parts):
        return False
    if len(parts) == 1:
        return re.search(rf"(?m)^\s*(?:async\s+)?(?:def|class)\s+{re.escape(parts[0])}\b|\b{re.escape(parts[0])}\s*=", text) is not None
    owner, member = parts[0], parts[-1]
    return _member_in_python_class(text, owner, member) or any(_member_in_brace_type(text, owner, member))


def _member_in_python_class(text: str, owner: str, member: str) -> bool:
    """Accept only a direct method of the named Python class, including multiline headers."""
    try:
        module = ast.parse(text)
    except SyntaxError:
        return False
    for node in ast.walk(module):
        if isinstance(node, ast.ClassDef) and node.name == owner:
            if any(isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) and child.name == member for child in node.body):
                return True
    return False


def _brace_block(text: str, start: int) -> str | None:
    opening = text.find("{", start)
    if opening < 0:
        return None
    depth = 0
    for index, character in enumerate(text[opening:], opening):
        if character == "{": depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0: return text[opening + 1:index]
    return None


def _member_in_brace_type(text: str, owner: str, member: str):
    headers = [rf"\bclass\s+{re.escape(owner)}\b", rf"\bimpl(?:<[^>]+>)?\s+{re.escape(owner)}\b"]
    member_re = re.compile(rf"(?m)(?:\b(?:async\s+)?(?:fn|function)\s+|^\s*)(?:{re.escape(member)})\s*\(")
    for header in headers:
        for match in re.finditer(header, text):
            block = _brace_block(text, match.end())
            yield block is not None and member_re.search(block) is not None


def locator_matches(content: bytes, locator: str) -> bool:
    text = content.decode("utf-8", "replace")
    pieces = [piece.strip() for piece in locator.split(";") if piece.strip()]
    return bool(pieces) and all(locator_piece_matches(text, piece) for piece in pieces)


def missing_locator_pieces(content: bytes, locator: str) -> list[str]:
    """Return every unmatched all-fragment locator component for audit output."""
    text = content.decode("utf-8", "replace")
    pieces = [piece.strip() for piece in locator.split(";") if piece.strip()]
    return [piece for piece in pieces if not locator_piece_matches(text, piece)]


def verify_remote(sources: list[dict[str, Any]], errors: list[str], api: Callable[[str], Any] = gh_api) -> Counter:
    counts: Counter = Counter()
    for source in sources:
        name, repo, commit = source["source_id"], source["repo"], source["commit_sha"]
        try:
            commit_info = api(f"repos/{repo}/git/commits/{commit}")
            tree_sha = commit_info["tree"]["sha"]
            tree = api(f"repos/{repo}/git/trees/{tree_sha}?recursive=1")
            paths = {entry.get("path"): entry.get("sha") for entry in tree.get("tree", []) if entry.get("type") == "blob"}
        except Exception as exc:
            err(errors, f"remote:{name}", f"Not verified: commit/tree lookup failed: {exc}")
            continue
        for index, record in enumerate(source["records"]):
            if record.get("status") != "read_at_fixed_commit": continue
            where, path = f"remote:{name}.records[{index}]", record.get("path")
            tree_blob = paths.get(path)
            if tree_blob != record.get("git_blob_sha"):
                err(errors, where, f"path/blob mismatch: tree has {tree_blob!r}, contract has {record.get('git_blob_sha')!r}")
                continue
            try:
                blob = api(f"repos/{repo}/git/blobs/{tree_blob}")
                content = base64.b64decode(blob["content"])
                actual = hashlib.sha1(f"blob {len(content)}\0".encode() + content).hexdigest()
                if actual != tree_blob: err(errors, where, "downloaded blob Git SHA does not match tree blob")
                elif missing := missing_locator_pieces(content, record["locator"]): err(errors, where, f"locator fragments not found in downloaded blob: {missing!r}")
                else: counts[name] += 1
            except Exception as exc:
                err(errors, where, f"Not verified: blob/locator lookup failed: {exc}")
    return counts


def validate_paths(batch_paths: list[Path], manifest_path: Path, catalog_path: Path, *, complete: bool = True, verify_remote_mode: bool = False, api: Callable[[str], Any] = gh_api) -> tuple[dict[str, int], list[str], Counter]:
    errors: list[str] = []
    manifest, catalog = load_yaml(manifest_path), load_yaml(catalog_path)
    allowlist = set(manifest.get("legacy_batch_allowlist", [])) if isinstance(manifest, dict) else set()
    logical: list[dict[str, Any]] = []
    for path in batch_paths:
        data = load_yaml(path)
        legacy_allowed = path.resolve().parent == ROOT.resolve() and path.resolve().name in allowlist
        errors.extend(schema_errors(data, ROOT / "coverage.schema.yaml", legacy_allowed))
        sources = normalize_batch(data, path.name, errors, legacy_allowed=legacy_allowed)
        logical.extend(sources)
    required = validate_global(logical, manifest, catalog, errors)
    validate_logical_sources(logical, "coverage", errors, required, complete=complete)
    ids = [source["source_id"] for source in logical]
    for source_id, count in Counter(ids).items():
        if count != 1: err(errors, "global", f"source_id {source_id!r} appears in {count} batches")
    records = [record for source in logical for record in source["records"]]
    statuses = Counter(record.get("status") for record in records)
    remote = verify_remote(logical, errors, api) if verify_remote_mode else Counter()
    return {"batches": len(batch_paths), "sources": len(logical), "records": len(records), "read": statuses["read_at_fixed_commit"], "not_found": statuses["not_found"], "incomplete": statuses["not_found"]}, errors, remote


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batches", nargs="*", type=Path, default=sorted(ROOT.glob("batch-*.yaml")))
    parser.add_argument("--manifest", type=Path, default=ROOT / "manifest.yaml")
    parser.add_argument("--catalog", type=Path, default=ROOT.parent / "github-ai-repositories.yaml")
    parser.add_argument("--incomplete-ok", action="store_true", help="allow required roles recorded as not_found")
    parser.add_argument("--verify-remote", action="store_true", help="read-only GitHub commit/tree/blob/locator verification via authenticated gh api")
    args = parser.parse_args()
    summary, errors, remote = validate_paths(args.batches, args.manifest, args.catalog, complete=not args.incomplete_ok, verify_remote_mode=args.verify_remote)
    print("coverage: batches={batches} sources={sources} records={records} read={read} not_found={not_found} incomplete={incomplete}".format(**summary))
    complete = summary["not_found"] == 0 and not any('missing roles:' in problem for problem in errors)
    print(f"coverage: schema_valid={'no' if any(problem.startswith('schema:') for problem in errors) else 'yes'} coverage_complete={'yes' if complete else 'no'} errors={len(errors)}")
    if args.verify_remote: print("remote: " + (", ".join(f"{name}={count}" for name, count in sorted(remote.items())) or "no records verified"))
    for problem in errors: print(f"ERROR: {problem}")
    return 1 if errors else 0


if __name__ == "__main__": raise SystemExit(main())
