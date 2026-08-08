# Agent Skills Individual Reports — Batch 036

Batch 036 completed ten repository identities and mapped them to seven already-reviewed canonical skill bodies. No new canonical content body was introduced in this batch.

## Repository → skill mapping

| Repository | Skill | Reviewed revision | Canonical status |
|---|---|---|---|
| `ShawnSiao/self-rationalization-guard` | `self-rationalization-guard` | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | existing canonical review |
| `ajunlonglive/adversarial-verification` | `adversarial-verification` | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | existing canonical review |
| `YTT-CSH/lightweight-explorer` | `lightweight-explorer` | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | existing canonical review |
| `camCX/worker-prompt-craft` | `worker-prompt-craft` | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | existing canonical review |
| `drcaonet/lightweight-explorer` | `lightweight-explorer` | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | exact-tree duplicate |
| `howknows/memory-type-system` | `memory-type-system` | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | existing canonical review |
| `4ccsds/memory-type-system` | `memory-type-system` | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | exact-tree duplicate |
| `howknows/lightweight-explorer` | `lightweight-explorer` | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | exact-tree duplicate |
| `drcaonet/task-concurrency-patterns` | `task-concurrency-patterns` | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | existing canonical review |
| `drcaonet/smart-memory-guard` | `smart-memory-guard` | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | existing canonical review |

## Individual skill reports

### `self-rationalization-guard`

**Purpose.** Prompt-level guard against declaring completion from appearance, assumption, or repeated rationalization.

**Useful pattern.** Explicitly distinguish execution evidence from source inspection and require a completion self-check.

**Limits.** “Always do the opposite of the shortcut” is not a safe universal policy. Command execution, exhaustive edge-case handling, task ordering, and documentation timing must remain conditional on scope, authorization, cost, and risk.

**Evidence status.** README and `SKILL.md` directly read at the pinned commit. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

### `adversarial-verification`

**Purpose.** Turn verification into an attempt to falsify the implementation rather than merely confirm the happy path.

**Useful pattern.** Record observed evidence and include non-happy-path/adversarial checks appropriate to the change.

**Limits.** The repository is itself prompt-only and supplies no harness proving that an agent follows the procedure. Mandatory command-running is too broad for analysis-only work or actions requiring additional authorization.

**Evidence status.** README and `SKILL.md` directly read at the pinned commit. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

### `lightweight-explorer`

**Purpose.** Read-only codebase exploration with explicit search-depth modes and concise evidence output.

**Useful pattern.** Separate exploration from mutation and vary search depth (`quick` / `medium` / `thorough`) instead of always loading everything.

**Limits.** Read-only status does not make repository rules irrelevant. Search-output truncation can hide decisive evidence, and mandatory parallel search is too absolute when rate limits or shared resources matter.

**Repository identities.** `YTT-CSH/lightweight-explorer`, `drcaonet/lightweight-explorer`, and `howknows/lightweight-explorer` expose the same reviewed Git commit tree.

**Evidence status.** README and `SKILL.md` were directly read from all three identities. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

### `worker-prompt-craft`

**Purpose.** Make worker/sub-agent prompts self-contained with exact paths, purpose, completion criteria, and verification expectations.

**Useful pattern.** Treat delegation as an explicit contract so a worker does not depend on hidden coordinator context.

**Limits.** Examples that include branch creation, commits, pushes, PR creation, or reviewer changes should not make those external side effects implicit. They need a separate authorization gate.

**Evidence status.** README and `SKILL.md` directly read at the pinned commit. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

### `memory-type-system`

**Purpose.** Structure durable memory into `user`, `feedback`, `project`, and `reference` records, with per-item frontmatter and a compact index.

**Useful pattern.** Keep the index separate from record bodies and re-validate remembered paths/state before acting on them.

**Limits.** Absolute NOT-to-save rules can conflict with explicit user-authorized retention. Fixed size/line limits are heuristics without retrieval-quality evaluation.

**Repository identities.** `howknows/memory-type-system` and `4ccsds/memory-type-system` expose the same reviewed Git commit tree.

**Evidence status.** README and `SKILL.md` directly read from both identities. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

### `task-concurrency-patterns`

**Purpose.** Model multi-worker concurrency, dependencies, fan-out/fan-in, and failure escalation.

**Useful pattern.** Explicit dependency edges and separating reads from writes are strong orchestration primitives.

**Limits.** A single boolean `concurrencySafe` cannot encode resource scope, locks, credentials, rate limits, databases, transaction boundaries, or idempotency. Fixed retry counts should depend on failure class and cost.

**Evidence status.** README and `SKILL.md` directly read at the pinned commit. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

### `smart-memory-guard`

**Purpose.** Reduce memory drift and uncontrolled growth through admission rules, drift checks, typed memory, and pruning guidance.

**Useful pattern.** Verify current state before acting on remembered code/project facts; preserve `Why` and `How to apply` for feedback rules.

**Limits.** Blanket refusal to store some information even when explicitly requested is too absolute. The fixed 5 KB / seven-day thresholds are unvalidated heuristics, and the README's reported size reduction is anecdotal rather than a reproducible benchmark.

**Evidence status.** README and `SKILL.md` directly read at the pinned commit. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

## Deduplication result

- Repository identities completed: **10**
- Unique Git content trees: **7**
- Unique canonical skill bodies represented: **7**
- New canonical skill reports: **0**

Exact shared commit SHAs are used only as full-tree duplicate evidence; repository identity coverage remains recorded separately from canonical content coverage.
