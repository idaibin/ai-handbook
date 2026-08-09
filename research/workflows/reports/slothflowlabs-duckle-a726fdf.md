# slothflowlabs/duckle workflow assessment

- Fixed commit: `a726fdf9382e82a468a729dde9f120abb69a9ce9`
- Content identity: `a5e54b6b0d3fca0b7b32e8ed9aac74bbebc53d50`
- Evidence: `source_validated`
- Subtype/topic fit: `compiled_scheduled_data_pipeline_engine`; `fit`
- Topic rationale: Its central behavior is local-first orchestration of data pipeline nodes and scheduled runs, rather than a generic agent or CI workflow.
- Runtime execution: none

## Verified

- The scheduler supports Cron, Interval, and FileWatch triggers, persists definitions and status fields in workspace schedules.json, and run_now resolves workspace/context/environment/secrets before launching a fresh per-run engine cancellation scope.
- Cron and interval due runs are claimed by advancing next_run before spawning, avoiding repeated 15-second ticker launches of the same due occurrence; they acquire the shared semaphore whose size is declared by DUCKLE_MAX_CONCURRENT_RUNS (default 8).
- Stage retryAttempts and retryBackoffMs are parsed into retry_attempts and retry_backoff_ms; the executor consumes both in an attempt loop, stops on success or cancellation, and applies linear sleep between failures. Tests exercise three attempts and backoff.
- Iterate count is validated as positive and consumed by for i in 0..count with ITER_INDEX substitution and fail-fast behavior. Foreach concurrency is parsed with minimum one and consumed as sequential execution or bounded chunks; tests cover iteration, foreach outputs, and concurrent scratch isolation.
- Each run receives a unique temporary database name using an atomic counter, and for_new_run creates an isolated cancellation scope, reducing same-process concurrent-run interference.
- Incremental execution loads the last successful high-water mark and accumulates pending watermarks; the executor persists them only when the entire non-targeted run finishes with status ok, so failed, cancelled, and partial targeted runs do not advance incremental state.
- Run history records trigger, status, duration, rows, node count, error, and category with bounded retention; component-level NDJSON logging records phases, status, rows, duration, errors, SQL, and control events when configured. Metrics textfile publication uses temporary-file rename.
- Review support compiles and structurally compares plans, while CI builds and tests the workspace across platforms and includes frontend, Python contract, connector integration, and release jobs. The project is dual licensed under MIT and Apache-2.0.

## Inference

- Claim-before-spawn makes cron/interval scheduling resistant to duplicate ticker dispatch, but it is not a durable exactly-once execution guarantee across process crashes.
- Successful-run watermark commit provides useful incremental resume semantics, although it is pipeline progress rather than arbitrary instruction-level checkpoint/resume.
- Retrying a whole stage is safe only when that stage's sink or subpipeline is idempotent; control stages can replay externally visible effects.

## Not verified

- The FileWatch listener directly spawns run_now without acquiring the shared scheduler semaphore, so DUCKLE_MAX_CONCURRENT_RUNS is not consumed on every trigger path and no global concurrency guarantee is credited.
- Whole-stage retries can include RunJob, Iterate, Foreach, Parallelize, or side-effecting sinks; no universal idempotency key, deduplication protocol, or compensation mechanism was found.
- The Checkpoint node writes a Parquet sidecar and passes data downstream, but no automatic engine restart/resume consumption of that artifact was found; it is not treated as a workflow checkpoint.
- Watermark and some scheduler/history persistence writes are best-effort or plain file writes; atomic crash consistency and concurrent lost-update protection were not established.
- review.rs provides informational compile/diff review, but no approval decision, approver identity, or enforced approval state transition was found.
- No code or tests were executed, and current CI status, live connector behavior, deployment behavior, and branch protection were not checked.

## Limitations

- Read-only source review at the fixed commit; DuckDB execution, schedulers, file watchers, connectors, and failure recovery were not run.
- Connector-specific transactional guarantees and sink semantics were outside the selected key-file set.
- Scores reflect only controls whose declarations were traced to concrete consumption in the inspected source.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 5 |
| `state_and_resume` | 4 |
| `idempotency` | 3 |
| `side_effect_control` | 3 |
| `human_gate` | 1 |
| `observability` | 5 |
| `validation` | 5 |
| `reuse_value` | 5 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Files read

- `README.md`
- `LICENSE-MIT`
- `LICENSE-APACHE`
- `crates/scheduler/src/lib.rs`
- `crates/duckdb-engine/src/plan/mod.rs`
- `crates/duckdb-engine/src/plan/specs.rs`
- `crates/duckdb-engine/src/lib.rs`
- `crates/duckdb-engine/src/history.rs`
- `crates/duckdb-engine/src/run_log.rs`
- `crates/duckdb-engine/src/review.rs`
- `crates/duckdb-engine/tests/execution.rs`
- `.github/workflows/ci.yml`

## Evidence URLs

- https://github.com/slothflowlabs/duckle/tree/a726fdf9382e82a468a729dde9f120abb69a9ce9
- https://github.com/slothflowlabs/duckle/blob/a726fdf9382e82a468a729dde9f120abb69a9ce9/crates/scheduler/src/lib.rs
- https://github.com/slothflowlabs/duckle/blob/a726fdf9382e82a468a729dde9f120abb69a9ce9/crates/duckdb-engine/src/plan/specs.rs
- https://github.com/slothflowlabs/duckle/blob/a726fdf9382e82a468a729dde9f120abb69a9ce9/crates/duckdb-engine/src/lib.rs
- https://github.com/slothflowlabs/duckle/blob/a726fdf9382e82a468a729dde9f120abb69a9ce9/crates/duckdb-engine/src/history.rs
- https://github.com/slothflowlabs/duckle/blob/a726fdf9382e82a468a729dde9f120abb69a9ce9/crates/duckdb-engine/src/run_log.rs
- https://github.com/slothflowlabs/duckle/blob/a726fdf9382e82a468a729dde9f120abb69a9ce9/crates/duckdb-engine/tests/execution.rs
- https://github.com/slothflowlabs/duckle/blob/a726fdf9382e82a468a729dde9f120abb69a9ce9/.github/workflows/ci.yml
