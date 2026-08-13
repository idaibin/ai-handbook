from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

import yaml

HARNESS = Path(__file__).resolve().parents[1]
ROOT = HARNESS.parent
CORPUS = ROOT / "corpus"
sys.path.insert(0, str(HARNESS))
sys.path.insert(0, str(CORPUS))

from common import sha256_value  # noqa: E402
from build_corpus import extract_contract, infer_operation  # noqa: E402
from validate_corpus import validate_cases  # noqa: E402


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class CorpusPlanWithoutRawPrompts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plans = load_json(CORPUS / "plan-slots.json")
        cls.commitments = load_json(CORPUS / "case-commitments.json")
        cls.report = load_json(CORPUS / "corpus-report.json")
        cls.families = yaml.safe_load((CORPUS / "families.yaml").read_text(encoding="utf-8"))
        cls.locks = yaml.safe_load((ROOT / "locks" / "sources.yaml").read_text(encoding="utf-8"))

    def test_candidate_scope_and_deferred_families(self):
        deferred = {
            family_id for family_id, family in self.families["families"].items()
            if family.get("first_wave_status") == "deferred_no_fit"
        }
        self.assertEqual(deferred, {"F02", "F03", "F05", "F06", "F07", "F09", "F11"})
        self.assertEqual(self.report["materialized_cases"], 50)
        self.assertEqual(self.report["status"], "candidate_smoke_test_materialized")
        self.assertIn("local_only_untracked", self.report["case_file_distribution"])
        self.assertEqual(len(self.commitments["commitments"]), 50)

    def test_plan_slots_are_not_false_case_commitments(self):
        slots = self.plans["slots"]
        self.assertEqual(len(slots), 1200)
        self.assertTrue(all(slot["slot_kind"] == "plan_not_case_commitment" for slot in slots))
        for slot in slots:
            if not slot["materialized"]:
                self.assertEqual(slot["selector_status"], "pending_source_specific_selector")
            if slot["sealed"]:
                self.assertFalse({"prompt", "query", "locator", "source_index"} & slot.keys())

    def test_source_quota_and_holdout_stratification(self):
        slots = self.plans["slots"]
        for family_id, family in self.families["families"].items():
            family_slots = [slot for slot in slots if slot["family_id"] == family_id]
            expected = Counter({key: int(value) for key, value in family["source_plan"].items()})
            self.assertEqual(Counter(slot["planned_source"] for slot in family_slots), expected)
            holdout = [slot for slot in family_slots if slot["sealed"]]
            self.assertEqual(Counter(slot["planned_language"] for slot in holdout), {"zh": 10, "en": 10})
            self.assertGreaterEqual(len({slot["planned_source"] for slot in holdout}), 2)

    def test_lock_binding_and_redistribution_block(self):
        lock = self.locks["sources"]["writingbench"]
        self.assertEqual(lock["redistribution"], "review_required")
        self.assertEqual(lock["third_party_material_review"], "required_before_publication")
        self.assertEqual(len(sha256_value(lock)), 64)
        self.assertTrue(all(item["source_id"] == "writingbench" for item in self.commitments["commitments"]))

    def test_constraint_parser_uses_explicit_task_text(self):
        contract = extract_contract(
            'Write for security engineers in 300-500 words. You may omit appendices. '
            'If no changes are needed, return the original unchanged.', "F01", "en"
        )
        self.assertEqual(contract["length_contract"]["minimum"], 300)
        self.assertEqual(contract["length_contract"]["maximum"], 500)
        self.assertEqual(contract["no_op_policy"], "required")
        self.assertEqual(contract["permitted_omissions"], ["appendices"])
        self.assertEqual(infer_operation("Please rewrite this paragraph.", "draft"), "rewrite")


@unittest.skipUnless(os.environ.get("WRITINGBENCH_PATH"), "set WRITINGBENCH_PATH for hash-locked integration test")
class BuilderIntegration(unittest.TestCase):
    def test_builds_and_validates_50_local_candidates(self):
        source = Path(os.environ["WRITINGBENCH_PATH"])
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            subprocess.run(
                [sys.executable, str(CORPUS / "build_corpus.py"), "--writingbench-path", str(source), "--output-dir", str(output)],
                cwd=ROOT, check=True,
            )
            cases = [json.loads(line) for line in (output / "cases.wave-01.jsonl").read_text(encoding="utf-8").splitlines()]
            result = validate_cases(cases, ROOT, complete=False, strict_source_locks=True)
            self.assertEqual(result["cases"], 50)
            self.assertEqual({case["family_id"] for case in cases}, {"F01", "F04", "F08", "F10", "F12"})


if __name__ == "__main__":
    unittest.main()
