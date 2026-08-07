# Agent Skills Individual Reports — Batch 030

- Batch ID: `2026-08-08-batch-030`
- Unique repository-scoped skill reports: **6**
- Repositories represented: **10**
- Runtime/build/test/eval execution: **not_executed**

Four repository pairs are exact full-tree duplicates at identical Git commit SHAs. Each unique skill body is reported once and duplicate repository identities are mapped to the same report rather than counted as new skill content.

## 1. `adversarial-verification`

- Repositories:
  - `camCX/adversarial-verification`
  - `YTT-CSH/adversarial-verification`
- Shared revision: `909a2f70fc0de13aff1175c0b507ec24bf0b4815`
- Type: verification/review policy skill
- Executable artifacts: none observed
- Repository-local evals: none observed

### Purpose

Force an agent to validate a change by executing representative checks and recording actual observed output rather than declaring success from code reading. The skill explicitly includes edge/adversarial probes and non-happy-path checks.

### Design

The skill branches validation by change type: frontend, backend/API, CLI/script, infrastructure/config, bug fix and refactor. Every reported check must contain the command run, observed output and PASS/FAIL result, followed by a single final verdict.

### Assessment

This is a strong behavioral guard against "verification by narration." It is especially useful as a post-implementation gate because it requires execution evidence. However, enforcement is prompt-only: there is no harness or eval proving compliance. Personalized triggers (`bobooo`) reduce portability, and some assumed tools may not exist in every environment.

### Provenance/install observation

The README installation URL targets `Arxchibobo/adversarial-verification`, not either reviewed repository identity. Treat the reviewed repositories as mirrors/copies unless separate provenance is established.

## 2. `smart-memory-guard`

- Repositories:
  - `ajunlonglive/smart-memory-guard`
  - `k1w1f1sh/smart-memory-guard`
- Shared revision: `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb`
- Type: memory admission/pruning policy skill
- Executable artifacts: none observed
- Repository-local evals: none observed

### Purpose

Prevent long-term agent memory from becoming noisy or stale by classifying entries, refusing selected low-value content, re-verifying remembered claims before action and pruning periodically.

### Design

Four types are defined: `user`, `feedback`, `project`, `reference`. Feedback entries must include why the rule exists and how to apply it. Remembered paths/symbols/endpoints/project-state claims must be checked against current reality before use.

### Assessment

The authority separation is useful: code structure and Git history should normally be read from their authoritative stores instead of copied into long-lived memory. Drift checks are also a strong safety property. The weaknesses are overly rigid thresholds and authority rules: refusing some explicit "remember this" requests can conflict with user-authorized intent, while the 5 KB and seven-day pruning heuristics are not justified by repository-local evidence.

The README reports a 13.4 KB → 5.0 KB example reduction, but there is no eval artifact demonstrating general retrieval-quality improvement.

### Provenance/install observation

Installation points to `Arxchibobo/smart-memory-guard`, not the reviewed owners.

## 3. `coordinator-orchestrator`

- Repositories:
  - `alexchenyu/coordinator-orchestrator`
  - `k1w1f1sh/coordinator-orchestrator`
- Shared revision: `a6d0311d279b32497a9c952061fafb798309b4e3`
- Type: multi-agent orchestration policy skill
- Executable artifacts: none observed
- Repository-local evals: none observed

### Purpose

Define a coordinator role that parallelizes research, performs its own synthesis, delegates implementation and uses a separate verification stage.

### Design

The workflow is research → synthesis → implementation → verification. The coordinator is explicitly responsible for understanding worker findings before issuing precise downstream instructions. Continue-vs-Spawn rules try to balance context reuse against fresh perspective.

### Assessment

The synthesis requirement is the most valuable rule because it prevents the main thread from acting as a blind message router. Spawning a fresh verifier after implementation can reduce anchoring. The principal risk is over-delegation: the identity statement "coordinator, not executor" is stronger than necessary and can conflict with the skill's own instruction to directly answer simple tasks. Fixed failure/retry counts are also environment-insensitive.

### Provenance/install observation

The README attributes inspiration to reverse-engineered Claude Code source-map material; that provenance was not independently verified here. Installation points to `Arxchibobo/coordinator-orchestrator`.

## 4. `task-concurrency-patterns`

- Repositories:
  - `ajunlonglive/task-concurrency-patterns`
  - `k1w1f1sh/task-concurrency-patterns`
- Shared revision: `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e`
- Type: orchestration/concurrency policy skill
- Executable artifacts: none observed
- Repository-local evals: none observed

### Purpose

Give multi-agent workflows a simple dependency model, explicit task states and a baseline rule for parallel reads versus serialized conflicting writes.

### Design

Tasks move through `pending`, `in_progress`, `completed` and expose `blocks` / `blockedBy`. The skill demonstrates serial chains, research fan-out and implementation fan-in. A binary `concurrencySafe` declaration distinguishes parallelizable from serialized work.

### Assessment

Explicit dependency edges are simple and inspectable. The binary concurrency model is nevertheless incomplete for production systems: read-only operations can contend on quotas or external resources, while writes to separate files can still share databases, generated outputs or deployment state. "Unlimited" read-only parallelism should not be promoted as a universal rule.

### Provenance/install observation

Installation points to `Arxchibobo/task-concurrency-patterns`.

## 5. `worker-prompt-craft`

- Repository: `YTT-CSH/worker-prompt-craft`
- Revision: `8f8a14fc8da0e687457516da3d9f79f8873e9061`
- Type: sub-agent instruction-authoring skill
- Executable artifacts: none observed
- Repository-local evals: none observed

### Purpose

Make worker prompts self-contained so a sub-agent that cannot see the parent conversation still receives concrete scope, context and completion criteria.

### Design

The skill requires concrete files/paths/lines when known, an explicit definition of done and a purpose statement. It provides separate prompt shapes for research, implementation, correction and Git operations, plus a checklist for write/read-only intent and validation.

### Assessment

The skill directly addresses a high-frequency multi-agent failure mode: context that exists only in the parent thread. It also usefully distinguishes "report findings, do not modify" from implementation requests. The counter-risk is premature anchoring: supplying a specific diagnosis and line number before independent investigation can bias a worker toward the parent's hypothesis. Templates that demand commits or Git mutations should be conditioned on explicit repository authorization.

### Provenance/install observation

Installation points to `Arxchibobo/worker-prompt-craft`.

## 6. `memory-type-system`

- Repository: `camCX/memory-type-system`
- Revision: `d3805f3e5a576afd0c55e2de9cddb78511a30c95`
- Type: memory schema/retrieval policy skill
- Executable artifacts: none observed
- Repository-local evals: none observed

### Purpose

Structure long-term memory into four semantic types and separate a compact retrieval index from full per-memory bodies.

### Design

Each memory is stored with frontmatter containing `name`, `description` and `type`. `MEMORY.md` is treated as an index, not the canonical memory body. The skill also requires converting relative project dates to absolute dates and validating remembered mutable facts against current state.

### Assessment

The index/body split is a concrete progressive-disclosure mechanism and is better than continuously appending full memory text into one global file. The main trade-off is operational complexity: one file per memory can create file sprawl, and the fixed 200-line / 25 KB index limits are not tied to measured retrieval performance. `project` and `reference` can overlap, so deterministic tie-breaking or multi-label semantics would improve the schema.

This skill substantially overlaps `smart-memory-guard`. A catalog consumer should treat them as related variants: `memory-type-system` emphasizes storage schema and recall, while `smart-memory-guard` emphasizes admission, drift and pruning.

### Provenance/install observation

Installation points to `Arxchibobo/memory-type-system`.

## Batch validation note

The six unique `SKILL.md` bodies and their README files were read at pinned revisions. Repository searches across the six unique repositories returned no `scripts`, `references`, or `eval` matches, and the reviewed documentation does not identify such repository-local artifacts. No build, command, test or evaluation was executed, so these reports make no runtime-success claim.
