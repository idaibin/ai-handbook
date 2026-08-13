#!/usr/bin/env python3
"""Fail-closed sealed-holdout unlock state machine."""

from __future__ import annotations

from typing import Any

from common import ValidationError, hash_without, sha256_value

STATES = {"sealed", "candidate_frozen", "unlocked", "completed", "invalidated"}
TRANSITIONS = {
    "sealed": {"candidate_frozen"},
    "candidate_frozen": {"unlocked"},
    "unlocked": {"completed", "invalidated"},
    "completed": {"invalidated"},
    "invalidated": set(),
}


def transition(state: dict[str, Any], target: str, evidence: dict[str, Any]) -> dict[str, Any]:
    allowed = {"schema_version", "experiment_id", "state", "candidate_revision", "candidate_tree", "corpus_commitment_sha256", "events", "state_sha256"}
    if set(state) != allowed or state["schema_version"] != "holdout-state/v1" or hash_without(state, "state_sha256") != state["state_sha256"]:
        raise ValidationError("holdout state contract/hash invalid")
    if state["state"] not in STATES or target not in TRANSITIONS[state["state"]]:
        raise ValidationError(f"invalid holdout transition {state['state']} -> {target}")
    if target == "candidate_frozen":
        required = {"candidate_revision", "candidate_tree", "development_complete_sha256"}
        if set(evidence) != required or not all(evidence.values()):
            raise ValidationError("candidate freeze evidence incomplete")
        state["candidate_revision"] = evidence["candidate_revision"]
        state["candidate_tree"] = evidence["candidate_tree"]
    elif target == "unlocked":
        if set(evidence) != {"commitment_sha256", "freeze_state_sha256"}:
            raise ValidationError("unlock evidence incomplete")
        if evidence["commitment_sha256"] != state["corpus_commitment_sha256"] or evidence["freeze_state_sha256"] != state["state_sha256"]:
            raise ValidationError("unlock evidence does not bind freeze and corpus")
    elif target == "completed":
        if set(evidence) != {"complete_240_case_artifact_sha256", "case_ids_sha256", "candidate_revision"} or not all(evidence.values()):
            raise ValidationError("holdout completion evidence incomplete")
        if evidence["candidate_revision"] != state["candidate_revision"]:
            raise ValidationError("holdout completion revision differs from frozen candidate")
    elif target == "invalidated":
        if set(evidence) != {"reason", "replacement_required"} or evidence["replacement_required"] is not True:
            raise ValidationError("holdout invalidation evidence incomplete")
    updated = dict(state)
    updated["events"] = state["events"] + [{"from": state["state"], "to": target, "evidence": evidence}]
    updated["state"] = target
    updated["state_sha256"] = sha256_value({key: value for key, value in updated.items() if key != "state_sha256"})
    return updated


def require_unlocked(state: dict[str, Any], candidate_revision: str) -> None:
    if hash_without(state, "state_sha256") != state.get("state_sha256"):
        raise ValidationError("holdout state hash invalid")
    if state.get("state") != "unlocked" or state.get("candidate_revision") != candidate_revision:
        raise ValidationError("holdout materialization requires unlocked state for the frozen candidate")
