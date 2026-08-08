# Agent Skills Deep Analysis — Batch 035

- Batch ID: `2026-08-08-batch-035`
- Stage: repository deep analysis
- Queue source: `sources/catalog/batches/agentskills-created-2026-04-01-deterministic.json`
- Queue slice: entries 70–79 of the April 1 deterministic shard
- Repositories completed: **10**
- Repository `SKILL.md` reads: **10**
- Unique Git commit trees directly reviewed: **8**
- Unique `SKILL.md` bodies reviewed: **8**
- New canonical individual skill reports after content deduplication: **1**
- Runtime/build/test/eval execution: **not_executed**

## Completion gate

A repository is counted only after GitHub identity, exact observed star count, a pinned Git revision, and actual repository content were verified. All ten identities matched exact GitHub repository-search queries constrained with `stars:0`, so the observed star count for every repository was **0** during this review. Latest revisions were pinned through GitHub commit search. Root `SKILL.md` was directly fetched for all ten identities at the pinned revision. README bodies were directly reviewed for all eight unique Git commit trees.

Identical Git commit SHAs across repository identities are treated as deterministic full-tree duplicate evidence because the commit object binds the repository tree. Seven of the eight unique trees were already deeply reviewed in Batch 030 or Batch 031. `context-budget-analyzer` is the only content tree in this batch not previously represented in the AI-handbook deep-analysis corpus, so it receives one new canonical skill report.

## Repository results

| Repository | GitHub ID | Stars | Reviewed revision | Content-proven class | New canonical skill reports | Result |
|---|---:|---:|---|---|---:|---|
| `wbxjj2008/worker-prompt-craft` | `1198101932` | 0 | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `worker-prompt-craft` |
| `MandyDragon/task-concurrency-patterns` | `1197912503` | 0 | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `task-concurrency-patterns` |
| `MandyDragon/memory-type-system` | `1197912140` | 0 | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `memory-type-system` |
| `ajunlonglive/context-budget-analyzer` | `1198092186` | 0 | `7d969967a717beb52538d510d42ee45b9f2d65a8` | content-reviewed single document/policy skill | 1 | new canonical review in Batch 035 |
| `camCX/self-rationalization-guard` | `1198540077` | 0 | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 031 `self-rationalization-guard` |
| `alexchenyu/smart-memory-guard` | `1198042883` | 0 | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `smart-memory-guard` |
| `ShawnSiao/adversarial-verification` | `1198481081` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `adversarial-verification` |
| `YTT-CSH/task-concurrency-patterns` | `1198155959` | 0 | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | exact full-tree duplicate | 0 | same tree as `MandyDragon/task-concurrency-patterns` |
| `ajunlonglive/coordinator-orchestrator` | `1198083717` | 0 | `a6d0311d279b32497a9c952061fafb798309b4e3` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `coordinator-orchestrator` |
| `MandyDragon/self-rationalization-guard` | `1197912299` | 0 | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact full-tree duplicate | 0 | same tree as `camCX/self-rationalization-guard` |

## Structure and artifact inspection

All eight unique reviewed revisions are small document/policy skill packages centered on root `README.md` and root `SKILL.md`. Repository code search across all ten identities returned no matches for `scripts`, `references`, `eval`, or `package.json`. The reviewed docs expose no repository-local executable harness, package manifest, test suite, reference bundle, or evaluation suite.

This batch therefore records content review only. No runtime, build, test, deployment, token-counting, or evaluation success is inferred from prompt/document content.

## Revalidated skill groups

### `worker-prompt-craft`

Revision `8f8a14fc8da0e687457516da3d9f79f8873e9061` was directly re-read through `wbxjj2008/worker-prompt-craft`. It requires self-contained worker prompts with exact paths, completion criteria, purpose statements, and verification expectations.

The delegation-contract pattern remains useful. The main risk remains that Git examples normalize branch creation, commits, pushes, PR creation, and reviewer changes as normal completion steps without a separate authorization gate for external side effects.

### `task-concurrency-patterns`

Revision `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` was directly re-read through both `MandyDragon/task-concurrency-patterns` and `YTT-CSH/task-concurrency-patterns`; both expose the same commit tree. It defines read/write separation, a three-state task lifecycle, explicit `blocks`/`blockedBy` dependency edges, fan-out/fan-in patterns, worker stopping, and fixed three-attempt escalation.

Explicit dependency modeling is valuable, but the binary `concurrencySafe` model is too coarse. Real safety depends on resource scope, locks, rate limits, credentials, external side effects, transaction boundaries, and idempotency. Fixed retry counts are not calibrated by failure class or cost.

### `memory-type-system`

Revision `d3805f3e5a576afd0c55e2de9cddb78511a30c95` was directly re-read through `MandyDragon/memory-type-system`. It formalizes `user`, `feedback`, `project`, and `reference` memory records, per-item frontmatter, drift checks, and a bounded `MEMORY.md` index.

The index-versus-record separation remains structurally useful. Fixed 200-line / 25 KB limits still lack retrieval-quality evidence, and blanket NOT-to-save rules need an explicit user-authorized exception model.

### `self-rationalization-guard`

Revision `3df614e3ae87d80b3be338d247a2fc2488dc22a2` was directly re-read through both `camCX/self-rationalization-guard` and `MandyDragon/self-rationalization-guard`; both expose the same commit tree. It lists execution, communication, quality, and delegation rationalizations and maps them to counter-actions.

The anti-handwaving intent remains useful, especially distinguishing code reading from execution evidence. Universal inversion rules such as always running commands, always doing the hardest task first, handling every unlikely edge case, and always writing docs immediately can conflict with authorization, risk, expected value, and scope.

### `smart-memory-guard`

Revision `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` was directly re-read through `alexchenyu/smart-memory-guard`. It combines four memory types, a NOT-to-save list, drift verification, `Why`/`How to apply` feedback metadata, and pruning heuristics.

Current-state verification before acting on remembered paths, functions, endpoints, or project status remains strong. Risks remain around blanket rejection of explicitly requested memories, fixed 5 KB / seven-day thresholds without repository-local evaluation, and the README's `13.4KB → 5.0KB` example being an anecdotal claim rather than a reproducible benchmark.

### `adversarial-verification`

Revision `909a2f70fc0de13aff1175c0b507ec24bf0b4815` was directly re-read through `ShawnSiao/adversarial-verification`. It requires actual command execution, observed output, non-happy-path checks, at least one adversarial probe, and an explicit final verdict.

The distinction between source inspection and runtime proof remains valuable. The repository itself provides no harness or eval proving policy compliance. Unconditional command-running guidance is too broad for analysis-only work, unavailable tools, or operations requiring authorization.

### `coordinator-orchestrator`

Revision `a6d0311d279b32497a9c952061fafb798309b4e3` was directly re-read through `ajunlonglive/coordinator-orchestrator`. It defines research → synthesis → implementation → verification, keeps synthesis with the coordinator, and distinguishes Continue from Spawn based on context overlap.

The synthesis requirement and fresh-agent verification pattern remain useful. The universal claim that independent tasks should always run in parallel is too broad because logically independent tasks can still contend for files, databases, rate limits, credentials, deployment targets, or other shared resources.

## New canonical review: `context-budget-analyzer`

Revision `7d969967a717beb52538d510d42ee45b9f2d65a8` was directly reviewed from `ajunlonglive/context-budget-analyzer`. The skill proposes a manual context-budget diagnosis model with six message categories, per-tool request/result accounting, duplicate file-read detection, optimization heuristics, and action thresholds at 50%, 75%, and 90% of the context limit.

### Useful ideas

- Separating human, assistant, tool-request, tool-result, attachment, and system/other cost makes context pressure easier to reason about than a single total.
- Tool-result volume and repeated file reads are legitimate candidates for investigation in long tool-heavy sessions.
- Recommending narrower retrieval rather than repeated full-file reads is a useful efficiency principle when state has not changed.
- The skill turns context pressure into an explicit resource-management problem rather than relying only on intuition.

### Material limitations

1. **No actual token counter is implemented.** The repository provides templates containing `XXX tokens`, but no tokenizer, host integration, trace parser, or message-accounting script. Exact percentages therefore cannot be produced by this repository alone.
2. **Observable context is incomplete on many hosts.** Hidden system messages, tool schemas, cached prefixes, model-specific tokenization, compression behavior, and provider accounting can make local manual estimates diverge from real context consumption.
3. **Repeated reads are not automatically waste.** A re-read can be required after file mutation, after compaction, when the earlier read was partial, or when verification deliberately seeks fresh state. A safe cache policy needs invalidation by revision/hash/state change.
4. **The 50/75/90% thresholds are unvalidated heuristics.** No repository-local eval relates those thresholds to truncation risk, answer quality, or model behavior.
5. **Output truncation can remove evidence.** Advising `head -N` or `tail -N` as a generic fix can hide the decisive error lines. Narrow queries and structured filters are safer than blind truncation when correctness matters.
6. **Attachment-removal advice can destroy required evidence.** Image or document blocks may be the task input itself; compaction must preserve task-critical information.
7. **The README's qualitative claims are not benchmarked.** Statements such as duplicate reads being a major waste source and FileRead results often being largest are plausible hypotheses, not demonstrated repository-local measurements.

### Verdict

Useful as a **diagnostic checklist**, not as an analyzer implementation. For production use it needs host-specific accounting, content-version-aware read caching, preservation rules for task-critical evidence, and evals that measure token savings against correctness/recall regressions.

## Cross-batch findings

1. **Mirror density remains high.** Nine of ten repository identities in this slice map to seven previously reviewed skill-content trees; only `context-budget-analyzer` adds new canonical content.
2. **Two duplicate pairs are visible inside this batch.** `task-concurrency-patterns` and `self-rationalization-guard` each have two repository identities sharing identical commit SHAs.
3. **Repository coverage and unique content coverage must remain separate metrics.** This batch adds ten verified repository identities but only one new canonical skill body.
4. **Provenance remains separate from repository identity.** The reviewed READMEs instruct installation from `Arxchibobo/...` while the indexed owners are `wbxjj2008`, `MandyDragon`, `ajunlonglive`, `camCX`, `alexchenyu`, `ShawnSiao`, and `YTT-CSH`. That is self-declared upstream provenance, not proof that the indexed repositories are canonical sources.
5. **Several skills encode universal rules where conditional gates are required.** Parallelism, memory retention, command execution, retries, Git side effects, output truncation, and context compaction all need authority-, state-, risk-, and resource-aware conditions.

## Validation status

- Repository identity: **verified for all 10**.
- Stars: exact observed value **0** verified for all 10 with GitHub repository-search `stars:0` constraints.
- Exact revision: **pinned for all 10**.
- `SKILL.md`: **directly fetched for all 10 repository identities**.
- README: **8 unique bodies directly reviewed**, covering every unique commit tree in this batch.
- Scripts/references/evals/package manifests: **none surfaced** in repository code search or reviewed docs.
- Runtime/build/tests/evals: **not_executed / not_verified**.
