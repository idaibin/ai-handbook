#!/usr/bin/env python3
"""Preregistered weighted, median, gate-aware benchmark aggregation."""
from __future__ import annotations
import argparse, json, math, random, re, statistics
from collections import defaultdict
from pathlib import Path
from typing import Any
from blind import verify_position_balance
from common import DIMENSIONS, ROOT, ValidationError, hash_without, read_json, sha256_value, write_json
from deterministic_gates import validate_gate_report
from evidence import complete_evidence_digest
from validate_judgments import validate_judge_diversity, validate_judgment

WEIGHTS={"fidelity":.30,"task_specific":.20,"instruction_structure":.15,"clarity":.10,"naturalness":.15,"restraint":.10}
def mean(v):
    if not v: raise ValidationError("cannot average empty values")
    return sum(v)/len(v)
def quantile(v,p):
    v=sorted(v); x=p*(len(v)-1); a=int(x); b=min(a+1,len(v)-1); return v[a]*(b-x)+v[b]*(x-a)
def weighted(s,task_specific):
    if set(s)!=(set(WEIGHTS)-{"task_specific"}): raise ValidationError("five fixed general leaves required")
    return sum(s[k]*WEIGHTS[k] for k in s)+task_specific*WEIGHTS["task_specific"]
def stratified_bootstrap(strata:dict[str,list[float]],samples=10000,seed=20260813):
    if samples!=10000 or not strata or any(not x for x in strata.values()): raise ValidationError("bootstrap requires 10000 samples and nonempty strata")
    rng=random.Random(seed); draws=[]
    for _ in range(samples):
        draws.append(mean([mean([x[rng.randrange(len(x))] for _ in x]) for x in [strata[k] for k in sorted(strata)]]))
    p=min(1.,2*min(sum(x<=0 for x in draws)/samples,sum(x>=0 for x in draws)/samples))
    return [round(quantile(draws,.025),4),round(quantile(draws,.975),4)],p
def holm(items):
    out={}; running=0.; n=len(items)
    for i,(name,p) in enumerate(sorted(items,key=lambda x:x[1])):
        running=max(running,min(1.,(n-i)*p)); out[name]=round(running,4)
    return out
def load_bundle(path:Path):
    mapping=read_json(path/"mapping.json")
    packets={x["judge_id"]:x for x in (read_json(p) for p in sorted(path.glob("packet-J*.json")))}
    judgments={x["judge_id"]:x for x in (read_json(p) for p in sorted(path.glob("judgment-J*.json")))}
    return mapping,packets,judgments
def validate_mapping(m,order="base"):
    allowed={"schema_version","experiment_id","batch_id","case_offset","order_contract","slice_values","skills","packets","mapping_sha256"}
    if set(m)!=allowed or m["schema_version"]!="blind-mapping/v1" or m["order_contract"]!=order: raise ValidationError("mapping/order contract invalid")
    if hash_without(m,"mapping_sha256")!=m["mapping_sha256"]: raise ValidationError("mapping hash mismatch")
    locks={x["skill_id"]:x["revision"] for x in m["skills"]}
    if len(locks)!=4 or len(m["packets"])!=3: raise ValidationError("mapping skill/judge cardinality invalid")
    cases=None
    for p in m["packets"]:
        cases=set(p["cases"]) if cases is None else cases
        if set(p)!={"judge_id","packet_sha256","cases"} or set(p["cases"])!=cases: raise ValidationError("mapping packet contract invalid")
        for labels in p["cases"].values():
            for x in labels.values():
                if set(x)!={"skill_id","skill_revision","task_id","output_sha256"} or x["skill_revision"]!=locks.get(x["skill_id"]): raise ValidationError("mapping revision identity invalid")
                if not re.fullmatch(r"[0-9a-f]{64}",x["task_id"]+"") or not re.fullmatch(r"[0-9a-f]{64}",x["output_sha256"]+""): raise ValidationError("mapping evidence hash invalid")
    verify_position_balance(m)
def collect(bundle,gates,root=ROOT,order="base"):
    m,packets,judgments=bundle; validate_mapping(m,order)
    maps={x["judge_id"]:x for x in m["packets"]}
    if set(maps)!=set(packets) or set(maps)!=set(judgments): raise ValidationError("judge artifact set mismatch")
    validate_judge_diversity(list(judgments.values()))
    expected={x["task_id"]:{"output_sha256":x["output_sha256"]} for p in maps.values() for labels in p["cases"].values() for x in labels.values()}
    packet_case_index={case["case_id"]:case for packet in packets.values() for case in packet["cases"]}
    gates=validate_gate_report(gates,expected,packet_case_index); rows=[]
    for jid,mp in maps.items():
        packet=packets[jid]
        if sha256_value(packet)!=mp["packet_sha256"]: raise ValidationError("packet hash mismatch")
        validate_judgment(judgments[jid],packet,root)
        pc={x["case_id"]:x for x in packet["cases"]}; jr={x["case_id"]:x for x in judgments[jid]["cases"]}
        for cid,labels in mp["cases"].items():
            po={x["label"]:x for x in pc[cid]["candidates"]}; jo={x["label"]:x for x in jr[cid]["candidates"]}
            for label,x in labels.items():
                if po[label]["output_sha256"]!=x["output_sha256"]: raise ValidationError("mapping/output hash mismatch")
                leaders=jr[cid]["ranking"][0]
                rows.append({"batch_id":m["batch_id"],"judge_id":jid,"case_id":cid,"family_id":cid[:3],"split":"development" if "-D" in cid else "holdout","language":pc[cid]["language"],"length_unit":pc[cid]["length_contract"]["unit"],"no_op":pc[cid]["no_op_policy"]=="required","skill_id":x["skill_id"],"skill_revision":x["skill_revision"],"task_id":x["task_id"],"scores":jo[label]["scores"],"task_specific":jo[label]["task_specific"],"criteria":pc[cid]["criteria"],"judge_hard":bool(jo[label]["hard_issues"]),"judge_critical":any(issue["material"] for issue in jo[label]["hard_issues"]),"critical_gate":gates[x["task_id"]]["critical_failure"],"first_share":(1/len(leaders)) if label in leaders else 0})
    if len(rows)!=len({x["case_id"] for x in rows})*12: raise ValidationError("bundle cardinality incomplete")
    return rows
def preference_leaders(bundle):
    m,_,judgments=bundle; maps={x["judge_id"]:x for x in m["packets"]}; counts=defaultdict(lambda:defaultdict(int))
    for jid,j in judgments.items():
        reviews={x["case_id"]:x for x in j["cases"]}
        for cid,labels in maps[jid]["cases"].items():
            for label in reviews[cid]["ranking"][0]: counts[cid][labels[label]["skill_id"]]+=1
    result={}
    for cid,skills in counts.items():
        maximum=max(skills.values()); result[cid]={skill for skill,count in skills.items() if count==maximum}
    return result
def aggregate_bundles(bundles,gate_reports,root=ROOT,mode="development_partial",bootstrap_samples=10000,swap_bundles=None,swap_gate_reports=None,holdout_state=None,human_calibration=None):
    if mode not in {"development_partial","holdout_headline"} or not bundles or len(bundles)!=len(gate_reports): raise ValidationError("aggregation mode/input invalid")
    rows=[]; batches=set(); cases=set(); experiment=bundles[0][0]["experiment_id"]
    for bundle,gates in zip(bundles,gate_reports):
        m=bundle[0]; batch_cases=set(m["packets"][0]["cases"])
        if m["experiment_id"]!=experiment or m["batch_id"] in batches or cases&batch_cases: raise ValidationError("duplicate/mixed experiment evidence")
        batches.add(m["batch_id"]); cases|=batch_cases; rows+=collect(bundle,gates,root)
    splits={x["split"] for x in rows}
    if mode=="development_partial" and splits!={"development"}: raise ValidationError("partial mode accepts development only")
    if mode=="holdout_headline":
        if not isinstance(holdout_state,dict) or hash_without(holdout_state,"state_sha256")!=holdout_state.get("state_sha256") or holdout_state.get("state")!="completed": raise ValidationError("headline requires hash-valid completed holdout state")
        completion=holdout_state.get("events",[])[-1] if holdout_state.get("events") else None
        if not completion or completion.get("to")!="completed": raise ValidationError("completed holdout state lacks completion artifact commitment")
        completion_evidence=completion.get("evidence",{})
        expected_calibration={"schema_version","reviewed_case_ids","reviewer_records","disagreement_case_ids","adjudications","pairwise_agreement","weighted_kappa","position_consistency","calibration_sha256"}
        if not isinstance(human_calibration,dict) or set(human_calibration)!=expected_calibration or hash_without(human_calibration,"calibration_sha256")!=human_calibration.get("calibration_sha256"): raise ValidationError("headline requires hash-valid human calibration report")
        reviewed=human_calibration["reviewed_case_ids"]
        if human_calibration["schema_version"]!="human-calibration/v1" or len(reviewed)<24 or len(reviewed)!=len(set(reviewed)) or len(human_calibration["reviewer_records"])<2 or human_calibration["pairwise_agreement"]<.75 or human_calibration["weighted_kappa"]<.50 or human_calibration["position_consistency"]<.90: raise ValidationError("human calibration completion thresholds not met")
        if any(sum(case.startswith(f"F{i:02d}-H") for case in reviewed)<2 for i in range(1,13)): raise ValidationError("human calibration requires at least two reviewed cases per family")
        reviewer_ids=set()
        for record in human_calibration["reviewer_records"]:
            if set(record)!={"reviewer_id","reviewed_case_ids","review_sha256"} or record["reviewer_id"] in reviewer_ids or set(record["reviewed_case_ids"])!=set(reviewed) or not re.fullmatch(r"[0-9a-f]{64}",record["review_sha256"]): raise ValidationError("human calibration reviewer record invalid")
            reviewer_ids.add(record["reviewer_id"])
        adjudicated={item["case_id"] for item in human_calibration["adjudications"] if set(item)=={"case_id","adjudicator_id","decision_sha256"} and re.fullmatch(r"[0-9a-f]{64}",item["decision_sha256"])}
        if adjudicated!=set(human_calibration["disagreement_case_ids"]): raise ValidationError("human calibration disagreements require exact adjudication records")
        if splits!={"holdout"} or len(cases)!=240 or bootstrap_samples!=10000: raise ValidationError("headline requires complete 240-case holdout and 10000 bootstrap")
        if {sum(c.startswith(f"F{i:02d}-H") for c in cases) for i in range(1,13)}!={20}: raise ValidationError("headline needs 20 cases per family")
        if set(reviewed)-cases: raise ValidationError("human calibration reviewed unknown holdout cases")
        actual_digest=complete_evidence_digest(bundles,gate_reports,swap_bundles or [],swap_gate_reports or [])
        if completion_evidence.get("case_ids_sha256")!=sha256_value(sorted(cases)) or completion_evidence.get("complete_240_case_artifact_sha256")!=actual_digest: raise ValidationError("holdout completion artifact/case commitment mismatch")
    rev=defaultdict(set)
    for x in rows: rev[(x["split"],x["skill_id"])].add(x["skill_revision"])
    if mode=="holdout_headline" and any(len(x)!=1 for x in rev.values()): raise ValidationError("headline mixes revisions")
    if mode=="holdout_headline" and (completion_evidence.get("candidate_revision")!=next(iter(rev[("holdout","human-writing")])) or holdout_state.get("candidate_revision")!=completion_evidence.get("candidate_revision")): raise ValidationError("completed holdout state does not bind current human-writing revision")
    grouped=defaultdict(list)
    for x in rows: grouped[(x["split"],x["skill_id"],x["skill_revision"],x["case_id"])].append(x)
    case_rows=[]
    for (split,skill,revision,cid),rs in grouped.items():
        if len(rs)!=3 or len({x["judge_id"] for x in rs})!=3: raise ValidationError("case/skill needs three judges")
        med={d:statistics.median(x["scores"][d] for x in rs) for d in DIMENSIONS}
        criteria=rs[0]["criteria"]
        if any(x["criteria"]!=criteria for x in rs): raise ValidationError("case criteria changed across judge packets")
        criterion_medians={criterion["criterion_id"]:statistics.median(next(item["score"] for item in row["task_specific"] if item["criterion_id"]==criterion["criterion_id"]) for row in rs) for criterion in criteria}
        total_weight=sum(criterion["weight"] for criterion in criteria)
        if total_weight<=0: raise ValidationError("case criterion weights must sum above zero")
        task_score=sum(criterion_medians[criterion["criterion_id"]]*criterion["weight"] for criterion in criteria)/total_weight
        case_rows.append({"split":split,"skill_id":skill,"skill_revision":revision,"case_id":cid,"family_id":cid[:3],"language":rs[0]["language"],"length_unit":rs[0]["length_unit"],"no_op":rs[0]["no_op"],"leaf_medians":med,"task_specific_medians":criterion_medians,"task_specific_weighted":task_score,"uncapped_weighted_score":weighted(med,task_score),"eligible_preference":not any(x["critical_gate"] or x["judge_critical"] for x in rs),"judge_hard_rate":sum(x["judge_hard"] for x in rs)/3,"first_place_share":sum(x["first_share"] for x in rs)})
    identities=defaultdict(list)
    for x in case_rows: identities[(x["split"],x["skill_id"],x["skill_revision"])].append(x)
    summary={}
    for (split,skill,revision),rs in sorted(identities.items()):
        def slices(field): return {value:round(mean([x["uncapped_weighted_score"] for x in rs if x[field]==value]),4) for value in sorted({x[field] for x in rs},key=str)}
        summary[f"{split}:{skill}@{revision}"]={"split":split,"skill_id":skill,"skill_revision":revision,"cases":len(rs),"uncapped_weighted_mean":round(mean([x["uncapped_weighted_score"] for x in rs]),4),"eligible_cases":sum(x["eligible_preference"] for x in rs),"critical_gate_rate":round(sum(not x["eligible_preference"] for x in rs)/len(rs),4),"unified_hard_rate":round(sum((not x["eligible_preference"]) or x["judge_hard_rate"]>0 for x in rs)/len(rs),4),"judge_hard_rate":round(mean([x["judge_hard_rate"] for x in rs]),4),"first_place_share":round(sum(x["first_place_share"] for x in rs)/(3*len(rs)),4),"family_means":slices("family_id"),"language_means":slices("language"),"length_unit_means":slices("length_unit"),"no_op_means":slices("no_op")}
    comparisons=[]
    humans=[x for x in identities if x[1]=="human-writing"]; others=[x for x in identities if x[1]!="human-writing"]
    for h in sorted(humans):
        for c in sorted(others):
            if h[0]!=c[0]: continue
            hi={x["case_id"]:x for x in identities[h]}; ci={x["case_id"]:x for x in identities[c]}; strata=defaultdict(list); all_strata=defaultdict(list); w=t=l=bad=0
            for cid in sorted(set(hi)&set(ci)):
                a,b=hi[cid],ci[cid]; d=a["uncapped_weighted_score"]-b["uncapped_weighted_score"]
                all_strata[a["family_id"]].append(d)
                if not a["eligible_preference"] or not b["eligible_preference"]: bad+=1; continue
                strata[a["family_id"]].append(d); w+=d>1e-12; l+=d< -1e-12; t+=abs(d)<=1e-12
            item={"split":h[0],"candidate":f"{h[1]}@{h[2]}","comparator":f"{c[1]}@{c[2]}","paired_cases":len(set(hi)&set(ci)),"eligible_paired_cases":sum(map(len,strata.values())),"ineligible_pairs":bad,"win_tie_loss":{"win":w,"tie":t,"loss":l}}
            item["all_case_uncapped_mean_difference"]=round(mean([mean(values) for values in all_strata.values()]),4)
            if mode=="holdout_headline":
                if set(strata)!={f"F{i:02d}" for i in range(1,13)}: raise ValidationError("headline lost an entire eligible family")
                item["eligible_mean_difference"]=round(mean([mean(x) for x in strata.values()]),4); item["family_stratified_bootstrap_95_ci"]=stratified_bootstrap(strata,bootstrap_samples,int(sha256_value([h,c])[:8],16))[0]
                fam=[]; ps=[]
                for family,x in sorted(strata.items()):
                    ci95,p=stratified_bootstrap({family:x},bootstrap_samples,int(sha256_value([h,c,family])[:8],16)); fam.append({"family_id":family,"mean_difference":round(mean(x),4),"bootstrap_95_ci":ci95,"p_value":round(p,4)}); ps.append((family,p))
                adjusted=holm(ps)
                for x in fam:x["holm_adjusted_p"]=adjusted[x["family_id"]]
                item["families"]=fam
                h_key=f"{h[0]}:{h[1]}@{h[2]}"; c_key=f"{c[0]}:{c[1]}@{c[2]}"; h_hard=summary[h_key]["unified_hard_rate"]; c_hard=summary[c_key]["unified_hard_rate"]
                family_blocker=any(result["mean_difference"]<-.15 for result in fam)
                item["hard_issue_rate_difference"]=round(h_hard-c_hard,4)
                candidate_critical=summary[h_key]["critical_gate_rate"]>0
                item["parity_decision"]=(item["paired_cases"]==240 and item["eligible_paired_cases"]==240 and not candidate_critical and item["all_case_uncapped_mean_difference"]>=-.10 and item["family_stratified_bootstrap_95_ci"][0]>-.15 and h_hard-c_hard<=.01 and not family_blocker)
                item["candidate_critical_failure_blocker"]=candidate_critical
                item["family_regression_blocker"]=family_blocker
            comparisons.append(item)
    position={"required":mode=="holdout_headline","audited_cases":0,"position_inconsistent_cases":[]}
    if swap_bundles:
        if len(swap_bundles)!=len(swap_gate_reports or []): raise ValidationError("swap gate reports mismatch")
        swapped=set(); swap_leaders={}; base_leaders={}
        for b in bundles: base_leaders.update(preference_leaders(b))
        for b,g in zip(swap_bundles,swap_gate_reports or []): swapped|={x["case_id"] for x in collect(b,g,root,"swapped")}
        for b in swap_bundles: swap_leaders.update(preference_leaders(b))
        if not swapped<=cases: raise ValidationError("swap audit outside base cases")
        for split in splits:
            for family in {c[:3] for c in cases}:
                n=sum(c.startswith(family+"-") for c in cases); a=sum(c.startswith(family+"-") for c in swapped)
                if a<math.ceil(n*.2): raise ValidationError(f"swap audit below 20% for {split}/{family}")
        position["audited_cases"]=len(swapped)
        position["position_inconsistent_cases"]=sorted(cid for cid in swapped if base_leaders.get(cid)!=swap_leaders.get(cid))
    elif mode=="holdout_headline": raise ValidationError("headline requires swapped-order audit")
    todos=[]
    if mode=="holdout_headline": todos.append("TODO: independently verify each reviewer_records.review_sha256 against the external blinded human-review artifact before publication; scaffold validation currently verifies shape, coverage, and digest syntax only.")
    result={"schema_version":"aggregate/v2","mode":mode,"headline_eligible":mode=="holdout_headline","experiment_id":experiment,"batches":len(bundles),"cases":len(cases),"case_skill_rows":len(case_rows),"score_weights":WEIGHTS,"judge_aggregation":"median","summary":summary,"comparisons":comparisons,"position_audit":position,"publication_todos":todos}; result["aggregate_sha256"]=sha256_value(result); return result
def main():
    p=argparse.ArgumentParser(); p.add_argument("--root",type=Path,default=ROOT); p.add_argument("--bundle",type=Path,action="append",required=True); p.add_argument("--gate-report",type=Path,action="append",required=True); p.add_argument("--swap-bundle",type=Path,action="append"); p.add_argument("--swap-gate-report",type=Path,action="append"); p.add_argument("--mode",choices=["development_partial","holdout_headline"],default="development_partial"); p.add_argument("--bootstrap-samples",type=int,default=10000); p.add_argument("--holdout-state",type=Path); p.add_argument("--human-calibration",type=Path); p.add_argument("--output",type=Path,required=True); a=p.parse_args()
    state=read_json(a.holdout_state) if a.holdout_state else None; calibration=read_json(a.human_calibration) if a.human_calibration else None
    r=aggregate_bundles([load_bundle(x) for x in a.bundle],[read_json(x) for x in a.gate_report],a.root,a.mode,a.bootstrap_samples,[load_bundle(x) for x in (a.swap_bundle or [])],[read_json(x) for x in (a.swap_gate_report or [])],state,calibration); write_json(a.output,r); print(json.dumps({"mode":r["mode"],"cases":r["cases"],"headline_eligible":r["headline_eligible"]},indent=2))
if __name__=="__main__": main()
