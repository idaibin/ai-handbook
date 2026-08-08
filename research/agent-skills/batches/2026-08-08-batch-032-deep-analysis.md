# Agent Skills Deep Analysis — Batch 032

- Batch ID: `2026-08-08-batch-032`
- Stage: repository deep analysis
- Queue source: `sources/catalog/batches/agentskills-created-2026-04-01-deterministic.json`
- Repositories completed: **10**
- Unique Git commit trees directly re-read: **5**
- Direct `SKILL.md` bodies reviewed: **5**
- New canonical individual skill reports after content deduplication: **0**
- Runtime/build/test/eval execution: **not_executed**

## Completion gate

A repository is counted only after GitHub identity, exact observed star count, an exact Git revision, and actual repository content were verified. Every repository below matched an exact GitHub repository-search qualifier `repo:<owner/name> stars:0`, so the observed star count for all ten identities was **0** at review time. Latest repository commits were pinned through GitHub commit search. Shared commit SHAs are treated as deterministic full-tree duplicate evidence because the Git commit object binds the repository tree.

Five unique README/`SKILL.md` pairs were directly re-read at the pinned revisions. All five bodies were already content-reviewed in Batch 030 or Batch 031, so this batch records ten additional repository identities as reviewed without generating duplicate canonical skill reports.

## Repository results

| Repository | GitHub ID | Stars | Reviewed revision | Content-proven class | New canonical skill reports | Result |
|---|---:|---:|---|---|---:|---|
| `camCX/lightweight-explorer` | `1198535778` | 0 | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | exact full-tree duplicate of reviewed single skill | 0 | same tree as Batch 031 `lightweight-explorer` |
| `camCX/smart-memory-guard` | `1198535005` | 0 | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | exact full-tree duplicate of reviewed single skill | 0 | same tree as Batch 030 `smart-memory-guard` |
| `alexchenyu/task-concurrency-patterns` | `1198044270` | 0 | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | exact full-tree duplicate of reviewed single skill | 0 | same tree as Batch 030 `task-concurrency-patterns` |
| `wbxjj2008/smart-memory-guard` | `1198101399` | 0 | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | exact full-tree duplicate | 0 | same tree as `camCX/smart-memory-guard` |
| `wbxjj2008/task-concurrency-patterns` | `1198102830` | 0 | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | exact full-tree duplicate | 0 | same tree as `alexchenyu/task-concurrency-patterns` |
| `MandyDragon/worker-prompt-craft` | `1197911989` | 0 | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | exact full-tree duplicate of reviewed single skill | 0 | same tree as Batch 030 `worker-prompt-craft` |
| `k1w1f1sh/adversarial-verification` | `1198053996` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | exact full-tree duplicate of reviewed single skill | 0 | same tree as Batch 030 `adversarial-verification` |
| `wbxjj2008/adversarial-verification` | `1198101453` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | exact full-tree duplicate | 0 | same tree as `k1w1f1sh/adversarial-verification` |
| `wbxjj2008/lightweight-explorer` | `1198101362` | 0 | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | exact full-tree duplicate | 0 | same tree as `camCX/lightweight-explorer` |
| `ShawnSiao/lightweight-explorer` | `1198482434` | 0 | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | exact full-tree duplicate | 0 | same tree as `camCX/lightweight-explorer` |

## Structure and artifact inspection

All five unique revisions are small root-level document packages centered on `README.md` and `SKILL.md`. A repository code search across all ten identities for `scripts references eval package.json` returned no results. The five README/skill pairs likewise expose no repository-local script directory, reference bundle, package manifest, test harness, or eval suite. They are therefore document/policy skills at the reviewed revisions.

No runtime, build, command, test, or evaluation execution was performed; source review is not reported as runtime validation.

## Skill-group analysis

### `lightweight-explorer`

Revision `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` was re-read through `camCX/lightweight-explorer`; the same commit also backs `wbxjj2008/lightweight-explorer` and `ShawnSiao/lightweight-explorer`.

The skill enforces read-only exploration with `find`, `grep`, direct reads, parallel independent searches, and qualitative `quick`/`medium`/`thorough` depth levels. The read/write separation is useful for repository reconnaissance, but the statement that read-only work need not load all project rules remains too broad: repository instructions can govern confidentiality, allowed paths, generated files, or tool policy without involving writes. Examples using `head` can also silently truncate evidence. There is no eval defining measurable completion for the depth levels.

README installation points to `Arxchibobo/lightweight-explorer`, not any reviewed identity, so catalog repository identity and declared upstream provenance remain separate fields.

### `smart-memory-guard`

Revision `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` was re-read through `camCX/smart-memory-guard`; `wbxjj2008/smart-memory-guard` is the same full tree.

The skill's strongest ideas remain authority separation and drift verification before acting on remembered paths, symbols, API endpoints, or project state. Its weaknesses are fixed heuristics and over-broad refusal rules: the five-kilobyte pruning threshold and seven-day summary rule have no repository-local evidence, and the NOT-to-save list says some information should not be saved even when explicitly requested by the owner. The README's reported `13.4KB → 5.0KB` example is an anecdotal local claim, not a general eval.

### `task-concurrency-patterns`

Revision `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` was re-read through `alexchenyu/task-concurrency-patterns`; `wbxjj2008/task-concurrency-patterns` is identical.

Useful patterns include explicit read/write separation, dependency edges, fan-out/fan-in, and stopping workers when direction changes. The main risk is treating `concurrencySafe` as a static binary property without resource scope: two writes can be safe if disjoint, while two nominally read-only operations may still contend for rate limits or external resources. Fixed three-attempt escalation is also not calibrated to cost, side effects, or failure class.

### `worker-prompt-craft`

Revision `8f8a14fc8da0e687457516da3d9f79f8873e9061` was re-read through `MandyDragon/worker-prompt-craft`.

The core requirement that delegated prompts be self-contained and include exact paths, completion criteria, purpose, and verification requirements is useful. However, several examples assume the worker may commit, push, create a PR, or add reviewers; those are side-effecting capabilities and should require authority and environment checks rather than being copied as universal prompt requirements. The strong rule that implementation prompts always request commit/report-hash behavior is therefore context-dependent.

### `adversarial-verification`

Revision `909a2f70fc0de13aff1175c0b507ec24bf0b4815` was re-read through `k1w1f1sh/adversarial-verification`; `wbxjj2008/adversarial-verification` is identical.

The skill correctly separates execution evidence from code-reading confidence and requires observed command output, non-happy-path checks, and at least one adversarial probe. The document is still prompt-enforced only: the repository contains no harness or eval proving reliable compliance. Its directive to run commands whenever explanation is being written is over-generalized for analytical tasks, unavailable tooling, or operations requiring authorization. Personalized triggers such as `bobooo` also reduce portability.

## Cross-batch findings

1. **Ten repository identities collapse to five already-known content trees.** Commit-level deduplication prevents duplicate canonical skill reports while still recording repository-level completion.
2. **This cluster is highly mirrored.** Multiple owners publish byte-identical Git commit trees, while READMEs often declare `Arxchibobo/...` as the install source. Repository identity, content identity, and claimed upstream provenance must remain distinct catalog fields.
3. **No executable evidence surfaced.** The inspected trees contain no repository-local scripts, references, package manifest, tests, or eval suite; runtime claims must not be inferred from policy prose.
4. **Common design risk: universal rules without authority/resource gates.** Read-only exploration, memory admission, concurrency, delegation, and verification all contain useful heuristics but several rules become unsafe or inaccurate when generalized across environments.

## Validation status

- Repository identity: **verified for all 10**.
- Stars: exact observed value **0** verified for all 10 with exact GitHub repository-search qualifiers.
- Exact revision: **pinned for all 10**.
- README: **5 unique bodies directly re-read**.
- `SKILL.md`: **5 unique bodies directly re-read**.
- Scripts/references/evals/package manifests: **none surfaced** in repository search or reviewed docs.
- Runtime/build/tests/evals: **not_executed**.
