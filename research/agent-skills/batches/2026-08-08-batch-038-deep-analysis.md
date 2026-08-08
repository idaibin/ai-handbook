# Agent Skills Deep Analysis — Batch 038

- Batch ID: `2026-08-08-batch-038`
- Stage: repository deep analysis
- Queue source: `sources/catalog/batches/agentskills-created-2026-04-02-deterministic.json`
- Qualified repositories completed: **10**
- Repository `SKILL.md` reads: **10**
- Repository README reads: **9**
- Verified README absence: **1** (`Akera-Agency/thekey-skill`)
- Unique Git commit trees directly reviewed: **8**
- New canonical individual skill reports: **2**
- Existing canonical skill bodies revalidated: **6**
- Runtime/build/test/eval execution: **not_executed**

## Queue handling

Batch 037 ended at qualified queue entry `drcaonet/coordinator-orchestrator`. This run continued in deterministic queue order. The index entry `tagai-dao/self-ip-agency` is classified `adjacent_search_hit`, so it was **not counted complete** and did not consume one of the ten qualified slots. A repository-content check confirmed it is a broader three-agent operating system with many runtime scripts and documentation references to an installed TagClaw skill pack, but no root `SKILL.md` surfaced. It remains held outside the qualified deep-analysis count.

The ten completed qualified entries are therefore queue positions 30–37, then 39–40.

## Completion gate

A repository is counted only after all available evidence below was checked:

1. exact GitHub repository identity;
2. exact observed star count through repository search;
3. latest revision pinned to a concrete commit SHA;
4. root README read when present, or absence verified when not present;
5. root `SKILL.md` / equivalent skill definition read;
6. scripts, references, tests/evals, and package artifacts inspected when available;
7. findings written from repository content rather than metadata alone.

Eight completed repositories matched exact `stars:0` searches and are mirrors of six previously reviewed policy-skill trees. `lostinheaven-knt/skill-evolution-skill` and `Akera-Agency/thekey-skill` also matched exact `stars:0` searches and introduce two new skill bodies to this corpus.

## Repository results

| Repository | GitHub ID | Stars | Reviewed revision | README | Content-proven class | New canonical reports |
|---|---:|---:|---|---|---|---:|
| `4ccsds/task-concurrency-patterns` | `1199653059` | 0 | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | read | exact duplicate of reviewed policy skill | 0 |
| `howknows/coordinator-orchestrator` | `1199422882` | 0 | `a6d0311d279b32497a9c952061fafb798309b4e3` | read | exact duplicate of reviewed policy skill | 0 |
| `drcaonet/adversarial-verification` | `1198989767` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | read | exact duplicate of reviewed policy skill | 0 |
| `drcaonet/memory-type-system` | `1198990070` | 0 | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | read | exact duplicate of reviewed policy skill | 0 |
| `howknows/task-concurrency-patterns` | `1199422112` | 0 | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | read | exact duplicate of reviewed policy skill | 0 |
| `howknows/smart-memory-guard` | `1199421586` | 0 | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | read | exact duplicate of reviewed policy skill | 0 |
| `4ccsds/adversarial-verification` | `1199648142` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | read | exact duplicate of reviewed policy skill | 0 |
| `drcaonet/worker-prompt-craft` | `1198990009` | 0 | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | read | exact duplicate of reviewed policy skill | 0 |
| `lostinheaven-knt/skill-evolution-skill` | `1199523227` | 0 | `b7cb91acce415f82b0459968147fa6f9f2e7fedd` | read | runnable skill-evolution prototype | 1 |
| `Akera-Agency/thekey-skill` | `1199591229` | 0 | `4d5a534fc5d1f36faa6f4de09c8181e0ec1f34bd` | absent | operational LMS API/CLI skill | 1 |

## Existing canonical bodies revalidated

### `task-concurrency-patterns`

Both completed identities expose the same pinned commit. The skill models `blocks` / `blockedBy`, fan-out/fan-in execution, read/write separation, worker cancellation, and a fixed failure-escalation sequence. The useful part is explicit dependency modeling and recognition that concurrent writes need serialization. The main weakness remains its absolute statement that read-only work may run with no concurrency limit: shared API quotas, file descriptors, database readers, credentials, remote services, CPU/memory, and rate limits can couple nominally read-only tasks. Fixed retry counts also ignore failure class, cost, and idempotency.

### `coordinator-orchestrator`

The content preserves a clear four-stage split: parallel research, coordinator synthesis, worker implementation, and independent verification. It correctly treats synthesis as the coordinator's responsibility and distinguishes Continue from Spawn based on context reuse and anchoring risk. The main unresolved issue is the rule that independent tasks should always run in parallel; independence must include shared resources and external side effects, not only distinct file targets.

### `adversarial-verification`

Both completed identities share the same pinned tree. The skill strongly separates source inspection from execution evidence and asks for non-happy-path/adversarial probes before a PASS. This is useful validation discipline, but mandatory command execution is too broad for analysis-only work, unavailable tooling, or actions requiring separate authorization. The repository itself has no executable validation harness, so compliance remains prompt-enforced.

### `memory-type-system`

The skill defines `user`, `feedback`, `project`, and `reference` records, per-record frontmatter, current-state verification before relying on remembered paths/symbols, and a bounded `MEMORY.md` index. The schema and drift checks are useful. Fixed capacity limits and blanket NOT-to-save rules remain heuristics and need explicit user-authorized exceptions plus retrieval-quality evidence.

### `smart-memory-guard`

The skill combines memory admission, four-type classification, drift verification, and pruning. Its fixed 5 KB heartbeat threshold, seven-day summarization rule, and README claim of a 62% memory reduction have no repository-local evaluation proving improved retrieval or task quality. Its instruction to refuse some memories even when explicitly requested also needs an authorization-aware exception model.

### `worker-prompt-craft`

The strongest pattern is self-contained delegation: exact paths, concrete completion criteria, purpose, error information, and verification requirements. However, its generic Git example bundles branch creation, cherry-pick, push, draft PR creation, and reviewer assignment into ordinary worker instructions. Those are external side effects and should sit behind explicit authorization rather than being normalized as default prompt structure.

## New canonical review: `skill-evolution`

Repository: `lostinheaven-knt/skill-evolution-skill`

### Structure and implementation

This repository is materially different from the mirror-heavy policy skills. It contains a runnable Python prototype with `scripts/`, JSON schemas, `references/`, configuration, a roadmap, and `tests/`. The README describes a replayable passive-evolution loop: consume hook events, normalize them, attribute a recommended action, create and materialize candidates, structurally validate them, generate promotion recommendations, and write lineage records.

Supported signals include `skill_failure`, `user_correction`, and `repeated_success_pattern`. The current promotion policy is intentionally conservative: failed structural validation is rejected; passing candidates stop at review-required/experimental states; nothing is automatically promoted to stable.

### Direct code findings

`consume_hook_events.py` implements the orchestration flow rather than only documenting it. It validates transaction JSON, resolves a parent skill from event fields or runtime config, invokes each stage as a Python subprocess, persists transaction state, writes processed events, and clears the inbox after processing. The code also skips malformed JSONL/non-object lines with warnings.

`validate_candidate.py` is explicit that current validation is structural. It checks candidate metadata, `SKILL.md`, frontmatter, stub markers, body/file shape, parent availability, diff presence, and patch notes, then writes `behavioral_verification: "unverified"`. This is an important truthful boundary: the prototype does not claim that structural validity proves a candidate is behaviorally better.

The repository's evaluation policy independently defines four layers — structural validity, trigger alignment, behavioral improvement, and risk delta — and states that behavioral improvement still needs case replay, spot checks, or a future regression bundle.

### Tests inspected

`tests/test_p1_pipeline.py` contains real `unittest` coverage for an end-to-end three-event demo, invalid candidate-schema values, malformed/non-object JSONL lines, and missing-parent behavior. These tests were **read but not executed in this batch**, so test success is not claimed here.

### Strengths

- Separates evolution transaction state from candidate assets and lineage.
- Uses explicit schemas and review gates instead of silently mutating a stable skill.
- Keeps automatic stable promotion disabled while behavioral evaluation is incomplete.
- Makes the structural-vs-behavioral validation boundary explicit in code and documentation.
- Includes abnormal-path tests instead of only a happy-path README example.
- Preserves reversible candidate artifacts and parent links.

### Risks and gaps

1. **No behavioral regression engine yet.** Structural checks can prove a candidate is loadable, not that it fixes the triggering task or avoids regressions.
2. **Subprocess stages have no timeout.** A hung script can stall the consumer indefinitely.
3. **Rejected events are still moved to processed state.** This avoids repeated ingestion, but recovery/retry requires an external mechanism; a transient failure can become operationally terminal without a dead-letter/retry queue.
4. **Malformed inbox records are skipped rather than quarantined.** Warnings exist, but the original bad record is not preserved in a dedicated error artifact.
5. **Attribution policy is intentionally simple.** Mapping correction→patch, repeated success→composition, and failure→patch/replacement is not enough to prove root-cause attribution.
6. **Parent-skill path resolution is a trust boundary.** Event-provided/local paths need host-level authorization and workspace confinement if the prototype is embedded into an autonomous runtime.
7. **Production observability/canary evaluation is explicitly unfinished.** The repository correctly documents this limitation.

### Verdict

**High-value prototype and one of the more engineering-complete repositories in this queue, but it is a review-gated structural evolution system rather than a verified self-improving skill platform.** The next decisive improvement is behavioral regression replay with explicit task cases, risk deltas, timeouts, and recoverable event processing.

## New canonical review: `thekey`

Repository: `Akera-Agency/thekey-skill`

### Structure and implementation

No root README exists at the pinned revision. The repository instead contains a large `SKILL.md`, `references/api-reference.md`, `references/course-ids.md`, and `scripts/thekey-api.sh`. The skill is operational: it gives commands for course/chapter/objective management, content updates, AI-generated slide flows, thumbnails, question reports, gradebook operations, quizzes, and raw API calls against a development LMS environment.

The shell helper reads an access token from a local auth file and sends it as a cookie to the configured API. It provides wrappers for GET/POST/PATCH/DELETE plus higher-level course, objective, question-report, gradebook, and thumbnail helpers.

### Critical security and privacy finding

The committed `SKILL.md` contains shared plaintext development credentials and account identifiers. The secret value is intentionally **not reproduced in this report**. This should be treated as a credential exposure: rotate the affected credentials, remove secrets from the current file, assess repository history, and add secret scanning/pre-commit protection.

The skill and helper also handle student/report data and can print reporter names, email addresses, comments, and gradebook information to stdout. Operational logging therefore has a privacy boundary that is currently not modeled.

### Additional risks

1. **No authorization/confirmation policy around mutating operations.** The skill exposes create/update/delete, uploads, content changes, and account-sensitive operations as direct instructions. A production AgentSkill should distinguish read-only inspection from externally visible mutations and require appropriate user authorization.
2. **Environment-specific absolute paths reduce portability.** The skill assumes particular CLI and credential locations and a fixed development API host.
3. **JSON payloads are built by shell string interpolation.** User-provided titles/descriptions containing quotes, backslashes, or control characters can break request JSON. A serializer such as `jq -n --arg` or Python `json.dumps` should be used.
4. **HTTP error handling is weak.** `curl -s` is used without a consistent `--fail-with-body`, timeout, retry classification, or explicit status validation, so downstream Python parsing may obscure the real API error.
5. **Authentication material is placed in a curl header argument.** Depending on the host/process model, command-line exposure should be considered; safer token transport and process isolation may be required.
6. **PII is emitted by helper output.** Reporter identities, student emails/comments, and grade information need minimum-necessary display and redaction rules.
7. **Reference data is environment snapshot data.** Course IDs, classroom details, and endpoint quirks can go stale; the skill has no freshness gate or schema/version verification.
8. **No repository-local tests or eval harness surfaced.** The documented endpoint quirks and auth behavior are operational claims, not reproduced validation in this batch.

### Verdict

**Useful domain-specific operational knowledge, but not safe for autonomous adoption in its current form.** Credential rotation/removal is the first priority, followed by authorization gates, PII redaction, portable configuration, safe JSON serialization, and reproducible API contract tests.

## Artifact inspection summary

| Artifact type | First 8 mirror/policy repos | `skill-evolution-skill` | `thekey-skill` |
|---|---|---|---|
| README | present | present | absent |
| `SKILL.md` | present | present | present |
| scripts | none surfaced | present | present |
| references | none surfaced | present | present |
| tests | none surfaced | present | none surfaced |
| dedicated eval harness | none surfaced | none; behavioral eval explicitly unfinished | none surfaced |
| `package.json` | none surfaced | none surfaced | none surfaced |

## Cross-repository findings

1. **Mirror density remains high.** Eight repository identities collapse to six already-reviewed content trees.
2. **The queue now reaches materially richer implementations.** `skill-evolution-skill` contains executable orchestration, schemas, tests, and explicit validation boundaries; it deserves different treatment from prompt-only skills.
3. **Structural validation must not be conflated with behavioral validation.** `skill-evolution-skill` models this distinction correctly and explicitly marks behavioral verification unverified.
4. **Operational skills need a safety contract.** `thekey-skill` demonstrates why skills that can mutate external systems need authorization, secret handling, environment scoping, PII rules, and failure handling in addition to command examples.
5. **Repository content can reveal a classification error or hold decision.** `tagai-dao/self-ip-agency` remains a broader adjacent agent system rather than being promoted merely because it mentions skills.

## Validation status

- Repository identity: **verified for all 10 completed repositories**.
- Stars: exact observed value **0** verified for all 10 completed repositories.
- Exact revision: **pinned for all 10**.
- `SKILL.md`: **directly fetched for all 10**.
- README: **directly fetched for 9; absence verified for 1**.
- Unique content trees: **8**.
- New canonical skill bodies: **2**.
- Source tests: **inspected for `skill-evolution-skill`; not executed**.
- Runtime/build/tests/evals: **not_executed / not_verified**.
- Held adjacent repository: **not counted complete**.
- Unselected qualified queue entries remain **pending**.
