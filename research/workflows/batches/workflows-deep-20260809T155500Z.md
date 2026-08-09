# Workflows deep analysis — workflows-deep-20260809T155500Z

Snapshot: `workflows-coding-agent-pipeline-20260809T155200Z` (`ready`, source commit `71b34a3139645743461d79334b4af2735c8ad995`). Claim `workflows-claim-20260809T155500Z` was committed and re-read before repository access. This batch reviewed all five pending identities at their snapshot commits.

## Result

- Repositories reviewed: 5
- Unique contents reviewed: 5
- Analyses reused: 0
- New repository reports: 5
- Evidence: 5 `source_validated`
- Runtime boundary: no package install, build, test, model call, production pipeline, host tool or external side effect was executed

| Repository | Subtype | Evidence | Topic decision | Central limitation |
| --- | --- | --- | --- | --- |
| calesthio/OpenMontage | instruction_driven_checkpointed_media_production_pipeline | source | strong fit | Runtime behavior, test results, external provider calls, rendering quality, and end-to-end recovery were not executed. |
| alibaba/open-code-review | deterministic_concurrent_code_review_pipeline_with_resumable_file_checkpoints | source | strong fit | Runtime behavior, tests, live model calls, GitHub comment delivery, artifact upload, and telemetry export were not executed. |
| rocketride-org/rocketride-server | bounded_parallel_wave_planning_agent | source | fit | _TOOL_TIMEOUT_S=120 is declared and documented, but no consumption or timeout enforcement was found; the advertised tool timeout therefore receives no credit. |
| slothflowlabs/duckle | compiled_scheduled_data_pipeline_engine | source | fit | The FileWatch listener directly spawns run_now without acquiring the shared scheduler semaphore, so DUCKLE_MAX_CONCURRENT_RUNS is not consumed on every trigger path and no global concurrency guarantee is credited. |
| open-mercato/open-mercato | skill-defined spec-to-code implementation workflow | source | fit | Not verified: which agent runtimes parse the skill description and how natural-language trigger phrases are matched or prioritized. |

## Cross-repository findings

1. OpenMontage and Open Code Review expose the strongest checkpoint/resume contracts in this batch, but their external generation and publication effects still require action-specific safeguards.
2. Declaration-to-consumption tracing prevented unimplemented retry, iteration and parallelism language from receiving behavioral credit.
3. RocketRide's planning loop records tool observations and supports bounded parallel waves, but host-tool effects are not made idempotent by the agent loop.
4. Duckle provides strong compiled DAG validation, scheduling and observability; its human-approval contract is weak compared with explicit workflow waitpoints.
5. Open Mercato's installed spec-to-code skill gives a reusable phase protocol, while divergent monorepo/create-app copies make approval semantics context-dependent.

## Reusable patterns

- Stable session or manifest checkpoints with deterministic resume.
- Bounded concurrency whose scheduler actually consumes the configured limit.
- Pre-effect approval and cost gates for paid or irreversible operations.
- Compilation/lint validation that can run without credentials or side effects.
- Semantic drift checks for duplicated workflow definitions across packaging contexts.

## Evidence boundary

All conclusions are static at fixed commits. Checked-in tests were read where relevant but not executed. No report claims runtime validation.

Next queue candidate: none in this ready snapshot. Discovery continues at `agent-workflow:second-partition`.
