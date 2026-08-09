# juanjuandog/FinSight-AI workflow assessment

- Fixed commit: `d31cec0b0dd40451aa5d35a357545094dc963a13`
- Content identity: `git-tree:9b8d8704b87241058166539dcc71353287bd9122`
- Evidence: `source_validated`
- Subtype/topic fit: `leased_idempotent_async_research_pipeline`; `strong_fit`
- Runtime execution: none

## Verified

- The workflow is a staged research pipeline: data ingestion, metric recalculation, document indexing, company-intelligence building, and stock AI analysis, with lifecycle states including created, running, retrying, succeeded, failed, and dead-letter.
- Workflow tasks persist an idempotency key, lifecycle status, agent stage, attempt count, payload, error, lease owner, fencing token, and timestamps.
- Execution is triggered through published workflow tasks; the inspected API exposes task listing, summaries, detail, and an explicit retry endpoint for failed or dead-letter tasks.
- The orchestrator returns immediately for already-succeeded tasks, acquires a five-minute lease by idempotency key, records lease-wait when acquisition fails, and renews the lease on a heartbeat.
- Redis lease acquisition, renewal, and release are owner/token-checked Lua operations. Acquisition increments a monotonic fencing counter; production can disable local fallback and fail closed when Redis is unavailable.
- Task transitions use compare-and-set on expected status and fencing token, preventing a stale worker from overwriting a recovered or newly owned task.
- Next-stage tasks are created or reused with a deterministic key composed from task type, company symbol, and root task ID; only created or retrying tasks are published.
- Failures become FAILED until the third attempt and then DEAD_LETTER. A scheduled recovery scan claims timed-out RUNNING tasks with CAS and republishes retryable tasks.
- The workflow API's manual retry is also CAS-protected and returns conflict if the task changed concurrently.
- Micrometer counters and timers capture execution result, duration, lease renewal status, and recovery counts; the summary endpoint reports status and stage populations.
- The sampled repository tests prove in-memory CAS behavior for stale workers and wrong fencing tokens, and the CI workflow runs Maven tests plus script syntax checks on pull requests and master pushes.

## Inference

- This is an at-least-once asynchronous pipeline whose duplicate-execution risk is reduced by repository uniqueness, leases, fencing tokens, and deterministic downstream task keys.
- Because each expensive stage performs its domain operation before the success CAS, a lease loss or crash can still cause repeated stage-level side effects unless each domain service is itself idempotent.
- The workflow is optimized for automated recovery rather than deliberative human approval; its human control is operational retry, not a mandatory content sign-off gate.

## Not verified

- No services, RabbitMQ consumer, Redis scripts, PostgreSQL schema, scheduler, or test suite were executed.
- The initial business API that creates and publishes the root ingestion task was not fully traced within the file budget.
- Idempotency of ingestion, indexing, metric calculation, intelligence building, AI analysis, and report writes is not verified.
- RabbitMQ acknowledgement, backoff, dead-letter exchange configuration, and publish-confirm semantics are not verified.
- No mandatory human approval or report sign-off transition was found in the inspected workflow files.
- Repository branch protection and current CI health are not verified.

## Limitations

- Source-only review at the fixed commit; evidence level cannot exceed source_validated.
- Eleven key files were read; publisher/listener configuration, database migration details, and domain-stage implementations were outside the sample.
- Documentation describes intended production behavior; only the cited implementation paths were treated as verified behavior.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 4 |
| `state_and_resume` | 5 |
| `idempotency` | 5 |
| `side_effect_control` | 4 |
| `human_gate` | 1 |
| `observability` | 4 |
| `validation` | 4 |
| `reuse_value` | 5 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Evidence URLs

- https://github.com/juanjuandog/FinSight-AI/blob/d31cec0b0dd40451aa5d35a357545094dc963a13/docs/design-agent-workflow.md
- https://github.com/juanjuandog/FinSight-AI/blob/d31cec0b0dd40451aa5d35a357545094dc963a13/backend/src/main/java/com/finsight/workflow/WorkflowOrchestrator.java
- https://github.com/juanjuandog/FinSight-AI/blob/d31cec0b0dd40451aa5d35a357545094dc963a13/backend/src/main/java/com/finsight/workflow/RedisBackedWorkflowLeaseService.java
- https://github.com/juanjuandog/FinSight-AI/blob/d31cec0b0dd40451aa5d35a357545094dc963a13/backend/src/main/java/com/finsight/workflow/WorkflowRecoveryScheduler.java
- https://github.com/juanjuandog/FinSight-AI/blob/d31cec0b0dd40451aa5d35a357545094dc963a13/backend/src/main/java/com/finsight/infrastructure/jdbc/JdbcWorkflowTaskRepository.java
- https://github.com/juanjuandog/FinSight-AI/blob/d31cec0b0dd40451aa5d35a357545094dc963a13/.github/workflows/ci.yml
