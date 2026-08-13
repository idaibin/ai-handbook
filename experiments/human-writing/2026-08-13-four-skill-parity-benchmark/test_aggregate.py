#!/usr/bin/env python3
"""Regression tests proving aggregate.py rejects malformed review evidence."""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "aggregate.py"


def run(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(SCRIPT), "--root", str(root)],
        capture_output=True, text=True,
    )


baseline = run(ROOT)
if baseline.returncode != 0:
    raise SystemExit(f"baseline aggregation failed: {baseline.stderr}")

with tempfile.TemporaryDirectory() as tmp:
    trial = Path(tmp)
    shutil.copytree(ROOT / "results", trial / "results")
    judge = trial / "results/judge-1.md"
    text = judge.read_text()
    judge.write_text(text.replace("Ranking:", "Ranking: E > ", 1))
    if run(trial).returncode == 0:
        raise AssertionError("invalid ranking was accepted")

with tempfile.TemporaryDirectory() as tmp:
    trial = Path(tmp)
    shutil.copytree(ROOT / "results", trial / "results")
    path = trial / "results/blind-mappings.json"
    mappings = json.loads(path.read_text())
    mappings["1"]["C01"]["A"] = mappings["1"]["C01"]["B"]
    path.write_text(json.dumps(mappings, ensure_ascii=False, indent=2) + "\n")
    if run(trial).returncode == 0:
        raise AssertionError("non-bijective mapping was accepted")

print("aggregate fail-closed regressions: PASS")
