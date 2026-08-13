#!/usr/bin/env python3
"""Canonical commitment over every artifact used by a completed holdout."""
from __future__ import annotations
from typing import Any
from common import ValidationError, sha256_value

def _artifact_rows(role:str,bundles:list[tuple[dict[str,Any],dict[str,dict[str,Any]],dict[str,dict[str,Any]]]],gates:list[dict[str,Any]]):
    if len(bundles)!=len(gates): raise ValidationError(f"{role} bundle/gate cardinality mismatch")
    rows=[]
    for (mapping,packets,judgments),gate in zip(bundles,gates):
        rows.append({"role":role,"batch_id":mapping["batch_id"],"mapping_sha256":sha256_value(mapping),
                     "packets":[{"judge_id":jid,"sha256":sha256_value(packets[jid])} for jid in sorted(packets)],
                     "judgments":[{"judge_id":jid,"sha256":sha256_value(judgments[jid])} for jid in sorted(judgments)],
                     "gate_report_sha256":sha256_value(gate)})
    return sorted(rows,key=lambda row:(row["batch_id"],row["mapping_sha256"]))

def complete_evidence_digest(base_bundles,base_gates,swap_bundles,swap_gates)->str:
    evidence={"schema_version":"complete-evidence/v1","base":_artifact_rows("base",base_bundles,base_gates),
              "swapped":_artifact_rows("swapped",swap_bundles,swap_gates)}
    if not evidence["base"] or not evidence["swapped"]: raise ValidationError("complete evidence requires base and swapped artifacts")
    return sha256_value(evidence)

def completion_evidence(candidate_revision:str,case_ids:set[str],base_bundles,base_gates,swap_bundles,swap_gates)->dict[str,str]:
    return {"complete_240_case_artifact_sha256":complete_evidence_digest(base_bundles,base_gates,swap_bundles,swap_gates),
            "case_ids_sha256":sha256_value(sorted(case_ids)),"candidate_revision":candidate_revision}
