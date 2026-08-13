from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

H = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(H))

from aggregate import aggregate_bundles
from artifact_store import ArtifactStore
from common import ValidationError, load_manifest, sha256_value, skill_revisions
from dispatch import dispatch, export_outputs
from execution_state import complete_development_wave, initialize, revisions_for_next_wave
from test_harness import SKILLS, bundle, case, gates, outputs


def snapshots(revisions):
    items = []
    for skill_id, revision in revisions.items():
        text = f"# {skill_id}\nfixture instructions\n"
        import hashlib
        items.append({"skill_id": skill_id, "revision": revision, "source_uri": "fixture://skill",
                      "skill_text": text, "skill_sha256": hashlib.sha256(text.encode()).hexdigest()})
    return {"schema_version": "skill-snapshots/v1", "skills": items}


ADAPTER = r'''
import json,sys
r=json.load(sys.stdin); g=r["generator_contract"]
json.dump({"schema_version":"generation-response/v1","task_id":r["task"]["task_id"],
"text":"fixture generated text","provider_request_id":"req-1","model_provider":g["model_provider"],
"model_family":g["model_family"],"model_revision":g["model_revision"],
"usage":{"input_tokens":2,"output_tokens":3,"total_tokens":5},"cost":None},sys.stdout)
'''

SECRET_ADAPTER = r'''
import sys
sys.stderr.write("fixture-secret-token")
raise SystemExit(7)
'''


class DispatchPersistence(unittest.TestCase):
    def test_real_adapter_dispatch_receipts_resume_and_export(self):
        revisions = {skill: str(index + 1) * 40 for index, skill in enumerate(SKILLS)}
        cases = [case(1, "D", 1)]
        _, plan = outputs(cases, revisions)
        plan["generator_contract"] = {
            "model_provider": "fixture-provider", "model_family": "fixture-generator", "model_revision": "fixture-v1",
            "system_prompt_sha256": "a"*64, "decoding": {"temperature": 0}, "tool_access": "none",
            "token_limit": 4096, "retry_policy": "none",
        }
        plan["generator_contract_sha256"] = sha256_value(plan["generator_contract"])
        with tempfile.TemporaryDirectory() as temp:
            store = ArtifactStore(Path(temp))
            first = dispatch(plan, cases, snapshots(revisions), store, "D01", [sys.executable, "-c", ADAPTER], max_tasks=2)
            self.assertEqual((first["completed"], first["pending"]), (2, 2))
            second = dispatch(plan, cases, snapshots(revisions), store, "D01", [sys.executable, "-c", ADAPTER])
            self.assertEqual((second["completed"], second["pending"]), (4, 0))
            self.assertEqual(len(export_outputs(plan, store, "D01")), 4)
            attempts = list((Path(temp)/"runs"/"D01"/"attempts").glob("*/*.json"))
            self.assertEqual(len(attempts), 4)
            receipt = store.get_json(json.loads(attempts[0].read_text()))
            self.assertIsNone(receipt["cost"])
            self.assertEqual(receipt["usage"]["total_tokens"], 5)

    def test_prepare_only_never_claims_generation(self):
        revisions = {skill: str(index + 1) * 40 for index, skill in enumerate(SKILLS)}
        cases = [case(1, "D", 1)]; _, plan = outputs(cases, revisions)
        plan["generator_contract"] = {
            "model_provider": "fixture-provider", "model_family": "fixture-generator", "model_revision": "fixture-v1",
            "system_prompt_sha256": "a"*64, "decoding": {"temperature": 0}, "tool_access": "none",
            "token_limit": 4096, "retry_policy": "none"}
        plan["generator_contract_sha256"] = sha256_value(plan["generator_contract"])
        with tempfile.TemporaryDirectory() as temp:
            result = dispatch(plan, cases, snapshots(revisions), ArtifactStore(Path(temp)), "prepare", None)
            self.assertEqual(result["completed"], 0); self.assertEqual(result["pending"], 4)
            with self.assertRaisesRegex(ValidationError, "incomplete run"):
                export_outputs(plan, ArtifactStore(Path(temp)), "prepare")

    def test_failure_receipt_redacts_stderr_and_rejects_dot_run_ids(self):
        revisions = {skill: str(index + 1) * 40 for index, skill in enumerate(SKILLS)}
        cases = [case(1, "D", 1)]; _, plan = outputs(cases, revisions)
        plan["generator_contract"] = {
            "model_provider": "fixture-provider", "model_family": "fixture-generator", "model_revision": "fixture-v1",
            "system_prompt_sha256": "a"*64, "decoding": {"temperature": 0}, "tool_access": "none",
            "token_limit": 4096, "retry_policy": "none"}
        plan["generator_contract_sha256"] = sha256_value(plan["generator_contract"])
        with tempfile.TemporaryDirectory() as temp:
            store=ArtifactStore(Path(temp)/"store"); restricted=Path(temp)/"restricted"
            with self.assertRaisesRegex(ValidationError,"run id"):
                dispatch(plan,cases,snapshots(revisions),store,".",None)
            with self.assertRaisesRegex(ValidationError,"run id"):
                dispatch(plan,cases,snapshots(revisions),store,"..",None)
            result=dispatch(plan,cases,snapshots(revisions),store,"D01",[sys.executable,"-c",SECRET_ADAPTER],max_tasks=1,restricted_log_dir=restricted)
            self.assertEqual(result["failed"],1)
            attempt=next((Path(temp)/"store"/"runs"/"D01"/"attempts").glob("*/*.json"))
            receipt=store.get_json(json.loads(attempt.read_text()))
            serialized=json.dumps(receipt)
            self.assertNotIn("fixture-secret-token",serialized)
            self.assertEqual(receipt["error"]["category"],"adapter_exit")
            self.assertEqual(receipt["error"]["exit_code"],7)
            log=next(restricted.glob("D01/*/*.stderr"))
            self.assertEqual(log.read_text(),"fixture-secret-token")


def reviews_for(wave, revision, decision="no_change", next_revision=None):
    start = (wave-1)*10 + 1
    expected = [f"F{family:02d}-D{index:02d}" for family in range(1,13) for index in range(start,start+10)]
    rows=[]
    for family in range(1,13):
        row={"schema_version":"review/v2","batch_id":f"D{wave:02d}","wave_id":f"D{wave:02d}","scope":"family_slice",
             "family_id":f"F{family:02d}","reviewed_case_ids":[f"F{family:02d}-D{i:02d}" for i in range(start,start+10)],
             "skill_revision":revision,"failure_cases":[],"root_causes":[],"decision":"no_change",
             "proposed_change":None,"counterexample":None,"next_revision":None}
        row["review_sha256"]=sha256_value(row); rows.append(row)
    global_row={"schema_version":"review/v2","batch_id":f"D{wave:02d}","wave_id":f"D{wave:02d}","scope":"global_wave",
                "family_id":None,"reviewed_case_ids":expected,"skill_revision":revision,
                "failure_cases":["F01-D01"] if decision=="accepted" else [],
                "root_causes":[{"tag":"recurring","evidence":["two failures"],"recurrence":2}] if decision=="accepted" else [],
                "decision":decision,"proposed_change":"fix" if decision=="accepted" else None,
                "counterexample":"counter" if decision=="accepted" else None,"next_revision":next_revision}
    global_row["review_sha256"]=sha256_value(global_row); rows.append(global_row); return rows


class ReviewLoop(unittest.TestCase):
    def test_cannot_skip_review_and_accepted_revision_opens_next_wave(self):
        state=initialize(); revisions=skill_revisions(load_manifest())
        cases=[case(f,"D",i) for f in range(1,13) for i in range(1,11)]
        out,plan=outputs(cases,revisions); b,g=bundle(cases,revisions,batch="D01")
        aggregate=aggregate_bundles([b],[g])
        new_revision="e"*40
        with self.assertRaisesRegex(ValidationError,"12 family"):
            complete_development_wave(state,1,cases,plan,out,g,aggregate,[],[b])
        updated=complete_development_wave(state,1,cases,plan,out,g,aggregate,reviews_for(1,revisions["human-writing"],"accepted",new_revision),[b])
        self.assertEqual(updated["next_wave"],2)
        self.assertEqual(revisions_for_next_wave(updated)["human-writing"],new_revision)
        with self.assertRaisesRegex(ValidationError,"not currently open"):
            complete_development_wave(updated,3,cases,plan,out,g,aggregate,reviews_for(1,new_revision),[b])
        wrong=copy.deepcopy(state); wrong["current_revisions"]=dict(wrong["current_revisions"]); wrong["current_revisions"]["human-writing"]="f"*40
        wrong["state_sha256"]=sha256_value({key:value for key,value in wrong.items() if key!="state_sha256"})
        with self.assertRaisesRegex(ValidationError,"revisions differ"):
            complete_development_wave(wrong,1,cases,plan,out,g,aggregate,reviews_for(1,"f"*40),[b])
        forged=copy.deepcopy(aggregate)
        first=next(iter(forged["summary"].values())); first["uncapped_weighted_mean"]+=0.5
        forged["aggregate_sha256"]=sha256_value({key:value for key,value in forged.items() if key!="aggregate_sha256"})
        with self.assertRaisesRegex(ValidationError,"complete blind/judge input commitment"):
            complete_development_wave(state,1,cases,plan,out,g,forged,reviews_for(1,revisions["human-writing"]),[b])


if __name__ == "__main__":
    unittest.main()
