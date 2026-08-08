# Agent Skills Individual Reports — Batch 037

Batch 037 completed ten repository identities and mapped them to six already-reviewed canonical skill bodies. No new canonical content body was introduced in this batch.

## Repository → skill mapping

| Repository | Skill | Reviewed revision | Canonical status |
|---|---|---|---|
| `4ccsds/smart-memory-guard` | `smart-memory-guard` | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | existing canonical review |
| `drcaonet/self-rationalization-guard` | `self-rationalization-guard` | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | existing canonical review |
| `howknows/adversarial-verification` | `adversarial-verification` | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | existing canonical review |
| `howknows/self-rationalization-guard` | `self-rationalization-guard` | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact-tree duplicate |
| `4ccsds/worker-prompt-craft` | `worker-prompt-craft` | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | existing canonical review |
| `4ccsds/coordinator-orchestrator` | `coordinator-orchestrator` | `a6d0311d279b32497a9c952061fafb798309b4e3` | existing canonical review |
| `4ccsds/lightweight-explorer` | `lightweight-explorer` | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | existing canonical review |
| `4ccsds/self-rationalization-guard` | `self-rationalization-guard` | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact-tree duplicate |
| `howknows/worker-prompt-craft` | `worker-prompt-craft` | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | exact-tree duplicate |
| `drcaonet/coordinator-orchestrator` | `coordinator-orchestrator` | `a6d0311d279b32497a9c952061fafb798309b4e3` | exact-tree duplicate |

## Individual skill reports

### `smart-memory-guard`

**Purpose.** Reduce memory drift and uncontrolled growth through typed admission, drift checks, and pruning guidance.

**Useful pattern.** Verify current state before acting on remembered code/project facts; preserve `Why` and `How to apply` for feedback rules.

**Limits.** Blanket refusal to retain some information even when explicitly requested is too absolute. The fixed 5 KB and seven-day thresholds are unvalidated heuristics, and the README's reported size reduction is anecdotal rather than a reproducible benchmark.

**Evidence status.** README and `SKILL.md` directly read at the pinned commit from `4ccsds/smart-memory-guard`. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

### `self-rationalization-guard`

**Purpose.** Prompt-level guard against declaring completion from appearance, assumption, or repeated rationalization.

**Useful pattern.** Distinguish execution evidence from source inspection and require a completion self-check.

**Limits.** “Always do the opposite of the shortcut” is not a safe universal policy. Command execution, exhaustive edge-case handling, task ordering, and documentation timing must remain conditional on scope, authorization, cost, and risk.

**Repository identities.** `drcaonet/self-rationalization-guard`, `howknows/self-rationalization-guard`, and `4ccsds/self-rationalization-guard` expose the same reviewed Git commit tree.

**Evidence status.** README and `SKILL.md` were directly read from all three identities at the pinned revision. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

### `adversarial-verification`

**Purpose.** Turn verification into an attempt to falsify an implementation rather than merely confirm the happy path.

**Useful pattern.** Record observed evidence and include non-happy-path/adversarial checks appropriate to the change.

**Limits.** The repository is prompt-only and supplies no harness proving that an agent follows the procedure. Mandatory command-running is too broad for analysis-only work, unavailable tools, or actions requiring additional authorization.

**Evidence status.** README and `SKILL.md` directly read at the pinned commit from `howknows/adversarial-verification`. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

### `worker-prompt-craft`

**Purpose.** Make worker/sub-agent prompts self-contained with exact paths, purpose, completion criteria, and verification expectations.

**Useful pattern.** Treat delegation as an explicit contract so a worker does not depend on hidden coordinator context.

**Limits.** Examples that include branch creation, commits, pushes, PR creation, or reviewer changes should not make those external side effects implicit. They need a separate authorization gate.

**Repository identities.** `4ccsds/worker-prompt-craft` and `howknows/worker-prompt-craft` expose the same reviewed Git commit tree.

**Evidence status.** README and `SKILL.md` were directly read from both identities. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

### `coordinator-orchestrator`

**Purpose.** Separate multi-agent work into research, coordinator synthesis, worker implementation, and verification.

**Useful pattern.** Keep synthesis in the coordinator instead of forwarding raw worker findings, and choose Continue versus Spawn based on context overlap and the need for a fresh perspective.

**Limits.** “Always parallelize independent work” is too broad because shared files, databases, locks, credentials, rate limits, deployment targets, and external side effects may couple tasks. The fixed retry/escalation sequence is also heuristic rather than evidence-based.

**Repository identities.** `4ccsds/coordinator-orchestrator` and `drcaonet/coordinator-orchestrator` expose the same reviewed Git commit tree.

**Evidence status.** README and `SKILL.md` were directly read from both identities. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

### `lightweight-explorer`

**Purpose.** Read-only codebase exploration with explicit search-depth modes and concise evidence output.

**Useful pattern.** Separate exploration from mutation and vary search depth (`quick` / `medium` / `thorough`) instead of loading everything by default.

**Limits.** Read-only status does not make repository rules irrelevant. Search-output truncation can hide decisive evidence, and mandatory parallel search is too absolute when rate limits or shared resources matter.

**Evidence status.** README and `SKILL.md` directly read at the pinned commit from `4ccsds/lightweight-explorer`. No repository-local script, reference bundle, package manifest, or eval surfaced. Runtime behavior not verified.

## Deduplication result

- Repository identities completed: **10**
- Unique Git content trees: **6**
- Unique canonical skill bodies represented: **6**
- New canonical skill reports: **0**

Exact shared commit SHAs are used only as full-tree duplicate evidence; repository identity coverage remains recorded separately from canonical content coverage.
