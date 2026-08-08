# Agent Skills Deep Analysis — Batch 043

- Batch: `2026-08-08-batch-043`
- Phase: deep analysis
- Queue source: existing deterministic Agent Skills repository index
- Completed repository identities: **10**
- Repository README files directly read for completed identities: **10**
- `SKILL.md` files directly read for completed identities: **19**
- Unique pinned Git content trees represented: **8**
- Unique skill bodies directly reviewed: **16**
- New batch-local individual skill reports: **15**
- Runtime/build/test/eval execution: **not executed**
- Completion rule: a repository is counted only after identity/stars/revision verification plus direct repository content reading. Metadata-only hits are never marked complete.

## Executive result

Batch 043 completed 10 genuinely qualified repository identities from the existing indexed queue. The run crossed the April 6 → April 7 → April 8 staging boundary because many intervening index candidates were specification/tooling repositories or had become unavailable. Those entries were not counted toward completion.

The 10 completed identities are:

1. `MarkkuPekkarinen/skills`
2. `HannanSolo/zephyr-agent-skills`
3. `kent666/memory-system-ops-skill`
4. `makakin/Anthropic-Cybersecurity-Skills`
5. `Lucub0x/Anthropic-Cybersecurity-Skills`
6. `adampielak/Anthropic-Cybersecurity-Skills`
7. `xtremebeing/Anthropic-Cybersecurity-Skills`
8. `junefish1414/AgentSkills`
9. `ever-just/agentskills`
10. `dgallitelli/aws-data-agent-skill-strands-agentcore`

The strongest reusable patterns are persistent orchestration artifacts, evidence-first memory state, decomposed source→spec→review document pipelines, progressive disclosure, and schema-grounded data-agent execution. The recurring weakness is that useful workflow prose often lacks executable behavioral evals, while operational Skills sometimes encode environment-specific side effects that should be governed by a higher-precedence authorization policy.

## Completed repositories

| # | Repository | Stars | Pinned revision | Tree | Content gate |
|---:|---|---:|---|---|---|
| 1 | `MarkkuPekkarinen/skills` | 0 | `7702dbcb3873689cb73e9c513599c6c68b37cf4c` | `3b300c02272e082006a06cd13da34528ffbf39e2` | README + `design-code-architecture/SKILL.md`; repository skill/test surfaces inspected |
| 2 | `HannanSolo/zephyr-agent-skills` | 0 | `6dc057cf3eee08a36a801e66428e8a6c22cd175b` | `3af15c2ec9a557e3837a65ce36c2d02fcb6b84a8` | README + `skills/zephyr-index/SKILL.md`; references/scripts surfaced |
| 3 | `kent666/memory-system-ops-skill` | 0 | `c5e08ac08ab97280d6dca65429b98c49da1aa33f` | `bda1dff118b94f5d4b5ac784610bb82a702a7583` | README + root `SKILL.md`; reference templates inspected |
| 4 | `makakin/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative Skill; collection/index/workflows inspected |
| 5 | `Lucub0x/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | identity-specific README + same representative Skill reread |
| 6 | `adampielak/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | identity-specific README + same representative Skill reread |
| 7 | `xtremebeing/Anthropic-Cybersecurity-Skills` | 0 | `0f429d0f96ee70d2a6c259c4ecc6c6e18e0d23ff` | `2ecf446313034b6167577fbde9bde832e5859369` | README + representative Skill; sampled body matches newer lineage |
| 8 | `junefish1414/AgentSkills` | 0 | `b80c9bae2afa109b04be8f1778f2f921708cd98f` | `9893f737a59738832af0db81513102fa2e313392` | README + all 9 local Skill bodies; installer/references/assets inspected |
| 9 | `ever-just/agentskills` | 3 | `6c1ec73a213da4b8b72714e530c4bfd3cdd6f9c7` | `677880fd61f9c8fa68c5cffa231121e13b441ae4` | 115+ inventory/structure verified; README + 2 representative Skill bodies + reference index read |
| 10 | `dgallitelli/aws-data-agent-skill-strands-agentcore` | 0 | `6c297673421bdf027268630c273bdd03c9186f04` | `0638067c1404c9977a7c1b54c5c74463a6b5a242` | README + Skill + references + actual Python integration read |

Observed Stars are point-in-time metadata and are not treated as quality evidence.

## Repository findings

### `MarkkuPekkarinen/skills`

The directly reviewed `design-code-architecture` body is a Wondel-derived metaskill that orchestrates multiple design/architecture skills and persists architecture, reliability and plan artifacts. Its strongest pattern is explicit phase/handoff state rather than a single oversized prompt. The main gaps are convention-based constituent-skill compatibility and absence of executed behavioral evals in this review.

Verdict: `strong orchestration/body report added; runtime/eval evidence not executed`.

### `HannanSolo/zephyr-agent-skills`

`zephyr-index` was directly reread as the representative routing hub and its reference/script surfaces were confirmed. The same Zephyr family was already body-reviewed in Batch 027, so this repository increases independently content-gated repository coverage without duplicating canonical reports.

Verdict: `qualified lineage; prior canonical Zephyr report retained`.

### `kent666/memory-system-ops-skill`

The Skill makes memory retrieval, writeback, task state, archive/resume semantics and context-reset checkpoints explicit. Evidence-sufficiency retrieval and structured Decision/Why/Impact/Next/Verify writebacks are useful patterns. The file topology/state vocabulary are host-specific and timing/repetition thresholds are uncalibrated heuristics; no executable eval harness was surfaced or run.

Verdict: `high-value state/evidence pattern; parameterize topology/thresholds and add replay fixtures`.

### Anthropic Cybersecurity Skills lineage

Four repository identities were independently identity/stars/revision gated and had README plus the same representative Skill reread. Three share exact tree `5dd2ce82978a50cd014d4b310f5993bf5bba6f43`; `xtremebeing/...` has a distinct repository tree while the sampled representative body remains the same newer lineage.

The collection has a large generated index and structural validation workflows. This batch records one new representative defensive-forensics body report; operational command material is intentionally not reproduced here. Structural validation does not prove correctness/safe execution of the collection, and large inventory counts remain inventory evidence rather than body-level completion.

Verdict: `qualified collection lineage; one new representative body report, mirrors deduplicated`.

### `junefish1414/AgentSkills`

All nine local Skill bodies were directly read: `axure-to-md` (`name: axure-to-md-cli`), `blocker-overview`, `confluence-to-md`, `jira-analyzer`, `jira-to-spec-iterate`, `jira-to-spec`, `spec-md-to-po-html`, `spec-reviewer`, and `spec-to-prd`.

The repository forms a coherent source/prototype → specification → iterative update → review → PRD/HTML pipeline. Particularly useful patterns are responsibility separation, `spec-reviewer` separating readiness from readability, and `jira-to-spec-iterate` preserving unaffected sections. Risks include installer/output side effects that should be authorized by higher-precedence policy, version-sensitive external integrations, and lack of repository-local behavioral evals in the inspected tree.

Verdict: `strong multi-skill product-document workflow; add centralized side-effect policy and executable fixtures`.

### `ever-just/agentskills`

The README presents a 115+ Skill collection. This batch verified the inventory/tree but does **not** claim 115+ body-level reviews. Direct body reviews were limited to `deployment-testing` and `programmatic-osint-sources`, plus the latter's reference index.

Progressive reference routing, explicit source caveats and privacy/authorization notes are useful. However, organization-specific deployment runbooks should be separated from portable generic Skills, operational actions need higher-level authorization, and historical/live-test assertions or API availability/pricing must be reverified when used.

Verdict: `high-value reference architecture; separate generic Skills from private runbooks and require current external verification`.

### `dgallitelli/aws-data-agent-skill-strands-agentcore`

This repository contains a real Python Strands/AgentCore integration plus bundled Skill and five references. The Skill grounds SQL in discovered schema, asks for approval before execution, and preserves Lake Formation denial as a governance boundary. `src/main.py` actually wires the Skill plugin, file reader, model and AWS MCP client into a streaming entrypoint.

The main gaps are architectural: the Python layer imports the MCP tool surface dynamically rather than enforcing a deterministic read-only allowlist, approval remains a prompt-level contract rather than an application-enforced state transition, and no repository-local tests/evals demonstrate grounding, approval, governance or failure recovery.

Verdict: `promising executable AgentSkill integration; enforce tool capability/approval state in code and add behavioral tests`.

## Reclassified / unavailable queue entries — not completed

Content-verified reclassifications:

- `ColonistOne/skilldock.io` → `skill_tooling` (registry/SDK/CLI rather than repository-scoped Skill content).
- `drakevonduck/agentskills` → specification/documentation/reference SDK.
- `unclenate/agentskills` → specification/documentation/reference SDK.
- `O-Morgan/agentskills` → specification/documentation/reference SDK.

Unavailable at review time and not completed: `AnaisHeaney/development-companies`, `butangero/Anthropic-Cybersecurity-Skills`, `AibotyCoder/Anthropic-Cybersecurity-Skills`, `NhatPrime/claude-skills`, `akhanal/anthropic-claude-skills`, `ronabi/agentskills`, `hosank/Awesome-AI-Agentskills`, `AliB0367/Anthropic-Cybersecurity-Skills`, `senathn/skills`, `rgheck/lab-notebook-skills`, `Yutoolius/memory-system`, `UnleashedMindZ/awesome-skills-for-claude-code`, `CactusTechDev/agent-skills`, `wrdeepak/skills`, `bazuara/skill-recipes`, `farli84/agent-skills`, `x365global/ai_appstore`, `AnkitKumar-12/soft-ai`.

None of these were promoted from metadata to deep-analysis completion.

## Verification boundary

- Identity/Stars: verified from GitHub metadata.
- Pinned revisions/trees: verified from GitHub commit/tree data.
- README/SKILL/references/scripts/implementation: direct source reads as described above.
- Builds: **not executed**.
- Tests: **not executed**.
- Evals: **not executed**.
- External API/runtime behavior: **not executed**.

`structure-reviewed` therefore means source/content evidence was inspected; it does **not** mean behavioral correctness has been proven.

## Progress

- Prior structure-reviewed total: `420`
- Added this batch: `10`
- New structure-reviewed total: **430**
- Prior recorded skill reports: `2896`
- New batch-local body reports: **15**
- New recorded skill-report total: **2911**
- Frozen canonical eligible basis: `2088`
- Arithmetic remaining estimate: **1658**
- Historical canonical reconciliation: `pending`

`1658` is only `2088 - 430`; it is not a reconciled unique-repository remainder.

Queue resumption note: `dgallitelli/aws-data-agent-skill-strands-agentcore` was completed ahead of several April 8 candidates to reach the next 10 genuinely qualified repositories after a long run of unavailable/specification hits. Resume at `edulazaro/agentskills`, content-gate forward, and skip `dgallitelli/...` when its already-completed position is reached.
