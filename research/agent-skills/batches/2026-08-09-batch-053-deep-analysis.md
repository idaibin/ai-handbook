# Agent Skills Deep Analysis — Batch 053

Observed: 2026-08-09

## Scope and validation boundary

This batch continues the deterministic indexed queue after Batch 052. A repository is counted only after live GitHub identity/Stars verification plus direct repository-content inspection. Index metadata alone is never completion evidence.

Completed repository identities: **10**. Root READMEs directly read: **10**. Direct `SKILL.md` reads: **10**, representing **3 unique Skill bodies** across **3 unique Git trees**. Scripts/references/workflows were inspected once per distinct content tree when available and reused only after exact-tree equality plus per-repository README/Skill gates were established. No repository code, builds, browser flows, live APIs, external services, tests or evals were executed, so this batch remains `structure-reviewed`, not runtime-validated.

## Completed repositories

| # | Repository | Stars observed | Pinned revision / content tree | Direct content gate | Report action |
|---|---|---:|---|---|---|
| 1 | `TenTh0usand/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` / `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | README + root `SKILL.md`; exact-tree render/reference evidence inherited from Batch 052 only after tree equality | exact-tree reuse; no duplicate report |
| 2 | `XiaoCC/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` / `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | README + root `SKILL.md`; exact-tree render/reference evidence reused | exact-tree reuse; no duplicate report |
| 3 | `wrqf/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` / `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | README + root `SKILL.md`; exact-tree render/reference evidence reused | exact-tree reuse; no duplicate report |
| 4 | `muddlelife/Anthropic-Cybersecurity-Skills` | 0 | `9e8a8cda8080bf6f9f02b40c3035c55813e0ba39` / `4537b50decc9c1a4614cfadec02b30d0007944fa` | README + representative Skill + representative directory + helper script + workflow inventory/validator | 1 new report for previously unreported content snapshot |
| 5 | `ansulev/Anthropic-Cybersecurity-Skills` | 0 | `673da1f3b0b7be34ffc9624ef3858fe45f1c3bed` / `9a59737db682a71fe1ecedb32781103613c70436` | README + representative Skill + representative directory + workflow inventory/validator | 1 new report for distinct evolved snapshot |
| 6 | `mayomacam/Anthropic-Cybersecurity-Skills` | 0 | `9e8a8cda8080bf6f9f02b40c3035c55813e0ba39` / `4537b50decc9c1a4614cfadec02b30d0007944fa` | README + representative Skill | exact-tree reuse within batch |
| 7 | `W1lsp0/Anthropic-Cybersecurity-Skills` | 0 | `9e8a8cda8080bf6f9f02b40c3035c55813e0ba39` / `4537b50decc9c1a4614cfadec02b30d0007944fa` | README + representative Skill | exact-tree reuse within batch |
| 8 | `starnightcyber/Anthropic-Cybersecurity-Skills` | 0 | `9e8a8cda8080bf6f9f02b40c3035c55813e0ba39` / `4537b50decc9c1a4614cfadec02b30d0007944fa` | README + representative Skill | exact-tree reuse within batch |
| 9 | `reachsridhargit/Claude-Skill` | 0 | `9e8a8cda8080bf6f9f02b40c3035c55813e0ba39` / `4537b50decc9c1a4614cfadec02b30d0007944fa` | README + representative Skill | exact-tree reuse within batch |
| 10 | `KIKI-flower/Anthropic-Cybersecurity-Skills` | 0 | `9e8a8cda8080bf6f9f02b40c3035c55813e0ba39` / `4537b50decc9c1a4614cfadec02b30d0007944fa` | README + representative Skill | exact-tree reuse within batch |

## Repository analyses

### 1–3. html-ppt snapshot `656ebee6d1e4...`

`TenTh0usand`, `XiaoCC`, and `wrqf` were each independently identity/Stars checked and had their README plus root Skill read directly. All three resolve to the already-reviewed Batch-052 tree `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11`, so the prior content report is reused rather than duplicated.

The snapshot remains a substantial static HTML presentation system with themes, full-deck templates, single-page layouts, animations, canvas effects, references and render tooling. The direct README/Skill reads reconfirm the same internal inventory drift: the prose advertises 31 layouts while later wording still refers to 30, and the animation inventory text also contains a hand-maintained count mismatch. The Skill is unusually prescriptive about fixed visual/runtime choices and about editing HTML rather than post-processing generated PowerPoint output.

The exact-tree render path was already inspected in Batch 052: it hard-codes the macOS Chrome binary and invokes headless Chrome with `--no-sandbox`. Existing GIFs/screenshots demonstrate intended output but are not current-run visual-regression evidence. No browser/render execution was performed here.

### 4, 6–10. Cybersecurity snapshot `4537b50d...`

Six independently indexed repository identities resolve to the exact same tree `4537b50decc9c1a4614cfadec02b30d0007944fa`. Each received its own README and representative Skill content gate before exact-tree reuse was accepted. One content report is therefore materialized for the unique snapshot rather than six duplicated reports.

The README describes a large agentskills.io-style security library with **754 Skills across 26 domains and five framework mappings**. The representative `performing-memory-forensics-with-volatility3` Skill is a long operational playbook with prerequisites, workflow, concepts and result-checking guidance. Its directory contains localized Skill material, a reference file and a real Python helper. The helper invokes external forensic tooling via argument-vector `subprocess.run` rather than shell-string construction, but it can collect highly sensitive forensic artifacts into a JSON report. Catalog-level authorization, workspace/data handling and redaction policies therefore need to sit above Skill activation.

There is a concrete documentation/implementation drift in the pinned tree. README's generic Skill-anatomy example names `references/standards.md`, `references/workflows.md` and `scripts/process.py`; the directly inspected representative directory instead contains `references/api-reference.md` and `scripts/agent.py`. This does not invalidate the Skill, but it means README anatomy cannot be treated as an exact schema for every package.

The repository includes three GitHub workflows: marketplace-version sync, index update and `validate-skills`. The directly read validator checks required frontmatter, kebab-case naming, maximum name length, duplicate names and reports counts. It is a structural/catalog gate, not a behavioral eval. No runtime success rate or security correctness can be inferred from its presence.

### 5. `ansulev/Anthropic-Cybersecurity-Skills`

This is a distinct evolved content tree, not the 754-Skill snapshot above. The README headline reports **817 Skills, 29 domains and six framework mappings**, adding MITRE F3 and ATT&CK v19.1-era material. However, the same README later retains the heading **“MITRE ATT&CK v19.1 — 754/754 skills mapped”**. That is direct inventory/documentation drift inside the pinned revision and should be generated from the authoritative index rather than maintained manually.

The representative memory-forensics Skill differs from the 754 snapshot by adding `mitre_attack` frontmatter mappings while retaining the same core body and the same representative references/scripts subtree. This is exactly the kind of change that requires blob/tree-aware deduplication: same Skill name does not mean same Skill revision.

Its `validate-skills` workflow delegates frontmatter validation to `tools/validate-skill.py`, checks duplicate names and reports Skill counts. This is stronger maintainability than duplicated inline parsing, but it still validates structure/inventory rather than whether a Skill triggers correctly, uses tools safely or reaches a correct real-world result. No behavioral eval suite was executed or treated as passed.

## Cross-repository findings

1. **Content identity must remain separate from repository identity.** Three html-ppt identities reuse one previously reviewed tree; six Cybersecurity identities reuse one new tree; `ansulev` is distinct despite sharing the same project lineage and Skill names. Repository coverage and Skill-report counts should therefore continue to use separate identity and content-addressed dimensions.
2. **Generated inventories are preferable to prose counts.** html-ppt and the evolved Cybersecurity snapshot both show internal count drift. Inventory headings/badges should be generated from the filesystem/index and checked in CI.
3. **Structural validation is not behavioral validation.** Both Cybersecurity snapshots have CI that validates frontmatter/naming/count properties. That does not establish operational correctness, safety, trigger precision or real-world outcome quality.
4. **Operational Skills need higher-level authorization/data policy.** The representative security Skill can invoke external tooling and handle sensitive forensic artifacts. A catalog/orchestrator should own authorization, allowed targets, data retention/redaction and external side effects rather than inheriting permission from Skill activation alone.
5. **README anatomy should be lintable against real package structure.** The 754-Skill snapshot's generic anatomy names files that do not exist in the representative package. Documentation examples should either be marked illustrative or checked against a canonical fixture.

## Batch result

- Qualified repository identities completed: **10**
- Root READMEs directly read for completed repositories: **10**
- Direct `SKILL.md` reads: **10**
- Unique Skill bodies directly reviewed: **3**
- Unique Git trees represented: **3**
- New repository-scoped Skill reports: **2**
- Cumulative structure-reviewed repositories: **530**
- Cumulative repository-scoped Skill reports: **3052**
- Arithmetic remaining from frozen eligible basis 2088: **1558**
- Runtime/build/test/eval execution: **not_executed**
- Cross-repository canonical reconciliation: **pending**

The next unresolved qualified-index candidate after these completed gates is `priyanshuz/Anthropic-Cybersecurity-Skills`; it must receive its own live identity/Stars/content gate before it can be counted.