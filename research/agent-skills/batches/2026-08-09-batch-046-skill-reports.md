# Agent Skills Individual Reports — Batch 046

Observed: 2026-08-09

This file contains only newly materialized canonical individual Skill reports from Batch 046. Directly re-read mirrors and previously analyzed content are mapped instead of duplicated.

## 1. `SGuibord/chainlink-agent-skills` — `chainlink-ccip-skill`

- Repository: `SGuibord/chainlink-agent-skills`
- Revision: `bada72c0fbdba616412c65c239d69e4f94154abd`
- Skill blob: `2a2401bc3babee92f8921316d1c268347caa4946`
- Classification: operational developer/domain Skill with external-effect safety gates
- Canonical action: new revision report

### Evidence read

- `README.md`
- `chainlink-ccip-skill/SKILL.md`
- `chainlink-ccip-skill/references/ccip-mcp.md`
- `evals/chainlink-ccip-skill/README.md`
- `evals/chainlink-ccip-skill/rubrics/must-pass.txt`

### Structure and behavior

The Skill uses progressive disclosure: the root Skill routes the request, while live-source, contract, monitoring, discovery, local-testing and MCP details are separated into references. The SGuibord revision is materially different from the earlier reviewed `chethanuk/chainlink-agent-skills` CCIP body: its Skill blob changed from `45aa8d7bd7089a8d953970aaf78edafe5be70ff9` to `2a2401bc3babee92f8921316d1c268347caa4946`, adding MCP metadata and a dedicated MCP route/reference.

External effects are not treated as ordinary tool calls. The Skill distinguishes read-only work from state-changing operations and requires a preflight/approval boundary before side effects. This separation is a reusable pattern for Skills that can cross from information retrieval into irreversible external actions.

### Validation assets

The repository contains Promptfoo-oriented evaluation documentation and a must-pass safety rubric. These are stronger evidence than prose-only claims because expected behavioral constraints are made machine-reviewable, but they remain definitions until executed.

**Validation status:** eval files inspected; Promptfoo/tests/runtime were not executed in this batch.

### Main strengths

- Progressive reference disclosure limits default context load.
- Freshness-sensitive facts are delegated to current sources/tooling rather than hard-coded into the root Skill.
- Side-effecting actions are separated from read-only actions with explicit authorization boundaries.
- MCP support is represented as a capability path rather than silently replacing all other routes.
- A repository-local eval contract exists for critical behavior.

### Main gaps / risks

- MCP server/tool availability and current external behavior are outside the static Skill contract and require live verification when used.
- The existence of a rubric does not establish pass rate or behavioral reliability without execution.
- The Skill remains dependent on external Chainlink surfaces whose APIs, routes and supported capabilities can change.

### Reuse value

High for the AI-handbook as a reference for: progressive disclosure, explicit external-effect authorization, current-source routing, and separating static Skill instructions from behavioral eval contracts.

---

## 2. `raykao/obsidian-plugin-skill` — `obsidian-plugin`

- Repository: `raykao/obsidian-plugin-skill`
- Revision: `7633460c8bc776030936d86d737f9e2679eeb7b6`
- Git tree: `7fb97ded5a5248b33b139cbf055ceb2b18e85dd9`
- Classification: procedural developer Skill with API reference
- Canonical action: new report

### Evidence read

- `README.md`
- `obsidian-plugin/SKILL.md`
- `obsidian-plugin/references/API-REFERENCE.md`

### Structure and behavior

The repository is deliberately small: a root project README, one focused Skill definition and a separate API reference. The Skill provides a development workflow and delegates detailed API lookup to the reference instead of embedding the entire API surface in the main instructions.

At the pinned tree, no repository-local scripts, executable validator, test suite or eval harness was found. It should therefore be classified as a documentation/procedure Skill, not as a runtime-validated implementation.

### Main strengths

- Simple repository layout with clear Skill-to-reference separation.
- API material is moved out of the main Skill, reducing default context cost.
- Scope is narrow enough to be reusable without a large orchestration layer.

### Main gaps / risks

- API guidance can drift as Obsidian/plugin APIs evolve.
- No deterministic contract test checks that referenced APIs remain current.
- No repository-local eval verifies whether an agent follows the intended plugin-development workflow.
- No executable helper means outcomes depend heavily on the consuming agent/tool environment.

### Reuse value

Moderate. The strongest reusable pattern is the small `SKILL.md` + targeted reference split. Before adopting it as a high-confidence engineering Skill, add version/freshness metadata and automated API/behavior validation.

---

## Existing-content mappings from this batch

The following directly read content did not create new canonical reports:

- `gigantsc/skills-hermes-` → existing Wondel-derived canonical content.
- `NailRunner/skills-base-2604` → same exact Wondel Git tree.
- `SGuibord/chainlink-agent-skills :: chainlink-cre-skill` → previously analyzed Chainlink CRE lineage.
- `michaelgallese3-coder/Anthropic-Cybersecurity-Skills` → previously analyzed Cybersecurity collection lineage; representative Skill is a distinct older blob variant.
- `0xhexrecon/Anthropic-Cybersecurity-Skills` → previously analyzed current Cybersecurity collection lineage.
- `hnizil/Anthropic-Cybersecurity-Skills` → exact-tree mapping to the same current Cybersecurity lineage.
- `imperius361/Anthropic-Cybersecurity-Skills` → exact-tree mapping to the same current Cybersecurity lineage.
- `suriyaJaboon/Anthropic-Cybersecurity-Skills` → exact-tree mapping to the same current Cybersecurity lineage.
- `casky-ai/Anthropic-Cybersecurity-Skills` → different repository tree, but the directly reviewed representative Skill blob matches the current shared body and does not justify a duplicate report.

Generated inventory size is not treated as deep-analysis completion. Historical cross-repository canonical reconciliation remains pending.
