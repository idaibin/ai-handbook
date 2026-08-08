# Agent Skills Deep Analysis — Batch 036

- Batch ID: `2026-08-08-batch-036`
- Stage: repository deep analysis
- Queue sources:
  - `sources/catalog/batches/agentskills-created-2026-04-01-deterministic.json`
  - `sources/catalog/batches/agentskills-created-2026-04-02-deterministic.json`
- Repositories completed: **10**
- Repository `SKILL.md` reads: **10**
- Repository README reads: **10**
- Unique Git commit trees directly reviewed: **7**
- New canonical individual skill reports after content deduplication: **0**
- Runtime/build/test/eval execution: **not_executed**

## Completion gate

A repository is counted only after GitHub identity, exact observed star count, a pinned Git revision, and actual repository content were verified. All ten identities matched exact GitHub repository-search queries constrained with `stars:0`, so the observed star count for every completed repository was **0** during this review. Latest revisions were pinned through GitHub commit search. Root `SKILL.md` and README were directly fetched from each repository identity at its pinned revision.

Repository code search across all ten identities returned no matches for `scripts`, `references`, `eval`, or `package.json`. These revisions are therefore treated as document/policy skill packages, not as repositories with a local executable harness or evaluation suite. Runtime/build/test/eval success is not inferred from their prose.

The queue contains other repository entries between the April 1 and April 2 selections used here. Entries that were not suitable for this content-review pass remain **pending** and are **not counted complete**; this batch continued with qualified document-skill identities so that ten repositories could be completed without converting metadata-only or unsuitable entries into false completions.

## Repository results

| Repository | GitHub ID | Stars | Reviewed revision | Content-proven class | New canonical reports | Result |
|---|---:|---:|---|---|---:|---|
| `ShawnSiao/self-rationalization-guard` | `1198484362` | 0 | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `self-rationalization-guard` review |
| `ajunlonglive/adversarial-verification` | `1198092610` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `adversarial-verification` review |
| `YTT-CSH/lightweight-explorer` | `1198141106` | 0 | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `lightweight-explorer` review |
| `camCX/worker-prompt-craft` | `1198538019` | 0 | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `worker-prompt-craft` review |
| `drcaonet/lightweight-explorer` | `1198989891` | 0 | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | exact full-tree duplicate | 0 | same tree as `YTT-CSH/lightweight-explorer` |
| `howknows/memory-type-system` | `1199422616` | 0 | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `memory-type-system` review |
| `4ccsds/memory-type-system` | `1199651939` | 0 | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | exact full-tree duplicate | 0 | same tree as `howknows/memory-type-system` |
| `howknows/lightweight-explorer` | `1199421879` | 0 | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | exact full-tree duplicate | 0 | same tree as other `lightweight-explorer` identities |
| `drcaonet/task-concurrency-patterns` | `1198990180` | 0 | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `task-concurrency-patterns` review |
| `drcaonet/smart-memory-guard` | `1198989830` | 0 | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `smart-memory-guard` review |

## Content review

### `self-rationalization-guard`

The skill is a prompt-level anti-shortcut checklist: distinguish source inspection from execution evidence, notice repeated rationalizations, and force an explicit completion check. The useful core is preventing an agent from declaring success based only on appearance or narration.

Its universal inversion rules are too broad. “Run commands instead of explaining”, “do the hardest task first”, handle every unlikely edge case, and write documentation immediately can conflict with authorization, scope, risk, or expected value. These should be conditional gates, not unconditional laws.

### `adversarial-verification`

The skill distinguishes verification from code reading and asks for observed evidence, non-happy-path checks, and adversarial probes. That discipline is useful for code-change validation.

The repository itself contains no harness or eval proving compliance. Mandatory command execution is also too broad for analysis-only tasks, unavailable tools, or actions requiring user authorization. It should define risk-matched verification levels rather than equating every valid verification with command execution.

### `lightweight-explorer`

The read-only exploration boundary, search-depth modes, and concise evidence-oriented output are useful. However, the claim that read-only work does not need full project rules is unsafe as a general rule: repository rules may govern secrets, generated files, restricted paths, or required evidence. Generic use of output truncation can also hide the decisive match, and mandatory parallel search can conflict with rate limits or shared-resource constraints.

### `worker-prompt-craft`

The strongest pattern is making delegated prompts self-contained: exact paths, completion criteria, purpose, and verification expectations. This reduces context-loss failures between coordinator and worker.

The Git examples normalize branch creation, commits, pushes, PR creation, and reviewer changes as routine completion steps. Those are external side effects and should be separated behind explicit authorization rather than embedded in a generic worker-prompt template.

### `memory-type-system`

The four-type memory taxonomy (`user`, `feedback`, `project`, `reference`), per-record frontmatter, index-versus-record separation, and drift verification are structurally useful. Treating remembered paths and project state as claims to re-check is especially strong.

The absolute NOT-to-save rules can conflict with explicit user-authorized retention. Fixed limits such as 200 lines / 25 KB are heuristics without repository-local retrieval-quality evidence. The README also attributes the design to analysis of another system; that provenance claim was not independently verified in this batch.

### `task-concurrency-patterns`

Explicit `blocks` / `blockedBy` dependencies, read/write separation, fan-out/fan-in, and stopping work that has gone in the wrong direction are useful orchestration ideas.

A binary `concurrencySafe` flag is too coarse for real systems because safety also depends on file regions, locks, databases, credentials, rate limits, deployment targets, idempotency, and external side effects. The fixed three-attempt escalation policy is likewise not calibrated to failure class or cost.

### `smart-memory-guard`

The strongest part is drift checking before acting on remembered paths, symbols, endpoints, or project state. Feedback records that preserve both `Why` and `How to apply` also improve later interpretation.

The rule that some information must never be stored even when explicitly requested is too absolute. The 5 KB pruning threshold and seven-day summary rule are unvalidated heuristics. The README's `13.4KB → 5.0KB` / 62% reduction is an anecdotal repository claim, not a reproducible benchmark in this repository.

## Cross-repository findings

1. **Mirror density is extremely high.** Ten repository identities collapse to seven content trees, all seven already represented in prior canonical reviews.
2. **Repository coverage and unique-content coverage must stay separate.** This batch legitimately adds ten content-verified repository identities but adds zero new canonical skill bodies.
3. **Provenance differs from indexed ownership.** Multiple READMEs point installation/source attribution at another owner while the indexed repositories belong to different owners. That is self-declared provenance, not proof of canonical upstream status.
4. **The packages are policy documents, not implementations.** No repository-local scripts, references, evals, or package manifests surfaced in code search for this batch.
5. **Several rules need authority- and risk-aware conditions.** Command execution, parallelism, retries, memory retention, Git side effects, and truncation should be conditional rather than universal.

## Validation status

- Repository identity: **verified for all 10**.
- Stars: exact observed value **0** verified for all 10.
- Exact revision: **pinned for all 10**.
- `SKILL.md`: **directly fetched for all 10 repository identities**.
- README: **directly fetched for all 10 repository identities**.
- Unique content trees: **7**.
- Scripts/references/evals/package manifests: **none surfaced** in repository code search.
- Runtime/build/tests/evals: **not_executed / not_verified**.
