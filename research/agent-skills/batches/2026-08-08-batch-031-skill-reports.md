# Agent Skills Individual Reports — Batch 031

- Batch ID: `2026-08-08-batch-031`
- New unique repository-scoped skill reports: **3**
- Repositories represented: **10**
- Unique content revisions directly reviewed: **6**
- Runtime/build/test/eval execution: **not_executed**

Ten repository identities reduce to six unique Git commit trees. Three of those six trees (`memory-type-system`, `coordinator-orchestrator`, `smart-memory-guard`) were already fully reported in Batch 030, so this batch adds only the three genuinely new skill bodies below. Duplicate identities are mapped to existing or new reports rather than counted as new skill content.

## Duplicate mappings to prior reports

- `ShawnSiao/memory-type-system` and `alexchenyu/memory-type-system` → Batch 030 `memory-type-system`, shared revision `d3805f3e5a576afd0c55e2de9cddb78511a30c95`.
- `wbxjj2008/coordinator-orchestrator` → Batch 030 `coordinator-orchestrator`, shared revision `a6d0311d279b32497a9c952061fafb798309b4e3`.
- `YTT-CSH/smart-memory-guard` → Batch 030 `smart-memory-guard`, shared revision `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb`.

## 1. `lightweight-explorer`

- Repositories:
  - `alexchenyu/lightweight-explorer`
  - `k1w1f1sh/lightweight-explorer`
  - `ajunlonglive/lightweight-explorer`
- Shared revision: `ba11d7eaab78fafd3982d36bff78c0f3fba633b1`
- Type: repository exploration / read-only search policy skill
- Executable artifacts: none observed
- Repository-local evals: none observed

### Purpose

Provide a low-cost, read-only exploration mode for locating files/functions, understanding repository structure, comparing implementations, and answering location-oriented code questions without mutating the repository.

### Design

The skill distinguishes broad search from direct reads, recommends trying alternative naming/scope strategies after misses, and requires independent searches to run in parallel. It defines `quick`, `medium`, and `thorough` exploration depths and asks for concise findings with file/line evidence.

### Assessment

The read-only boundary is useful because it prevents exploratory work from accidentally becoming implementation. Broad-search → focused-read is also a sensible retrieval progression, and explicit file/line reporting improves auditability.

The main weakness is the claim that read-only work does not need all project rules. Project instructions can constrain permitted paths, secrets, generated files, interpretation, network access, and tool usage even when nothing is written. The example use of `head` also makes search output intentionally incomplete, so an agent must not treat the displayed matches as exhaustive. Finally, the three depth labels have no measurable coverage target or repository-local evaluation demonstrating recall/token trade-offs.

### Provenance/install observation

The README installs from `Arxchibobo/lightweight-explorer`, not any reviewed repository identity. Treat current identity and self-declared upstream provenance as separate catalog fields.

## 2. `self-rationalization-guard`

- Repositories:
  - `YTT-CSH/self-rationalization-guard`
  - `wbxjj2008/self-rationalization-guard`
- Shared revision: `3df614e3ae87d80b3be338d247a2fc2488dc22a2`
- Type: execution-discipline / anti-shortcut policy skill
- Executable artifacts: none observed
- Repository-local evals: none observed

### Purpose

Detect common agent rationalizations for skipping difficult work, omitting verification, ignoring edge cases, over-delegating understanding, or substituting confidence for evidence.

### Design

The skill groups rationalizations into execution, communication, quality, and delegation categories. It then applies simple counter-rules such as running commands instead of relying on code appearance, independently verifying tests, changing approach when reasoning loops repeat, and performing a five-item completion self-check.

### Assessment

The strongest contribution is making shortcut detection explicit. In implementation contexts, `code looks correct` versus `observed execution evidence` is an important distinction, and the checklist can expose omitted validation or selectively ignored failure paths.

The rules are too universal to apply literally. Some tasks are analytical and need explanation rather than execution; some commands require authorization, pose side effects, or are unavailable; and exhaustive edge-case handling can become overengineering. The communication rules can also create unnecessary confirmations. The skill would be stronger if it first classified task type, authority, side-effect risk, and available tools, then selected an appropriate anti-shortcut check rather than treating command execution as the default remedy.

### Provenance/install observation

The README installs from `Arxchibobo/self-rationalization-guard`, not either reviewed repository identity.

## 3. `context-compressor`

- Repository: `ajunlonglive/context-compressor`
- Revision: `b8b5f37cdf027df2cb85f5ad9838701c90dd9c8e`
- Type: conversation/context compaction policy skill
- Executable artifacts: none observed
- Repository-local evals: none observed

### Purpose

Preserve task continuity when a long conversation is compacted by emitting a structured summary of user intent, technical context, files/code, errors/fixes, unresolved work, current work, and the immediate next step.

### Design

The skill specifies a nine-section summary. It gives special emphasis to all user messages, concrete current-work details, and a next-step section tied to the latest request. It also instructs image replacement with textual placeholders, prohibits tool calls during compaction, and describes post-compaction restoration of recent files, active skills, and tool-list changes.

### Assessment

The strongest idea is to preserve mutable work state and pending commitments explicitly rather than generating a generic topical summary. A concrete current-work section with filenames and incomplete validation steps can materially reduce continuation drift.

Several claims and rules are not robust. Compressing a very large conversation to a fixed smaller target without losing any key information cannot be guaranteed by this repository. Enumerating every user message can consume much of the saved context and retain irrelevant or sensitive material; decision-relevant intent and constraints are a better compression target. A blanket prohibition on tools can leave file/project state stale when grounding is needed. The described automatic re-injection of files, skills, and tool changes is not implemented by repository-local code at this revision and therefore should be treated as an external integration requirement, not a demonstrated feature. The `<analysis>` scratch-draft convention is also not a portable interface contract across agent runtimes.

### Provenance/install observation

The README installs from `Arxchibobo/context-compressor`, not the reviewed repository identity.

## Batch validation note

Six unique README/`SKILL.md` pairs were directly read at pinned revisions. Repository searches across all ten identities returned no matches for `scripts`, `references`, `eval`, or `package.json`, and the reviewed documentation identifies no repository-local executable helpers, references, tests, or eval suites. No build, command, test, or evaluation was executed, so these reports make no runtime-success claim.
