#!/usr/bin/env python3
"""Small content-addressed store for immutable benchmark evidence."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from common import ValidationError, canonical_bytes, sha256_value


class ArtifactStore:
    def __init__(self, root: Path):
        self.root = root

    def put_json(self, kind: str, value: Any) -> dict[str, str]:
        if not kind or "/" in kind or kind in {".", ".."}:
            raise ValidationError("artifact kind must be one safe path component")
        digest = sha256_value(value)
        relative = Path("objects") / kind / digest[:2] / f"{digest}.json"
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        payload = canonical_bytes(value) + b"\n"
        try:
            descriptor = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
        except FileExistsError:
            if target.read_bytes() != payload:
                raise ValidationError(f"content-address collision or corruption: {target}")
        else:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
        return {"kind": kind, "sha256": digest, "path": relative.as_posix()}

    def get_json(self, reference: dict[str, str]) -> Any:
        if set(reference) != {"kind", "sha256", "path"}:
            raise ValidationError("artifact reference keys invalid")
        expected = Path("objects") / reference["kind"] / reference["sha256"][:2] / f"{reference['sha256']}.json"
        if Path(reference["path"]) != expected or expected.is_absolute() or ".." in expected.parts:
            raise ValidationError("artifact reference path invalid")
        path = self.root / expected
        try:
            value = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError) as exc:
            raise ValidationError(f"cannot load artifact {path}: {exc}") from exc
        if sha256_value(value) != reference["sha256"]:
            raise ValidationError(f"artifact digest mismatch: {path}")
        return value

    def put_ref_once(self, relative: Path, reference: dict[str, str]) -> None:
        if relative.is_absolute() or ".." in relative.parts:
            raise ValidationError("reference path must stay inside artifact store")
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        payload = canonical_bytes(reference) + b"\n"
        try:
            descriptor = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
        except FileExistsError:
            if target.read_bytes() != payload:
                raise ValidationError(f"refusing to replace immutable reference: {target}")
        else:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())

    def read_ref(self, relative: Path) -> dict[str, str] | None:
        path = self.root / relative
        if not path.exists():
            return None
        try:
            value = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError) as exc:
            raise ValidationError(f"cannot read reference {path}: {exc}") from exc
        if not isinstance(value, dict):
            raise ValidationError(f"reference is not an object: {path}")
        self.get_json(value)
        return value
