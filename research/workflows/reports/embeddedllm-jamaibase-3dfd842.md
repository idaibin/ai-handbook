# EmbeddedLLM/JamAIBase workflow assessment

- Fixed commit: `3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03`
- Content identity: `git-tree:3a08a23dae6afea6d55ad9c44276aac04c5ad487`
- Evidence: `source_validated`
- Subtype/topic fit: `in-request dependency-DAG generative-table workflow executor`; `fit`
- Runtime execution: none

## Verified

- JamAIBase describes generative/action tables as a declarative spreadsheet-like mechanism for LLM workflow orchestration exposed through REST APIs.
- POST /v2/gen_tables/{table_type}/rows/add and /rows/regen authenticate project or organization membership, check generation/storage/egress quotas, open the table, and construct MultiRowGenExecutor.
- The add contract accepts a table ID, one to 100 row mappings, streaming control, and concurrent-generation control; regeneration supports run_all, run_before, run_selected, and run_after strategies and validates the selected-column requirement.
- The executor derives dependencies from prompt variables, source columns, and Python-column ordering, computes topological levels, and uses the maximum level width when planning safe column concurrency.
- Each generated cell is represented by a Task with pending, running, and done states; only tasks whose upstream columns are available are scheduled, and ready tasks run concurrently within the configured column limit.
- Multi-row execution batches row executors, streams per-cell SSE responses when requested, emits a terminal [DONE] marker, and otherwise returns a MultiRowCompletionResponse.
- Completed row data is persisted in batches with table.add_rows for new rows or table.update_rows for regeneration; streamed response bytes also create an egress billing event.
- Task failures are materialized into per-column state/error data and upstream-dependent tasks reject errored inputs, allowing other row/column work to complete.
- The sampled executor contains no workflow checkpoint, persisted resume token, human approval pause, or executor-level retry policy; regeneration is an explicit new API operation rather than continuation from a checkpoint.
- Source tests exercise dependency chains, all regeneration strategies, streaming and non-streaming response shapes, context-length failures, and concurrency planning; CI runs grouped SDK/API pytest suites against composed services on main/legacy branches and pull requests.

## Inference

- The subtype is supported by REST-triggered execution, dynamically constructed per-row task DAGs, dependency-aware readiness checks, in-request TaskGroup scheduling, and final row persistence.
- Sorted regeneration row IDs make regeneration order deterministic, but a repeated add request creates new row IDs and is not idempotent by contract.
- Because batch-write exceptions are logged and the in-memory batch is then cleared, callers may receive workflow completion even when a persistence batch failed; this weakens side-effect consistency and recoverability.
- The declarative column model is reusable for data-enrichment pipelines, but long-running durable orchestration is not established by the sampled executor.

## Not verified

- Not verified: persisted checkpoint/resume or crash recovery for an in-flight generative-table request.
- Not verified: idempotency keys, duplicate-request suppression, or exactly-once external model/S3/table side effects.
- Not verified: human approval, manual pause/resume, reviewer authorization, escalation, or timeout behavior.
- Not verified: automatic executor retry/backoff for failed cells or failed batch writes; lower-level model clients may have independent retries outside the sampled workflow files.
- Not verified: end-to-end execution, test results, deployment behavior, and current CI status at the fixed commit.
- Not verified: durable workflow-level metrics or traces beyond request-ID logs, SSE output, progress cache endpoint, and billing events.

## Limitations

- Read-only review of 11 selected files at the exact commit; no Python tests, API services, models, storage, or GitHub Actions were executed.
- Evidence level is capped at source_validated; scores use 1 (weak/not present in sampled evidence) through 5 (strong source evidence).
- The review focuses on generative-table orchestration; the sampled Celery configuration and periodic database task do not establish durable execution for this workflow.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 5 |
| `state_and_resume` | 2 |
| `idempotency` | 2 |
| `side_effect_control` | 2 |
| `human_gate` | 1 |
| `observability` | 3 |
| `validation` | 4 |
| `reuse_value` | 4 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Evidence URLs

- https://github.com/EmbeddedLLM/JamAIBase/blob/3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03/README.md#L14-L46
- https://github.com/EmbeddedLLM/JamAIBase/blob/3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03/services/api/src/owl/routers/gen_table.py#L527-L572
- https://github.com/EmbeddedLLM/JamAIBase/blob/3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03/services/api/src/owl/routers/gen_table.py#L771-L814
- https://github.com/EmbeddedLLM/JamAIBase/blob/3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03/services/api/src/owl/types/__init__.py#L512-L549
- https://github.com/EmbeddedLLM/JamAIBase/blob/3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03/services/api/src/owl/types/__init__.py#L573-L618
- https://github.com/EmbeddedLLM/JamAIBase/blob/3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03/services/api/src/owl/db/gen_executor.py#L188-L256
- https://github.com/EmbeddedLLM/JamAIBase/blob/3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03/services/api/src/owl/db/gen_executor.py#L259-L449
- https://github.com/EmbeddedLLM/JamAIBase/blob/3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03/services/api/src/owl/db/gen_executor.py#L523-L659
- https://github.com/EmbeddedLLM/JamAIBase/blob/3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03/services/api/src/owl/db/gen_executor.py#L1339-L1414
- https://github.com/EmbeddedLLM/JamAIBase/blob/3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03/.github/workflows/ci.yml#L1-L57
- https://github.com/EmbeddedLLM/JamAIBase/blob/3dfd842d2b1d9721ec86ecd22e7d7b1f91c6bf03/.github/workflows/ci.yml#L213-L236
