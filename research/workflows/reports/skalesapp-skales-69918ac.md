# skalesapp/skales workflow assessment

- Fixed commit: `69918acb15977d04a357f0871df415b2ae903249`
- Content identity: `github:skalesapp/skales@69918acb15977d04a357f0871df415b2ae903249`
- Evidence: `source_validated`
- Subtype/topic fit: `local_first_scheduled_autonomous_task_queue_with_hitl`; `fit`
- Runtime execution: none

## Verified

- The historical v7 source implements multiple triggers: user-created autonomous tasks, stored five-field cron jobs, and an Electron shell. The README separately describes /goal and saved workflow trigger words, but the visual workflow compiler itself was not present in the sampled execution files.
- Agent tasks use a persisted state machine in ~/.skales-data/tasks.json with pending, in_progress, completed, failed, blocked, and cancelled states, plus priority, source, retry counters, model assignment, approval fields, and timestamps.
- Crash recovery resets stale in_progress tasks to pending on startup. Failed autonomous tasks are requeued until maxRetries (default three), then permanently blocked by the anti-loop protocol.
- Human approval is an executable gate, not only documentation: requiresApproval plus approvalStatus=pending excludes a task from getExecutablePendingTasks; approve changes the decision, while reject cancels it. A separate persistent pending-approval store supports Telegram approve/deny and expires stale records after 30 minutes.
- The task executor runs a bounded decide/execute tool loop, polls for a user stop, uses AbortController timeouts, writes incremental logs, and saves a progress checkpoint at 80% of the time budget, on timeout, or at the step limit. The resume mechanism is a user prompt that asks Skales to read the checkpoint, rather than transparent continuation of a serialized model session.
- Cron dispatch checks five fields and applies a last-run guard with a minimum 55-minute gap before creating a task. The in-memory dedup map is seeded from a persisted job.lastRun value when available, but the sampled code did not establish an atomic durable claim.
- Side effects are broad: the autonomous runner explicitly enables tool execution including web search, file writes, email and general execute calls; stand-up reports may be sent to Telegram. The approval model names consequential actions such as mass communication, but not every tool call is necessarily gated.
- Observability includes per-task logs, aggregate state counts, live incremental task updates, autopilot_logs.json logging, task/tool events, and Electron startup/status/error logs.
- The planner reads events and settings, invokes an LLM, and writes the resulting schedule JSON. No test scripts appear in the root package.json, and no test/CI definition was found in this bounded sample.

## Inference

- The source-backed subtype is a local-first scheduled autonomous task queue with optional HITL, while the README's reusable visual workflows are a higher-level playbook compiler onto the same goal concept.
- Retry capping and cron gap checks reduce loops and duplicate dispatch, but without an atomic persisted execution claim they do not establish exactly-once behavior across concurrent processes or crashes.
- The checkpoint design supports recoverable progress artifacts, not deterministic replay: resumption depends on a later agent reading a JSON checkpoint and reconstructing context.

## Not verified

- Not verified: source implementation of the visual Workflow canvas/compiler, named workflow inputs, success criteria, or /goal-ship dispatch; these are documented in README but not established by the bounded execution sample.
- Not verified: atomic cron claiming, cross-process locking, durable idempotency keys, or exactly-once delivery for email, Telegram, file, shell, browser, or deploy effects.
- Not verified: whether every consequential tool is mapped to requiresApproval; only task-level and Telegram approval stores were inspected.
- Not verified: automated tests or CI validation for the fixed commit.
- Not verified: behavior of the currently distributed Skales binary; the repository states this is an outdated historical v7 snapshot and not the maintained product source.

## Limitations

- Static review of 10 files at the fixed commit; no Electron app, task runner, cron tick, model/tool integration, or tests were run.
- The README explicitly says this source tree is an outdated historical v7 snapshot and is not what current binaries run, so findings apply only to the fixed commit.
- BSL 1.1 permits limited non-production/personal use and restricts commercial SaaS/competing products until the change date, materially limiting reuse.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 4 |
| `state_and_resume` | 4 |
| `idempotency` | 3 |
| `side_effect_control` | 3 |
| `human_gate` | 5 |
| `observability` | 4 |
| `validation` | 2 |
| `reuse_value` | 1 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Evidence URLs

- https://github.com/skalesapp/skales/blob/69918acb15977d04a357f0871df415b2ae903249/README.md
- https://github.com/skalesapp/skales/blob/69918acb15977d04a357f0871df415b2ae903249/LICENSE
- https://github.com/skalesapp/skales/blob/69918acb15977d04a357f0871df415b2ae903249/package.json
- https://github.com/skalesapp/skales/blob/69918acb15977d04a357f0871df415b2ae903249/apps/web/src/actions/autonomous.ts
- https://github.com/skalesapp/skales/blob/69918acb15977d04a357f0871df415b2ae903249/apps/web/src/actions/planner.ts
- https://github.com/skalesapp/skales/blob/69918acb15977d04a357f0871df415b2ae903249/apps/web/src/actions/tasks.ts
- https://github.com/skalesapp/skales/blob/69918acb15977d04a357f0871df415b2ae903249/apps/web/src/lib/autonomous-runner.ts
- https://github.com/skalesapp/skales/blob/69918acb15977d04a357f0871df415b2ae903249/apps/web/src/lib/approval-store.ts
- https://github.com/skalesapp/skales/blob/69918acb15977d04a357f0871df415b2ae903249/apps/web/src/lib/agent-tasks.ts
- https://github.com/skalesapp/skales/blob/69918acb15977d04a357f0871df415b2ae903249/electron/main.js
