from __future__ import annotations
import copy, hashlib, json, subprocess, sys, tempfile, unittest
from pathlib import Path
H=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(H))
from aggregate import WEIGHTS, aggregate_bundles
from blind import build_blind_bundle, verify_position_balance
from common import DIMENSIONS, ROOT, ValidationError, hash_without, load_manifest, sha256_value
from deterministic_gates import execute_gates, validate_gate_report
from evidence import completion_evidence
from holdout import require_unlocked, transition
from plan import build_plan
from validate_corpus import validate_cases
from validate_judgments import validate_judge_diversity, validate_judgment
from validate_review import validate_review, validate_wave_reviews

SKILLS=["human-writing","humanizer","humanizer-zh","stop-slop"]
REVS={s:str(i+1)*40 for i,s in enumerate(SKILLS)}
GEN={"model_provider":"fixture-provider","model_family":"fixture-generator","model_revision":"fixture-v1","system_prompt_sha256":"a"*64,"decoding":{"temperature":0},"tool_access":"none","token_limit":4096,"retry_policy":"none"}
JUDGES={"J01":("current-entitlement","current-model"),"J02":("current-entitlement","current-model"),"J03":("current-entitlement","current-model")}
def unlocked(revision):
    s={"schema_version":"holdout-state/v1","experiment_id":"e","state":"unlocked","candidate_revision":revision,"candidate_tree":"2"*40,"corpus_commitment_sha256":"a"*64,"events":[]}; s["state_sha256"]=sha256_value(s); return s
def headline_evidence(case_ids,base,g,swap,sg):
    s=unlocked(REVS["human-writing"]); evidence=completion_evidence(REVS["human-writing"],case_ids,[base],[g],[swap],[sg]); s["events"]=[{"from":"unlocked","to":"completed","evidence":evidence}]; s["state"]="completed"; s["state_sha256"]=hash_without(s,"state_sha256")
    reviewed=[f"F{f:02d}-H{i:02d}" for f in range(1,13) for i in (1,2)]; records=[{"reviewer_id":rid,"reviewed_case_ids":reviewed,"review_sha256":str(n)*64} for n,rid in ((6,"r1"),(7,"r2"))]
    c={"schema_version":"human-calibration/v1","reviewed_case_ids":reviewed,"reviewer_records":records,"disagreement_case_ids":[],"adjudications":[],"pairwise_agreement":.80,"weighted_kappa":.60,"position_consistency":.95}; c["calibration_sha256"]=sha256_value(c); return s,c
def case(f,m,i):
    source=f"source {f}-{i}"; evidence_sha=hashlib.sha256(source.encode()).hexdigest()
    x={"schema_version":"case/v2","case_id":f"F{f:02d}-{m}{i:02d}","family_id":f"F{f:02d}","split":"development" if m=="D" else "holdout","batch":(i-1)//10+1,"language":"zh" if i%2 else "en","operation":"rewrite","output_form":"paragraph","audience":"technical reader","length_contract":{"unit":"unspecified","minimum":None,"maximum":None,"source":"unspecified"},"risk_level":"low","prompt":f"prompt {f}-{m}-{i}","source":source,"atomic_claims":[],"evidence":[{"evidence_id":"e1","kind":"source_text","text":source,"source_span_sha256":evidence_sha}],"permitted_omissions":[],"gates":[{"gate_id":"g1","gate_type":"contains","target":"fixture","expected":True}],"no_op_policy":"forbidden","constraints":{"protected":[],"required_fields":[],"forbidden_additions":[]},"criteria":[{"criterion_id":"c","text":"criterion","weight":1}],"provenance":{"source_id":"fixture","revision":"a"*40,"license":"Apache-2.0","locator":f"x:{f}:{m}:{i}","content_sha256":"b"*64,"redistribution":"allowed","source_lock_sha256":"d"*64}}; x["case_sha256"]=sha256_value(x); return x
def corpus(): return [case(f,"D",i) for f in range(1,13) for i in range(1,81)]+[case(f,"H",i) for f in range(1,13) for i in range(1,21)]
def ten(m="D",start=1,f=1): return [case(f,m,i) for i in range(start,start+10)]
def fixture_plan(cs,revs=REVS):
    manifest=load_manifest(ROOT); schedule={"development":{},"holdout":{s:manifest["skills"][s]["commit"] for s in SKILLS}}
    # Small fixtures cannot use full-plan validator, so construct exactly the task contract.
    gsha=sha256_value(GEN); tasks=[]
    for c in cs:
        for s in sorted(SKILLS):
            body={"schema_version":"generation-task/v1","experiment_id":"fixture-exp","split":c["split"],"wave":c["batch"],"case_id":c["case_id"],"family_id":c["family_id"],"case_sha256":c["case_sha256"],"prompt_sha256":sha256_value(c["prompt"]),"skill_id":s,"skill_revision":revs[s],"generator_contract_sha256":gsha,"replicate":1}; body["task_id"]=sha256_value(body); body["task_sha256"]=sha256_value(body); tasks.append(body)
    return {"tasks":tasks,"generator_contract_sha256":gsha}
def outputs(cs,revs=REVS):
    p=fixture_plan(cs,revs); rows=[]
    for t in p["tasks"]:
        text=f"{t['case_id']} {t['skill_id']}"; rows.append({**{k:t[k] for k in ("task_id","task_sha256","case_id","case_sha256","prompt_sha256","skill_id","skill_revision","generator_contract_sha256")},"text":text,"output_sha256":hashlib.sha256(text.encode()).hexdigest()})
    return rows,p
def judgment(packet):
    cases=[]
    for c in packet["cases"]: cases.append({"case_id":c["case_id"],"candidates":[{"label":x["label"],"scores":{d:5 for d in DIMENSIONS},"task_specific":[{"criterion_id":criterion["criterion_id"],"score":5} for criterion in c["criteria"]],"hard_issues":[],"evidence":"fixture evidence"} for x in c["candidates"]],"ranking":[["A","B","C","D"]]})
    provider,family=JUDGES[packet["judge_id"]]
    return {"schema_version":"judgment/v1","judge_id":packet["judge_id"],"provider":provider,"model_family":family,"model_revision":"judge-v1","judge_prompt_sha256":"c"*64,"context_id":"ctx-"+packet["judge_id"],"packet_sha256":sha256_value(packet),"cases":cases}
def gates(out,batch="b"):
    r={"schema_version":"deterministic-gates/v1","batch_id":batch,"outputs":[{"task_id":x["task_id"],"case_id":x["case_id"],"output_sha256":x["output_sha256"],"checks":[{"check_id":"g1","gate_type":"contains","target":"fixture","expected":True,"passed":True,"severity":"critical","evidence":"fixture pass"}],"critical_failure":False} for x in out]}; r["report_sha256"]=sha256_value(r); return r
def bundle(cs,revs=REVS,offset=0,batch="b",order="base"):
    out,p=outputs(cs,revs); packets,m=build_blind_bundle(cs,out,SKILLS,"fixture-exp",batch,offset,plan=p,order_contract=order); return (m,{x["judge_id"]:x for x in packets},{x["judge_id"]:judgment(x) for x in packets}),gates(out,batch)

class CorpusPlan(unittest.TestCase):
 def test_1200_80_20_and_4800(self):
    c=corpus(); self.assertEqual(validate_cases(c)["splits"],{"development":960,"holdout":240}); revision=load_manifest(ROOT)["skills"]["human-writing"]["commit"]
    dev=[x for x in c if x["split"]=="development" and x["batch"]==1]; holdout=[x for x in c if x["split"]=="holdout"]
    self.assertEqual(build_plan(dev,generator_contract=GEN)["task_count"],480); self.assertEqual(build_plan(holdout,generator_contract=GEN,holdout_state=unlocked(revision))["task_count"],960)
 def test_hash_and_duplicate_fail(self):
    c=corpus(); bad=copy.deepcopy(c); bad[0]["prompt"]="x"
    with self.assertRaises(ValidationError): validate_cases(bad)
    with self.assertRaises(ValidationError): validate_cases(c+[c[0]])
    bad=copy.deepcopy(c); bad[0]["criteria"].append(copy.deepcopy(bad[0]["criteria"][0])); bad[0]["case_sha256"]=hash_without(bad[0],"case_sha256")
    with self.assertRaisesRegex(ValidationError,"duplicate criterion_id"): validate_cases(bad)
 def test_generator_contract_and_fixed_comparator(self):
    with self.assertRaisesRegex(ValidationError,"one plan"): build_plan(corpus())
    defaults={s:load_manifest(ROOT)["skills"][s]["commit"] for s in SKILLS}; wave=dict(defaults); wave["humanizer"]="f"*40
    dev=[x for x in corpus() if x["split"]=="development" and x["batch"]==1]
    with self.assertRaisesRegex(ValidationError,"fixed comparator"): build_plan(dev,schedule={"development":{"1":wave},"holdout":defaults},generator_contract=GEN)

class BlindJudgeGate(unittest.TestCase):
 def setUp(self): self.cs=ten(); self.out,self.plan=outputs(self.cs); self.packets,self.mapping=build_blind_bundle(self.cs,self.out,SKILLS,"fixture-exp","b",plan=self.plan)
 def test_position_balance_and_swap_contract(self):
    verify_position_balance(self.mapping); _,sw=build_blind_bundle(self.cs,self.out,SKILLS,"fixture-exp","s",plan=self.plan,order_contract="swapped"); self.assertEqual(sw["order_contract"],"swapped")
 def test_task_binding(self):
    bad=copy.deepcopy(self.out); bad[0]["skill_revision"]="e"*40
    with self.assertRaisesRegex(ValidationError,"identity"): build_blind_bundle(self.cs,bad,SKILLS,"fixture-exp","b",plan=self.plan)
    bad_plan=copy.deepcopy(self.plan); bad_plan["tasks"][0]["prompt_sha256"]="0"*64
    with self.assertRaisesRegex(ValidationError,"task_id"): build_blind_bundle(self.cs,self.out,SKILLS,"fixture-exp","b",plan=bad_plan)
 def test_judge_metadata_diversity(self):
    js=[judgment(x) for x in self.packets]; validate_judge_diversity(js)
    js[2]["context_id"]=js[1]["context_id"]
    with self.assertRaisesRegex(ValidationError,"three distinct contexts"): validate_judge_diversity(js)
 def test_schema_packet_and_hard_cap(self):
    j=judgment(self.packets[0]); validate_judgment(j,self.packets[0]); j["cases"][0]["candidates"][0]["hard_issues"]=[{"type":"scope","claim":"x","evidence":"y","material":False}]
    with self.assertRaisesRegex(ValidationError,"cap fidelity"): validate_judgment(j,self.packets[0])
 def test_task_specific_ids_fail_closed(self):
    j=judgment(self.packets[0]); c=j["cases"][0]["candidates"][0]; c["task_specific"]=[]
    with self.assertRaises(ValidationError): validate_judgment(j,self.packets[0])
    j=judgment(self.packets[0]); c=j["cases"][0]["candidates"][0]; c["task_specific"].append(copy.deepcopy(c["task_specific"][0]))
    with self.assertRaises(ValidationError): validate_judgment(j,self.packets[0])
    j=judgment(self.packets[0]); j["cases"][0]["candidates"][0]["task_specific"][0]["criterion_id"]="wrong"
    with self.assertRaisesRegex(ValidationError,"match packet"): validate_judgment(j,self.packets[0])
 def test_gate_report_fail_closed(self):
    r=gates(self.out); expected={x["task_id"]:{"output_sha256":x["output_sha256"]} for x in self.out}; case_index={c["case_id"]:c for c in self.cs}; validate_gate_report(r,expected,case_index); r["outputs"][0]["checks"][0]["passed"]=False
    with self.assertRaises(ValidationError): validate_gate_report(r,expected,case_index)
    r=gates(self.out); r["outputs"][0]["checks"]=[]; r["outputs"][0]["critical_failure"]=False; r["report_sha256"]=hash_without(r,"report_sha256")
    with self.assertRaisesRegex(ValidationError,"cover every"): validate_gate_report(r,expected,case_index)
    r=gates(self.out); r["outputs"][0]["checks"][0]["target"]="tampered"; r["report_sha256"]=hash_without(r,"report_sha256")
    with self.assertRaisesRegex(ValidationError,"frozen case gate"): validate_gate_report(r,expected,case_index)
    with self.assertRaisesRegex(ValidationError,"case contracts"): validate_gate_report(gates(self.out),expected)
 def test_gate_executor_blocks_unsupported_semantic_gate(self):
    cs=copy.deepcopy(self.cs); cs[0]["gates"][0]["gate_type"]="grounding"
    with self.assertRaisesRegex(ValidationError,"dedicated verified executor"): execute_gates("b",cs,self.out)

class StateReviewAggregate(unittest.TestCase):
 def test_holdout_state_machine(self):
    s={"schema_version":"holdout-state/v1","experiment_id":"e","state":"sealed","candidate_revision":None,"candidate_tree":None,"corpus_commitment_sha256":"a"*64,"events":[]}; s["state_sha256"]=sha256_value(s)
    f=transition(s,"candidate_frozen",{"candidate_revision":"1"*40,"candidate_tree":"2"*40,"development_complete_sha256":"3"*64})
    with self.assertRaises(ValidationError): require_unlocked(f,"1"*40)
    u=transition(f,"unlocked",{"commitment_sha256":"a"*64,"freeze_state_sha256":f["state_sha256"]}); require_unlocked(u,"1"*40)
    u["candidate_revision"]="9"*40
    with self.assertRaisesRegex(ValidationError,"hash invalid"): require_unlocked(u,"9"*40)
 def test_review_hash_change_control(self):
    r={"schema_version":"review/v2","batch_id":"D01","wave_id":"D01","scope":"global_wave","family_id":None,"reviewed_case_ids":[f"F{f:02d}-D{i:02d}" for f in range(1,13) for i in range(1,11)],"skill_revision":"1"*40,"failure_cases":["x"],"root_causes":[{"tag":"t","evidence":["e"],"recurrence":2}],"decision":"accepted","proposed_change":"change","counterexample":"counter","next_revision":"2"*40}; r["review_sha256"]=sha256_value(r); validate_review(r,"1"*40)
    weak=copy.deepcopy(r); weak["root_causes"][0]["recurrence"]=1; weak["review_sha256"]=hash_without(weak,"review_sha256")
    with self.assertRaisesRegex(ValidationError,"recurring"): validate_review(weak,"1"*40)
 def test_wave_review_requires_12x10_plus_global(self):
    expected={f"F{f:02d}-D{i:02d}" for f in range(1,13) for i in range(1,11)}; reviews=[]
    for f in range(1,13):
        r={"schema_version":"review/v2","batch_id":"D01","wave_id":"D01","scope":"family_slice","family_id":f"F{f:02d}","reviewed_case_ids":[f"F{f:02d}-D{i:02d}" for i in range(1,11)],"skill_revision":"1"*40,"failure_cases":[],"root_causes":[],"decision":"no_change","proposed_change":None,"counterexample":None,"next_revision":None}; r["review_sha256"]=sha256_value(r); reviews.append(r)
    g={"schema_version":"review/v2","batch_id":"D01","wave_id":"D01","scope":"global_wave","family_id":None,"reviewed_case_ids":sorted(expected),"skill_revision":"1"*40,"failure_cases":[],"root_causes":[],"decision":"no_change","proposed_change":None,"counterexample":None,"next_revision":None}; g["review_sha256"]=sha256_value(g); reviews.append(g)
    self.assertEqual(validate_wave_reviews(reviews,"1"*40,expected)["reviewed_cases"],120)
    with self.assertRaisesRegex(ValidationError,"12 family"): validate_wave_reviews(reviews[:-1],"1"*40,expected)
 def test_partial_weight_median_and_gate_eligibility(self):
    b,g=bundle(ten()); result=aggregate_bundles([b],[g]); self.assertFalse(result["headline_eligible"]); self.assertEqual(result["score_weights"],WEIGHTS); self.assertEqual(result["judge_aggregation"],"median")
    g2=copy.deepcopy(g); g2["outputs"][0]["checks"][0]["passed"]=False; g2["outputs"][0]["critical_failure"]=True; g2["report_sha256"]=hash_without(g2,"report_sha256"); result=aggregate_bundles([b],[g2]); self.assertTrue(any(x["critical_gate_rate"]>0 for x in result["summary"].values()))
    b2=copy.deepcopy(b)
    for j in b2[2].values():
        c=j["cases"][0]["candidates"][0]; c["scores"]["fidelity"]=1; c["hard_issues"]=[{"type":"scope","claim":"material reversal","evidence":"fixture evidence","material":True}]
    result=aggregate_bundles([b2],[g]); self.assertTrue(any(x["critical_gate_rate"]>0 for x in result["summary"].values()))
 def test_task_specific_weight_must_be_positive(self):
    b,g=bundle(ten());
    for packet in b[1].values(): packet["cases"][0]["criteria"][0]["weight"]=0
    # Rebind packet hashes in mapping and judgments so failure reaches weight gate.
    maps={x["judge_id"]:x for x in b[0]["packets"]}
    for jid,packet in b[1].items(): maps[jid]["packet_sha256"]=sha256_value(packet); b[2][jid]["packet_sha256"]=sha256_value(packet)
    b[0]["mapping_sha256"]=hash_without(b[0],"mapping_sha256")
    with self.assertRaisesRegex(ValidationError,"weights"): aggregate_bundles([b],[g])
 def test_holdout_partial_cannot_headline(self):
    b,g=bundle(ten("H"))
    with self.assertRaisesRegex(ValidationError,"partial mode"): aggregate_bundles([b],[g])
    with self.assertRaises(ValidationError): aggregate_bundles([b],[g],mode="holdout_headline")
 def test_mixed_holdout_revision_rejected_before_headline(self):
    b1,g1=bundle(ten("H",1),batch="h1"); changed=dict(REVS); changed["human-writing"]="e"*40; b2,g2=bundle(ten("H",11),changed,10,"h2")
    with self.assertRaises(ValidationError): aggregate_bundles([b1,b2],[g1,g2],mode="holdout_headline")
 def test_complete_headline_has_family_ci_and_holm(self):
    all_cases=[case(f,"H",i) for f in range(1,13) for i in range(1,21)]; base,g=bundle(all_cases,batch="holdout")
    audit_cases=[case(f,"H",i) for f in range(1,13) for i in range(1,5)]; swap,sg=bundle(audit_cases,batch="swap",order="swapped")
    state,calibration=headline_evidence({c["case_id"] for c in all_cases},base,g,swap,sg); result=aggregate_bundles([base],[g],mode="holdout_headline",swap_bundles=[swap],swap_gate_reports=[sg],holdout_state=state,human_calibration=calibration)
    self.assertTrue(result["headline_eligible"]); self.assertEqual(result["cases"],240)
    self.assertEqual(len(result["comparisons"]),3)
    self.assertTrue(all(len(x["families"])==12 and all("holm_adjusted_p" in f for f in x["families"]) for x in result["comparisons"]))
    self.assertTrue(all(0<=x["first_place_share"]<=1 for x in result["summary"].values()))
    tampered=copy.deepcopy(base); tampered[2]["J01"]["cases"][0]["candidates"][0]["evidence"]="tampered but schema-valid and locally reserialized"
    with self.assertRaisesRegex(ValidationError,"artifact/case commitment"): aggregate_bundles([tampered],[g],mode="holdout_headline",swap_bundles=[swap],swap_gate_reports=[sg],holdout_state=state,human_calibration=calibration)
    bad_cal=copy.deepcopy(calibration); bad_cal["reviewed_case_ids"]=bad_cal["reviewed_case_ids"][:-1]; bad_cal["calibration_sha256"]=hash_without(bad_cal,"calibration_sha256")
    with self.assertRaises(ValidationError): aggregate_bundles([base],[g],mode="holdout_headline",swap_bundles=[swap],swap_gate_reports=[sg],holdout_state=state,human_calibration=bad_cal)
    critical=copy.deepcopy(g); critical["outputs"][0]["checks"][0]["passed"]=False; critical["outputs"][0]["critical_failure"]=True; critical["report_sha256"]=hash_without(critical,"report_sha256")
    with self.assertRaisesRegex(ValidationError,"artifact/case commitment"): aggregate_bundles([base],[critical],mode="holdout_headline",swap_bundles=[swap],swap_gate_reports=[sg],holdout_state=state,human_calibration=calibration)
    critical_state,_=headline_evidence({c["case_id"] for c in all_cases},base,critical,swap,sg)
    blocked=aggregate_bundles([base],[critical],mode="holdout_headline",swap_bundles=[swap],swap_gate_reports=[sg],holdout_state=critical_state,human_calibration=calibration)
    self.assertTrue(all(not item["parity_decision"] and item["eligible_paired_cases"]<240 for item in blocked["comparisons"]))
 def test_headline_cli_accepts_swap_artifacts(self):
    all_cases=[case(f,"H",i) for f in range(1,13) for i in range(1,21)]; base,g=bundle(all_cases,batch="holdout")
    audit=[case(f,"H",i) for f in range(1,13) for i in range(1,5)]; swap,sg=bundle(audit,batch="swap",order="swapped"); state,cal=headline_evidence({c["case_id"] for c in all_cases},base,g,swap,sg)
    with tempfile.TemporaryDirectory() as td:
        root=Path(td); bd=root/"base"; sd=root/"swap"; bd.mkdir(); sd.mkdir()
        for directory,data in ((bd,base),(sd,swap)):
            (directory/"mapping.json").write_text(json.dumps(data[0]));
            for jid,packet in data[1].items():(directory/f"packet-{jid}.json").write_text(json.dumps(packet))
            for jid,j in data[2].items():(directory/f"judgment-{jid}.json").write_text(json.dumps(j))
        paths={"g":g,"sg":sg,"state":state,"cal":cal}
        for name,value in paths.items():(root/f"{name}.json").write_text(json.dumps(value))
        command=[sys.executable,str(H/"aggregate.py"),"--bundle",str(bd),"--gate-report",str(root/"g.json"),"--swap-bundle",str(sd),"--swap-gate-report",str(root/"sg.json"),"--mode","holdout_headline","--holdout-state",str(root/"state.json"),"--human-calibration",str(root/"cal.json"),"--output",str(root/"out.json")]
        run=subprocess.run(command,capture_output=True,text=True)
        self.assertEqual(run.returncode,0,run.stderr); self.assertTrue(json.loads((root/"out.json").read_text())["headline_eligible"])

if __name__=="__main__": unittest.main()
