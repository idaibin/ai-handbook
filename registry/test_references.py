import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from registry.reference_index import validate_reference_index

ROOT = Path(__file__).resolve().parents[1]


class ReferenceIndexTest(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads((ROOT / 'registry/references.json').read_text())

    def test_metadata_validation_never_reads_source_bytes(self):
        with patch.object(Path, 'read_bytes', side_effect=AssertionError('body read')):
            result = validate_reference_index(self.doc)
        self.assertEqual(result['entry_count'], 5)
        self.assertFalse(result['source_bytes_checked'])
        self.assertFalse(result['authorizes_execution'])

    def test_real_chinese_metadata_remains_exact(self):
        row = self.doc['entries'][0]
        self.assertIn('滚动交互', row['topics'])
        self.assertIn('粘性定位', row['topics'])
        before = copy.deepcopy(self.doc)
        validate_reference_index(self.doc)
        self.assertEqual(self.doc, before)

    def test_safe_unicode_locator_and_tags_are_valid_metadata(self):
        # Compatibility probe, not a claim that this source exists.
        row = self.doc['entries'][0]
        row['source']['path'] = 'research/界面设计/滚动交互.md'
        row['topics'] = ['滚动交互', 'UI设计', 'é', 'e\u0301']
        validate_reference_index(self.doc)
        self.assertEqual(row['topics'][-2:], ['é', 'e\u0301'])

    def test_unicode_does_not_relax_path_safety(self):
        for path in ['research/界面/../秘密.md', '/界面/设计.md', '界面/\x00.md', '界面\\设计.md']:
            with self.subTest(path=path):
                doc = copy.deepcopy(self.doc)
                doc['entries'][0]['source']['path'] = path
                with self.assertRaises(ValueError):
                    validate_reference_index(doc)

    def test_actual_fixed_source_hashes(self):
        self.assertTrue(validate_reference_index(self.doc, ROOT)['source_bytes_checked'])

    def test_bad_metadata_is_rejected(self):
        mutations = [
            lambda d: d['entries'].append(copy.deepcopy(d['entries'][0])),
            lambda d: d['entries'][0]['source'].update(path='../README.md'),
            lambda d: d['entries'][0]['source'].update(path='/README.md'),
            lambda d: d['entries'][0]['source'].update(path='a//b'),
            lambda d: d['entries'][0]['source'].update(path='research/\x00.md'),
            lambda d: d['entries'][0]['source'].update(revision='main'),
            lambda d: d['entries'][0]['source'].update(sha256='unknown'),
            lambda d: d['entries'][0]['rights'].update(allowed_use=['copy']),
            lambda d: d['entries'][0].update(command='execute this'),
            lambda d: d['entries'][0].update(kind=[]),
            lambda d: d['entries'][0]['evidence'].update(level={}),
            lambda d: d['entries'][0]['evidence'].update(level='production-verified'),
            lambda d: d['entries'][0]['freshness'].update(checked_at='2026-02-30'),
            lambda d: d['entries'][0].update(applies_to=['x'], excludes=['x']),
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                doc = copy.deepcopy(self.doc)
                mutation(doc)
                with self.assertRaises(ValueError):
                    validate_reference_index(doc)

    def test_stale_source_is_not_missing_match(self):
        self.doc['entries'][0]['source']['sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'source stale'):
            validate_reference_index(self.doc, ROOT)

    def test_unavailable_source_is_not_missing_match(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, 'source unavailable'):
                validate_reference_index(self.doc, Path(directory))

    def test_private_candidate_indexes_metadata_not_media(self):
        row = next(r for r in self.doc['entries'] if r['id'] == 'forgeway-ui-directions')
        self.assertEqual(row['source']['path'], 'registry/assets.yaml')
        self.assertEqual(row['status'], 'candidate')
        self.assertIn('accepted-design', row['excludes'])
        self.assertIn('private-media-fetch', row['excludes'])

    def test_sample_does_not_claim_architecture_coverage(self):
        self.assertFalse(any('database-sharding' in r['topics'] for r in self.doc['entries']))
        row = next(r for r in self.doc['entries'] if r['id'] == 'dashboard-prompt-comparison')
        self.assertEqual(row['evidence']['level'], 'not-verified')


if __name__ == '__main__':
    unittest.main()
