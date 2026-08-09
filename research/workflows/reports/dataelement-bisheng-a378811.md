# dataelement/bisheng workflow assessment

- Fixed commit: `a3788115d71f4b5888a34fbe7e1f0f3f9f13784c`
- Content identity: `git-tree:206b56261575fcf40e7ef6c65a77cfca9ed128a7`
- Evidence: `source_validated`
- Subtype/topic fit: `outbox-mediated durable human-approval state machine`; `strong_fit`
- Runtime execution: none

## Verified

- The repository describes BISHENG as an enterprise LLM application platform and explicitly advertises visual workflows with loops, parallelism, batching, conditionals, multi-type I/O, and human-in-the-loop intervention.
- The approval gate accepts a structured ApprovalGateRequest, deduplicates active requests by tenant, scenario, business key, and applicant, resolves a scenario route and approvers, then returns pass, pending, or exception outcomes.
- Persisted instance states include pending, approved, executing, executed, rejected, exception, withdrawn, cancelled, and execute_failed; task, exception, outbox, and action-log records separately capture operational progress.
- A pass route still creates a pending outbox record and asynchronously dispatches the business handler, while an approval route creates a pending instance and one task per resolved approver.
- User-facing endpoints expose task listing/detail, an explicit decision action, request listing/detail, withdrawal, and scenario-specific application/revocation operations.
- The human decision contract distinguishes approve and reject and carries an optional bounded reason/comment; the generic endpoint forwards operator identity, tenant, administrator status, comment, and request IP to the decision service.
- Outbox execution marks both outbox and instance success on a successful handler call; on failure it increments retry_count, records an error summary, changes the instance to execute_failed, creates an exception, sends a notification, and writes a handler audit log.
- Administrative retry reuses the persisted payload snapshot, increments retry_count on repeated failure, and resolves the exception only after a successful handler call.
- The runtime test fixture creates real in-memory SQL tables for scenario, route, version, node, instance, task, exception, outbox, and action-log models and covers direct-pass, pending-task, and final-approval/outbox persistence paths.
- The sampled GitHub workflow is triggered only by pushes to develop/* and builds/pushes backend and frontend images; it is not evidence that the approval tests ran for this fixed commit.

## Inference

- The subtype is supported by the persisted approval/task/exception/outbox state model, explicit human decision endpoints, route-to-node progression, and deferred handler dispatch.
- Duplicate-active lookup reduces repeat submissions, but the sampled database index is not unique, so race-free idempotency cannot be inferred from the index alone.
- The outbox and payload snapshot improve recoverability, but a handler that succeeds externally and fails before local success persistence could still be invoked again unless each handler is independently idempotent.
- This approval subsystem is reusable across business scenarios because routing is scenario-driven and execution is delegated through a handler registry, although the sampled files do not establish every registry extension contract.

## Not verified

- Not verified: atomic transaction boundaries across instance/task/outbox creation and asynchronous dispatch.
- Not verified: uniqueness enforcement or locking inside find_duplicate_active_instance under concurrent submissions.
- Not verified: delivery semantics, retry policy, and acknowledgement configuration of the Celery worker task that executes an approval outbox.
- Not verified: idempotency guarantees of scenario handlers and their external side effects.
- Not verified: end-to-end execution, test results, deployment behavior, and current CI status at the fixed commit.
- Not verified: metrics, distributed traces, or alerting beyond sampled logs, audit records, exceptions, and notifications.

## Limitations

- Read-only review of 11 selected files at the exact commit; no code, tests, services, or workflows were executed.
- Evidence level is capped at source_validated; scores use 1 (weak/not present in sampled evidence) through 5 (strong source evidence).
- The review focuses on the approval workflow subsystem rather than every workflow implementation in this large repository.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 4 |
| `state_and_resume` | 4 |
| `idempotency` | 3 |
| `side_effect_control` | 4 |
| `human_gate` | 5 |
| `observability` | 4 |
| `validation` | 4 |
| `reuse_value` | 4 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Evidence URLs

- https://github.com/dataelement/bisheng/blob/a3788115d71f4b5888a34fbe7e1f0f3f9f13784c/README.md#L31-L51
- https://github.com/dataelement/bisheng/blob/a3788115d71f4b5888a34fbe7e1f0f3f9f13784c/src/backend/bisheng/approval/domain/models/approval_instance.py#L13-L42
- https://github.com/dataelement/bisheng/blob/a3788115d71f4b5888a34fbe7e1f0f3f9f13784c/src/backend/bisheng/approval/domain/models/approval_instance.py#L45-L158
- https://github.com/dataelement/bisheng/blob/a3788115d71f4b5888a34fbe7e1f0f3f9f13784c/src/backend/bisheng/approval/domain/services/approval_gate.py#L92-L175
- https://github.com/dataelement/bisheng/blob/a3788115d71f4b5888a34fbe7e1f0f3f9f13784c/src/backend/bisheng/approval/domain/services/approval_gate.py#L177-L258
- https://github.com/dataelement/bisheng/blob/a3788115d71f4b5888a34fbe7e1f0f3f9f13784c/src/backend/bisheng/approval/api/endpoints/approval_user.py#L33-L97
- https://github.com/dataelement/bisheng/blob/a3788115d71f4b5888a34fbe7e1f0f3f9f13784c/src/backend/bisheng/approval/domain/services/approval_outbox_service.py#L13-L84
- https://github.com/dataelement/bisheng/blob/a3788115d71f4b5888a34fbe7e1f0f3f9f13784c/src/backend/bisheng/approval/domain/services/approval_exception_service.py#L510-L539
- https://github.com/dataelement/bisheng/blob/a3788115d71f4b5888a34fbe7e1f0f3f9f13784c/src/backend/test/approval/test_approval_flow_runtime.py#L35-L132
- https://github.com/dataelement/bisheng/blob/a3788115d71f4b5888a34fbe7e1f0f3f9f13784c/.github/workflows/test.yml#L1-L24
