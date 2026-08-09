# Agent Skills Deep Analysis — Batch 052

Observed: 2026-08-09

## Scope and validation boundary

This batch continues the deterministic indexed queue after Batch 051. A repository is counted only after live GitHub identity/Stars verification plus direct repository-content inspection. Index metadata alone is never completion evidence.

Completed repository identities: **10**. Direct `SKILL.md` reads: **20**, representing **15 unique Skill bodies** across **5 unique Git trees**. All ten completed repositories had their root README read directly. Scripts/references/tests were inspected when available, including the `ast-editor` smoke-test source in the Kamble snapshot and render/reference material in the distinct html-ppt snapshots. No repository code, builds, browser flows, live APIs, external services, tests or evals were executed, so this batch remains `structure-reviewed`, not runtime-validated.

## Completed repositories

| # | Repository | Stars observed | Pinned revision / content tree | Direct content gate | Report action |
|---|---|---:|---|---|---|
| 1 | `Ckzzz1/claude-code-longrun-skill` | 0 | `9ca7634840f9ee865f09d4dba76b33ac2fc80f43` / `c815f3b8b8b65d81a5c8ced105d68ddf996490d6` | README + Skill + both references + complete tree inventory | 1 new report |
| 2 | `iflow-mcp/kambleakash0-agent-skills` | 0 | `18ef42deb6574758fcf698e679bd3c33c5712a86` / `76101aa594ab1389a07b06603ad5a4666cbbda7c` | README + 11/11 Skill bodies + representative reference + MCP test source | 11 new reports |
| 3 | `wanli15nian/skills` | 0 | `7c71a845071e8f994253db0d26c7e36fa90e2b5e` / `33a909b3c9ece5dd8e1524796c7ca60d8e8be1f3` | README + `37signals-way` Skill + shaping reference + sync script | exact-tree reuse; no duplicate report |
| 4 | `5kon/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` / `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | README + Skill + render script | 1 new report for previously unreported snapshot |
| 5 | `Amateur0x1/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` / `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | README + Skill | exact-tree reuse within batch |
| 6 | `jianyun19999/html-ppt-skill` | 0 | `15fb85f05b3092b00e5a4eb181227339fe1af679` / `4169c880bcbea1895d2624594e458e85634db14d` | README + Skill + presenter-mode reference + render script | 1 new report for distinct snapshot |
| 7 | `kiakun-collab/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` / `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | README + Skill | exact-tree reuse within batch |
| 8 | `lccstc/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` / `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | README + Skill | exact-tree reuse within batch |
| 9 | `comeonzhj/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` / `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | README + Skill | exact-tree reuse within batch |
| 10 | `sunzhengtaolz/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` / `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | README + Skill | exact-tree reuse within batch |

## Repository analyses

### 1. `Ckzzz1/claude-code-longrun-skill`

This is a compact long-running-task orchestration Skill. The pinned tree contains a root README, one `SKILL.md`, and two reference documents; there are no scripts, tests, or evals in this revision. The design is operationally useful: dedicate a tmux session, persist task state outside chat, monitor at a low cadence, resume/recover instead of restarting, preserve secret hygiene in task files, and escalate only when the worker cannot make safe progress.

The material also exposes a critical authorization concern: its preferred launch path uses `claude --permission-mode bypassPermissions`. That may be convenient for an unattended worker, but it broadens local execution privilege substantially. A catalog should not promote that as an implicit default. Long-running execution needs a higher-level permission policy, constrained workspace, explicit side-effect budget, and recovery/termination rules.

### 2. `iflow-mcp/kambleakash0-agent-skills`

This pinned fork is a real 11-Skill engineering collection plus two Python MCP implementation surfaces (`ast-editor` and `notebook-editor`). All eleven Skill bodies were read directly: `code-review`, `deep-codebase-audit`, `domain-glossary`, `english-humanizer`, `git-workflow`, `grill-master`, `incremental-tdd`, `script-writer`, `slice-the-spec`, `spec-to-plan`, and `spec-writer`.

The collection is strongest where it separates phases and permissions. `code-review` requires diff/context inspection before prioritized findings; `deep-codebase-audit` uses progressive disclosure and confirmation before refactoring; `domain-glossary` ties definitions to code evidence and confidence; `git-workflow` requires explicit confirmation before Git operations; `incremental-tdd` keeps commit/push/PR effects opt-in; and `spec-to-plan` is explicitly read-only. The spec-writing/slicing/planning Skills form a useful requirements-to-execution decomposition rather than a single oversized prompt.

The repository also demonstrates why implementation tests must be classified carefully. The directly inspected `mcp-servers/ast-editor/tests/run_tests.py` performs real AST edit calls and prints resulting content plus a success banner, but it contains no assertions. It is better described as a smoke/demo harness than a deterministic regression test. Repository-local test source is evidence of intended verification, not evidence that the pinned revision passed. No behavioral eval was found that proves the eleven Skills trigger correctly or produce correct end-to-end outcomes.

### 3. `wanli15nian/skills`

This identity was independently checked and content-gated, then resolved to the already-reviewed Wondel tree `33a909b3c9ece5dd8e1524796c7ca60d8e8be1f3`. A representative `37signals-way/SKILL.md`, its shaping reference, and `scripts/sync-ide-skills.sh` were read directly before reuse was accepted.

The repository remains a useful progressive-disclosure collection. `37signals-way` moves long-form method detail into references, while the sync script deterministically discovers top-level Skill directories and recreates/validates symlink sets for multiple IDEs. Its 0–10 adherence scoring should be treated as an opinionated framework lens, not objective product truth. Exact-tree reuse avoids inflating individual Skill-report counts while still recording the repository identity as covered.

### 4–5, 7–10. html-ppt snapshot `656ebee6...`

`5kon`, `Amateur0x1`, `kiakun-collab`, `lccstc`, `comeonzhj`, and `sunzhengtaolz` were each independently identity/star checked and directly content-gated. They resolve to the same pinned revision/tree and the same README/Skill blobs, so only one individual report is materialized for the previously unreported content snapshot.

This snapshot exposes 36 themes, 14 full-deck templates, 31 layouts, 27 CSS animations and 20 canvas effects around a static HTML/CSS/JS runtime. It has a useful token-driven/template-first authoring model and progressive reference catalogs. However, its Skill text says to add a new layout only if none of the “30” fit while the same document advertises 31 layouts, an observable inventory drift. The README slogan `36 themes × 20 canvas FX × 31 layouts × 14 full decks = 101 PPT skills` is also not meaningful arithmetic; the authoritative counts are the separately enumerated inventories, not that multiplication string.

The directly read render script hard-codes `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` and invokes Chrome with `--no-sandbox`. That makes the verification path macOS-specific and weakens browser isolation. Existing screenshot files are artifacts, not passing evidence for this pinned revision unless the rendering/comparison workflow is actually executed.

### 6. `jianyun19999/html-ppt-skill`

This fork is a distinct intermediate html-ppt snapshot rather than the old 14-deck tree or the later Batch-051 upstream tree. It adds the 15th `presenter-mode-reveal` deck, a Chinese README, a presenter guide, iframe preview mode, `BroadcastChannel` synchronization, `postMessage` navigation, movable/resizable presenter cards, persisted card layout, notes and timer behavior.

The content also provides a concrete example of why inventory should be generated or linted. The README headline and Skill inventory say 15 full-deck templates, while later README image/caption, quick-start and project-tree text still say 14; the Skill similarly says 15 near the top but later asks the user to choose one of 14 templates and retains 14 in its tree documentation. The render script remains the same macOS-specific Chrome wrapper with `--no-sandbox`. No presenter-mode browser test or render comparison was executed in this batch, so “pixel-perfect” and “no flicker” remain implementation claims, not verified runtime outcomes here.

## Queue content-gate exclusions / held entries

- `qishilong/agentskills-learn` was live-checked and directly content-gated. Its actual repository is an Agent Skills specification/documentation/reference-SDK lineage fork, not a qualified Skill collection. It is excluded and not counted as completed.
- `NicoReiser/AgentSkillsQradrant` and `Robni5566/typewriter-video` remain `adjacent_search_hit` index entries and were not promoted to the qualified queue in this batch.

## Cross-repository findings

1. **Privilege needs to sit above Skill activation.** `claude-code-longrun` shows the risk clearly: unattended execution and `bypassPermissions` are materially different from ordinary Skill guidance. Authorization, filesystem/network scope, side-effect budget, termination and recovery should be enforced by the orchestrator rather than embedded as an implicit Skill default.
2. **Verification source is not a verification result.** Kamble's AST test script and html-ppt's screenshot/render infrastructure are useful, but neither proves a passing pinned revision without execution. Test files must be classified by what they actually assert.
3. **Content-addressed reuse prevents catalog inflation.** Six separately indexed html-ppt identities share one exact tree. Repository coverage should count identities after direct gates; individual Skill knowledge should deduplicate by actual content revision/body.
4. **Spec → slice → plan → implementation is a reusable Skill decomposition.** The Kamble collection separates requirements writing, slicing, planning, TDD and review instead of putting the entire software lifecycle into one monolithic Skill. This is a better basis for composable validation boundaries.
5. **Inventory drift should be mechanically linted.** Both observed html-ppt snapshots contain internal count drift. Counts and generated documentation should derive from the filesystem/registry rather than hand-maintained prose.

## Batch result

- Qualified repository identities completed: **10**
- Root READMEs directly read for completed repositories: **10**
- Direct `SKILL.md` reads: **20**
- Unique Skill bodies directly reviewed: **15**
- Unique Git trees represented: **5**
- New repository-scoped Skill reports: **14**
- Cumulative structure-reviewed repositories: **520**
- Cumulative repository-scoped Skill reports: **3050**
- Arithmetic remaining from frozen eligible basis 2088: **1568**
- Runtime/build/test/eval execution: **not_executed**
- Cross-repository canonical reconciliation: **pending**

The next unresolved qualified-index candidate after the completed content gates is `TenTh0usand/html-ppt-skill`; it must still receive its own live identity/Stars/content gate before it can be counted.