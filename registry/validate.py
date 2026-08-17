#!/usr/bin/env python3
"""Validate AI Engineering Lab Registry route, ownership and experiment closure."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


class RegistryError(ValueError):
    pass


MANDATORY_PILOT_GATES = {
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
}

REQUIRED_PILOT_OUTPUTS = {
    "05-keyframe-image-production": {"approved_keyframe_sha256s", "image_probe_records", "image_review_evidence"},
    "06-image-to-video-production": {"rendered_video_sha256s", "clip_probe_records", "motion_continuity_review"},
    "07-voice-music-and-effects-production": {"audio_sha256s", "loudness_and_peak_probe"},
    "08-subtitles-and-edit-timeline": {"subtitle_srt", "forced_alignment_json", "edit_timeline", "timeline_sync_review"},
    "09-master-render-and-playback": {"master_mp4", "master_sha256", "ffprobe_record", "full_playback_record"},
    "10-publication-feedback-and-accounting": {"publication_receipt", "target_readback_record", "actual_cost_ledger"},
}


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise RegistryError(f"{path}: file does not exist")
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RegistryError(f"{path}: expected a YAML object")
    return value


def unique_rows(rows: list[dict[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        identity = row.get("id")
        if not isinstance(identity, str) or not identity or identity in result:
            raise RegistryError(f"{label}: ids must be present and unique")
        result[identity] = row
    return result


def validate_story_studio_pilot(root: Path, route_ids: set[str], projects: dict[str, Any]) -> dict[str, Any]:
    plan_path = root / "experiments" / "story-studio-60s-pilot" / "task-plan.yaml"
    if not plan_path.is_file():
        raise RegistryError(f"{plan_path}: story studio pilot task-plan.yaml is required")

    plan = load_yaml(plan_path)
    route = plan.get("route")
    if route not in route_ids or route != "media-production-system":
        raise RegistryError("story studio pilot: route must match media-production-system")

    owner = plan.get("product_owner")
    if owner not in projects or owner != "story-studio":
        raise RegistryError("story studio pilot: product_owner must match story-studio")

    if plan.get("status") != "not_verified":
        raise RegistryError("story studio pilot: status must remain not_verified")

    if plan.get("claimed_execution") is not False:
        raise RegistryError("story studio pilot: claimed_execution must remain false")

    roles = plan.get("roles")
    if not isinstance(roles, dict) or not roles:
        raise RegistryError("story studio pilot: accountable roles are required")
    if not plan.get("not_verified"):
        raise RegistryError("story studio pilot: explicit not_verified list is required")

    stages = plan.get("stages", [])
    if not isinstance(stages, list) or len(stages) < 5:
        raise RegistryError("story studio pilot: stages must be a non-empty list")

    declared_gates: set[str] = set()
    for stage in stages:
        stage_id = stage.get("id", "unknown")
        if stage.get("owner") not in roles:
            raise RegistryError(f"story studio pilot stage {stage_id}: missing owner")
        if stage.get("review_owner") not in roles:
            raise RegistryError(f"story studio pilot stage {stage_id}: missing review_owner")
        if stage.get("review_owner") == stage.get("owner"):
            raise RegistryError(f"story studio pilot stage {stage_id}: self-approval is forbidden")
        if not stage.get("inputs"):
            raise RegistryError(f"story studio pilot stage {stage_id}: missing inputs")
        if not stage.get("outputs"):
            raise RegistryError(f"story studio pilot stage {stage_id}: missing outputs")
        gates = stage.get("gates")
        if not gates or not isinstance(gates, list):
            raise RegistryError(f"story studio pilot stage {stage_id}: missing gates (fails closed)")
        declared_gates.update(gates)
        stop_conditions = stage.get("stop_conditions")
        if not stop_conditions or not isinstance(stop_conditions, list):
            raise RegistryError(f"story studio pilot stage {stage_id}: missing stop conditions")
        if stage.get("verified") is not False:
            raise RegistryError(f"story studio pilot stage {stage_id}: verified must be false")
        missing_outputs = REQUIRED_PILOT_OUTPUTS.get(stage_id, set()) - set(stage.get("outputs", []))
        if missing_outputs:
            raise RegistryError(f"story studio pilot stage {stage_id}: missing verifiable outputs {sorted(missing_outputs)}")

    missing = MANDATORY_PILOT_GATES - declared_gates
    if missing:
        raise RegistryError(f"story studio pilot: missing mandatory gates {sorted(missing)} (fails closed)")

    gates_summary = set(plan.get("gates_summary", []))
    if declared_gates != gates_summary:
        raise RegistryError("story studio pilot: gates_summary mismatch with stage gates")

    return {
        "contract_validated": True,
        "stage_count": len(stages),
        "gate_count": len(declared_gates),
        "role_count": len(roles),
    }


def validate(root: Path) -> dict[str, Any]:
    registry = root / "registry"
    workflow_root = root / "workflows" / "ai-engineering-system"
    routes_doc = load_yaml(registry / "routes.yaml")
    projects_doc = load_yaml(registry / "projects.yaml")
    domains_doc = load_yaml(registry / "domains.yaml")
    assets_doc = load_yaml(registry / "assets.yaml")
    relationships_doc = load_yaml(registry / "relationships.yaml")
    workflow_doc = load_yaml(workflow_root / "workflow.yaml")
    evals_doc = load_yaml(workflow_root / "evals" / "routing.yaml")
    ownership_doc = load_yaml(workflow_root / "ownership.yaml")

    if routes_doc.get("schema_version") != "2.0":
        raise RegistryError("routes: expected schema_version 2.0")
    routes = unique_rows(routes_doc.get("routes", []), "routes")
    projects = unique_rows(projects_doc.get("projects", []), "projects")
    domains = unique_rows(domains_doc.get("domains", []), "domains")
    assets = unique_rows(assets_doc.get("assets", []), "assets")
    route_ids = set(routes)

    allowed = set(routes_doc.get("execution_rules", {}).get("task_route", {}).get("allowed", []))
    if allowed != route_ids:
        raise RegistryError("routes: task_route.allowed must equal registered route ids")

    for project_id, project in projects.items():
        route = project.get("route")
        if route:
            if route.get("primary") not in route_ids:
                raise RegistryError(f"{project_id}: unknown primary route")
            unknown = set(route.get("secondary", [])) - route_ids
            if unknown:
                raise RegistryError(f"{project_id}: unknown secondary routes {sorted(unknown)}")
        unknown_domains = set(project.get("domains", [])) - set(domains)
        if unknown_domains:
            raise RegistryError(f"{project_id}: unknown domains {sorted(unknown_domains)}")

    relationships = relationships_doc.get("relationships", [])
    if not isinstance(relationships, list):
        raise RegistryError("relationships: expected an array")
    for relationship in relationships:
        target = relationship.get("to", {})
        if target.get("type") == "route" and target.get("id") not in route_ids:
            raise RegistryError(f"relationships: unknown route {target.get('id')}")
        if target.get("type") == "asset" and target.get("id") not in assets:
            raise RegistryError(f"relationships: unknown asset {target.get('id')}")

    for route_id, route in routes.items():
        owner = route.get("product", {}).get("id")
        if owner not in projects:
            raise RegistryError(f"{route_id}: unknown product owner {owner}")
        if projects[owner].get("route", {}).get("primary") != route_id:
            raise RegistryError(f"{route_id}: owner primary route mismatch")
        implements = any(
            row.get("from") == {"type": "product", "id": owner}
            and row.get("to") == {"type": "route", "id": route_id}
            and row.get("relation") == "implements"
            for row in relationships
        )
        if not implements:
            raise RegistryError(f"{route_id}: missing product implements relationship")

    workflow_routes = set(workflow_doc.get("task_routing", {}).get("routes", {}))
    if workflow_routes != route_ids:
        raise RegistryError("workflow: task routes drift from Registry")
    product_systems = ownership_doc.get("product_systems", {})
    expected_owners = {route["product"]["id"] for route in routes.values()}
    if set(product_systems) != expected_owners:
        raise RegistryError("ownership: product systems drift from route owners")
    for owner, row in product_systems.items():
        if row.get("route") != projects[owner].get("route", {}).get("primary"):
            raise RegistryError(f"ownership: {owner} route mismatch")

    for case in evals_doc.get("cases", []):
        expected = case.get("expected", {})
        task_route = expected.get("task_route")
        if task_route and task_route not in route_ids:
            raise RegistryError(f"eval {case.get('id')}: unknown task route")
        split_tasks = expected.get("split_tasks")
        if split_tasks:
            if len(split_tasks) != len(set(split_tasks)) or not set(split_tasks) <= route_ids:
                raise RegistryError(f"eval {case.get('id')}: invalid split task routes")
            if expected.get("mixed_route_task") is not False:
                raise RegistryError(f"eval {case.get('id')}: composition must fail closed")

    if evals_doc.get("workflow_version") != workflow_doc.get("workflow", {}).get("version"):
        raise RegistryError("workflow: eval version drift")

    content_outputs = set(routes["content-output-system"].get("outputs", []))
    media_outputs = set(routes["media-production-system"].get("outputs", []))
    narrative_media = {"video", "audio", "comic", "animation"}
    if content_outputs & narrative_media or not narrative_media <= media_outputs:
        raise RegistryError("Createway and Story Studio output boundary drift")

    pilot_result = validate_story_studio_pilot(root, route_ids, projects)

    return {
        "verified": True,
        "route_count": len(routes),
        "project_count": len(projects),
        "relationship_count": len(relationships),
        "routing_eval_count": len(evals_doc.get("cases", [])),
        "workflow_version": workflow_doc["workflow"]["version"],
        "pilot_experiment": pilot_result,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps(validate(args.root.resolve()), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
