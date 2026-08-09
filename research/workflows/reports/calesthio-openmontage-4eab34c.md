# calesthio/OpenMontage workflow assessment

- Fixed commit: `4eab34c5cfcccaa4f1970554928feccce73ee930`
- Content identity: `github:calesthio/OpenMontage@4eab34c5cfcccaa4f1970554928feccce73ee930`
- Evidence: `source_validated`
- Subtype/topic fit: `instruction_driven_checkpointed_media_production_pipeline`; `strong_fit`
- Topic rationale: A manifest-defined multi-stage production workflow has persisted state, executable approval gates, governed paid side effects, and CI-validated support code.
- Runtime execution: none

## Verified

- The documented entry contract accepts a natural-language brief and optional reference/local media; the agent must select a pipeline, load its YAML manifest, preflight required tools, then execute ordered stage skills and emit canonical artifacts/checkpoints.
- animated-explainer declares research→proposal→script→scene_plan→assets→edit→compose→publish, per-stage inputs/outputs, tool availability, checkpoint requirements, review criteria, and approval defaults; proposal, script, scene_plan, assets, and publish are human-gated.
- Approval is traced declaration→consumption: pipeline_loader reads human_approval_default; checkpoint.write_checkpoint resolves the manifest gate, rejects completed without human_approved, and prevents later stages from advancing past incomplete or unapproved predecessors.
- State/resume is implemented with schema-validated per-stage JSON checkpoints, deterministic manifest order, next-stage calculation, in-progress partial-progress guidance, atomic temp-file replacement, and history copies for superseded non-heartbeat checkpoints.
- Decision logging de-duplicates decision_id values into a cumulative project log; project initialization preserves created_at on rerun. These are local idempotency safeguards, not guarantees for external media-generation calls.
- CostTracker consumes budget mode, per-action threshold, first-paid-tool approval, reserve, warning/cap, reconcile, refund, and persisted cost-log state; the workflow guidance requires estimate/reserve/reconcile around paid operations.
- The reviewer instruction consumes stage review_focus/success_criteria and prescribes revision/re-review, but the inspected executable code does not enforce its round counter.
- CI checks Python validation and invokes make test; tests were not executed for this review. The repository is AGPL-3.0 licensed.

## Inference

- Resume after an ordinary interruption should avoid repeating completed stages and can skip completed sub-items when partial_progress is faithfully maintained by the instruction-following agent.
- The workflow is most reusable where an agent runtime reliably follows repository instructions; orchestration is intentionally not centralized in an executable engine.

## Not verified

- Runtime behavior, test results, external provider calls, rendering quality, and end-to-end recovery were not executed.
- Manifest fields max_revisions_per_stage, max_send_backs, and max_wall_time_minutes were observed as declarations but no executable consumer was verified in the inspected files; they do not support iteration/retry scoring.
- The reviewer document's two-round limit is instruction-level and not backed by a verified programmatic loop counter.
- Exactly-once or provider-level idempotency for paid image, video, TTS, music, compose, export, or publish operations was not verified.
- Concurrent writers, crash recovery during history archival, and rollback of partially completed external side effects were not verified.

## Limitations

- Source-only review of 10 selected files at the fixed commit; instruction-following behavior and CI claims were not dynamically validated.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 4 |
| `state_and_resume` | 5 |
| `idempotency` | 4 |
| `side_effect_control` | 4 |
| `human_gate` | 5 |
| `observability` | 4 |
| `validation` | 4 |
| `reuse_value` | 4 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Files read

- `README.md`
- `LICENSE`
- `AGENT_GUIDE.md`
- `pipeline_defs/animated-explainer.yaml`
- `lib/checkpoint.py`
- `lib/pipeline_loader.py`
- `tools/cost_tracker.py`
- `skills/meta/checkpoint-protocol.md`
- `skills/meta/reviewer.md`
- `.github/workflows/ci.yml`

## Evidence URLs

- https://github.com/calesthio/OpenMontage/blob/4eab34c5cfcccaa4f1970554928feccce73ee930/README.md
- https://github.com/calesthio/OpenMontage/blob/4eab34c5cfcccaa4f1970554928feccce73ee930/LICENSE
- https://github.com/calesthio/OpenMontage/blob/4eab34c5cfcccaa4f1970554928feccce73ee930/AGENT_GUIDE.md
- https://github.com/calesthio/OpenMontage/blob/4eab34c5cfcccaa4f1970554928feccce73ee930/pipeline_defs/animated-explainer.yaml
- https://github.com/calesthio/OpenMontage/blob/4eab34c5cfcccaa4f1970554928feccce73ee930/lib/checkpoint.py
- https://github.com/calesthio/OpenMontage/blob/4eab34c5cfcccaa4f1970554928feccce73ee930/lib/pipeline_loader.py
- https://github.com/calesthio/OpenMontage/blob/4eab34c5cfcccaa4f1970554928feccce73ee930/tools/cost_tracker.py
- https://github.com/calesthio/OpenMontage/blob/4eab34c5cfcccaa4f1970554928feccce73ee930/skills/meta/checkpoint-protocol.md
- https://github.com/calesthio/OpenMontage/blob/4eab34c5cfcccaa4f1970554928feccce73ee930/skills/meta/reviewer.md
- https://github.com/calesthio/OpenMontage/blob/4eab34c5cfcccaa4f1970554928feccce73ee930/.github/workflows/ci.yml
