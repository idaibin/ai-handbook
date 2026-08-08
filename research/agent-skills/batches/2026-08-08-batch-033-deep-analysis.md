# Agent Skills Deep Analysis — Batch 033

- Batch ID: `2026-08-08-batch-033`
- Stage: repository deep analysis
- Queue source: `sources/catalog/batches/agentskills-created-2026-04-01-deterministic.json`
- Repositories completed: **10**
- Unique Git commit trees directly reviewed: **8**
- Repository `SKILL.md` reads: **10**
- Unique `SKILL.md` bodies reviewed: **8**
- New canonical individual skill reports after content deduplication: **1**
- Runtime/build/test/eval execution: **not_executed**

## Completion gate

A repository is counted only after GitHub identity, exact observed star count, a pinned Git revision, and actual repository content were verified. All ten repositories matched exact GitHub repository-search queries constrained with `stars:0`, so the observed star count for every identity was **0** at review time. Latest revisions were pinned through GitHub commit search. Each repository's root `SKILL.md` was directly fetched at the pinned revision; README bodies were directly reviewed for each of the eight unique commit trees.

Shared Git commit SHAs are treated as deterministic full-tree duplicate evidence because the Git commit object binds a repository tree. Seven of the eight unique trees are already represented by canonical reviews from Batch 030 or Batch 031. `background-memory-extractor` is new content and receives the only new canonical skill report in this batch.

## Repository results

| Repository | GitHub ID | Stars | Reviewed revision | Content-proven class | New canonical skill reports | Result |
|---|---:|---:|---|---|---:|---|
| `camCX/task-concurrency-patterns` | `1198540612` | 0 | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `task-concurrency-patterns` |
| `ShawnSiao/smart-memory-guard` | `1198481215` | 0 | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `smart-memory-guard` |
| `ajunlonglive/memory-type-system` | `1198085103` | 0 | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `memory-type-system` |
| `k1w1f1sh/memory-type-system` | `1198055223` | 0 | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | exact full-tree duplicate | 0 | same tree as `ajunlonglive/memory-type-system` |
| `MandyDragon/adversarial-verification` | `1197911298` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `adversarial-verification` |
| `YTT-CSH/coordinator-orchestrator` | `1198154524` | 0 | `a6d0311d279b32497a9c952061fafb798309b4e3` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `coordinator-orchestrator` |
| `ajunlonglive/background-memory-extractor` | `1198087351` | 0 | `e1fc9103f5714eca3b203d13bbc1ce1130a7e892` | document-only single skill | 1 | new canonical content review |
| `k1w1f1sh/worker-prompt-craft` | `1198055067` | 0 | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `worker-prompt-craft` |
| `MandyDragon/coordinator-orchestrator` | `1197911713` | 0 | `a6d0311d279b32497a9c952061fafb798309b4e3` | exact full-tree duplicate | 0 | same tree as `YTT-CSH/coordinator-orchestrator` |
| `k1w1f1sh/self-rationalization-guard` | `1198055381` | 0 | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 031 `self-rationalization-guard` |

## Structure and artifact inspection

The eight unique revisions are small root-level document packages centered on `README.md` and `SKILL.md`. Repository code search across all ten identities for `scripts references eval package.json` returned no results. The reviewed README/skill bodies do not expose a repository-local executable harness, script directory, reference bundle, package manifest, test suite, or eval suite.

Therefore these repositories are analyzed as document/policy skills at the pinned revisions. No runtime, build, test, hook, or evaluation success is inferred from prompt/document content.

## Revalidated skill groups

### `task-concurrency-patterns`

Revision `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` was directly re-read through `camCX/task-concurrency-patterns`. The skill defines read/write separation, a three-state task lifecycle, explicit `blocks`/`blockedBy` edges, fan-out/fan-in patterns, worker stopping, and fixed three-attempt escalation.

The useful part remains explicit dependency modeling and avoiding conflicting writes. The main weakness remains the binary `concurrencySafe` model: safety depends on resource scope, locks, rate limits, and side effects, not only whether an operation is described as read or write. Fixed retry counts are also not calibrated by failure class or external cost.

### `smart-memory-guard`

Revision `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` was directly re-read through `ShawnSiao/smart-memory-guard`. It combines four memory types, a NOT-to-save list, drift verification, `Why`/`How to apply` feedback metadata, and pruning heuristics.

Current-state verification before acting on remembered paths, functions, endpoints, or project status remains strong. However, the rule that six categories must not be stored even when the owner explicitly requests it is over-broad, and the 5 KB / seven-day thresholds are policy constants without repository-local eval evidence. README's `13.4KB → 5.0KB` example is an anecdotal claim rather than a reproducible benchmark.

### `memory-type-system`

Revision `d3805f3e5a576afd0c55e2de9cddb78511a30c95` was directly fetched from both `ajunlonglive/memory-type-system` and `k1w1f1sh/memory-type-system`; both identities expose the same commit tree. The skill formalizes `user`, `feedback`, `project`, and `reference` memories, per-memory frontmatter, drift checks, and a bounded `MEMORY.md` index.

The separation between an index and per-item memory records is structurally useful. Risks remain around fixed 200-line / 25 KB limits without measured retrieval-quality evidence and the blanket claim that code/Git/debug information should never be remembered even when a user intentionally wants an exception or a non-code fact is not recoverable from the repository.

### `adversarial-verification`

Revision `909a2f70fc0de13aff1175c0b507ec24bf0b4815` was directly re-read through `MandyDragon/adversarial-verification`. It requires command execution, observed output, non-happy-path checks, an adversarial probe, and an explicit verdict.

The distinction between source inspection and runtime proof remains valuable. The repository itself still contains no harness or eval proving that an agent follows the policy reliably. The unconditional heuristic to run commands whenever explanation is being written is too broad for analysis-only work, unavailable tools, or side-effecting operations that require authorization.

### `coordinator-orchestrator`

Revision `a6d0311d279b32497a9c952061fafb798309b4e3` was fetched through both `YTT-CSH/coordinator-orchestrator` and `MandyDragon/coordinator-orchestrator`. It defines research → synthesis → implementation → verification, emphasizes synthesis by the coordinator, and distinguishes Continue from Spawn based on context overlap.

The synthesis requirement and fresh-agent verification pattern are useful. The universal claim that independent tasks should always start in parallel needs resource and side-effect gates; independent tasks can still contend for shared rate limits, databases, files, credentials, or external systems.

### `worker-prompt-craft`

Revision `8f8a14fc8da0e687457516da3d9f79f8873e9061` was directly re-read through `k1w1f1sh/worker-prompt-craft`. It requires self-contained worker prompts with exact paths, completion criteria, purpose, and verification expectations.

This is useful delegation-contract guidance. Several examples normalize commits, pushes, PR creation, and reviewer changes as prompt content, so production use needs an explicit authority gate separating normal implementation requirements from external side effects.

### `self-rationalization-guard`

Revision `3df614e3ae87d80b3be338d247a2fc2488dc22a2` was directly re-read through `k1w1f1sh/self-rationalization-guard`. It lists execution, communication, quality, and delegation rationalizations and maps them to counter-actions.

The anti-handwaving intent is useful, especially the separation of code reading from execution evidence. Several counter-rules are over-generalized: "directly run commands", "do the hardest thing first", "handle every unlikely edge case", and "write docs now" can increase risk or waste when authorization, expected value, or task scope says otherwise. The skill needs a risk/authority/value gate rather than universal inversion of every shortcut impulse.

## New canonical skill: `background-memory-extractor`

Revision `e1fc9103f5714eca3b203d13bbc1ce1130a7e892` was directly reviewed through `ajunlonglive/background-memory-extractor`.

### What it defines

The skill proposes automatic memory extraction after every conversation turn, duplicate prevention, a two-phase "parallel read then parallel write" procedure, four-type memory classification, and permission limits that allow broad reads plus writes only to `MEMORY.md` and a memory directory.

### Strong ideas

- Separates memory extraction from explicit user phrases such as "remember this", reducing reliance on a single trigger phrase.
- Requires deduplication and stale-memory updates rather than append-only accumulation.
- Reuses typed memory categories, making extracted facts easier to route and retrieve.
- Attempts to isolate writes to memory artifacts rather than project code.

### Material risks

1. **The claimed background trigger is not implemented by this repository.** A Markdown skill cannot by itself guarantee execution after a final response. The repository contains no lifecycle hook, daemon, script, package, or host integration. Automatic after-turn behavior therefore remains a host-level requirement, not a verified capability of this repository.
2. **Parallel writes can violate index/content consistency.** Updating `MEMORY.md` in parallel with creating or changing referenced memory files can expose an index entry before its target exists, lose concurrent edits, or produce conflicting updates. A safer contract is write/validate content records first, then update the index atomically or with compare-and-swap semantics.
3. **"Read any file" is too broad for memory extraction.** It can expose secrets or unrelated sensitive material to a retention process. Extraction needs data-minimization and allowed-scope rules rather than unrestricted reads.
4. **Automatic extraction after every turn can over-retain information.** The document has no consent, privacy, retention, or confidence threshold beyond a short NOT-to-save list. A production system needs an explicit memory policy and deletion/override authority.
5. **The skip-if-memory-was-already-written rule is lossy.** One proactive memory write does not prove that all other relevant facts from the turn were captured.
6. **No eval exists for extraction quality.** There are no precision/recall cases, duplicate-rate tests, stale-update tests, or privacy/false-positive evaluations.

### Provenance boundary

README and `SKILL.md` describe the design as inspired by reverse-engineered Claude Code `extractMemories` behavior and install from `Arxchibobo/background-memory-extractor`, not the indexed `ajunlonglive` identity. This is a self-declared provenance claim, not independently verified upstream equivalence. Catalog fields should continue to separate repository identity, exact content identity, and claimed upstream source.

## Cross-batch findings

1. **The mirror cluster continues.** Nine of ten repository identities map to seven already-reviewed content trees; repository-level coverage and unique skill-content coverage must remain separate metrics.
2. **Commit-level deduplication is doing useful work.** Two repositories in this batch share the memory-type tree and two share the coordinator tree, while other identities reproduce trees seen in earlier batches.
3. **The only new concept is lifecycle-dependent.** `background-memory-extractor` is not merely prompt guidance: its central promise requires host orchestration after a final response, but the repository provides no implementation for that lifecycle integration.
4. **Common design gap is missing authority/resource policy.** Parallelism, memory access, external side effects, retries, verification commands, and automatic retention are all described with universal rules that need task-specific gates.
5. **Provenance remains distinct from identity.** Multiple READMEs install from `Arxchibobo/...` while the indexed repositories belong to other owners; cataloging must not collapse these without verified lineage.

## Validation status

- Repository identity: **verified for all 10**.
- Stars: exact observed value **0** verified for all 10 with GitHub repository-search `stars:0` constraints.
- Exact revision: **pinned for all 10**.
- `SKILL.md`: **directly fetched for all 10 repository identities**.
- README: **8 unique bodies directly reviewed**, covering every unique commit tree in this batch.
- Scripts/references/evals/package manifests: **none surfaced** in repository search or reviewed docs.
- Runtime/build/tests/evals/host lifecycle hook: **not_executed / not_verified**.
