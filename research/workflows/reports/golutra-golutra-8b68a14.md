# golutra/golutra workflow assessment

- Fixed commit: `8b68a14183afa6ec26f9905f2a81cbd91ed1b35b`
- Tree/content: `git-tree:b53350a0e5f9eae9835ce0d38c35fedbd36462e2`
- Observed: 3,798 Stars on 2026-08-09; `master`; not forked or archived
- License: BSL-1.1, Additional Use Grant none; production restriction until change to GPL-2.0-or-later on 2030-02-25
- Evidence: `source_validated`; runtime not validated
- Subtype/topic fit: `multi-agent-dispatch-orchestrator`; partial fit

## Verified

A Tauri command persists a chat message and enqueues a Redb outbox task. A worker claims due tasks with an eight-second lease, dispatches mentions to configured agent terminals and marks sent/failed. Failures use exponential backoff, six attempts and a dead state. Re-enqueue by message ID replaces the existing task, while the per-terminal batcher rejects an in-flight or queued duplicate message ID and releases the next batch only after a semantic flush. Codex sessions can resume by session ID.

Inputs are chat text, conversation/sender IDs, mentions, workspace path and terminal member configuration; outputs are persisted message/run status, terminal input and diagnostics. Effects are the arbitrary CLI commands performed by connected agents. The invite UI defaults `unlimitedAccess` to true; for Codex this appends `--dangerously-bypass-approvals-and-sandbox`, so a user-visible toggle exists but the default weakens approval and sandbox boundaries.

No source implementing README claims for custom workflow definitions or one-click workflow-template import/export was found. The README marks a month-long CEO agent and autonomous network as future work. Existing code validates durable message dispatch, not that future autonomous workflow.

## Inference

The durable outbox and per-terminal duplicate suppression are useful orchestration primitives. Marking the repository as a general long-running workflow engine would overstate the fixed source.

## Not verified

Build/tests were not run. Terminal delivery after worker/process crashes, external CLI behavior, custom workflow templates and long-horizon autonomous operation remain unverified.

Evidence: [README](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/README.md), [outbox store](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/src-tauri/src/message_service/chat_db/outbox.rs), [worker](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/src-tauri/src/orchestration/chat_outbox.rs), [dispatch](https://github.com/golutra/golutra/blob/8b68a14183afa6ec26f9905f2a81cbd91ed1b35b/src-tauri/src/orchestration/dispatch.rs).
