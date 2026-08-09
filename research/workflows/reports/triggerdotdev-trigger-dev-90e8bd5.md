# triggerdotdev/trigger.dev workflow assessment

- Fixed commit: `90e8bd5c12056eb21c91513efb1233dff3b0fbd3`
- Tree/content: `git-tree:f03c49578a950f431d32c0e8500ea91a3651e2cb`
- Observed: 15,949 Stars; `main`; not forked or archived
- License: Apache-2.0
- Evidence: `source_validated`; runtime not executed in this batch
- Subtype/topic fit: `durable-task-runtime`; strong fit

## Verified

The SDK defines stable-ID tasks with JSON payloads, asynchronous outputs, retry, queues, machine constraints and TTL. Entry methods cover single/batch trigger, trigger-and-wait and subscriptions. The run engine distinguishes delayed, pending, dequeued, executing, paused, waiting, retrying and terminal outcomes. Retry decisions enforce error eligibility and configured attempt limits; long retries requeue and short retries create a new snapshot. Waitpoint completion resumes execution or queues from a checkpoint.

Task triggers and wait tokens accept idempotency keys. Completing an already completed token returns success without repeating the transition. Human review can be built with `createToken`, an authorized external completion, and `forToken`. User task code can still perform arbitrary effects; the platform does not prove transactional or exactly-once behavior for those external effects.

## Inference

The platform has strong durable state, retry and waitpoint primitives. Safe reuse still requires workflow authors to propagate idempotency into external APIs.

## Not verified

Build, tests, checkpoint restoration, self-host/cloud behavior and fixed-commit CI were not run or verified.

Evidence: [task SDK](https://github.com/triggerdotdev/trigger.dev/blob/90e8bd5c12056eb21c91513efb1233dff3b0fbd3/packages/trigger-sdk/src/v3/tasks.ts), [retry engine](https://github.com/triggerdotdev/trigger.dev/blob/90e8bd5c12056eb21c91513efb1233dff3b0fbd3/internal-packages/run-engine/src/engine/retrying.ts), [wait SDK](https://github.com/triggerdotdev/trigger.dev/blob/90e8bd5c12056eb21c91513efb1233dff3b0fbd3/packages/trigger-sdk/src/v3/wait.ts).
