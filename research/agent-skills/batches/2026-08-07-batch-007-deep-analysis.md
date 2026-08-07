# GitHub Skills Deep Analysis — Batch 007

- Observed date: `2026-08-07`
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Index snapshot: `1937` unique repositories; `1523` provisionally deep-analysis eligible; `414` held for review
- Repositories completed: `10`
- Individual skills reviewed: `135`
- Completion state: `structure-reviewed`
- Runtime validation: `not_executed`

A repository is counted complete only after its GitHub identity and displayed star count were checked and actual repository content was read. This batch inspected each repository's README/equivalent and current skill inventory, read primary `SKILL.md` definitions or equivalent skill documentation, and inspected representative scripts, references, tests, or eval assets where available. Metadata-only inspection is not sufficient for completion.

For large multi-skill repositories, the individual skill table is an inventory-level report grounded in the repository's current README/index plus directly inspected representative `SKILL.md` files and maintenance/eval assets. It should not be interpreted as a runtime validation of every skill. No third-party skill command, browser automation, external API call, build, test suite, or deployment was executed.

Star counts are GitHub UI observations from 2026-08-07 and can change. Values abbreviated with `k` are retained as displayed.

## Batch summary

| Repository | GitHub ID | Stars observed | Skills | Result |
|---|---:|---:|---:|---|
| `addyosmani/web-quality-skills` | `1136782037` | `2.6k` | 6 | structure-reviewed |
| `browserbase/skills` | `1074669117` | `3.7k` | 16 | structure-reviewed |
| `getsentry/skills` | `1128612043` | `900` | 28 | structure-reviewed |
| `intellectronica/agent-skills` | `1138465232` | `281` | 22 | structure-reviewed |
| `vercel-labs/agent-skills` | `1112540808` | `29.8k` | 8 | structure-reviewed |
| `Dimillian/Skills` | `1125330672` | `3.9k` | 16 | structure-reviewed |
| `spences10/svelte-claude-skills` | `1094542538` | `217` | 4 | structure-reviewed |
| `jykim/claude-obsidian-skills` | `1104389499` | `49` | 14 | structure-reviewed |
| `am-will/codex-skills` | `1135937291` | `1.0k` | 17 | structure-reviewed |
| `cha9ro/agent-skills` | `1135072800` | `0` | 4 | structure-reviewed |

## 1. `addyosmani/web-quality-skills`

- GitHub repository ID: `1136782037`
- Stars observed: `2.6k`
- Primary skills reviewed: `6`

**Structure and evidence.** The repository is a compact six-skill collection under `skills/`. `README.md` and all six primary skill entrypoints were inspected: `web-quality-audit`, `performance`, `core-web-vitals`, `accessibility`, `seo`, and `best-practices`. Supporting references such as `skills/accessibility/references/A11Y-PATTERNS.md` were also inspected.

**Analysis.** The collection uses a useful orchestration split: one holistic audit router delegates conceptual responsibility to five narrower domains. Progressive disclosure keeps detailed patterns in references while the primary files remain task-oriented. The strongest reusable pattern is the explicit separation of performance, Core Web Vitals, accessibility, SEO, and best-practice concerns instead of a single oversized quality skill.

**Validation boundary.** No Lighthouse run, browser test, accessibility scanner, or production-site audit was executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `web-quality-audit` | Orchestrates a holistic web quality review across the five specialist domains. |
| `performance` | Covers rendering, network, bundle, and runtime performance investigation and improvement. |
| `core-web-vitals` | Focuses on LCP, INP, CLS diagnosis and practical optimization patterns. |
| `accessibility` | Applies WCAG 2.2-oriented semantics, keyboard, contrast, focus, forms, and assistive-technology guidance. |
| `seo` | Covers crawlability, metadata, structured data, URL/canonical, sitemap, and on-page technical SEO. |
| `best-practices` | Covers security, compatibility, dependency hygiene, and modern web implementation practices. |

## 2. `browserbase/skills`

- GitHub repository ID: `1074669117`
- Stars observed: `3.7k`
- Primary skills reviewed: `16`

**Structure and evidence.** `README.md` exposes sixteen current skills. Direct inspection included `skills/browser/SKILL.md`, `skills/autobrowse/SKILL.md`, the repository validator `scripts/validate-skills.mjs`, and the AutoBrowse harness `skills/autobrowse/scripts/evaluate.mjs`; code search also confirmed the current primary entrypoints plus supporting scripts/references for research and WebMCP generation.

**Analysis.** The repository combines browser operations with deterministic maintenance infrastructure. `validate-skills.mjs` checks frontmatter, directory/name consistency, licenses, banned files, and size/reference conventions. AutoBrowse separates skill source from run artifacts, uses trace-driven iteration, and explicitly restricts trace file permissions because traces may contain sensitive session data. This is a stronger operational pattern than a prose-only browser skill collection.

**Validation boundary.** No browser session, protected-site interaction, network request, trace capture, or validator execution was performed. Authentication/session-related capabilities are recorded only at the architectural level.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `browser` | General CLI-driven browser automation with structured page-state inspection and local/remote execution modes. |
| `functions` | Provides browser-automation function primitives for programmatic workflows. |
| `browser-trace` | Captures and analyzes browser network, console, and page-lifecycle evidence for debugging. |
| `browser-to-api` | Converts repeatable browser interactions into more deterministic API-oriented workflows. |
| `autobrowse` | Iteratively evaluates browser tasks, reads traces, and improves task strategy artifacts. |
| `safe-browser` | Adds guarded browser-use constraints and safer interaction defaults. |
| `webmcp-gen` | Generates WebMCP-oriented tooling from web-interface behavior and schemas. |
| `cookie-sync` | Handles browser session-state synchronization; the data involved is security-sensitive. |
| `fetch` | Retrieves and extracts web content for downstream agent use. |
| `search` | Encodes web-search workflows over browser/search tooling. |
| `ui-test` | Uses browser automation for UI-oriented test workflows. |
| `browser-use-to-stagehand` | Guides migration from browser-use style automation to Stagehand-oriented patterns. |
| `agent-experience` | Reviews and improves web experiences for agent usability and machine interaction. |
| `company-research` | Runs a structured company-research workflow using web evidence. |
| `event-prospecting` | Structures event-oriented research and prospect discovery. |
| `competitor-analysis` | Structures browser-assisted competitor research and comparison. |

## 3. `getsentry/skills`

- GitHub repository ID: `1128612043`
- Stars observed: `900`
- Primary skills reviewed: `28`

**Structure and evidence.** The canonical skill surface is `skills/`, with mirrored agent-facing packaging and material skill contracts supported by `SPEC.md` files. Direct inspection included `skills/skill-writer/SKILL.md`, `skills/skill-writer/EVAL.md`, and `skills/skill-writer/scripts/quick_validate.py`, plus the README inventory of twenty-eight skills.

**Analysis.** This repository has one of the strongest maintenance/evaluation designs in this batch. `skill-writer` is a router into focused references for mode selection, execution shape, source synthesis, authoring, iteration, trigger optimization, registration, and validation. Its maintainer eval uses AXIS with isolated workspaces, baseline comparison, observable judge criteria, manual rubric dimensions, and an explicit adoption gate. The quick validator checks frontmatter, name-directory alignment, referenced local files, and advisory size limits. The combination of contract (`SPEC.md`), runtime router, structural validator, and eval suite creates a clear distinction between structure correctness and behavioral quality.

**Validation boundary.** AXIS, Codex harnesses, validators, security reviews, and GitHub mutations were inspected but not executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `agents-md` | Creates or maintains repository agent-guidance documentation. |
| `blog-writing-guide` | Encodes Sentry-oriented blog writing standards and review guidance. |
| `brand-guidelines` | Applies brand voice and presentation constraints. |
| `claude-settings-audit` | Audits Claude configuration/settings for correctness and drift. |
| `code-review` | Provides a structured code-review workflow. |
| `code-simplifier` | Simplifies code while aiming to preserve observable behavior. |
| `commit` | Prepares repository changes for a clean commit workflow. |
| `create-branch` | Creates branches according to repository workflow conventions. |
| `django-access-review` | Reviews Django access-control and authorization behavior defensively. |
| `django-perf-review` | Reviews Django code for performance risks and optimization opportunities. |
| `doc-coauthoring` | Guides collaborative drafting and refinement of documentation. |
| `document-api-endpoint` | Produces API endpoint documentation from implementation evidence. |
| `find-bugs` | Runs a targeted bug-finding review over code changes or scoped code. |
| `gh-review-requests` | Manages and inspects GitHub review-request workflows. |
| `gha-security-review` | Reviews GitHub Actions workflows for defensive security issues. |
| `iterate-pr` | Iterates on pull-request feedback, checks, and fixes. |
| `presentation-creator` | Creates structured presentation artifacts and associated content. |
| `pr-link-issue` | Maintains issue/PR linkage and repository workflow metadata. |
| `pr-writer` | Drafts evidence-grounded pull-request descriptions. |
| `prompt-optimizer` | Refines prompts for clearer task contracts and more reliable behavior. |
| `replay-ux-research` | Structures UX research using Sentry Replay evidence. |
| `security-review` | Performs defensive application/code security review. |
| `skill-scanner` | Scans and evaluates skill structure/content for maintenance issues. |
| `skill-writer` | Creates and improves skills through routed references, source synthesis, validation, and eval-aware iteration. |
| `sred-project-organizer` | Organizes SRE/developer project work into reusable project artifacts. |
| `sred-work-summary` | Summarizes SRE/developer work from available evidence. |
| `triage-frontend-issues` | Triages frontend issues into actionable engineering work. |
| `typing-exclusion-worker` | Handles type-checking exclusion cleanup and migration work. |

## 4. `intellectronica/agent-skills`

- GitHub repository ID: `1138465232`
- Stars observed: `281`
- Primary skills reviewed: `22`

**Structure and evidence.** The README currently lists twenty-two skills spanning documentation retrieval, API/CLI integrations, image workflows, productivity services, and meta/prompting utilities. Direct inspection included `skills/context7/SKILL.md` and `skills/copilot-sdk/SKILL.md`; repository search also identified generated plugin mirrors and maintenance scripts under `.github/scripts/`.

**Analysis.** The repository's strongest pattern is external-source freshness routing. `context7` explicitly retrieves current library documentation rather than relying on model memory. `copilot-sdk` similarly treats official SDK docs and language-specific READMEs as authority and calls out preview/version drift. The collection is broad, so quality depends on keeping service/API assumptions current; generated packaging helps reduce duplication between canonical skill roots and plugin surfaces.

**Validation boundary.** No external API, CLI, image-generation service, task service, or documentation endpoint was invoked.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `anki-connect` | Automates Anki/deck operations through the local AnkiConnect surface. |
| `beautiful-mermaid` | Creates polished Mermaid diagrams from structured requirements. |
| `context7` | Retrieves current library/framework documentation from Context7. |
| `copilot-sdk` | Provides version-aware GitHub Copilot SDK guidance across supported languages and extension surfaces. |
| `gog-cli` | Wraps Google ecosystem workflows through its CLI integration. |
| `gpt-image-1-5` | Provides an image-generation/editing workflow for the named OpenAI image model family. |
| `here-be-git` | Supports Git repository navigation and workflow tasks. |
| `lorem-ipsum` | Generates placeholder text for development/design tasks. |
| `markdown-converter` | Converts source content/documents into Markdown-oriented output. |
| `mgrep-code-search` | Performs targeted semantic/code search over repositories. |
| `monologue-notes-api` | Integrates with a notes API for note capture and retrieval workflows. |
| `nano-banana-2` | Encodes an image-generation workflow for the named Google model/tool version. |
| `nano-banana-pro` | Encodes the corresponding higher-capability image workflow. |
| `notion-api` | Performs structured Notion API operations. |
| `promptify` | Rewrites rough requests into stronger prompts/task instructions. |
| `raindrop-api` | Integrates with Raindrop bookmark management APIs. |
| `ray-so-code-snippet` | Creates shareable styled code-snippet outputs. |
| `tavily` | Uses Tavily for web search/research retrieval. |
| `todoist-api` | Integrates with Todoist task/project APIs. |
| `ultrathink` | Provides a deliberate reasoning/planning protocol for complex tasks. |
| `upstash-redis-kv` | Operates Upstash Redis/KV workflows. |
| `youtube-transcript` | Retrieves and processes YouTube transcript content. |

## 5. `vercel-labs/agent-skills`

- GitHub repository ID: `1112540808`
- Stars observed: `29.8k`
- Primary skills reviewed: `8`

**Structure and evidence.** The README exposes eight skills. Direct inspection included `skills/vercel-optimize/SKILL.md`, `skills/react-best-practices/SKILL.md`, and `skills/react-view-transitions/references/implementation.md`. Repository search also identified Vercel Optimize tests such as public-release safety and collection-command documentation tests.

**Analysis.** `vercel-optimize` is notably evidence-gated: it collects production signals first, applies deterministic candidate gates, constrains source inspection to candidate-backed files, verifies recommendations, and separates customer report rendering from internal evidence. `vercel-react-best-practices` encodes seventy prioritized React/Next performance rules across eight impact categories. The view-transition skill uses a reference-backed implementation workflow with an explicit navigation verification phase. Together these show three useful skill shapes: data-driven operational audit, large rule corpus, and reference-backed implementation workflow.

**Validation boundary.** No Vercel metrics were collected, no deployment was changed, no React app was built, and no repository tests were executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `vercel-optimize` | Evidence-gated Vercel cost/performance audit with deterministic investigation and recommendation verification. |
| `vercel-react-best-practices` | React/Next performance rule corpus prioritized by expected impact. |
| `web-design-guidelines` | Reviews web UI implementations against design/usability guidelines. |
| `writing-guidelines` | Provides concise product/interface writing guidance. |
| `react-native-guidelines` | Covers React Native implementation and performance guidance. |
| `react-view-transitions` | Implements and reviews React/Next view-transition patterns with routed references and path-by-path verification. |
| `composition-patterns` | Encodes scalable React component/composition design patterns. |
| `vercel-deploy-claimable` | Guides creation of a claimable Vercel deployment artifact. |

## 6. `Dimillian/Skills`

- GitHub repository ID: `1125330672`
- Stars observed: `3.9k`
- Primary skills reviewed: `16`

**Structure and evidence.** Sixteen root-level skills are documented in the README. Direct inspection included `project-skill-audit/SKILL.md` and `scripts/build_docs_index.py`, which scans root directories containing `SKILL.md`, parses frontmatter, collects reference metadata, and generates `docs/skills.json`.

**Analysis.** The collection emphasizes engineering workflows rather than generic topic knowledge. `project-skill-audit` is especially relevant to catalog design: it requires evidence from project history/sessions and existing skills, recommends updating an existing skill before creating a duplicate, and treats repeated procedures/validation flows as stronger evidence than repeated themes. The generated docs index provides a simple deterministic catalog surface without introducing a second hand-maintained source of truth.

**Validation boundary.** No Xcode/simulator session, build, signing/notarization, GitHub mutation, refactor swarm, or generated-doc script was executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `app-store-changelog` | Converts git history since the previous release into user-facing App Store release notes. |
| `github` | Uses GitHub CLI workflows for issues, PRs, checks, logs, and repository data. |
| `ios-debugger-agent` | Builds, launches, inspects, and debugs iOS apps through Xcode-oriented agent tooling. |
| `macos-menubar-tuist-app` | Guides Tuist/SwiftUI menubar app architecture, manifests, and local launch behavior. |
| `macos-spm-app-packaging` | Builds, packages, signs, and optionally notarizes SwiftPM macOS apps without an Xcode project. |
| `orchestrate-batch-refactor` | Plans and coordinates dependency-aware multi-agent refactor work. |
| `project-skill-audit` | Audits recurring project workflows and existing skills to recommend high-value updates or additions. |
| `react-component-performance` | Diagnoses React re-render churn, expensive render work, unstable props, and list bottlenecks. |
| `bug-hunt-swarm` | Runs a read-only multi-agent root-cause investigation and ranks likely proof paths. |
| `review-and-simplify-changes` | Reviews scoped changes and can apply safe behavior-preserving simplifications. |
| `review-swarm` | Runs read-only multi-agent diff review for regressions, security, reliability, performance, and test/contract gaps. |
| `swift-concurrency-expert` | Reviews/fixes Swift concurrency, actor-isolation, `Sendable`, and data-race issues. |
| `swiftui-liquid-glass` | Applies iOS 26+ Liquid Glass patterns with ordering, grouping, and fallback considerations. |
| `swiftui-performance-audit` | Audits SwiftUI invalidation, identity, layout, and rendering performance. |
| `swiftui-ui-patterns` | Provides SwiftUI navigation, state, component, and reusable UI patterns. |
| `swiftui-view-refactor` | Refactors SwiftUI views toward smaller components and clearer data/dependency flow. |

## 7. `spences10/svelte-claude-skills`

- GitHub repository ID: `1094542538`
- Stars observed: `217`
- Primary skills reviewed: `4`

**Structure and evidence.** The README explicitly marks this repository as the legacy/testing ground for the maintained `svelte-skills-kit`. Four current skill entrypoints under `.claude/skills/` were directly read: `svelte-runes`, `sveltekit-data-flow`, `sveltekit-remote-functions`, and `sveltekit-structure`. `EVAL-STATUS.md` was also inspected.

**Analysis.** The skills use short router-style entrypoints with detailed reference files, a clear example of progressive disclosure. More importantly, the repository preserves negative evaluation evidence: `EVAL-STATUS.md` says its API eval setup did not reproduce manual runtime behavior and distinguishes manual hook activation results from unreliable API results. That candor is useful: evaluation infrastructure should not be treated as proof merely because it exists. Because the repository identifies itself as superseded, it should be retained for historical/evaluation-pattern learning rather than treated as the current Svelte authority.

**Validation boundary.** Historical/manual evaluation notes were read, but no Svelte project, hook comparison, API eval, or Claude runtime test was executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `svelte-runes` | Concise Svelte 5 runes/reactivity and migration guidance with routed references. |
| `sveltekit-data-flow` | Covers server/universal loads, form actions, serialization, and redirect/error flow. |
| `sveltekit-remote-functions` | Covers `.remote.ts` command/query/form patterns and associated server/client constraints. |
| `sveltekit-structure` | Covers routing, layouts, error boundaries, SSR, hydration, and Svelte boundary structure. |

## 8. `jykim/claude-obsidian-skills`

- GitHub repository ID: `1104389499`
- Stars observed: `49`
- Primary skills reviewed: `14`

**Structure and evidence.** The README documents twelve main skills across PKM, Obsidian, Markdown, video, and image workflows. Repository search found two additional current top-level skill definitions, `video-add-chapters/SKILL.md` and `video-full-process/SKILL.md`, so the current content inventory is fourteen. Direct inspection included `obsidian-links/SKILL.md`, `video-cleaning/SKILL.md`, the video script inventory, and `video-full-process/process_video.py`.

**Analysis.** This repository mixes documentation-oriented PKM skills with executable media pipelines. `obsidian-links` is evidence-oriented about validating target files/headers before modifying links. The video pipeline is more operational: the full-process script reuses transcription, orchestrates chapter detection, cleaning, timestamp remapping, and embedding, and exposes preview/skip controls. The README-versus-repository count drift (12 documented vs 14 current skill entrypoints) is a concrete catalog-maintenance issue and should be fixed upstream if this repository is used as an inventory source.

**Validation boundary.** No FFmpeg/MoviePy task, transcription API, image-generation API, or video mutation was executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `ai4pkm-helper` | Provides PKM onboarding/help and handoff into the broader AI4PKM workflow. |
| `gobi-onboarding` | Guides a voice-oriented Gobi Desktop onboarding flow. |
| `obsidian-canvas` | Creates and manages Obsidian Canvas visual knowledge maps. |
| `obsidian-links` | Validates and fixes Obsidian wiki links and exact section targets before writing them. |
| `obsidian-yaml-frontmatter` | Standardizes Obsidian/YAML properties and naming conventions. |
| `obsidian-markdown-structure` | Validates Markdown heading hierarchy and document organization. |
| `obsidian-mermaid` | Produces Obsidian-compatible Mermaid diagrams while avoiding common rendering errors. |
| `markdown-slides` | Converts Markdown content into Deckset/Marp-oriented slide structure. |
| `interactive-writing-assistant` | Supports outline/prose co-evolution with PKM context. |
| `markdown-video` | Converts Markdown slide content into a narrated-video workflow. |
| `video-cleaning` | Uses transcript timing to remove pauses/fillers and produce a cleaned video plus report. |
| `gemini-image-skill` | Wraps Gemini image-generation workflows and output options. |
| `video-add-chapters` | Detects and applies chapter structure using transcript/video evidence. |
| `video-full-process` | Orchestrates transcription, chaptering, cleaning, timestamp remapping, and final media output. |

## 9. `am-will/codex-skills`

- GitHub repository ID: `1135937291`
- Stars observed: `1.0k`
- Primary skills reviewed: `17`

**Structure and evidence.** The repository combines `skills/` with reusable Codex `hooks/`, agent configurations, prompts, and supporting tooling. The README currently lists seventeen skills. Direct inspection included `skills/planner/SKILL.md`, `skills/gpt-5-6-prompt-builder/SKILL.md`, and `hooks/README.md`. The hook catalog currently documents fifty-one generated/adapted bundles and a temporary-workspace dry harness.

**Analysis.** This is broader than a pure skill repository. `planner` requires codebase research, requirement clarification, documentation retrieval, atomic/testable task planning, and a post-plan gotcha pass. `gpt-5-6-prompt-builder` uses an explicit completeness gate covering success criteria, authority, evidence, tools, approvals, validation, and stop rules, which is a strong reusable task-contract pattern. The hook catalog distinguishes direct from adapted compatibility and intentionally skips network/service hooks in the dry harness, preserving a visible validation boundary. Several skills are imported or adapted from upstream sources, so provenance and synchronization matter as much as local authoring.

**Validation boundary.** The hook harness, multi-model council, browser automation, plugin installation, and agent creation workflows were not executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `planner` | Produces phased implementation plans with codebase research, atomic tasks, and explicit validation. |
| `plan-harder` | Provides a deeper planning variant for higher-detail decomposition. |
| `parallel-task` | Executes existing plan work by splitting independent tasks across multiple agents. |
| `llm-council` | Collects independent plans from multiple model providers and synthesizes them through a judge workflow. |
| `ctx7old` | Retrieves current library documentation through Context7 tooling. |
| `openai-docs-skill` | Queries OpenAI developer documentation through its configured docs tooling. |
| `markdown-url` | Converts web content into a Markdown-friendly retrieval surface. |
| `read-github` | Retrieves/searches GitHub repository documentation through a repository-to-MCP bridge. |
| `gpt-5-6-prompt-builder` | Builds outcome-first prompts with explicit success, evidence, authority, approval, validation, and stop contracts. |
| `frontend-design` | Imported frontend design guidance for distinctive UI implementation. |
| `frontend-responsive-ui` | Encodes responsive interface design and implementation guidance. |
| `vercel-react-best-practices` | Imported React/Next performance guidance sourced from Vercel's rule corpus. |
| `create-hook` | Creates or updates Codex hook configuration and supporting scripts. |
| `pluginstaller` | Discovers, validates, installs, and registers Codex plugins. |
| `role-creator` | Creates custom Codex agent/role TOML definitions. |
| `gemini-computer-use` | Wraps a browser-control agent workflow with explicit safety/confirmation behavior. |
| `agent-browser` | Provides headless browser automation through a snapshot/action workflow. |

## 10. `cha9ro/agent-skills`

- GitHub repository ID: `1135072800`
- Stars observed: `0`
- Primary locally-authored skills reviewed: `4`

**Structure and evidence.** The repository is a small personal registry with `skills/`, `template/`, and two git submodules under `skills/public/` pointing to `anthropics/skills` and `openai/skills`. Those external submodules are not re-counted here to avoid double-counting upstream repositories. Search of current repository content found four locally-authored skills under `skills/custom/`: `python-project-scaffold`, `web-uiux-design`, `kenya-hara-white-design`, and `unit-test-generator`. All four `SKILL.md` files were read, along with `python-project-scaffold/scripts/scaffold.py` and its reference-file inventory.

**Analysis.** The custom skills cover two implementation workflows and two design-guidance domains. `python-project-scaffold` is the most deterministic: it pairs onion-architecture guidance with an executable scaffolder and layer-specific references. `unit-test-generator` explicitly uses a build → execution → coverage → non-regression filter cascade, making validation part of the skill contract rather than an afterthought. The two design skills are primarily prose/reference guidance. The repository's use of upstream submodules is a useful provenance boundary, but a catalog consumer must distinguish locally-authored skills from externally-owned submodule content.

**Validation boundary.** The scaffold script, test-generation filter cascade, and generated project tooling were inspected but not executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `python-project-scaffold` | Generates a modern Python/onion-architecture project shape with a deterministic scaffold script and layer-specific references. |
| `web-uiux-design` | Applies SHIG-derived interaction, conceptual-model, layout, accessibility, and cognitive-load principles. |
| `kenya-hara-white-design` | Encodes a specific restrained Japanese-inspired visual philosophy for spacious, minimalist interfaces. |
| `unit-test-generator` | Generates test additions through explicit build, execution, coverage-improvement, and non-regression filters. |

## Cross-repository findings

1. **Strongest validation architecture:** `getsentry/skills` combines runtime router, maintenance contract, structural validator, isolated eval harness, baseline comparison, and adoption gate.
2. **Strongest evidence-gated operational skill:** `vercel-labs/agent-skills` uses production signals and deterministic candidate gates before source investigation in `vercel-optimize`.
3. **Strongest deterministic catalog maintenance:** `browserbase/skills` and `Dimillian/Skills` both turn skill structure into machine-checked/generated artifacts instead of relying only on README prose.
4. **Useful negative-eval evidence:** `spences10/svelte-claude-skills` explicitly records when API eval behavior diverges from manual runtime behavior rather than reporting misleading success.
5. **Catalog drift detected:** `jykim/claude-obsidian-skills` documents twelve skills in README while current top-level skill entrypoints show fourteen; repository-content discovery must therefore supplement README inventory.
6. **Provenance boundary matters:** `cha9ro/agent-skills` vendors public upstream skill repositories as git submodules, while `am-will/codex-skills` includes imported/adapted skills. Catalogs should keep origin/provenance explicit to avoid double-counting and false ownership.

## Verification boundary

- Verified: repository identity, public/non-archived state, displayed stars, README/current inventory evidence, primary skill definitions or equivalent content, and representative available scripts/references/evals described above.
- Not executed: third-party skill runtime commands, browser sessions, network/API calls, builds, test suites, deploys, generators, or eval harnesses.
- Therefore the completion label is `structure-reviewed`, not runtime-validated.
