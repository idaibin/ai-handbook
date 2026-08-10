import base64
import builtins
import copy
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import validate_coverage as coverage


IDENTITY = {"source_id": "fixture", "repo": "owner/repo", "commit_sha": "a" * 40}
ROLES = ["readme", "core", "security_or_boundary", "evaluation_or_testing", "code_or_test"]


def record(role):
    return {**IDENTITY, "role": role, "status": "read_at_fixed_commit", "path": f"docs/{role}.md", "git_blob_sha": "b" * 40, "locator": "# heading", "coverage": "A bounded reading.", "atomic_claims": ["A source-supported claim."], "boundaries_or_counterexamples": ["A boundary."], "not_verified": ["Runtime behavior."]}


def source(): return {**IDENTITY, "records": [record(role) for role in ROLES]}


def batch(item, version="canonical-v2"):
    return {"format_version": version, "batch_id": "fixture", "checked_at": "2026-07-31", "evidence_policy": {"method": "fixture"}, "sources": [item]}


class CoverageContractTests(unittest.TestCase):
    def validate_one(self, item, *, complete=True, version="canonical-v2", legacy_allowed=False):
        errors = coverage.schema_errors(batch(item, version), coverage.ROOT / "coverage.schema.yaml", legacy_allowed)
        logical = coverage.normalize_batch(batch(item, version), "fixture.yaml", errors, legacy_allowed=legacy_allowed)
        coverage.validate_logical_sources(logical, "fixture", errors, set(ROLES), complete=complete)
        return errors

    def test_normal_canonical_source(self): self.assertEqual([], self.validate_one(source()))

    def test_missing_role_fails(self):
        item = source(); item["records"] = item["records"][:-1]
        self.assertIn("missing roles: code_or_test", "\n".join(self.validate_one(item)))

    def test_parent_child_identity_conflict_fails(self):
        item = source(); item["records"][0]["repo"] = "other/repo"
        self.assertIn("conflicts with parent", "\n".join(self.validate_one(item)))

    def test_empty_claims_fail(self):
        item = source(); item["records"][0]["atomic_claims"] = []
        self.assertIn("non-placeholder atomic_claims", "\n".join(self.validate_one(item)))

    def test_bad_blob_fails(self):
        item = source(); item["records"][0]["git_blob_sha"] = "bad"
        self.assertIn("git_blob_sha", "\n".join(self.validate_one(item)))

    def test_source_commit_drift_fails(self):
        errors = []
        manifest = {"required_roles": ROLES, "sources": {"fixture": {"repo": "owner/repo", "commit_sha": "c" * 40}}}
        catalog = {"repositories": [{"repo": "owner/repo", "commit_sha": "a" * 40}]}
        coverage.validate_global([source()], manifest, catalog, errors)
        self.assertIn("repo/commit differs from manifest", "\n".join(errors))

    def test_all_not_found_fails_complete_mode(self):
        item = source()
        for entry in item["records"]:
            entry.clear(); entry.update({**IDENTITY, "role": entry.get("role", "readme"), "status": "not_found", "search_evidence": {"commit": "a" * 40, "method_or_query": "searched complete repository tree", "searched_paths_or_tree": ["repository tree"], "result": "No role-specific document located", "gap": "No fixed-commit file supplies this role"}})
        # Restore unique roles after clear/update.
        for role, entry in zip(ROLES, item["records"]): entry["role"] = role
        self.assertIn("coverage_complete forbids", "\n".join(self.validate_one(item)))

    def test_not_found_requires_specific_structured_evidence(self):
        item = source(); entry = item["records"][0]
        entry.clear(); entry.update({**IDENTITY, "role": "readme", "status": "not_found", "search_evidence": {"commit": "a" * 40, "method_or_query": "x", "searched_paths_or_tree": ["x"], "result": "x", "gap": "x"}})
        errors = self.validate_one(item, complete=False)
        self.assertIn("must be specific, not a placeholder", "\n".join(errors))

    def test_bare_read_fails_after_normalization(self):
        item = source(); item["records"][0] = {**IDENTITY, "role": "readme", "status": "read"}
        self.assertIn("requires non-placeholder path", "\n".join(self.validate_one(item)))

    def test_canonical_child_identity_missing_fails(self):
        item = source(); del item["records"][0]["source_id"]
        self.assertIn("canonical-v2 requires repeated source_id", "\n".join(self.validate_one(item)))

    def test_legacy_must_be_allowlisted(self):
        flat = {**IDENTITY, **record("readme")}
        self.assertIn("not in manifest legacy allowlist", "\n".join(self.validate_one(flat, version="legacy-v1")))

    def test_schema_format_branches_and_execution_path(self):
        flat = {**IDENTITY, **record("readme")}
        self.assertTrue(coverage.schema_errors(batch(flat), coverage.ROOT / "coverage.schema.yaml", False))
        self.assertEqual([], coverage.schema_errors(batch(flat, "legacy-v1"), coverage.ROOT / "coverage.schema.yaml", True))
        try:
            import jsonschema
        except ImportError:
            # This is the runtime fallback path used by the CLI on this host.
            self.assertIn("unknown field", "\n".join(self.validate_one({**source(), "unexpected": 1})))
        else:
            schema = coverage.load_yaml(coverage.ROOT / "coverage.schema.yaml")
            self.assertTrue(list(jsonschema.Draft202012Validator(schema).iter_errors(batch(flat))))

    def test_schema_errors_merge_semantic_and_structural_findings(self):
        try:
            import jsonschema  # noqa: F401
        except ImportError:
            self.skipTest("jsonschema is not installed")
        item = source()
        item["document_identity"] = 5
        item["records"][0]["role"] = []
        errors = coverage.schema_errors(batch(item, "legacy-v1"), coverage.ROOT / "coverage.schema.yaml", True)
        joined = "\n".join(errors)
        self.assertIn("role must be a non-empty string", joined)
        self.assertIn("document_identity must be an identity object", joined)

    def test_schema_errors_fallback_contract_without_jsonschema(self):
        legacy_item = source(); legacy_item["document_identity"] = 5
        legacy_empty_identity = source(); legacy_empty_identity["document_identity"] = {}
        canonical_item = source(); canonical_item["document_identity"] = 5
        child_identity = source(); child_identity["records"][0]["repo"] = "bad"
        read_item = source(); read_item["records"][0]["search_evidence"] = 5
        read_empty_evidence = source(); read_empty_evidence["records"][0]["search_evidence"] = {}
        not_found_item = source()
        not_found = not_found_item["records"][0]
        not_found["status"] = "not_found"
        not_found["path"] = []
        not_found["search_evidence"] = {
            "commit": "a" * 40,
            "method_or_query": "searched complete repository tree",
            "searched_paths_or_tree": ["repository tree"],
            "result": "No role-specific document located",
            "gap": "No fixed-commit file supplies this role",
        }
        cases = [
            (batch(legacy_item, "legacy-v1"), True, "document_identity must be an identity object"),
            (batch(legacy_empty_identity, "legacy-v1"), True, "document_identity missing required field 'source_id'"),
            (batch(canonical_item), False, "document_identity is not allowed in canonical-v2"),
            (batch(child_identity), False, "repo must be owner/name"),
            (batch(read_item), False, "search_evidence must be an object"),
            (batch(read_empty_evidence), False, "search_evidence missing required field 'commit'"),
            (batch(not_found_item), False, "path must be a non-empty string"),
        ]
        original_import = builtins.__import__

        def block_jsonschema(name, *args, **kwargs):
            if name == "jsonschema":
                raise ImportError("forced test absence")
            return original_import(name, *args, **kwargs)

        builtins.__import__ = block_jsonschema
        try:
            for data, legacy_allowed, expected in cases:
                errors = coverage.schema_errors(data, coverage.ROOT / "coverage.schema.yaml", legacy_allowed)
                self.assertIn(expected, "\n".join(errors))
        finally:
            builtins.__import__ = original_import

    def test_legacy_allowlist_requires_coverage_root_path(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "batch-agent-rag.yaml"
            path.write_text("format_version: legacy-v1\nbatch_id: fixture\nchecked_at: today\nevidence_policy: {method: fixture}\nsources: []\n")
            _, errors, _ = coverage.validate_paths([path], coverage.ROOT / "manifest.yaml", coverage.ROOT.parent / "github-ai-repositories.yaml")
        self.assertIn("legacy-v1 batch is not in manifest legacy allowlist at coverage ROOT", "\n".join(errors))

    def test_manifest_role_drift_fails(self):
        errors = []
        coverage.validate_global([source()], {"required_roles": ROLES[:-1], "sources": {}}, {"repositories": []}, errors)
        self.assertIn("required_roles must equal supported role set", "\n".join(errors))

    def test_unknown_field_fails_schema(self):
        item = source(); item["records"][0]["surprise"] = "no"
        self.assertIn("unknown field", "\n".join(self.validate_one(item)))

    def test_schema_and_cli_contract_agree_on_invalid_status_fixture(self):
        item = source(); item["records"][0] = {**IDENTITY, "role": "readme", "status": "not_found"}
        errors = self.validate_one(item)
        self.assertTrue(any("requires search_evidence" in error for error in errors))

    def test_remote_verification_rejects_bad_path_blob_and_locator(self):
        content = b"# Correct heading\nbody\n"
        blob_sha = hashlib.sha1(f"blob {len(content)}\0".encode() + content).hexdigest()
        item = source()
        for entry in item["records"]:
            entry["path"] = "docs/a.md"; entry["git_blob_sha"] = blob_sha; entry["locator"] = "# Correct heading"
        calls = []
        def api(endpoint):
            calls.append(endpoint)
            if "/commits/" in endpoint: return {"tree": {"sha": "c" * 40}}
            if "/trees/" in endpoint: return {"tree": [{"path": "docs/a.md", "sha": blob_sha, "type": "blob"}]}
            return {"content": base64.b64encode(content).decode(), "encoding": "base64"}
        errors = []; counts = coverage.verify_remote([item], errors, api)
        self.assertEqual(5, counts["fixture"]); self.assertFalse(errors); self.assertTrue(any("/trees/" in call for call in calls))
        item["records"][0]["path"] = "missing.md"
        errors = []; coverage.verify_remote([item], errors, api)
        self.assertIn("path/blob mismatch", "\n".join(errors))
        item["records"][0]["path"] = "docs/a.md"; item["records"][0]["git_blob_sha"] = "d" * 40
        errors = []; coverage.verify_remote([item], errors, api)
        self.assertIn("path/blob mismatch", "\n".join(errors))
        item["records"][0]["git_blob_sha"] = blob_sha; item["records"][0]["locator"] = "unlocatable marker"
        errors = []; coverage.verify_remote([item], errors, api)
        self.assertIn("locator fragments not found", "\n".join(errors))

    def test_locator_requires_every_composite_piece_and_real_heading(self):
        text = b"# Security Policy\nordinary security appears in the body\n# Other Heading\n"
        self.assertTrue(coverage.locator_matches(text, "# Security Policy; # Other Heading"))
        self.assertFalse(coverage.locator_matches(text, "# Security Policy; # Missing Heading"))
        self.assertFalse(coverage.locator_matches(text, "SECURITY.md#security"))
        self.assertEqual(["# Missing Heading"], coverage.missing_locator_pieces(text, "# Security Policy; # Missing Heading"))

    def test_symbol_locator_matches_declaration_not_call_spelling(self):
        text = b"class Runner:\n    async def run_sync(self):\n        pass\n"
        self.assertTrue(coverage.locator_matches(text, "symbol:Runner.run_sync"))
        self.assertFalse(coverage.locator_matches(text, "symbol:Runner.missing"))

    def test_symbol_member_requires_its_declaring_owner(self):
        text = b"class RightOwner(\n    GenericBase,\n):\n    def run(self):\n        pass\n\nclass WrongOwner:\n    def other(self):\n        pass\n"
        self.assertTrue(coverage.locator_matches(text, "symbol:RightOwner.run"))
        self.assertFalse(coverage.locator_matches(text, "symbol:WrongOwner.run"))

    def test_fallback_rejects_bad_basic_schema_types_without_throwing(self):
        cases = [
            ("batch_id", 1, "batch_id must be a non-empty string"),
            ("checked_at", [], "checked_at must be a non-empty string"),
            ("evidence_policy", [], "evidence_policy must be a non-empty object"),
        ]
        for field, value, expected in cases:
            data = batch(source()); data[field] = value
            self.assertIn(expected, "\n".join(coverage.fallback_schema_errors(data, False)))
        item = source(); item["repo"] = "bad repo"; item["records"][0]["repo"] = "bad repo"
        self.assertIn("repo must be owner/name", "\n".join(coverage.fallback_schema_errors(batch(item), False)))
        item = source(); item["commit_sha"] = "bad"; item["records"][0]["commit_sha"] = "bad"
        self.assertIn("commit_sha must be 40 lowercase hex characters", "\n".join(coverage.fallback_schema_errors(batch(item), False)))
        item = source(); item["records"][0]["role"] = []
        errors = self.validate_one(item)
        self.assertIn("role must be a non-empty string", "\n".join(errors))

    def test_non_string_status_returns_errors_without_throwing(self):
        for status in ([], {}):
            item = source(); item["records"][0]["status"] = status
            errors = self.validate_one(item)
            self.assertIn("status must be a string", "\n".join(errors))


if __name__ == "__main__": unittest.main()
