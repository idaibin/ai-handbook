# Agent Skills Deep Analysis — Batch 031

- Batch ID: `2026-08-08-batch-031`
- Stage: repository deep analysis
- Queue source: `sources/catalog/batches/agentskills-created-2026-04-01-deterministic.json`
- Repositories completed: **10**
- Direct `SKILL.md` bodies reviewed: **6**
- New individual skill reports added after content deduplication: **3**
- Runtime/build/test/eval execution: **not_executed**

## Completion gate

A repository is counted only after its GitHub identity and exact point-in-time star count were verified, an exact Git revision was pinned, and actual repository contents were read. For every repository in this batch, GitHub repository search with the exact qualifier `repo:<owner/name> stars:0` matched the intended repository, verifying an observed star count of zero at review time.

The batch contains six unique Git commit SHAs across ten repository identities. Because a Git commit is content-addressed and binds the complete tree, repositories resolving to the same commit are treated as deterministic full-tree duplicates. Six unique README/SKILL pairs were directly read at their pinned revisions. Three of those six revisions (`memory-type-system`, `coordinator-orchestrator`, `smart-memory-guard`) had already been fully reviewed in Batch 030, so this batch maps the new repository identities to the existing content reports rather than creating duplicate skill reports.

## Repository results

| Repository | ID | Stars | Reviewed revision | Content-proven class | New skill reports | Result |
|---|---:|---:|---|---|---:|---|
| `ShawnSiao/memory-type-system` | `1198483944` | 0 | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | exact full-tree duplicate of previously reviewed skill | 0 | same tree as Batch 030 `camCX/memory-type-system` |
| `alexchenyu/memory-type-system` | `1198043885` | 0 | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | exact full-tree duplicate of previously reviewed skill | 0 | same tree as Batch 030 `camCX/memory-type-system` |
| `alexchenyu/lightweight-explorer` | `1198043156` | 0 | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | document-only single skill | 1 | read-only repository exploration/search policy |
| `k1w1f1sh/lightweight-explorer` | `1198054716` | 0 | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | exact full-tree duplicate | 0 | same tree as `alexchenyu/lightweight-explorer` |
| `YTT-CSH/self-rationalization-guard` | `1198155685` | 0 | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | document-only single skill | 1 | anti-shortcut / execution-discipline policy |
| `ajunlonglive/lightweight-explorer` | `1198090423` | 0 | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | exact full-tree duplicate | 0 | same tree as `alexchenyu/lightweight-explorer` |
| `wbxjj2008/coordinator-orchestrator` | `1198101704` | 0 | `a6d0311d279b32497a9c952061fafb798309b4e3` | exact full-tree duplicate of previously reviewed skill | 0 | same tree as Batch 030 `alexchenyu/coordinator-orchestrator` |
| `wbxjj2008/self-rationalization-guard` | `1198102450` | 0 | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact full-tree duplicate | 0 | same tree as `YTT-CSH/self-rationalization-guard` |
| `ajunlonglive/context-compressor` | `1198091098` | 0 | `b8b5f37cdf027df2cb85f5ad9838701c90dd9c8e` | document-only single skill | 1 | nine-section conversation-compaction policy |
| `YTT-CSH/smart-memory-guard` | `1198119954` | 0 | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | exact full-tree duplicate of previously reviewed skill | 0 | same tree as Batch 030 `ajunlonglive/smart-memory-guard` |

## Structure and artifact inspection

All six unique revisions are very small prompt/document packages centered on a root `README.md` and root `SKILL.md`. Repository code search across all ten identities returned no matches for `scripts`, `references`, `eval`, or `package.json`. The reviewed READMEs and skill bodies likewise identify no repository-local executable helpers, reference directories, test harnesses, or evaluation suites. These revisions are therefore treated as document/policy skills rather than script-backed skills.

No runtime, build, command, test, or evaluation execution was performed. Source/document inspection is not promoted to runtime success.

## 1–2. `memory-type-system` duplicate identities

`ShawnSiao/memory-type-system` and `alexchenyu/memory-type-system` both resolve to `d3805f3e5a576afd0c55e2de9cddb78511a30c95`, the same full-tree revision already reviewed for `camCX/memory-type-system` in Batch 030. The README and `SKILL.md` were re-read in this batch and confirm the same four-type memory taxonomy (`user`, `feedback`, `project`, `reference`), per-memory frontmatter, drift checks, and `MEMORY.md` index limits.

No new skill report is generated because the content is byte-addressed by the identical commit. The previously recorded assessment still applies: the index/body split is a useful progressive-disclosure pattern, while fixed size limits and overlapping categories remain heuristic design choices rather than measured retrieval guarantees.

## 3–4 and 6. `lightweight-explorer` exact duplicate group

`alexchenyu/lightweight-explorer`, `k1w1f1sh/lightweight-explorer`, and `ajunlonglive/lightweight-explorer` all resolve to `ba11d7eaab78fafd3982d36bff78c0f3fba633b1`. The skill defines a read-only exploration mode using `find`, `grep`, direct file reads, parallel independent searches, and `quick` / `medium` / `thorough` depth labels.

### Strengths

The skill cleanly separates information gathering from mutation. It encourages narrowing from broad search to direct reads, changing search strategies after a miss, and reporting concrete file/line evidence. That is a useful default for repository reconnaissance and can reduce unnecessary write/tool exposure.

### Limits

The claim that read-only exploration does not need all project rules is too broad. Repository instructions can govern allowed paths, confidentiality, generated files, tool use, or interpretation even when no write occurs. The example commands also truncate with `head`, which can silently hide relevant matches unless the agent recognizes the output as a sample rather than an exhaustive result. The `quick`/`medium`/`thorough` levels are qualitative and have no measurable completion criteria or eval suite.

The README installs from `Arxchibobo/lightweight-explorer`, not any of the three reviewed repository identities, continuing the provenance/identity mismatch seen in Batch 030.

## 5 and 8. `self-rationalization-guard` exact duplicate pair

`YTT-CSH/self-rationalization-guard` and `wbxjj2008/self-rationalization-guard` both resolve to `3df614e3ae87d80b3be338d247a2fc2488dc22a2`. The skill lists common shortcut/rationalization patterns across execution, communication, quality, and delegation, then requires a pre-completion self-check.

### Strengths

The strongest rule is the distinction between code-reading confidence and execution evidence. The checklist also explicitly checks whether difficult steps, edge cases, and independent verification were skipped. These are useful guardrails for implementation workflows that otherwise drift toward narrative completion.

### Limits

Several rules are over-generalized. `If you are writing an explanation instead of running a command → run the command` is wrong for tasks that are purely analytical, lack tool access, or require authorization before mutation/execution. `Production can do anything` can encourage unbounded edge-case work, while always proactively explaining or confirming can create unnecessary interaction. The README instruction to provide a time estimate before doing expensive work is also not a reliable capability in environments that cannot predict execution duration. A safer design would gate action on task type, authority, risk, and available tools rather than treating execution as universally preferable to explanation.

The README installs from `Arxchibobo/self-rationalization-guard`, not either reviewed identity.

## 7. `wbxjj2008/coordinator-orchestrator`

Revision `a6d0311d279b32497a9c952061fafb798309b4e3` is the same full tree already reviewed for `alexchenyu/coordinator-orchestrator` and `k1w1f1sh/coordinator-orchestrator` in Batch 030. README and `SKILL.md` were directly re-read. No new skill report is generated.

The previous finding remains: synthesis-before-delegation is valuable, but the strong identity statement that the coordinator is "not executor" can cause needless delegation, and fixed retry counts are not calibrated to cost, risk, or side effects.

## 9. `ajunlonglive/context-compressor`

Revision `b8b5f37cdf027df2cb85f5ad9838701c90dd9c8e` contains a nine-section compaction template covering user intent, technical concepts, files/code, errors/fixes, problem solving, all user messages, pending work, current work, and next step. It also prescribes image placeholders, no tool calls during compression, and post-compression restoration of recent files, active skills, and tool-list changes.

### Strengths

The template explicitly preserves current work, unresolved tasks, and the latest user intent rather than producing a generic topical summary. Requiring file names and concrete current-state details can reduce post-compaction task drift. Separating "next step" from the historical summary is also useful for continuation.

### Limits

The stated goal of compressing roughly 100k tokens to 5k "without losing any key information" is an aspiration, not something the repository proves. Listing every user message can defeat compression on long conversations and unnecessarily retain irrelevant or sensitive material; preserving decision-relevant intent is preferable to exhaustive copying. A blanket ban on tool calls during compaction can also leave mutable file/project state stale when grounding is necessary. The claimed automatic restoration of recent file contents, active skills, and tool changes is not implemented by repository-local code at this revision, so it should be treated as an integration requirement rather than a demonstrated capability.

The instruction to emit a hidden-style `<analysis>` draft should not be treated as a portable interface contract across agent systems. The README installs from `Arxchibobo/context-compressor`, not the reviewed identity.

## 10. `YTT-CSH/smart-memory-guard`

Revision `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` is the same full tree already reviewed for `ajunlonglive/smart-memory-guard` and `k1w1f1sh/smart-memory-guard` in Batch 030. README and `SKILL.md` were directly re-read. No new skill report is generated.

The existing assessment still applies: authority separation and drift checks are useful; refusing some explicit remember requests and the fixed 5 KB / seven-day pruning thresholds are overly rigid without environment-specific evidence.

## Cross-batch findings

1. **Commit-level deduplication prevents inflated catalog counts.** Ten repository identities in this batch reduce to six unique content trees, and three of those trees were already reviewed in Batch 030.
2. **Only three genuinely new skill bodies were added:** `lightweight-explorer`, `self-rationalization-guard`, and `context-compressor`.
3. **Repository identity and declared upstream provenance continue to diverge.** Every newly reviewed README in this family installs from an `Arxchibobo/...` repository rather than the indexed owner.
4. **These packages are policy-only at the reviewed revisions.** No repository-local scripts, references, evals, package manifests, or executable harnesses surfaced in the inspected set.
5. **The dominant quality risk is over-generalization.** The new skills contain useful workflow heuristics, but rules such as skipping project instructions for read-only work, preferring command execution over explanation, or copying every user message during compression need authority/risk/context gates before production use.

## Validation status

- Repository identity: verified for all 10.
- Stars: exact observed value `0` verified for all 10 with GitHub repository-search qualifiers.
- Exact revision: pinned for all 10.
- README: directly read for all six unique content revisions.
- `SKILL.md`: **6 unique bodies directly reviewed**.
- Scripts/references/evals/package manifests: none surfaced in repository search across the ten identities or the reviewed documentation.
- Runtime/build/tests/evals: **not_executed**.
