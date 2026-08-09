# Agent Skills Individual Reports — Batch 051

Observed: 2026-08-09

This file materializes **10 new repository-scoped Skill reports** whose bodies were directly read in Batch 051. Four Cybersecurity repository identities were content-gated and mapped to a previously reviewed exact tree instead of duplicating reports. Static inspection is not runtime, build, test, API, browser, or behavioral-eval execution.

## `Player1Taco/morpheus-skill`

Pinned revision: `7870973330227c180002b16227048a61a7e86cd0` · tree: `a006e404b3c61320a2b3b72cde0b78eca9b4334e`.

### 1. `morpheus-skill`
- Path: root `SKILL.md`; supporting surface includes integration/deployment material and a substantial `scripts/` tree.
- Purpose: provide decentralized/model inference through an OpenAI-compatible local proxy with persistent services, external providers and optional MOR/blockchain operations.
- Strength: declares required binaries, credentials, network endpoints, local ports and persistent services rather than hiding operational effects.
- Verification design: `scripts/bootstrap-client.test.mjs` contains Node tests for fingerprint format/determinism and proof-of-work behavior, while explicitly leaving Redis integration and Base Sepolia E2E as next steps.
- Risk: setup can affect local services/configuration, credentials, external inference/network resources and optional blockchain state. These require an authorization policy above the Skill.
- Validation: README, Skill, script inventory and representative unit-test source inspected; tests/services/network/blockchain paths were not executed.

## `fabioassuncao/agentskills`

Pinned revision: `2883cf268e6919438d406025f517a97e21ca94f7` · tree: `b0abc9218c2ea010dc7fbf269ffbb4e913efadd1`.

### 2. `digital-product-analysis`
- Path: `skills/digital-product-analysis/SKILL.md`; supporting `references/references_template.md` is present.
- Purpose: turn a product/business idea into structured market, strategy, GTM, monetization, risk, benchmark and investor artifacts.
- Strength: refuses to proceed without minimum product/audience/market context, calls for live research, sources and explicit challenge of assumptions.
- Gap: TAM/SAM/SOM, projections and viability scoring are still prose/model driven; there is no deterministic calculator, provenance schema or behavioral eval checking arithmetic/source fidelity.
- Validation: Skill and reference inventory inspected; web research/output generation was not executed.

### 3. `domain-finder`
- Path: `skills/domain-finder/SKILL.md`.
- Purpose: generate domain candidates, validate availability with real WHOIS queries and return exactly ten qualified choices.
- Strength: strong evidence boundary—availability must not be assumed and unvalidated candidates must not be presented as available.
- Gap: WHOIS result parsing is encoded as prose string heuristics; no parser fixtures, RDAP/registrar fallback, bounded retry policy or automated tests are present.
- Validation: Skill inspected; WHOIS/network calls were not executed.

## `liamlan/agentskills`

Pinned revision: `8a6b9e1eb6493e892ea12814079aabae3e7e5d32` · tree: `cb6e298e7da1c3a8bb8bcb5553f99a8bc36b9c6e`. No conventional root README exists at this revision.

### 4. `a2a-communication`
- Path: `a2a-skills/a2a-communication/SKILL.md`; references cover field constraints, multi-turn patterns, payload examples and task lifecycle.
- Purpose: document A2A v1.0 task/message/context behavior plus an organization-specific low-code `input_request` / `input_response` extension.
- Strength: explicitly separates standard protocol behavior from the custom extension and makes stable `contextId`/`INPUT_REQUIRED` semantics visible.
- Gap: custom extension compatibility and edge cases are not backed by runnable fixtures or interoperability tests.
- Validation: Skill/reference inventory inspected; no protocol implementation was executed.

### 5. `a2a-orchestrator`
- Path: `a2a-skills/a2a-orchestrator/SKILL.md`; references cover dependency resolution, low-code generation and resolver dispatch.
- Purpose: orchestrate intent routing, prefetch, field resolution, dependency ordering, API/MCP dispatch and user-input collection.
- Strength: separates six responsibilities and calls for cycle detection, constrained classification, retries/timeouts/fallbacks and validation before forwarding user input.
- Gap: code examples are illustrative TypeScript, not a shipped runnable orchestrator; there is no local integration/eval suite proving the state machine or custom extension.
- Validation: Skill/reference inventory inspected; code examples were not executed.

## `lewislulu/html-ppt-skill`

Pinned revision: `f3a8435d3901697d5ac5e64d356c933637e43107` · tree: `c7a57a16de00fb96b207188c4433630f1cde883e`.

### 6. `html-ppt`
- Path: root `SKILL.md`; repository includes static runtime/assets, 36 themes, 15 full-deck templates, 31 layouts, 47 animations, references and render/scaffold scripts.
- Purpose: generate reusable static HTML presentations with keyboard navigation, presenter mode, templates and screenshot export.
- Strength: implementation, visual tokens, templates, runtime and authoring references live together; `scripts/render.sh` produces deterministic 1920×1080 headless-Chrome screenshots.
- Drift: current inventory says 15 full-deck templates while several later README/SKILL captions/tree comments still say 14.
- Portability gap: `scripts/render.sh` hard-codes `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`, so the verification path is macOS-specific.
- Validation: README, Skill and render script inspected; screenshots were not regenerated and runtime/render behavior was not executed.

## `NLP-planet/AgentSkills`

Pinned revision: `32bdbca6c23a24a9ca6a3fc2037d66faf5ff2788` · tree: `761f49f630d27497ca85cf36cf7ef5df344b7c96`. No conventional root README exists. Root `SKILL.md` and `drama-workflow/SKILL.md` are the same blob and are counted once as a unique body.

### 7. `drama-workflow`
- Path: root `SKILL.md` / duplicate `drama-workflow/SKILL.md`.
- Purpose: orchestrate long-text preprocessing, parallel dramatic-function analysis, consolidation and report generation.
- Strength: concise workflow/state responsibilities with explicit context-isolation and output shape.
- Gap: the repository provides no executable orchestration implementation or behavioral eval for chunk boundaries, merge consistency or report accuracy.
- Validation: unique Skill body inspected; execution not performed.

### 8. `douyin-video-forge`
- Path: `douyin-video-forge/SKILL.md`; supporting README, PRD, examples, `install.sh`, references, `scripts/kling_api.py` and `scripts/transcribe.py` are present.
- Purpose: coordinate short-video research, script generation, optional video API generation and media composition.
- Strength: explicit confirmation gates, dependency checks and credential rule that API keys should not be requested in chat; deterministic media/API work is delegated to scripts rather than only prose.
- Risk: browser/network/API/media operations, paid external services and recurring jobs require upper-layer authorization, budget and rate-limit controls.
- Gap: no repository-local behavioral eval/test suite was observed for trend selection, generated-script quality, browser resilience or end-to-end media generation.
- Validation: Skill, subproject README and implementation/reference inventory inspected; browser/API/media operations were not executed.

### 9. `novel-director`
- Path: `novel-director/SKILL.md`; a subproject README and metadata are present.
- Purpose: interactive long-form fiction workflow with persistent cross-session state.
- Strength: three-layer state model separates `world_knowledge.json`, `chapter_index.json`, recent chapters and drafts, avoiding full-history context dependence.
- Risk/gap: save/complete commands mutate multiple files and derived state, but there is no transactional implementation or regression suite proving chapter/index/world-state consistency after partial failure.
- Validation: Skill inspected; file lifecycle was not executed.

## `dsebastien/ai-skill-garmin`

Pinned revision: `22bfebaf567c60cf134229c77682c334aa35df10` · tree: `8227f0f870ced43de34d076797dd32f4830e1d8e`.

### 10. `garmin-connect`
- Path: `skills/garmin-connect/SKILL.md`; supporting `references/endpoints.md` and single-file `scripts/garmin.ts` implementation.
- Purpose: query Garmin Connect read-only health/fitness data through a Bun CLI and let an agent reason over returned JSON.
- Strength: narrow read-only scope, no npm dependencies, JSON stdout contract, environment credentials and local token cache documented with mode `0600`.
- Implementation note: consumer credentials are fetched from garth's S3 source, cached for 24 hours and fall back to an embedded public consumer pair when refresh fails. This is not a user secret, but it is a brittle compatibility dependency.
- Gap: Garmin's unofficial/mobile API surface is intentionally change-sensitive; the tree has self-repair guidance but no unit/integration fixture suite or CI/eval proving current compatibility.
- Validation: README, Skill and representative implementation source inspected; Garmin login/API calls were not executed.

## Exact-tree mappings without duplicate reports

The following four repository identities were individually live-gated in this batch but map to the already-reviewed tree `822878aa68d8a760149ce36542eb41c7aee429db` and the same representative defensive Skill body `skills/analyzing-api-gateway-access-logs/SKILL.md`:

- `motherhack3r/Anthropic-Cybersecurity-Skills`
- `acumenix/Anthropic-Cybersecurity-Skills`
- `itsjamessmith/Anthropic-Cybersecurity-Skills`
- `zrd4y/Anthropic-Cybersecurity-Skills`

They increase repository coverage but add **0** duplicate individual reports.