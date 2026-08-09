# Workflows deep analysis — workflows-deep-20260809T154000Z

Snapshot: `workflows-ai-evaluation-workflow-20260809T063604Z` (`ready`, source commit `14be7b4481ae708ea35ec908fdf18bfac6f2b22c`). Claim `workflows-claim-20260809T154000Z` was committed at `84a982197a7fdfa105a637a53b8ab060d1874840` and re-read before source analysis.

## Result

- Repositories reviewed: 10
- Unique contents reviewed: 10
- Analyses reused: 0
- New repository reports: 10
- Evidence: 10 `source_validated`; 0 `runtime_validated`
- Runtime boundary: no install, build, test, model request, database, scheduler, browser, SCM mutation or external side effect was executed

| Repository | Subtype | Evidence | Topic decision | Central unverified item |
| --- | --- | --- | --- | --- |
| langgenius/dify | persisted_event_queue_dag_with_hitl_pause | source_validated | strong_fit | Not verified: an end-to-end paused workflow was not resumed against a live database/queue, so exact resume token/session semantics and crash boundaries are not runtime-confirmed. |
| moazbuilds/CodeMachine-CLI | resumable_interactive_multi_agent_cli_state_machine | source_validated | fit | Not verified: generic task-level retry counts, exponential backoff, or per-side-effect idempotency keys; crash continuation is verified in source, but replay safety is not. |
| skalesapp/skales | local_first_scheduled_autonomous_task_queue_with_hitl | source_validated | fit | Not verified: source implementation of the visual Workflow canvas/compiler, named workflow inputs, success criteria, or /goal-ship dispatch; these are documented in README but not established by the bounded execution sample. |
| rpamis/comet | checkpointed_guarded_skill_engine | source_validated | strong_fit | No runtime command, test suite, CI run, crash-injection scenario, or concurrent writer scenario was executed. |
| juanjuandog/FinSight-AI | leased_idempotent_async_research_pipeline | source_validated | strong_fit | No services, RabbitMQ consumer, Redis scripts, PostgreSQL schema, scheduler, or test suite were executed. |
| Ricky-7-Yan/intelligent-audit-system | bounded_governed_multi_role_audit_agent_loop | source_validated | strong_fit | No API, skill, database, test, CI, or crash/restart scenario was executed. |
| dataelement/bisheng | outbox-mediated durable human-approval state machine | source_validated | strong_fit | Not verified: atomic transaction boundaries across instance/task/outbox creation and asynchronous dispatch. |
| trpc-group/trpc-agent-go | checkpointed interruptible Pregel-style agent graph runtime | source_validated | strong_fit | Not verified: durability and transactional behavior of any concrete checkpoint backend under process crash or network partition. |
| EmbeddedLLM/JamAIBase | in-request dependency-DAG generative-table workflow executor | source_validated | fit | Not verified: persisted checkpoint/resume or crash recovery for an in-flight generative-table request. |
| ray-r-ren/agent-apprenticeship | iterative-agent-evaluation-pipeline | source_validated | fit | No CLI, package installation, task run, model call, external coding agent, resume path, release validator or export was executed. |

## Cross-repository findings

1. **Persisted state does not imply safe side effects.** Dify, tRPC Agent Go, Comet and Bisheng expose substantial state/checkpoint or interruption machinery, but action-specific idempotency and compensation remain separate responsibilities.
2. **Human gates are uneven.** Dify and Bisheng expose explicit pause/approval states; FinSight-AI and JamAIBase lack equivalent first-class gates in the inspected paths.
3. **Lease/idempotency designs are strongest when carried through the whole pipeline.** FinSight-AI combines leases and idempotent async research processing; several other candidates bound retries but do not establish exactly-once external effects.
4. **Declared controls can be inert.** Agent Apprenticeship accepts `max_iterations`, `max_parallel`, and `retry_limit`, yet fixed source implements at most one revision and does not consume the latter two beyond the signature.
5. **Workflow subtypes matter.** Durable graph runtimes, local scheduled queues, interactive coding state machines and in-request dependency DAGs should not receive equivalent recovery or side-effect expectations.

## Reusable patterns

- Persisted pause state and explicit resume token for human approval.
- Task lease plus idempotency key and terminal failure state.
- Outbox/dispatch separation from workflow state.
- Checkpointed graph state with typed interrupt/resume.
- Declaration-to-consumption audit for operational controls.

## Evidence boundary

All conclusions are fixed-source findings. Runtime behavior, provider credentials, process crashes, distributed contention, release pipelines and exactly-once external effects remain unverified.

The current ready snapshot is exhausted. Next discovery shard: `coding-agent-pipeline:first-partition`.
