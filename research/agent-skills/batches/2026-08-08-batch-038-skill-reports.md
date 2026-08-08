# Agent Skills Individual Reports — Batch 038

- Batch ID: `2026-08-08-batch-038`
- Repository `SKILL.md` reads: **10**
- Direct unique skill bodies reviewed: **8**
- New canonical skill bodies: **2**
- Existing canonical bodies revalidated: **6**
- Runtime/build/test/eval execution: **not_executed**

This file preserves content-level deduplication. Eight qualified repository identities in this batch map to six exact Git commit trees already represented in earlier canonical reports. `skill-evolution` and `thekey` are new to the current AI-handbook deep-analysis corpus and receive new canonical reports below.

## `task-concurrency-patterns`

- Reviewed repository identities: `4ccsds/task-concurrency-patterns`, `howknows/task-concurrency-patterns`
- Repository IDs: `1199653059`, `1199422112`
- Stars observed: `0` for both
- Shared revision: `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e`
- Existing canonical deep review: prior batch
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: task dependencies, fan-out/fan-in, read/write concurrency rules, cancellation, and failure escalation
- Strengths: explicit `blocks`/`blockedBy`; recognizes same-area write conflicts; supports stop/correct instead of wasting worker execution
- Risks: unlimited read-only parallelism ignores shared remote/service/resource limits; binary concurrency flags are too coarse; retry count is failure-class agnostic
- Verdict: useful orchestration vocabulary after adding resource-scoped concurrency and failure-aware retry policy

## `coordinator-orchestrator`

- Reviewed repository identity: `howknows/coordinator-orchestrator`
- Repository ID: `1199422882`
- Stars observed: `0`
- Revision: `a6d0311d279b32497a9c952061fafb798309b4e3`
- Existing canonical deep review: prior batch
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: research → synthesis → implementation → independent verification orchestration
- Strengths: coordinator owns synthesis; Continue-vs-Spawn captures context reuse versus anchoring trade-offs; verification is separated from implementation
- Risks: “independent tasks always parallel” ignores shared resources, credentials, APIs, locks, databases, and external side effects
- Verdict: strong coordination pattern once concurrency is gated by resource ownership and side-effect boundaries

## `adversarial-verification`

- Reviewed repository identities: `drcaonet/adversarial-verification`, `4ccsds/adversarial-verification`
- Repository IDs: `1198989767`, `1199648142`
- Stars observed: `0` for both
- Shared revision: `909a2f70fc0de13aff1175c0b507ec24bf0b4815`
- Existing canonical deep review: prior batch
- Structure: root `README.md` + root `SKILL.md`; no surfaced executable harness or eval suite
- Purpose: require observed execution evidence plus adversarial/non-happy-path probes before claiming success
- Strengths: explicitly distinguishes source inspection from runtime evidence and requires concrete command output
- Risks: prompt-level compliance only; unconditional command-running guidance can conflict with analysis-only scope, unavailable tooling, authorization, or side-effect risk
- Verdict: high-value validation discipline when task type, authorization, and environment are explicit

## `memory-type-system`

- Reviewed repository identity: `drcaonet/memory-type-system`
- Repository ID: `1198990070`
- Stars observed: `0`
- Revision: `d3805f3e5a576afd0c55e2de9cddb78511a30c95`
- Existing canonical deep review: prior batch
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: typed `user|feedback|project|reference` records, frontmatter, recall validation, and bounded index
- Strengths: index/content separation; current-state verification reduces stale-memory errors; feedback records preserve rationale
- Risks: fixed 200-line / 25 KB limits lack retrieval-quality evidence; blanket NOT-to-save rules require explicit user-authorized exceptions
- Verdict: useful memory schema if capacity and exception rules become evidence- and authorization-driven

## `smart-memory-guard`

- Reviewed repository identity: `howknows/smart-memory-guard`
- Repository ID: `1199421586`
- Stars observed: `0`
- Revision: `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb`
- Existing canonical deep review: prior batch
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: memory admission, typed classification, drift verification, and pruning
- Strengths: validates remembered paths/symbols/service facts before acting; separates durable information from repository-recoverable facts
- Risks: 5 KB and seven-day thresholds are unvalidated; README's reported 62% reduction is anecdotal; refusing requested memory categorically can conflict with explicit authorization
- Verdict: useful memory-hygiene policy after adding user-authorized exceptions and measurable retention criteria

## `worker-prompt-craft`

- Reviewed repository identity: `drcaonet/worker-prompt-craft`
- Repository ID: `1198990009`
- Stars observed: `0`
- Revision: `8f8a14fc8da0e687457516da3d9f79f8873e9061`
- Existing canonical deep review: prior batch
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: self-contained worker/sub-agent prompts with exact paths, errors, completion criteria, purpose, and validation expectations
- Strengths: reduces hidden-context dependence and vague delegation; clearly separates research and implementation prompts
- Risks: generic examples normalize commits, pushes, PR creation, and reviewer assignment without an explicit external-side-effect authorization gate
- Verdict: strong delegation guidance if mutation and publication actions are separately authorized

## `skill-evolution` — new canonical report

- Reviewed repository identity: `lostinheaven-knt/skill-evolution-skill`
- Repository ID: `1199523227`
- Stars observed: `0`
- Revision: `b7cb91acce415f82b0459968147fa6f9f2e7fedd`
- Canonical deep review: Batch 038
- Structure: `README.md`, `SKILL.md`, `config/`, `docs/`, `references/`, `schemas/`, `scripts/`, `tests/`
- Content class: runnable passive skill-evolution prototype
- Runtime execution in this review: **not_executed**

### Design summary

The repository implements a file-based, replayable evolution pipeline rather than only describing one. Hook events are normalized into reports and transactions, attributed to `patch` / `replacement` / `composition` / no-change decisions, materialized into candidate assets when a parent skill can be found, structurally validated, passed through promotion-review logic, and recorded in lineage.

Its design deliberately keeps stable promotion behind review. The repository distinguishes host-specific concerns from framework-agnostic evolution logic and treats lineage, rollback, and explicit transaction state as first-class artifacts.

### Implementation evidence

`consume_hook_events.py` directly implements the event consumer and stage orchestration. It validates transaction schemas, resolves parent-skill locations from event/config/fallback paths, invokes the report/attribution/materialization/validation/promotion scripts, records transaction state, appends processed events, and clears processed inbox content.

`validate_candidate.py` validates candidate metadata and structure: `SKILL.md`, frontmatter, stub markers, content/file shape, parent consistency, `DIFF.md`, and patch notes. Crucially, generated validation output explicitly records `behavioral_verification: "unverified"`.

`references/evaluation-policy-v0.1.md` defines Structural Validity, Trigger Alignment, Behavioral Improvement, and Risk Delta as separate evidence layers and states that current v0.1 automation does not yet supply full behavioral-improvement evidence.

### Test/eval evidence

`tests/test_p1_pipeline.py` contains executable unit/integration-style test source covering:

- a three-event end-to-end demo pipeline;
- invalid candidate types rejected by schema validation;
- malformed JSONL and non-object inbox records;
- unresolved parent-skill path behavior.

The test source was inspected but **not executed** in Batch 038. There is no repository-local task-level behavioral regression/eval suite proving that an evolved skill improves real agent task success.

### Strengths

1. **Truthful validation boundary.** Structural success is not presented as behavioral success.
2. **Review-gated promotion.** Stable auto-promotion is intentionally disabled while behavioral evaluation is incomplete.
3. **Reversible lineage.** Candidate metadata links changes back to parent skills and triggering traces.
4. **Runnable state machine.** Scripts, schemas, and transaction files make the flow auditable and replayable.
5. **Abnormal-path test source exists.** The repository is not limited to happy-path examples.
6. **Scope is conservative.** README explicitly states that it is not yet a production self-evolving platform.

### Risks and missing evidence

1. **Behavioral improvement remains unverified.** The decisive missing layer is replay of original failures and neighboring tasks against parent vs candidate.
2. **No subprocess timeout.** Stage execution can hang indefinitely.
3. **Processed-state semantics can lose retry opportunities.** Rejected/transiently failed events are still moved out of the active inbox; a dead-letter/retry mechanism is needed for production reliability.
4. **Malformed events are skipped, not quarantined.** The log preserves a warning but not a dedicated recoverable artifact.
5. **Attribution is heuristic.** Trigger type alone is insufficient evidence that a problem belongs to the skill rather than the host, model, tool, environment, or task specification.
6. **Filesystem path trust needs confinement.** Event-provided parent-skill paths should be authorized and constrained to permitted roots in an autonomous host.
7. **No canary/shadow evaluation or production observability.** The repository documents these as future work.

### Recommended adoption pattern

Use this repository as a reference for the **candidate lifecycle, lineage, review gates, and structural contracts**, not as proof that autonomous skill evolution is solved. Before automatic promotion, add deterministic task bundles, parent-vs-candidate replay, measurable regression criteria, risk-delta gates, timeouts, and recoverable event queues.

- Verdict: **strong engineering prototype; behavioral evolution still unverified**

## `thekey` — new canonical report

- Reviewed repository identity: `Akera-Agency/thekey-skill`
- Repository ID: `1199591229`
- Stars observed: `0`
- Revision: `4d5a534fc5d1f36faa6f4de09c8181e0ec1f34bd`
- Canonical deep review: Batch 038
- README: **absent at pinned revision**
- Structure: root `SKILL.md`, `scripts/thekey-api.sh`, `references/api-reference.md`, `references/course-ids.md`
- Content class: operational LMS CLI/API skill with external mutations
- Runtime/API execution in this review: **not_executed**

### Design summary

The skill packages operational knowledge for TheKey LMS: course/chapter/objective creation, content changes, AI slide generation, thumbnail upload, question-report inspection, gradebook analysis, quizzes, and raw API operations. `scripts/thekey-api.sh` provides Bash wrappers around a local auth file, cookie-authenticated `curl`, and higher-level helpers. Reference files document endpoints and environment-specific course data.

### Critical finding: committed credentials

`SKILL.md` contains shared plaintext development credentials together with account identifiers. The credential value is **redacted from this report and must not be propagated**. This should be handled as a secret exposure: rotate the affected credentials, remove them from current tracked content, assess Git history and downstream copies, and add automated secret detection.

### Security, privacy, and reliability risks

1. **External mutations lack an explicit authorization gate.** The skill includes create/update/delete/upload and raw API commands. An autonomous agent should distinguish observation from mutation and require appropriate authorization before destructive or externally visible operations.
2. **Student/user information can be printed to stdout.** Question-report and gradebook helpers include identity/contact/performance fields. Logs and agent transcripts need minimum-necessary output and redaction rules.
3. **Machine-specific credential/tool paths are embedded.** This reduces portability and encourages coupling to one host layout.
4. **Fixed development host.** Environment selection is not a first-class configuration/guardrail, increasing the risk of accidental use against the wrong target if copied or modified.
5. **Shell string interpolation builds JSON.** Titles/descriptions can contain quoting/control characters that break request payloads. Use a real JSON serializer.
6. **HTTP failure handling is weak.** `curl -s` lacks consistent fail/status/timeout/retry handling, so API failures can become opaque downstream JSON parse errors.
7. **Authentication data is passed in request-header arguments.** Host/process exposure should be considered and minimized.
8. **Reference snapshots can go stale.** Course IDs, classroom details, endpoint quirks, and environment-specific examples need freshness/version checks.
9. **No repository-local test/eval harness surfaced.** API quirks and operational recipes are not independently reproduced by this review.
10. **No README.** The skill file carries both operational instructions and sensitive environment context without a separate public-safe overview or threat/safety section.

### Useful aspects

- Endpoint quirks and content-array requirements are documented close to the commands that need them.
- The helper script centralizes repeated authentication/request behavior rather than duplicating every curl sequence.
- Separate API/course references reduce some `SKILL.md` overload.
- The skill covers both CLI paths and raw API escape hatches, which can be useful during tooling gaps if authorization and safety controls are added.

### Recommended adoption pattern

Do **not** adopt the repository verbatim into an autonomous agent. First rotate/remove committed secrets, parameterize environment and paths, add read-vs-write authorization gates, redact student/user data, use safe JSON serialization, add HTTP status/timeouts, and create contract tests against a disposable development fixture.

- Verdict: **operationally useful but currently unsafe for autonomous adoption**

## Held adjacent entry

`tagai-dao/self-ip-agency` remains an index-stage `adjacent_search_hit` and is not counted among Batch 038's completed repositories. Repository-content inspection showed a broader three-agent operating system with installer/runtime/wiki/AutoResearch components and references to installing a TagClaw skill pack, rather than a root AgentSkill package. It remains held pending any future catalog rule that explicitly admits full agent runtimes.

## Deduplication record

Ten qualified repository identities were completed. They collapse to eight unique Git commit trees: six already-canonical policy-skill trees plus two new implementations. Batch 038 therefore adds **2** new canonical skill reports while adding **10** content-verified repository identities to structure-reviewed coverage.
