#!/usr/bin/env python3
"""Validate complete per-family review bundles and one global wave decision."""
from __future__ import annotations
from typing import Any
from common import ValidationError, hash_without, load_schema, validate_schema

FAMILIES={f"F{i:02d}" for i in range(1,13)}
def validate_review(review:dict[str,Any],previous_revision:str)->None:
    validate_schema(review,load_schema("review"))
    if hash_without(review,"review_sha256")!=review["review_sha256"]: raise ValidationError("review hash mismatch")
    if review["skill_revision"]!=previous_revision: raise ValidationError("review revision does not match evaluated candidate")
    if review["batch_id"]!=review["wave_id"]: raise ValidationError("batch_id must equal wave_id")
    changed=review["decision"]=="accepted"
    if changed and (not review.get("next_revision") or review["next_revision"]==previous_revision or not review.get("proposed_change") or not review.get("counterexample")): raise ValidationError("accepted change requires new revision, proposal, and counterexample")
    if changed and (not review["failure_cases"] or not review["root_causes"] or max(x["recurrence"] for x in review["root_causes"])<2): raise ValidationError("accepted change requires recurring evidence-backed failure")
    if not changed and review.get("next_revision") not in {None,previous_revision}: raise ValidationError("non-accepted review cannot advance revision")

def validate_wave_reviews(reviews:list[dict[str,Any]],previous_revision:str,expected_case_ids:set[str])->dict[str,Any]:
    if len(reviews)!=13: raise ValidationError("wave requires 12 family slice reviews plus one global decision")
    for review in reviews: validate_review(review,previous_revision)
    if len({review["review_sha256"] for review in reviews})!=13: raise ValidationError("duplicate review evidence")
    waves={review["wave_id"] for review in reviews}
    if len(waves)!=1: raise ValidationError("review bundle mixes waves")
    family=[review for review in reviews if review["scope"]=="family_slice"]
    global_reviews=[review for review in reviews if review["scope"]=="global_wave"]
    if len(global_reviews)!=1 or len(family)!=12: raise ValidationError("wave must contain exactly one global and twelve family reviews")
    if {review["family_id"] for review in family}!=FAMILIES: raise ValidationError("family reviews must cover F01-F12 exactly once")
    union=set()
    for review in family:
        cases=set(review["reviewed_case_ids"])
        if len(cases)!=10 or any(not case.startswith(review["family_id"]+"-") for case in cases): raise ValidationError("each family review must cover exactly ten matching cases")
        if union&cases: raise ValidationError("case appears in multiple family reviews")
        union|=cases
        if review["decision"] in {"accepted","reverted"}: raise ValidationError("behavior change decision belongs only to global review")
    global_review=global_reviews[0]
    if global_review["family_id"] is not None or set(global_review["reviewed_case_ids"])!=union: raise ValidationError("global review must cover the exact 120-case family union")
    if union!=expected_case_ids or len(union)!=120: raise ValidationError("review bundle does not cover the expected 120-case wave")
    if sum(review["decision"]=="accepted" for review in reviews)>1: raise ValidationError("at most one accepted behavior change is allowed per wave")
    return {"wave_id":waves.pop(),"family_reviews":12,"reviewed_cases":120,"global_decision":global_review["decision"]}
