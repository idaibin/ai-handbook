# Agent Skills Deep Analysis — Batch 046

- Observed: 2026-08-09
- Scope: existing deterministic indexed queue
- Completion rule: repository identity + observed Stars + pinned revision + actual repository content reads. Metadata-only completion is prohibited.
- Runtime/build/test/eval execution: not executed
- Canonical reconciliation: pending

## Result

| Metric | Value |
|---|---:|
| Qualified repositories completed | 10 |
| README direct reads | 10 |
| `SKILL.md` direct reads | 11 |
| Direct unique skill bodies reviewed | 6 |
| Unique Git content trees | 6 |
| New canonical skill reports | 2 |
| Cumulative structure-reviewed repositories | 460 |
| Cumulative repository-scoped skill reports | 2929 |
| Frozen eligible basis | 2088 |
| Arithmetic remaining estimate | 1628 |

The ten repository identities below were not marked complete until their repository content had been read at a pinned Git revision. Exact-tree mirrors were re-read per repository identity, then deduplicated at the content/report layer.

## Completed repositories

| Repository | Stars | Pinned revision | Git tree | Direct content gate | Disposition |
|---|---:|---|---|---|---|
| `gigantsc/skills-hermes-` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | `32d2d4cb75cf113fbc8e145d7c52672832e34a2d` | README + `clean-architecture/SKILL.md` | Existing Wondel canonical content |
| `NailRunner/skills-base-2604` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | `32d2d4cb75cf113fbc8e145d7c52672832e34a2d` | README + `clean-architecture/SKILL.md` | Existing exact-tree content |
| `SGuibord/chainlink-agent-skills` | 0 | `bada72c0fbdba616412c65c239d69e4f94154abd` | `c78a0a34f3b952063f0bc45f87820615f4501a01` | README + both Skill bodies + CCIP reference + eval README/rubric | CRE maps existing; revised CCIP body gets new report |
| `raykao/obsidian-plugin-skill` | 0 | `7633460c8bc776030936d86d737f9e2679eeb7b6` | `7fb97ded5a5248b33b139cbf055ceb2b18e85dd9` | README + `obsidian-plugin/SKILL.md` + API reference | New report |
| `michaelgallese3-coder/Anthropic-Cybersecurity-Skills` | 0 | `d388b31205a9d31c21b6df6f28324075ec4f47a1` | `06755497f0ed54f925cc46b8cbc47cd6778ef7c6` | README + representative Skill + validator workflow | Existing Cybersecurity lineage; distinct formatting revision |
| `0xhexrecon/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative Skill + recursive tree + validator workflow | Existing Cybersecurity lineage |
| `hnizil/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative Skill | Existing exact-tree content |
| `imperius361/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative Skill | Existing exact-tree content |
| `suriyaJaboon/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative Skill | Existing exact-tree content |
| `casky-ai/Anthropic-Cybersecurity-Skills` | 0 | `888bbe4c6e4e54e026874cbf6072e84f0cfd3b7a` | `f22ca9d1c273c9278ef0a2aababa626552bd772b` | README + representative Skill + validator workflow | Existing Cybersecurity lineage; representative Skill body matches current shared body |

## Verified findings

### 1. Wondel-derived identities are duplicate repository coverage, not new Skill content

`gigantsc/skills-hermes-` and `NailRunner/skills-base-2604` resolve to the same pinned revision and Git tree. Their README and representative `clean-architecture` Skill were independently read. They therefore count as two repository identities reviewed but zero new canonical Skill reports.

### 2. `SGuibord/chainlink-agent-skills` contains a real CCIP revision

The CCIP body differs from the earlier `chethanuk/chainlink-agent-skills` canonical body: the pinned SGuibord revision adds MCP metadata/routing and a dedicated `references/ccip-mcp.md`. The repository also contains Promptfoo-oriented eval documentation and a must-pass rubric. These eval definitions were read, not executed. The safety design still separates read-only work from side-effecting actions and uses explicit preflight/confirmation boundaries. `chainlink-cre-skill` maps to the already-reviewed canonical lineage; the revised CCIP body receives one new report.

### 3. `raykao/obsidian-plugin-skill` is a procedural/reference Skill, not an executable harness

The repository contains a focused `SKILL.md` plus a substantial API reference. At the pinned tree, no repository-local scripts, tests, or eval harness were found. Its primary value is workflow/API guidance, while freshness and API compatibility remain document-maintenance risks without automated contract validation.

### 4. Cybersecurity mirrors were content-gated without converting inventory into synthetic completions

All six Cybersecurity repository identities had their own README and representative `SKILL.md` read at the pinned revision. Three distinct repository trees were observed across those six identities. The representative Skill has two blob variants: the Michael Gallese fork uses an older frontmatter formatting/content variant, while the `0xhexrecon`/shared-tree and `casky-ai` versions share the same representative Skill blob. The generated repository inventory advertises hundreds of Skills, but this batch does not convert that inventory count into body-level analysis reports.

The `validate-skills.yml` workflow was read for each distinct current lineage where present. It checks frontmatter fields, kebab-case naming, name length, duplicate Skill names and aggregate counts. This is a structural quality gate only; it does not validate cybersecurity behavioral accuracy, safety, or real-world efficacy. No workflow, test, script, build or eval was executed in this batch.

## Validation boundary

- Repository metadata: verified through GitHub.
- Stars: observed directly for each completed repository.
- Revisions/trees: pinned before content analysis.
- README / Skill content: directly read for every completed identity.
- References/evals/scripts: inspected when available and relevant to the unique content tree.
- Runtime/build/tests/evals: **not executed**.
- Historical cross-repository canonical reconciliation: **pending**.

The `1628` remaining figure is only `2088 - 460` on the frozen eligible basis. It is not a reconciled unique-repository remainder.

## Queue resume

Next unresolved qualified identity: `hanul93/Anthropic-Cybersecurity-Skills`.
