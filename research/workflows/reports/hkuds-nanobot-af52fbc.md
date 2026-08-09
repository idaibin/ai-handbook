# HKUDS/nanobot workflow assessment

- Fixed commit: `af52fbcbc43ee9b44bcdb1bb462c0db5c12f751d`
- Tree/content: `git-tree:9a93ca77ee66b91515fab82e7a75c8a15e2dccb1`
- Observed: 46,779 Stars; `main`; not forked or archived
- License: MIT
- Evidence: `source_validated`; Python compile check passed, behavioral runtime not validated
- Subtype/topic fit: `scheduled-agent-turn`; fit, but not a general DAG engine

## Verified

Cron jobs accept one-shot, interval or cron schedules, agent-turn messages and bound session/channel metadata. Persisted state records next/last run, success/error/skipped outcome and bounded history. Store writes use a temporary file, `fsync` and atomic replacement; corrupt stores are backed up instead of silently reset. Local triggers use an `inbox -> processing -> completed/failed` file queue. Gateway interruption requeues processing deliveries, producing at-least-once semantics with a ten-attempt infrastructure limit.

Inputs are messages and session/workspace bindings; outputs are agent responses and audit/run records. The agent may invoke shell, filesystem, web and MCP tools, so effects are permission- and prompt-dependent. No general multi-step workflow schema, approval node or side-effect idempotency contract was found.

## Inference

This is a durable scheduler and event delivery wrapper around an agent turn. It should not be compared directly with declarative engines. Requeued deliveries may repeat an entire agent turn, so external consumers need idempotency.

## Not verified

`compileall` only proved syntax validity. Pytest was unavailable; real gateway, model, channels and crash recovery were not exercised.

Evidence: [automation contract](https://github.com/HKUDS/nanobot/blob/af52fbcbc43ee9b44bcdb1bb462c0db5c12f751d/docs/automations.md), [cron service](https://github.com/HKUDS/nanobot/blob/af52fbcbc43ee9b44bcdb1bb462c0db5c12f751d/nanobot/cron/service.py), [trigger store](https://github.com/HKUDS/nanobot/blob/af52fbcbc43ee9b44bcdb1bb462c0db5c12f751d/nanobot/triggers/local_store.py).
