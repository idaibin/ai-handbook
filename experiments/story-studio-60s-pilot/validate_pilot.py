#!/usr/bin/env python3
"""Standalone validator for Story Studio 60-Second Pilot Experiment Task Plan."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


class PilotValidationError(ValueError):
    pass


MANDATORY_GATES = [
    "gate:story-positioning-complete",
    "gate:source-and-rights-resolved",
    "gate:world-character-bible-locked",
    "gate:script-timed-and-approved",
    "gate:storyboard-approved",
    "gate:keyframe-consistency-verified",
    "gate:motion-video-continuity-verified",
    "gate:audio-sync-and-voice-approved",
    "gate:subtitles-and-edit-timeline-closed",
    "gate:master-render-inspected",
    "gate:publication-readback-and-cost-quality-logged",
]

REQUIRED_ARTIFACT_OUTPUTS = {
    "05-keyframe-image-production": {"approved_keyframe_pngs", "approved_keyframe_sha256s", "image_probe_records", "image_review_evidence"},
    "06-image-to-video-production": {"rendered_video_clips", "rendered_video_sha256s", "clip_probe_records", "motion_continuity_review"},
    "07-voice-music-and-effects-production": {"audio_sha256s", "loudness_and_peak_probe", "pronunciation_and_mix_review"},
    "08-subtitles-and-edit-timeline": {"subtitle_srt", "forced_alignment_json", "edit_timeline", "subtitle_text_review", "timeline_sync_review"},
    "09-master-render-and-playback": {"master_mp4", "master_sha256", "ffprobe_record", "full_playback_record", "quality_review_evidence"},
    "10-publication-feedback-and-accounting": {"publication_receipt", "target_readback_record", "actual_cost_ledger", "quality_score_record"},
}


def validate_task_plan(plan_path: Path) -> dict[str, Any]:
    if not plan_path.is_file():
        raise PilotValidationError(f"{plan_path}: file does not exist")

    data = yaml.safe_load(plan_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise PilotValidationError(f"{plan_path}: expected YAML object")

    if data.get("route") != "media-production-system":
        raise PilotValidationError("task plan: route must be media-production-system")

    if data.get("product_owner") != "story-studio":
        raise PilotValidationError("task plan: product_owner must be story-studio")

    if data.get("status") != "not_verified":
        raise PilotValidationError("task plan: status must be not_verified for experiment plan")

    if data.get("claimed_execution") is not False:
        raise PilotValidationError("task plan: claimed_execution must be false")

    roles = data.get("roles")
    if not isinstance(roles, dict) or not roles:
        raise PilotValidationError("task plan: accountable roles are required")
    if not data.get("not_verified"):
        raise PilotValidationError("task plan: explicit not_verified list is required")

    stages = data.get("stages", [])
    if not isinstance(stages, list) or len(stages) < 5:
        raise PilotValidationError("task plan: stages must be a non-empty list of at least 5 stages")

    declared_gates: set[str] = set()
    for stage in stages:
        stage_id = stage.get("id", "unknown")
        if stage.get("owner") not in roles:
            raise PilotValidationError(f"stage {stage_id}: missing owner")
        if stage.get("review_owner") not in roles:
            raise PilotValidationError(f"stage {stage_id}: missing review_owner")
        if stage.get("review_owner") == stage.get("owner"):
            raise PilotValidationError(f"stage {stage_id}: owner cannot approve its own artifact")
        if not stage.get("inputs"):
            raise PilotValidationError(f"stage {stage_id}: missing inputs")
        if not stage.get("outputs"):
            raise PilotValidationError(f"stage {stage_id}: missing outputs")
        gates = stage.get("gates")
        if not gates or not isinstance(gates, list):
            raise PilotValidationError(f"stage {stage_id}: missing mandatory gates (fails closed)")
        declared_gates.update(gates)
        stop_conditions = stage.get("stop_conditions")
        if not stop_conditions or not isinstance(stop_conditions, list):
            raise PilotValidationError(f"stage {stage_id}: missing stop conditions")
        if stage.get("verified") is not False:
            raise PilotValidationError(f"stage {stage_id}: verified field must be false")
        required_outputs = REQUIRED_ARTIFACT_OUTPUTS.get(stage_id, set())
        missing_outputs = required_outputs - set(stage.get("outputs", []))
        if missing_outputs:
            raise PilotValidationError(f"stage {stage_id}: missing verifiable outputs {sorted(missing_outputs)}")

    gates_summary = set(data.get("gates_summary", []))
    missing_mandatory = set(MANDATORY_GATES) - declared_gates
    if missing_mandatory:
        raise PilotValidationError(f"task plan: missing mandatory gates {sorted(missing_mandatory)} (fails closed)")

    if declared_gates != gates_summary:
        raise PilotValidationError("task plan: gates_summary does not match stage gates")

    return {
        "contract_validated": True,
        "plan_id": data.get("plan_id"),
        "route": data.get("route"),
        "product_owner": data.get("product_owner"),
        "stage_count": len(stages),
        "gate_count": len(declared_gates),
        "role_count": len(roles),
        "status": data.get("status"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--plan",
        type=Path,
        default=Path(__file__).resolve().parent / "task-plan.yaml",
    )
    args = parser.parse_args()
    print(json.dumps(validate_task_plan(args.plan), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
