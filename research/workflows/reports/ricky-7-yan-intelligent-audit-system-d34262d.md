# Ricky-7-Yan/intelligent-audit-system workflow assessment

- Fixed commit: `d34262d981a5556265b88a1779747364b5492326`
- Content identity: `git-tree:ea146932b2e764444535cf7076b925d342129516`
- Evidence: `source_validated`
- Subtype/topic fit: `bounded_governed_multi_role_audit_agent_loop`; `strong_fit`
- Runtime execution: none

## Verified

- FastAPI endpoints create Agent tasks from an objective and context, run one step or a bounded loop, retrieve task/episode/evidence data, add manual steps, evaluate tasks, curate experience candidates, and submit human reviews for experience and Harness candidates.
- Task creation plans the objective, runs a safety check, persists a tenant-scoped task envelope, emits a task-created event, and automatically executes the first step unless blocked.
- The bounded loop stops on completed, blocked, needs_review, step-budget exhaustion, or no progress; tool-call and per-step retry budgets are explicit in task state.
- Plan dependencies are checked before execution. Missing dependencies, exhausted budgets, tool failures, and failed step evaluations transition the task to needs_review rather than silently continuing.
- Every step passes a deterministic safety gate that blocks credential-like or destructive content and warns when evidence signals are absent.
- Skill execution enforces declared permissions, input and output schemas, timeouts, tenant-scoped cache keys, failure-count circuit breaking, structured recoverability signals, redaction, and append-only run records.
- A failed skill is retried at most once by the Agent runtime. Tool attempts record status, duration, input/output size, cache hit, circuit state, validation errors, and trace attributes.
- Task state and events are persisted in tenant-scoped SQLite WAL storage with optimistic version checks. Episode packages bind context hashes, role traces, tool evidence, safety gates, failures, interventions, artifacts, event logs, and a SHA-256 integrity digest.
- Human governance is explicit for reusable experience: only approved lessons are selected into new task context, and review endpoints persist reviewer, decision, comment, and timestamp. Harness candidate promotion also has a review endpoint.
- Delivery packages include workpaper, evidence-request, control-test, finding/remediation, quality-review, event-log, and sign-off structures, with review_required derived from the quality gate.
- Authorization maps HTTP methods and API domains to RBAC permissions, persisted records are tenant/project filtered, and audit events use a hash chain with an optional HMAC-signed head checkpoint.
- CI runs Python 3.10/3.11/3.12 tests with a 75% targeted coverage floor, reproducibility, lint, Bandit, dependency audit, JavaScript syntax, and a container build; sampled production-boundary tests cover optimistic locking, tenant/project isolation, signed checkpoints, executable contracts, output validation, and artifact-integrity review.

## Inference

- The workflow is resumable at persisted task boundaries because completed steps and plan dependencies determine the next step, but it lacks a durable in-progress invocation lease, so a crash during a tool call can lead to re-execution.
- Its strongest human gate governs learning/promotion and post-failure review; ordinary low-risk task steps may execute automatically after deterministic policy checks.
- The platform is reusable as a single-process governed Agent runtime, but its built-in skill handlers and delivery schema are audit-domain specific.

## Not verified

- No API, skill, database, test, CI, or crash/restart scenario was executed.
- No repository LICENSE file was present in the inspected fixed tree; licensing is therefore not verified.
- No durable idempotency key, invocation lease, or exactly-once mechanism was found for Agent task creation or skill execution.
- Recovery after a crash between an external side effect and task persistence is not verified.
- The review endpoints' deployment-time authentication and authorization behavior was not exercised.
- External integrations and the real-world correctness of audit findings, evidence, or reports are not verified.
- Repository branch protection and current CI health are not verified.

## Limitations

- Source-only review at the fixed commit; evidence level cannot exceed source_validated.
- Twelve key files were read. Evaluation, Harness, audit repository, and individual built-in skill implementations were represented through their call sites and sampled tests rather than fully audited.
- The project explicitly describes a single-process orchestration; multi-node coordination and external KMS/object storage are outside its stated boundary.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 5 |
| `state_and_resume` | 4 |
| `idempotency` | 2 |
| `side_effect_control` | 4 |
| `human_gate` | 4 |
| `observability` | 5 |
| `validation` | 5 |
| `reuse_value` | 4 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Evidence URLs

- https://github.com/Ricky-7-Yan/intelligent-audit-system/blob/d34262d981a5556265b88a1779747364b5492326/services/agent_runtime.py
- https://github.com/Ricky-7-Yan/intelligent-audit-system/blob/d34262d981a5556265b88a1779747364b5492326/services/skill_registry.py
- https://github.com/Ricky-7-Yan/intelligent-audit-system/blob/d34262d981a5556265b88a1779747364b5492326/services/record_store.py
- https://github.com/Ricky-7-Yan/intelligent-audit-system/blob/d34262d981a5556265b88a1779747364b5492326/services/security.py
- https://github.com/Ricky-7-Yan/intelligent-audit-system/blob/d34262d981a5556265b88a1779747364b5492326/web/main.py
- https://github.com/Ricky-7-Yan/intelligent-audit-system/blob/d34262d981a5556265b88a1779747364b5492326/.github/workflows/ci.yml
