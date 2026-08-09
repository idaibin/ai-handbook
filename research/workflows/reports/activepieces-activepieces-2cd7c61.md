# activepieces/activepieces workflow assessment

- Fixed commit: `2cd7c61f302f88b5c24811ca480c0fceee602af5`
- Tree/content: `git-tree:640717fb80c71fad55c7db6ea463f533789b5587`
- Observed: 23,644 Stars; `main`; not forked or archived
- License: MIT for community code; separate enterprise terms under `packages/ee/` and `packages/server/api/src/app/ee/`
- Evidence: `source_validated`; runtime not executed in this batch
- Subtype/topic fit: `durable-workflow-engine`; strong fit

## Verified

`FlowVersion` stores a trigger and linked actions, including code, pieces, loops and routers. Flow runs move through queued, running, paused, success, failure, timeout and cancellation states. The executor persists step output, supports delay/webhook pause-and-resume, queues failed-step or latest-version retries, and applies exponential action retry. Trigger dedupe is an explicit, short Redis window rather than general exactly-once. `wait_for_approval` creates a webhook waitpoint and resumes with an approval result. Source tests cover queue/worker execution, retries, pause/resume and approval.

Inputs are trigger payload plus resolved step properties; outputs are per-step values and the final flow result. Piece actions can perform arbitrary network and data mutations. A universal transaction or idempotency key for all piece side effects was not found, so retry safety remains piece-specific.

## Inference

This is one of the batch's most complete reusable engines. Its strongest reusable pattern is a persisted run state plus explicit waitpoints; its main safety boundary is that durable orchestration does not make arbitrary external effects exactly-once.

## Not verified

Dependencies, tests and the production queue were not run. Worker crashes, Redis failover and end-to-end external side effects remain unverified.

Evidence: [flow definition](https://github.com/activepieces/activepieces/blob/2cd7c61f302f88b5c24811ca480c0fceee602af5/packages/core/execution/src/lib/flows/flow-version.ts), [run state](https://github.com/activepieces/activepieces/blob/2cd7c61f302f88b5c24811ca480c0fceee602af5/packages/core/execution/src/lib/flow-run/execution/flow-execution.ts), [executor](https://github.com/activepieces/activepieces/blob/2cd7c61f302f88b5c24811ca480c0fceee602af5/packages/server/engine/src/lib/handler/flow-executor.ts), [approval](https://github.com/activepieces/activepieces/blob/2cd7c61f302f88b5c24811ca480c0fceee602af5/packages/pieces/core/approval/src/lib/actions/wait-for-approval.ts).
