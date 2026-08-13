from __future__ import annotations

import csv
import hashlib
import io
import json
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

import yaml

HARNESS = Path(__file__).resolve().parents[1]
ROOT = HARNESS.parent
CORPUS = ROOT / "corpus"
sys.path.insert(0, str(CORPUS))

from source_selectors import _clean_markdown, load_nhtsa, select_by_hash  # noqa: E402


class Record:
    def __init__(self, source_id: str, record_id: str):
        self.source_id = source_id
        self.record_id = record_id


class SelectorTests(unittest.TestCase):
    def test_markdown_cleanup_claim_matches_behavior_and_lock(self):
        fixture = """---
title: Example
---
Prose with `inline_code()`.

```python
fenced_code()
```

    indented_code()
"""
        cleaned = _clean_markdown(fixture)
        self.assertNotIn("fenced_code", cleaned)
        self.assertIn("`inline_code()`", cleaned)
        self.assertIn("indented_code()", cleaned)

        locks = yaml.safe_load((ROOT / "locks" / "sources.yaml").read_text(encoding="utf-8"))["sources"]
        for source_id in ("github_docs", "mdn_content"):
            lock = locks[source_id]
            self.assertEqual(lock["markdown_code_handling"], "fenced_code_removed_only")
            self.assertEqual(lock["source_specific_license_review"], "required_before_case_materialization")
            self.assertEqual(lock["redistribution"], "review_required")

    def test_hash_selection_is_stable_and_unique(self):
        records = [Record("s", str(index)) for index in range(20)]
        first_used = set()
        second_used = set()
        first = select_by_hash(records, 5, "seed", first_used)
        second = select_by_hash(records, 5, "seed", second_used)
        self.assertEqual([item.record_id for item in first], [item.record_id for item in second])
        later = select_by_hash(records, 5, "seed-2", first_used)
        self.assertFalse({item.record_id for item in first} & {item.record_id for item in later})

    def test_nhtsa_rejects_cbi_and_keeps_latest_version(self):
        fields = ["Report ID", "Report Version", "Narrative", "Narrative - CBI?", "Report Month", "Report Year"]
        rows = [
            {"Report ID": "A", "Report Version": "1", "Narrative": "x" * 400, "Narrative - CBI?": ""},
            {"Report ID": "A", "Report Version": "2", "Narrative": "latest " + "y" * 400, "Narrative - CBI?": ""},
            {"Report ID": "B", "Report Version": "1", "Narrative": "secret " + "z" * 400, "Narrative - CBI?": "Y"},
        ]
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "sample.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            records = load_nhtsa([path], {"files": {"sample.csv": digest}, "minimum_candidate_rows": 1})
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0].record_id, "A")
            self.assertIn("latest", records[0].text)


if __name__ == "__main__":
    unittest.main()
