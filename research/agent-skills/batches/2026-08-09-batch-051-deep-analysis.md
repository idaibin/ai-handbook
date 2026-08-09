# Agent Skills Deep Analysis — Batch 051

Observed: 2026-08-09

## Scope and validation boundary

This batch continues the existing deterministic indexed queue after Batch 050. A repository is counted only after live GitHub identity/Stars verification plus direct content inspection. Index metadata alone is never completion evidence.

Completed repository identities: **10**. Direct `SKILL.md` reads: **14**, representing **11 unique Skill bodies** across **7 unique Git trees**. Two repositories have no conventional root README at the pinned revision (`liamlan/agentskills`, `NLP-planet/AgentSkills`); their tree and available subproject documentation were read instead. Repository-local scripts/tests/references were inspected when present. No repository code, builds, browser flows, live APIs, external services, or evals were executed, so this batch remains `structure-reviewed`, not runtime-validated.

## Completed repositories

| # | Repository | Stars observed | Pinned revision / content tree | Direct content gate | Report action |
|---|---|---:|---|---|---|
| 1 | `Player1Taco/morpheus-skill` | 1 | `7870973330227c180002b16227048a61a7e86cd0` / `a006e404b3c61320a2b3b72cde0b78eca9b4334e` | README, root `SKILL.md`, `scripts/` inventory and representative unit test | new report |
| 2 | `motherhack3r/Anthropic-Cybersecurity-Skills` | 0 | content tree `822878aa68d8a760149ce36542eb41c7aee429db` | README + representative defensive `SKILL.md` | exact-tree reuse; no duplicate report |
| 3 | `acumenix/Anthropic-Cybersecurity-Skills` | 0 | `efbbbba5e233089f8a95b722a6327ce9ae831246` / `822878aa68d8a760149ce36542eb41c7aee429db` | README + representative defensive `SKILL.md` | exact-tree reuse; no duplicate report |
| 4 | `itsjamessmith/Anthropic-Cybersecurity-Skills` | 0 | content tree `822878aa68d8a760149ce36542eb41c7aee429db` | README + representative defensive `SKILL.md` | exact-tree reuse; no duplicate report |
| 5 | `zrd4y/Anthropic-Cybersecurity-Skills` | 0 | content tree `822878aa68d8a760149ce36542eb41c7aee429db` | README + representative defensive `SKILL.md` | exact-tree reuse; no duplicate report |
| 6 | `fabioassuncao/agentskills` | 0 | `2883cf268e6919438d406025f517a97e21ca94f7` / `b0abc9218c2ea010dc7fbf269ffbb4e913efadd1` | README + both Skill bodies + reference template | 2 new reports |
| 7 | `liamlan/agentskills` | 0 | `8a6b9e1eb6493e892ea12814079aabae3e7e5d32` / `cb6e298e7da1c3a8bb8bcb5553f99a8bc36b9c6e` | no root README; both Skill bodies + reference inventory | 2 new reports |
| 8 | `lewislulu/html-ppt-skill` | 7731 | `f3a8435d3901697d5ac5e64d356c933637e43107` / `c7a57a16de00fb96b207188c4433630f1cde883e` | README, root Skill, `scripts/render.sh`, references/assets inventory | 1 new report |
| 9 | `NLP-planet/AgentSkills` | 0 | `32bdbca6c23a24a9ca6a3fc2037d66faf5ff2788` / `761f49f630d27497ca85cf36cf7ef5df344b7c96` | no root README; 3 unique Skill bodies, subproject README, scripts/references inventory | 3 new reports |
| 10 | `dsebastien/ai-skill-garmin` | 13 | `22bfebaf567c60cf134229c77682c334aa35df10` / `8227f0f870ced43de34d076797dd32f4830e1d8e` | README, Skill, endpoint reference inventory, implementation script | 1 new report |

## Repository analyses

### 1. `Player1Taco/morpheus-skill`

This is a forked operational inference Skill, not a prompt-only package. The pinned tree exposes a root `SKILL.md`, integration/deployment material and a substantial `scripts/` surface. The Skill declares local proxy ports, persistent services, credential handling, external inference/network endpoints and optional MOR/Base blockchain operations. A representative `bootstrap-client.test.mjs` was directly read: it tests fingerprint shape/determinism and proof-of-work behavior, but it also prints a `PASS` banner from the test source and explicitly leaves Redis integration and Base Sepolia E2E as future steps. The file existing is evidence of verification design, not a passing run.

The important architecture lesson is the authorization boundary: installation/invocation cannot imply blanket permission for service mutation, credentials, network calls or blockchain actions. Those effects need a policy layer above the Skill. This pinned tree differs from the previously reviewed `profbernardoj/morpheus-skill` tree in Batch 047, so tree identity was not used to suppress the new report.

### 2–5. Four Cybersecurity exact-tree identities

`motherhack3r`, `acumenix`, `itsjamessmith`, and `zrd4y` were individually identity/star checked and directly content-gated. Their observed content resolves to the same exact tree `822878aa68d8a760149ce36542eb41c7aee429db`; their README blob is the same 754-Skill / 26-domain / 5-framework snapshot, and the directly read representative `skills/analyzing-api-gateway-access-logs/SKILL.md` is the same defensive log-analysis body.

These identities therefore increase repository coverage but do not justify four duplicate Skill reports. Exact-tree reuse is applied only after direct content confirmation, not from repository name or fork metadata.

### 6. `fabioassuncao/agentskills`

The tree is small and auditable: two Skills, one reference template, no scripts/evals. `digital-product-analysis` forces an evidence-gathering phase before analysis, produces structured market/product/investment artifacts, calls for concrete sources and explicitly challenges weak assumptions. Its weakness is that calculations, source lineage and conclusion consistency are still prose-driven; there is no deterministic calculator/provenance schema/eval.

`domain-finder` has a useful evidence rule: a domain must not be presented as available until WHOIS is actually queried. It asks for a larger candidate pool and filters down to exactly ten validated outputs. However, WHOIS interpretation is encoded as prose string heuristics with no parser fixtures, retry budget, registrar/RDAP fallback or behavioral tests, so the verification contract is stronger than the implementation support.

### 7. `liamlan/agentskills`

There is no conventional root README. The pinned tree contains two A2A Skills plus focused references. `a2a-communication` separates standard A2A task/message/context mechanics from a custom low-code `input_request` / `input_response` extension. `a2a-orchestrator` decomposes orchestration into intent classification, intent-to-fields prefetch, field registry, resolver dispatcher, dependency resolution and low-code generation.

This is a useful architecture pattern because it makes resolution policy and dependencies explicit rather than embedding them in each subagent. It also calls for cycle checks, retries/timeouts/fallbacks and input validation. The limitation is that the TypeScript in the Skill is illustrative; the repository contains reference documents, not a runnable implementation/eval suite proving the custom extension or orchestration loop.

### 8. `lewislulu/html-ppt-skill`

This is the highest-star repository in this batch and a real implementation-heavy Skill: static HTML/CSS/JS runtime, 36 themes, 15 full-deck templates, 31 layouts, 47 animations, presenter-mode runtime, references and render/scaffold scripts. The README and Skill both expose internal inventory drift: several later sections/file-tree captions still say 14 full-deck templates while current top-level inventory says 15.

`scripts/render.sh` was directly read. It gives deterministic 1920×1080 headless screenshots but hard-codes the macOS Google Chrome path, making its validation path non-portable despite the underlying static deck format being portable. The repository includes `scripts/verify-output/` screenshots, but screenshots are artifacts, not a test result for this pinned revision unless regeneration/comparison is executed. No runtime/render test was executed in this batch.

### 9. `NLP-planet/AgentSkills`

There is no root README. The tree contains three unique Skill bodies: `drama-workflow`, `douyin-video-forge`, and `novel-director`; root `SKILL.md` and `drama-workflow/SKILL.md` are the same blob and are counted once as a unique body.

`drama-workflow` is a compact orchestration specification for chunking, parallel analysis and report consolidation. `novel-director` models long-running story state explicitly with `world_knowledge.json`, `chapter_index.json`, chapter files and drafts, which is a useful persistent-context pattern; however, the Skill itself promises file mutations without a repository-local implementation/eval demonstrating crash consistency or index/world-state synchronization.

`douyin-video-forge` is operational: browser collection, local media tools, optional transcription/API scripts, FFmpeg composition and recurring production plans. It has explicit human confirmation gates and says API credentials should stay out of chat, which is a good boundary. But browser/network/API/media side effects and recurring jobs still require upper-layer authorization/resource controls. The subproject has a README, PRD, examples, references and Python scripts; no repository-local behavioral eval/test suite was observed.

### 10. `dsebastien/ai-skill-garmin`

The repository uses a clean spec-oriented layout: `skills/garmin-connect/SKILL.md`, one TypeScript implementation, and an endpoint reference. The Skill is intentionally read-only with respect to Garmin data, uses environment credentials and documents local token storage with mode `0600`. The implementation directly contacts Garmin and fetches the mobile OAuth consumer pair from the garth-hosted S3 source, caches it for 24 hours, and falls back to an embedded public consumer pair if refresh fails.

The design is admirably small—single Bun file, no npm dependencies—but intentionally depends on an unstable unofficial Garmin surface. Its self-repair section acknowledges endpoint/credential drift. No unit/integration fixture suite or CI/eval was present in the pinned tree, so current compatibility remains unverified by this batch.

## Cross-repository findings

1. **Authorization remains a layer above Skills.** Morpheus and Douyin demonstrate why: a Skill can contain useful workflow logic while also touching credentials, local services, external networks, recurring jobs or paid/external APIs. Invocation is not sufficient authorization.
2. **Content-addressed reuse is necessary.** Four independently indexed Cybersecurity identities resolve to one already-reviewed tree. Repository identity is still tracked for coverage, but individual reports should follow actual content identity to avoid catalog inflation.
3. **Verification definitions are not verification results.** Morpheus contains tests and html-ppt contains verification screenshots; neither is counted as passing until executed at the pinned revision.
4. **Machine-readable state beats conversational memory.** `novel-director`'s world/index/chapter split and `liamlan`'s field/dependency registry are reusable patterns for long-lived agent state and orchestration.
5. **Inventory drift is measurable and should be linted.** `html-ppt-skill` contains 15 full-deck templates while several internal strings/captions still say 14. Inventory should be generated or checked from the tree rather than maintained manually.

## Batch result

- Qualified repository identities completed: **10**
- Direct `SKILL.md` reads: **14**
- Unique Skill bodies directly reviewed: **11**
- Unique Git trees represented: **7**
- New repository-scoped Skill reports: **10**
- Cumulative structure-reviewed repositories: **510**
- Cumulative repository-scoped Skill reports: **3036**
- Arithmetic remaining from frozen eligible basis 2088: **1578**
- Runtime/build/test/eval execution: **not_executed**
- Cross-repository canonical reconciliation: **pending**

The next unresolved indexed candidate after the completed content gates is `qishilong/agentskills-learn`; it is not pre-declared qualified until its own live content gate is completed.