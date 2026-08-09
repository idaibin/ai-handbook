# Agent Skills Deep Analysis — Batch 054

- observed_at: `2026-08-09`
- status: `structure-reviewed`
- runtime_validation: `not_executed`
- queue_source: `sources/catalog/batches/agentskills-created-2026-04-15-deterministic.json` + `sources/catalog/batches/agentskills-created-2026-04-16-deterministic.json`
- qualified_repository_identities_completed: `10`
- root_readmes_directly_read: `10`
- skill_or_equivalent_files_directly_read: `35`
- direct_unique_skill_body_reviews: `31`
- unique_git_trees: `9`
- new_repository_scoped_skill_reports: `30`
- completion_rule: repository identity and current Stars were verified, a fixed revision/tree was established, and actual repository content was read before completion. Metadata-only candidates were not promoted.

## Summary

Batch 054 advances the qualified queue by ten repository identities. One indexed candidate, `keeea/minimalist-entrepreneur-skills`, was encountered and revalidated but was not counted again because it was already structure-reviewed in Batch 023. Five metadata candidates were rejected after content gates as specification/reference/tooling/adjacent results, and one adjacent result was held. No repository code, tests, evals, builds, browser flows, live APIs, external services, publishing actions, or agent workflows were executed.

| Repository | Stars | Fixed revision | Fixed tree | New reports | Result |
|---|---:|---|---|---:|---|
| `priyanshuz/Anthropic-Cybersecurity-Skills` | 0 | `780757902b7faeb8d77d034d4faead329cdd6539` | `c814d5e74a58a6281a0d3763d7088945b59aee6d` | 0 | structure-reviewed; Skill content reused from prior 754-Skill snapshot |
| `hello121384/Anthropic-Cybersecurity-Skills` | 0 | `9e8a8cda8080bf6f9f02b40c3035c55813e0ba39` | `4537b50decc9c1a4614cfadec02b30d0007944fa` | 0 | structure-reviewed; exact-tree reuse |
| `Raavi29/Anthropic-Cybersecurity-Skills` | 0 | `9e8a8cda8080bf6f9f02b40c3035c55813e0ba39` | `4537b50decc9c1a4614cfadec02b30d0007944fa` | 0 | structure-reviewed; exact-tree reuse |
| `aaditagrawal/agentskills` | 0 | `0c2969eeb90c1294be55fae0680e794e4e5e2b52` | `a2516674d294c7d393a3c735412246e91714f68a` | 5 | structure-reviewed |
| `JarvAmrit/AgentSkills` | 1 | `ca6b7e51a7518ce58b5490e147448df5663500ac` | `cf515f96f8aba313a25b1f99ee75e761cb5260e8` | 4 | structure-reviewed |
| `VTSTech/skills` | 6 | `029c965c57aca8bc2b713072b04e59c560d15e6a` | `eae476da0c22285b14ac0a03d4f44ebbc5eb08ab` | 5 | structure-reviewed |
| `fiorellarmartins/skills` | 0 | `7980741f1209fda04f9294ccd7cc0e86e4bc979b` | `90173555363a9111c52c9f36b3e3e9499a379756` | 9 | structure-reviewed |
| `dsebastien/ai-skill-scholar` | 10 | `15ce494a761232f68610b261c9e4c8001e2c83fd` | `f59d8f4b1de2fb483b253cd1ec389f79d7407014` | 3 | structure-reviewed |
| `EliseT123/-VTSTech-Modular-Agent-skills` | 0 | `e48c68efdfe02b75c1b34745171788cac3d65b6b` | `93e68d187aa6d1f200ea5160846408176d61ecc6` | 1 | structure-reviewed; two exact Skill blobs reused from VTSTech |
| `dsebastien/ai-skill-arxiv` | 4 | `bbbe55b4c91ecd0555b819e3f547a7a3f379c8f5` | `4ecfd00858b4604e1ccc8569fec5bed5b7566993` | 3 | structure-reviewed |

Stars are point-in-time observations from GitHub during this run.

## Repository analyses

### 1. `priyanshuz/Anthropic-Cybersecurity-Skills`

**Verified**

- Identity, 0 Stars, README, fixed revision/tree, and a representative `SKILL.md` were directly checked.
- The representative Skill body matches the previously reviewed 754-Skill content snapshot. This repository tree is distinct because of ancillary repository workflow content, not because the inspected Skill body changed.
- The repository therefore increases repository-identity coverage without duplicating an individual Skill report.

**Not verified**

- Runtime behavior, security-tool execution, CI/eval pass status, or operational correctness.

### 2–3. `hello121384/Anthropic-Cybersecurity-Skills` and `Raavi29/Anthropic-Cybersecurity-Skills`

**Verified**

- Each identity and current Stars value was checked independently.
- Each README and the same representative Skill path were directly read at the fixed revision.
- Both resolve to exact tree `4537b50decc9c1a4614cfadec02b30d0007944fa`, already reviewed in Batch 053. Exact content reuse is recorded only after per-repository content gates.

**Not verified**

- Any security operation, external tooling, CI execution, or behavioral evaluation.

### 4. `aaditagrawal/agentskills`

**Verified**

- Fixed content contains five skills: `no-useeffect`, `no-slop`, `ai-taste`, `md-site`, and `openrouter-expert`.
- README currently documents only three, so the repository has a concrete inventory drift: 3 documented versus 5 actual Skill packages.
- `openrouter-expert` includes helper scripts that refresh live documentation/model inventories and fail when source retrieval fails. This is a useful source-of-truth pattern because stale model knowledge is treated as a validation failure rather than silently accepted.
- No repository-local test/eval workflow was found in the fixed tree.

**Inference**

- `no-useeffect` is intentionally opinionated and can over-constrain valid framework lifecycle use if treated as an absolute rule instead of a routing heuristic.

### 5. `JarvAmrit/AgentSkills`

**Verified**

- README presents two reusable agent workflows, while the fixed tree contains four: two Azure DevOps workflows plus SonarQube and Veracode remediation workflows.
- This is another inventory drift: 2 documented versus 4 actual equivalent skill/agent definitions.
- The workflows combine repository changes, tests, branch/PR operations, issue/work-item mutation, and credential-backed external integrations. They contain local safety/confirmation guidance, but the side-effect surface is broader than a read-only Skill.

**Inference**

- Authorization for external writes, branch changes, PR creation, or service mutation should be enforced above the individual workflow so activation does not implicitly grant all side effects.

**Not verified**

- Azure DevOps, SonarQube, Veracode, Git, test, or PR execution.

### 6. `VTSTech/skills`

**Verified**

- Five Skills were directly read: `acp`, `codebase-audit`, `godot-engine`, `ps2-elf`, and `terminal-video-recorder`.
- `acp` encodes a useful execution lifecycle: check/control state, log before execution, complete after execution, surface orphaned work, and retain agent ownership. It also documents a development-default security posture that should not be assumed safe for externally exposed deployments.
- `codebase-audit` separates a reusable orientation brief from a detailed evidence-grounded audit, but its load mode treats an existing `brief.md` as authoritative without binding it to a verified repository revision/content fingerprint.
- `terminal-video-recorder` has a real shell implementation, but its `scripts/tests/test-demo.sh` is a demo workload rather than an assertion-based regression test. The recorder also assumes a specific display/output layout and host utilities, so the README's broad statement that the collection has no runtime dependencies overgeneralizes the actual repository.
- `ps2-elf` was reviewed only at the structural/domain-workflow level; no operational reverse-engineering actions were executed.

**Not verified**

- ACP service behavior, codebase audit accuracy, Godot behavior, binary-analysis behavior, video rendering, or test pass status.

### 7. `fiorellarmartins/skills`

**Verified**

- README defines a portable Skill contract centered on precise triggers, procedures, pitfalls, verification, and no embedded secrets.
- Nine actual/example Skill bodies were read: one `eps-audit` example plus eight medical-insurance workflow Skills.
- The medical-insurance package forms an explicit pipeline: intake → independent administrative/medical/financial audits → consolidation → versioned document generation → human fix/review loop → outbound delivery.
- Strong engineering patterns include citable evidence fields, versioned documents, idempotency/state labels, independent sub-auditors, append-style audit logs, and a human-role gate before final approval/delivery.
- The repository contains natural-language procedures rather than an executable validation suite for the stated regulatory, clinical, financial, or legal rules.

**Inference**

- High-stakes rule catalogs, regulation references, thresholds, and external workflow contracts need machine-verifiable version/freshness provenance before production reliance. Outbound email and case-state mutation also require centralized authorization.

**Not verified**

- Medical, financial, regulatory, or legal correctness; Gmail/API behavior; document rendering; any live case outcome.

### 8. `dsebastien/ai-skill-scholar`

**Verified**

- Three Skills and their Python implementations were read: `scholar-search`, `scholar-citations`, and `literature-review`.
- The design cleanly separates deterministic mechanics (OpenAlex fetching, normalization, deduplication, state files) from agent judgment (screening and synthesis).
- The review workflow persists `state.json`, candidates, shortlist, fetch plan, and final synthesis, providing a reproducible/resumable research structure.
- Source-level documentation drift remains inside `literature-review`: parts of the Skill/script comments still refer to Semantic Scholar/S2 even though the repository has migrated to OpenAlex.
- The shared timestamp-file throttle is not protected by an inter-process lock, so simultaneous processes can race despite the cross-process-coordination intent.
- No repository-local tests/evals/workflows were present in the fixed tree.

**Not verified**

- OpenAlex network behavior, search quality, citation completeness, literature-review quality, or runtime correctness.

### 9. `EliseT123/-VTSTech-Modular-Agent-skills`

**Verified**

- GitHub identifies this repository as a fork; the fixed tree contains three Skills: `acp`, `codebase-audit`, and `ps2-elf`.
- `acp` and `ps2-elf` are exact blob matches to the reviewed VTSTech copies, so no duplicate reports were created.
- `codebase-audit` has a distinct blob but is semantically the same upstream content with a trivial textual/frontmatter punctuation delta; one content-addressed variant report is retained.
- README and Skill metadata continue to identify/link the upstream `VTSTech/skills`, so fork provenance is not fully rewritten.

**Not verified**

- Runtime behavior or any implied upstream synchronization guarantee.

### 10. `dsebastien/ai-skill-arxiv`

**Verified**

- Three Skills and all three Python implementations were read: `arxiv-search`, `arxiv-analyze`, and `arxiv-monitor`.
- The suite separates discovery, full-text acquisition, and persistent monitoring. Scripts use standard-library Python, structured JSON, persistent state, and bounded seen-ID storage.
- `arxiv-analyze` uses a tiered acquisition strategy, disk cache, and atomic replacement for rate-limit state. The fallback extraction path for environments lacking the safer tar extraction filter can fall back to unrestricted archive extraction; that should not be treated as a safe default for untrusted archives.
- `arxiv-monitor` uses atomic file replacement but no file locking around read-modify-write state, so concurrent monitor invocations can lose updates. It intentionally serializes `check-all` to respect service pacing.
- No repository-local tests/evals/workflows were present in the fixed tree.

**Not verified**

- arXiv/API availability, fetch fallback success, monitor correctness under live concurrency, paper-analysis quality, or runtime validation.

## Queue corrections and held candidates

The following entries were inspected but not used to fill the ten completed identities:

- `keeea/minimalist-entrepreneur-skills`: actual README and all ten Skill bodies were re-read, but repository identity was already completed in Batch 023, so it was not double-counted.
- `wihl520/agentskills`, `Balakier620/agentskills`, `xrey167/agentskills`: content gates showed Agent Skills specification/documentation/reference-SDK lineage rather than independent Skill collections.
- `harishrajora/agentskillsforall`: tooling/site repository with vendored Skill material; held as adjacent tooling rather than promoted as an independent collection.
- `DaceJoy/upstream-agentskills`: specification/reference lineage, not an independent Skill collection.
- `TheWillMundy/remotion-video-orchestrator`: remains `adjacent_search_hit`; no promotion by assumption.

The next raw indexed candidate after the completed `dsebastien/ai-skill-arxiv` entry is `jovd83/context-density-optimizer` (`adjacent_search_hit`, content gate still required). The next provisionally qualified entry after the adjacent block is `fr4ngou/claude-code-longrun-skill`.

## Cross-batch findings

1. **Queue identity dedup must happen before completion accounting.** Re-encountering `keeea/minimalist-entrepreneur-skills` exposed a prior Batch-023 completion; re-reading it does not justify incrementing repository totals twice.
2. **README inventory is not authoritative by itself.** `aaditagrawal/agentskills` and `JarvAmrit/AgentSkills` both contain more actual reusable definitions than their README inventories state.
3. **Content-addressed reuse prevents fork inflation.** Exact Skill blobs and exact Git trees are reused only after each repository identity passes an actual content gate.
4. **Mechanics and judgment benefit from separation.** The scholarly/arXiv suites keep retrieval/state machinery in scripts while leaving screening/synthesis to the agent; this produces a clearer validation boundary than prose-only orchestration.
5. **Presence of a test-named file is not a passing test.** VTSTech's terminal-recorder `tests/test-demo.sh` is a demo input without assertions; no validation status was upgraded.
6. **Operational authorization belongs above individual Skills.** Several repositories can mutate external systems, send messages, create PRs, or change persistent workflow state. Activation alone should not imply authorization.

## Validation boundary

`structure-reviewed` means repository identity/Stars were checked, a fixed revision/tree was recorded, root documentation and Skill/equivalent definitions were directly inspected, and scripts/references/eval surfaces were read when available and material. It does **not** mean any repository runtime, test, build, browser flow, external API, security tool, medical workflow, publisher, or eval suite executed successfully.
