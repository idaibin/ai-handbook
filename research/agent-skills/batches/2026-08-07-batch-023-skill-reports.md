# Repository-scoped Skill Reports — Batch 023

- observed_at: `2026-08-07`
- repository reports: `10`
- individual skill reports: `77`
- status: `structure-reviewed`
- runtime_validation: `not_executed`

Each row below is a repository-scoped report for one directly inspected `SKILL.md` or equivalent local skill definition. `Runtime` is intentionally `not executed` throughout this batch.

## `drunkcoding/AgentSkillsArxiv` — 19 reports

| # | Skill | Verified source-level capability | Scripts / references / dependencies | Runtime |
|---:|---|---|---|---|
| 1 | `academic-grant-proposal` | Structured academic grant-proposal workflow with proposal-section guidance and evidence-oriented drafting. | Progressive references; academic-domain templates/guidance. | not executed |
| 2 | `academic-rebuttal` | Reviewer-response/rebuttal workflow that organizes comments, responses, and revisions. | Reference-backed academic workflow. | not executed |
| 3 | `academic-reviewer` | Academic review checklist/workflow for evaluating manuscripts and producing structured feedback. | Text/reference driven. | not executed |
| 4 | `academic-writing` | Academic writing workflow emphasizing structure, evidence, revision, and publication-oriented prose. | Reference-backed. | not executed |
| 5 | `ast-grep` | Source search/refactoring guidance around AST-aware search rather than plain text matching. | External AST-search CLI dependency. | not executed |
| 6 | `auto-gpu-kernel` | Workflow for developing/iterating GPU kernels with correctness/performance verification stages. | Specialized GPU toolchain and scripts. | not executed |
| 7 | `better-grep` | Search workflow choosing stronger structural/text search patterns and narrowing result sets. | Search tooling dependency. | not executed |
| 8 | `citation-convert` | Academic citation-format conversion/normalization workflow. | Citation/reference data processing. | not executed |
| 9 | `conference-plot` | Publication/conference-oriented plotting workflow with style/figure guidance. | Plotting utilities/references. | not executed |
| 10 | `cuda-tutor` | CUDA tutoring/explanation workflow using progressive teaching and examples. | CUDA environment expected for practical exercises. | not executed |
| 11 | `cuda-tutor-setup` | Environment/setup companion for CUDA tutoring workflows. | CUDA/toolchain setup dependencies. | not executed |
| 12 | `function-dep-search` | Function/dependency discovery workflow for tracing code relationships. | Script-backed source analysis. | not executed |
| 13 | `mem0` | Guidance for integrating/using a memory service in agent workflows. | External service/library dependency. | not executed |
| 14 | `openviking` | Context/memory-oriented integration workflow for an external tool/service. | External runtime dependency. | not executed |
| 15 | `triton-tutor` | Triton GPU-programming tutoring workflow. | Triton/GPU environment expected for execution. | not executed |
| 16 | `triton-tutor-setup` | Environment/setup companion for Triton tutoring. | Triton/GPU toolchain dependency. | not executed |
| 17 | `tutor-handouts` | Produces/supports reusable tutor handout material for the GPU-tutoring workflow. | Supporting references/assets. | not executed |
| 18 | `openclaw-remote-bridge` | Remote-agent bridge workflow with explicit external-runtime integration. | Script/external-service dependent; side-effectful. | not executed |
| 19 | `openclaw-remote-dispatch` | Remote task-dispatch workflow with scripts for job/task coordination. | Script-heavy external integration; side-effectful. | not executed |

**Repository note:** installer source was directly inspected. It discovers skills by `SKILL.md`, handles nested names, validates frontmatter, prefers local definitions over same-named community entries, and installs by symlink with conflict checks.

## `TheColonyAI/colony-skill` — 1 report

| # | Skill | Verified source-level capability | Scripts / references / dependencies | Runtime |
|---:|---|---|---|---|
| 1 | `the-colony` | Single large integration skill for authenticated collaborative-platform actions: reading/writing content, notifications, search/directory, webhook/MCP integration, and other account-scoped actions. | Root `scripts/` exists; external authenticated network service required. Large side-effect surface. | not executed |

## `ahmadharis/agentskills` — 5 reports

| # | Skill | Verified source-level capability | Scripts / references / dependencies | Runtime |
|---:|---|---|---|---|
| 1 | `azure-work` | Azure DevOps work-item workflow for reading/working with assigned items and project context. | Azure CLI + Azure DevOps extension + Git. | not executed |
| 2 | `azure-pr` | Azure DevOps pull-request workflow covering PR context and review-oriented operations. | Azure CLI/DevOps extension. | not executed |
| 3 | `pr-complete` | Local cleanup/completion flow after PR work. Source can delete local branches despite prose calling cleanup read-only. | Git commands; documentation/behavior mismatch noted. | not executed |
| 4 | `azure-pr-comments` | Workflow for retrieving and acting on Azure DevOps PR comments. | Azure CLI/DevOps extension. | not executed |
| 5 | `azure-work-complete` | Workflow for completing/closing work associated with Azure DevOps items. | Azure CLI/DevOps extension. | not executed |

## `JayDoubleu/agentskills` — 2 reports

| # | Skill | Verified source-level capability | Scripts / references / dependencies | Runtime |
|---:|---|---|---|---|
| 1 | `roast-review` | External-model code-review workflow followed by independent validation of candidate findings against actual files/lines. | Python wrapper, external model CLI/service, repomix; verification step is explicit. | not executed |
| 2 | `spec-driven-development` | Constitution → specification → clarification → plan → tasks → implementation workflow with TDD orientation. | References include templates/philosophy material. | not executed |

## `dglijin-oss/xuanji-five-skills` — 5 reports

These are cultural/divination-oriented workflows. They are reported as repository capabilities, not as scientifically validated predictive methods.

| # | Skill | Verified source-level capability | Scripts / references / dependencies | Runtime |
|---:|---|---|---|---|
| 1 | `ze-ri-skill` | Date-selection themed workflow with a simplified deterministic JavaScript implementation. | `index.js` directly inspected; simplified heuristics. | not executed |
| 2 | `ziwei-skill` | Ziwei-themed workflow backed by simplified JavaScript logic. | `index.js` directly inspected; apparent source-level syntax/character defects observed. | not executed |
| 3 | `taiyi-skill` | Taiyi-themed structured interpretation workflow. | Local JS implementation referenced by skill. | not executed |
| 4 | `fengshui-skill` | Fengshui-themed structured interpretation workflow. | Local JS implementation referenced by skill. | not executed |
| 5 | `liuren-skill` | Liuren-themed structured interpretation workflow. | Local JS implementation referenced by skill. | not executed |

## `keeea/minimalist-entrepreneur-skills` — 10 reports

| # | Skill | Verified source-level capability | Scripts / references / dependencies | Runtime |
|---:|---|---|---|---|
| 1 | `find-community` | Methodology for identifying communities relevant to a target problem/customer group. | Text methodology. | not executed |
| 2 | `validate-idea` | Structured idea-validation methodology emphasizing evidence before build-out. | Text methodology. | not executed |
| 3 | `mvp` | MVP scoping workflow aimed at a constrained first usable product. | Text methodology. | not executed |
| 4 | `processize` | Converts recurring work into explicit repeatable processes. | Text methodology. | not executed |
| 5 | `first-customers` | Early-customer discovery/outreach methodology. | Text methodology. | not executed |
| 6 | `pricing` | Pricing-framing methodology and decision prompts. | Text methodology; no outcome validation asserted. | not executed |
| 7 | `marketing-plan` | Lightweight marketing-plan construction workflow. | Text methodology. | not executed |
| 8 | `grow-sustainably` | Sustainable-growth planning/checkpoint methodology. | Text methodology. | not executed |
| 9 | `company-values` | Workflow for articulating company values into usable decision principles. | Text methodology. | not executed |
| 10 | `minimalist-review` | Review/checkpoint workflow over the broader minimalist-entrepreneur process. | Text methodology. | not executed |

## `sorafujitani/skills` — 16 reports

| # | Skill | Verified source-level capability | Scripts / references / dependencies | Runtime |
|---:|---|---|---|---|
| 1 | `doc-prerequisite-knowledge` | Builds prerequisite-learning paths before reading a technical document and verifies authoritative references. | Web/reference oriented. | not executed |
| 2 | `dry-coding` | Read-only system/design exploration producing dry implementation ideas and multi-dimension evaluation. | Reference-backed; parallel-analysis pattern. | not executed |
| 3 | `exploratory-test` | Plans and can execute exploratory tests with explicit artifact/scope handling and non-destructive source principles. | Test-running workflow. | not executed |
| 4 | `graph-think-map` | Atomizes claims, labels fact/hypothesis, links relationships, and renders/validates a graph representation. | Mermaid/reference workflow. | not executed |
| 5 | `guided-code` | Teaching workflow in which the user writes code while the agent provides guided steps and feedback. | Text workflow. | not executed |
| 6 | `issue-analysis` | Read-only issue analysis using multiple hypotheses, contradiction checks, and a TDD-oriented fix plan. | Reference-backed. | not executed |
| 7 | `karin-info` | Web-research/disambiguation workflow for a named music artist. | Web/reference dependency. | not executed |
| 8 | `local-repo-finder` | Finds local repositories with filesystem search while applying scope precautions. | `fd`/`find` style local tooling. | not executed |
| 9 | `pr-comment-plan` | Analyzes PR comments and turns them into an implementation plan. | GitHub/PR context. | not executed |
| 10 | `pr-generator` | Generates a PR description/workflow from Git state. | Git/GitHub context. | not executed |
| 11 | `print-debug` | Stepwise print-debugging workflow with one observation/change at a time. | Code execution expected in normal use. | not executed |
| 12 | `property-based-test` | Generates property-based test strategy/files, then describes execution/reporting. | Multiple PBT ecosystems supported. | not executed |
| 13 | `review-code` | Parallel multi-perspective code review followed by verification/consolidation. | Multi-agent/reference pattern. | not executed |
| 14 | `skill-zip` | Packages a skill directory into a ZIP artifact. | References `scripts/zip_skill.sh`. | not executed |
| 15 | `sora-mode` | Meta execution/playbook skill defining principles, routing, and supporting references. | Large progressive-reference surface. | not executed |
| 16 | `ts-lint-searcher` | Maps TypeScript lint needs across ESLint/typescript-eslint/oxlint/Biome rule sets. | Reference-backed rule mappings. | not executed |

## `parilsanghvi/AgentSkills` — 0 reports

No local `SKILL.md` or equivalent skill definition was found in the actual reviewed repository. The current repository contains only a minimal README. It is therefore recorded as a content-level rejection/hold rather than manufacturing an individual skill report from repository metadata.

## `fn2ai/fn2-openclaw-skill` — 1 report

| # | Skill | Verified source-level capability | Scripts / references / dependencies | Runtime |
|---:|---|---|---|---|
| 1 | `fn2` | External market/economy research integration plus creation/management of recurring research agents. | `scripts/fn2.py` directly inspected; Python stdlib HTTP/SSE CLI. `references/api.md` directly inspected. `tests/test_cli.py` contains offline mocked unit tests for request/error/SSE/schedule/command behavior. | not executed |

**Validation note:** test definitions exist, but this batch did not execute them and does not claim they pass.

## `wuchubuzai2018/expert-skills-hub` — 18 reports

| # | Skill | Verified source-level capability | Scripts / references / dependencies | Runtime |
|---:|---|---|---|---|
| 1 | `nano-banana-2-image-gen` | Image generation/editing integration using an external provider and Node/Python helpers. | Provider credential + network; scripts and reference guides. | not executed |
| 2 | `nano-banana-pro-image-gen` | Image generation/editing integration with external provider and helper scripts. | Provider credential + network; Node/Python scripts. | not executed |
| 3 | `pdf-to-image-preview` | Converts PDF pages to PNG/JPG with configurable DPI and optional archive output. | Python + PyMuPDF; `scripts/convert_pdf_to_images.py`. | not executed |
| 4 | `juejin-article-trends` | Retrieves categorized popular/latest technical articles from Juejin. | Node script + network/site dependency. | not executed |
| 5 | `baidu-milan-winter-olympics-2026` | Retrieves event standings/news/schedule data from a sports webpage. | Multiple Node scraping/retrieval scripts + network/site dependency. | not executed |
| 6 | `image-resizer` | Local image resize/crop/format/target-size compression workflow. | `scripts/resize_image.js` directly inspected; Sharp dependency. Short `-h` option conflict found between height/help cases. | not executed |
| 7 | `toutiao-news-trends` | Retrieves a Chinese news hot-board and normalizes ranking/link fields. | Node script + network/site dependency. | not executed |
| 8 | `csdn-article-publish` | Draft/update/publish workflow for CSDN content with local validation and file→article mapping. | Authenticated network calls; config, script, API/troubleshooting references. High side-effect/credential surface. | not executed |
| 9 | `wechat-article-search` | Searches public-article results and can optionally resolve result links. | Node + Cheerio + network; anti-crawl limitations documented. | not executed |
| 10 | `wechat-red-envelope-cover-designer` | Design workflow for generating/resizing a set of red-envelope cover assets under platform dimension constraints. | Image-generation/resizing scripts + many design references. | not executed |
| 11 | `apiyi-gpt-image-2-all-gen` | External image-generation/editing integration with Node/Python clients and prompt-controlled dimensions. | Provider credential + network; size/batch references. | not executed |
| 12 | `apiyi-gpt-image-2-gen` | External image-generation/editing integration with explicit size/quality/output-format controls. | Provider credential + network; Node/Python clients and references. | not executed |
| 13 | `haizei-agnes-image-gen` | External image-generation/editing integration using a Node client and Base64 image transport. | Provider credential + network; size/batch references. | not executed |
| 14 | `haizei-cyberpunk-terminal-ppt` | Self-contained HTML presentation design system with a large set of terminal/cyberpunk layouts and rendering guidance. | Extensive progressive reference library; optional rendering script. | not executed |
| 15 | `project-knowledge-hierarchy` | Initializes/maintains a three-layer project documentation hierarchy with idempotent directory/README behavior. | Shell/file operations described in skill. | not executed |
| 16 | `haizei-ears-requirements` | Rewrites/reviews ambiguous requirements using EARS patterns, routing, split rules, and Chinese-output conventions. | Multiple focused references/examples. | not executed |
| 17 | `haizei-okr-writing` | Converts work facts into measurable OKR goals/actions with SMART/PDCA framing and anti-fabrication guidance. | Text methodology. | not executed |
| 18 | `haizei-project-wiki-generator` | Code-analysis-driven VitePress wiki workflow with analysis state, directory planning, explicit user-confirmation gate, then sub-agent document generation. | Initialization scripts plus extensive tech/business/agent/template/gotcha references. | not executed |

## Count check

```text
drunkcoding/AgentSkillsArxiv                  19
TheColonyAI/colony-skill                       1
ahmadharis/agentskills                         5
JayDoubleu/agentskills                         2
dglijin-oss/xuanji-five-skills                 5
keeea/minimalist-entrepreneur-skills          10
sorafujitani/skills                            16
parilsanghvi/AgentSkills                       0
fn2ai/fn2-openclaw-skill                       1
wuchubuzai2018/expert-skills-hub              18
------------------------------------------------
repository-scoped individual skill reports    77
```
