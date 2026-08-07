# Agent Skills Deep Analysis — Batch 023

- observed_at: `2026-08-07`
- status: `structure-reviewed`
- runtime_validation: `not_executed`
- queue_source: `sources/catalog/batches/agentskills-pages-4-6.json`
- repository_queue_entries_reviewed: `10`
- content-qualified repositories after review: `9`
- content-rejected / held repositories: `1`
- repository-scoped skill reports: `77`
- completion rule: a repository is counted as structure-reviewed only after repository identity, current star observation, README/root structure, and local skill definitions were inspected; metadata-only candidates are not marked complete.

## Summary

This batch performed source/content review only. No third-party installer, API, model, browser automation, publisher, image-generation provider, test runner, CLI, shell installer, external service, or remote agent was executed. Test/eval assets being present is recorded as source evidence only and is not treated as a passing runtime result.

| Repository | Stars observed | Local skill reports | Content-level classification | Result |
|---|---:|---:|---|---|
| `drunkcoding/AgentSkillsArxiv` | 4 | 19 | `skill_collection_research_developer_tooling` | structure-reviewed |
| `TheColonyAI/colony-skill` | 7 | 1 | `single_skill_external_social_api` | structure-reviewed |
| `ahmadharis/agentskills` | 2 | 5 | `skill_collection_azure_devops` | structure-reviewed |
| `JayDoubleu/agentskills` | 2 | 2 | `skill_collection_code_review_spec_workflow` | structure-reviewed |
| `dglijin-oss/xuanji-five-skills` | 0 | 5 | `skill_collection_cultural_divination` | structure-reviewed |
| `keeea/minimalist-entrepreneur-skills` | 15 | 10 | `skill_collection_business_methodology` | structure-reviewed |
| `sorafujitani/skills` | 7 | 16 | `skill_collection_engineering_workflows` | structure-reviewed |
| `parilsanghvi/AgentSkills` | 0 | 0 | `placeholder_or_empty_skill_scaffold` | content-rejected / held |
| `fn2ai/fn2-openclaw-skill` | 11 | 1 | `single_skill_market_research_api` | structure-reviewed |
| `wuchubuzai2018/expert-skills-hub` | 34 | 18 | `skill_collection_chinese_media_and_media_generation` | structure-reviewed |

Star counts above were observed from the public GitHub repository pages during this review. They are point-in-time observations and may change later.

## Repository analyses

### 1. `drunkcoding/AgentSkillsArxiv`

**Verified**

- Repository identity: GitHub repository id `1161986054`, default branch `main`.
- The repository contains local skill roots under `skills/` plus `openclaw/`, infrastructure scripts, and a community-skills submodule.
- Direct inspection found 19 local standalone `SKILL.md` definitions. `tutor-core` is supporting material rather than a standalone skill, and the community submodule is not counted as local repository-scoped skill output.
- The installer `infra/scripts/install-skills.sh` discovers directories by the presence of `SKILL.md`, supports nested skill directories, makes local install names deterministic, gives local skills precedence over same-named community skills, validates frontmatter before installation, and uses symlinks with conflict/safety handling.
- Several skills use progressive references and scripts; some require external services or specialized toolchains. Those runtime dependencies were not invoked.

**Inference**

- This repository is stronger as a research/developer-tooling skill library than as a uniform general-purpose catalog because the skill set clusters around academic work, code/search tooling, GPU tutoring, memory/context tooling, and remote-agent integration.

**Not verified**

- Installer execution, Python validator results, GPU kernels, external services, remote-agent flows, and any runtime behavior.

### 2. `TheColonyAI/colony-skill`

**Verified**

- Repository identity: GitHub repository id `1201895430`, default branch `main`.
- Root structure contains `scripts/`, `README.md`, `SKILL.md`, and contribution material.
- It is one large Agent Skill rather than a multi-skill collection. The README and `SKILL.md` describe authenticated network operations for a collaborative agent platform, including read/write social actions, notifications, directory/search, signed webhook integration, and MCP support.
- The skill has a large external-side-effect surface and requires external authentication. Source was read only; no account, key, network request, post, message, marketplace action, webhook, or MCP operation was performed.

**Inference**

- The main engineering risk is not skill-file structure but the breadth of authenticated side effects delegated through one activated skill. A consumer should treat it as an integration skill requiring explicit operation boundaries.

**Not verified**

- External API correctness, authentication flow, scripts runtime behavior, rate limits, or service availability.

### 3. `ahmadharis/agentskills`

**Verified**

- Repository identity: GitHub repository id `1177278088`, default branch `main`.
- README documents five Azure DevOps-oriented skills and dependencies on Azure CLI, the Azure DevOps extension, and Git.
- Directly read all five `SKILL.md` bodies: `azure-work`, `azure-pr`, `pr-complete`, `azure-pr-comments`, and `azure-work-complete`.
- Content-level inconsistency: `pr-complete` describes cleanup as read-only while the procedure can delete local branches with Git. This is a source-documentation mismatch and should not be interpreted as a read-only workflow.

**Not verified**

- Azure authentication, CLI commands, pull-request mutation behavior, branch deletion, or any integration tests.

### 4. `JayDoubleu/agentskills`

**Verified**

- Repository identity: GitHub repository id `1130384024`, default branch `main`.
- README exposes two skills under `.claude/skills/`.
- `roast-review` wraps an external-model review workflow and then requires findings to be validated against actual repository files/lines rather than trusting model output directly.
- `spec-driven-development` defines a constitution → specification → clarification → plan → tasks → implementation workflow, with TDD-oriented execution and referenced templates/philosophy material.

**Inference**

- `roast-review` has a useful verification pattern because model output is explicitly treated as candidate findings rather than ground truth.

**Not verified**

- External model invocation, wrapper scripts, repomix output, tests, or generated specifications.

### 5. `dglijin-oss/xuanji-five-skills`

**Verified**

- Repository identity: GitHub repository id `1195918665`, default branch `main`.
- Five local skill-equivalent directories were inspected: `ze-ri-skill`, `ziwei-skill`, `taiyi-skill`, `fengshui-skill`, and `liuren-skill`.
- These files are domain/cultural-divination workflows rather than scientifically validated predictive systems.
- Representative `index.js` implementation files show intentionally simplified deterministic heuristics. `ziwei-skill/index.js` also contains apparent source-level syntax/character defects that may prevent normal JavaScript parsing.

**Inference**

- The README/skill narratives are much richer than the underlying simplified implementations; consumers should not infer traditional-system completeness or scientific validity from the prose.

**Not verified**

- JavaScript parsing/execution or output correctness.

### 6. `keeea/minimalist-entrepreneur-skills`

**Verified**

- Repository identity: GitHub repository id `1212344894`, default branch `main`.
- Ten root-level `SKILL.md` definitions were directly read.
- The collection is primarily text-based business methodology: community discovery, idea validation, MVP scoping, early customers, pricing framing, marketing planning, process design, sustainable growth, company values, and a review/checkpoint skill.
- No central executable/eval framework was found in the reviewed material.

**Not verified**

- Business outcomes or effectiveness claims; the repository was reviewed as reusable methodology, not as validated commercial performance evidence.

### 7. `sorafujitani/skills`

**Verified**

- Repository identity: GitHub repository id `1163128950`, default branch `main`.
- Sixteen direct `SKILL.md` bodies were read. The collection spans documentation learning, read-only design/review, issue analysis, local repository discovery, PR workflows, debugging, property-based testing, packaging, TypeScript lint-rule mapping, and meta execution playbooks.
- Many skills explicitly separate planning/analysis from mutation and use references to keep the activated `SKILL.md` focused.
- `skill-zip` references a packaging script; several testing/review skills describe executing validations, but no command was executed during this review.

**Inference**

- This collection shows a comparatively strong pattern of explicit operational boundaries (read-only vs write/test operations) and progressive reference loading.

**Not verified**

- Property-based tests, PR operations, filesystem searches, packaging script output, or any external web research behavior.

### 8. `parilsanghvi/AgentSkills`

**Verified**

- Repository identity: GitHub repository id `1137655095`, default branch `main`.
- Actual repository content consists only of a minimal README: “Open Source skills for specialized agents”. No local `SKILL.md` or equivalent skill package was present in the inspected repository content.

**Content-level correction**

- The index-stage `skill_collection` classification is not supported by current repository contents. This entry is therefore held as `placeholder_or_empty_skill_scaffold` with 0 skill reports and is not treated as a content-qualified skill repository.

### 9. `fn2ai/fn2-openclaw-skill`

**Verified**

- Repository identity: GitHub repository id `1273907635`, default branch `main`.
- One `fn2` skill was directly read. It wraps an external market/economy research service and recurring research-agent management through a bundled Python standard-library CLI.
- `scripts/fn2.py` implements authenticated HTTP/SSE handling, CLI commands, scheduling payload construction, output cleanup, status/error mapping, and JSON output without third-party Python dependencies.
- `references/api.md` documents the CLI/API contract.
- `tests/test_cli.py` contains offline mocked unit tests for citation cleanup, schedule construction, HTTP handling, SSE parsing, and command behavior. The tests were read but not executed.

**Not verified**

- External research quality, live market data, service/API availability, agent scheduling, or test-suite pass status.

### 10. `wuchubuzai2018/expert-skills-hub`

**Verified**

- Repository identity: GitHub repository id `1151351528`, default branch `main`.
- Current README lists 18 skills, not 15. All 18 listed `SKILL.md` bodies were directly read in this review.
- The repository is heterogeneous: image-generation/editing integrations, PDF/image utilities, Chinese-content trend/search/publishing workflows, presentation/design workflows, EARS requirement rewriting, OKR writing, project knowledge hierarchy, and project-wiki generation.
- Several skills depend on external providers/credentials and network access; others are local utilities or methodology-only skills.
- Representative implementation inspection of `image-resizer/scripts/resize_image.js` shows a real Sharp-based resize/compress pipeline with dimension calculation, crop/fit modes, format conversion, target-size compression attempts, and fallback resolution reduction.
- Source-level issue in the representative image-resizer script: short option `-h` is assigned both to height and help in the switch; because the earlier `-h` height case wins, the short help alias is effectively shadowed.
- The CSDN publishing skill handles authenticated publishing state and therefore has a materially higher side-effect/credential risk than read-only content-trend skills.
- `haizei-project-wiki-generator` is a multi-phase analysis/planning/generation workflow with explicit user-confirmation gating before document generation and extensive progressive references.

**Inference**

- Quality and maintenance maturity vary substantially by skill; the repository should be evaluated per skill rather than assigned one uniform quality level.

**Not verified**

- Any external image provider, content site, publishing endpoint, scraping behavior, PDF conversion, browser rendering, VitePress generation, or runtime validation.

## Cross-batch findings

1. **Index metadata needs content correction.** `parilsanghvi/AgentSkills` demonstrates why metadata-only completion is unsafe: the indexed name/classification suggested a collection, while the actual repository currently contains no skill package.
2. **Repository README counts can drift.** `wuchubuzai2018/expert-skills-hub` currently lists 18 skill entries; the earlier provisional count of 15 was stale within this run and was corrected after direct README inspection.
3. **Tests/evals are evidence surfaces, not passing results.** `fn2ai/fn2-openclaw-skill` contains an offline unit-test suite, but this batch records only its presence and design because the runner was not executed.
4. **Side-effect boundaries matter.** Some skills are read-only/methodology oriented while others can publish, mutate Git state, or call authenticated external services. Reports preserve that distinction instead of treating every `SKILL.md` as equivalent.
5. **Narrative capability can exceed implementation.** `dglijin-oss/xuanji-five-skills` uses rich domain descriptions while representative JavaScript implementations explicitly simplify the underlying logic; runtime and domain-validity claims are therefore withheld.

## Validation boundary

`structure-reviewed` means: repository identity and current star observation checked; actual README/root structure read; local `SKILL.md` or equivalent definitions directly inspected; scripts/references/tests inspected when surfaced and material; repository-scoped reports written. It does **not** mean any third-party runtime, service, CLI, model, build, test, eval, browser, publisher, or API was executed successfully.
