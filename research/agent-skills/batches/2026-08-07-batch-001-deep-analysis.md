# Skills Catalog Deep Analysis — Batch 001

- Observed date: `2026-08-07`
- Queue authority: `sources/catalog/`
- Repositories completed: `10`
- Individual skills reviewed: `11`
- Review status: `structure-reviewed`
- Runtime/evaluation execution: `not performed`
- Evidence rule: a repository is counted only after its README status was checked, its actual skill entry file was read, and available scripts/references/validation artifacts were inspected.

## Evidence boundary

`Verified` means directly observed in GitHub repository content or the repository homepage during this run.  
`Inference` means a design or reuse conclusion derived from those files.  
`Not verified` means the repository makes a claim, or ships a validation mechanism, but this run did not execute it.

Star counts are the GitHub homepage display observed on `2026-08-07`; values using `k` are rounded by GitHub.

## Repository reports

### 1. `adithya-s-k/manim_skill`

- Stars observed: `1.0k`
- Category: multi-skill domain collection
- Skills: `manimce-best-practices`, `manimgl-best-practices`
- README: present
- Main structure: `skills/` contains two version-specific packages; `tests/` mirrors the same split.
- Files read:
  - `README.md` — blob `99aa94d7602ffc8b3130b4f647100ef648545eb1`
  - `skills/manimce-best-practices/SKILL.md` — blob `0f77bbaa9f1ffd6c875f250ccadd5e323d454580`
  - `skills/manimgl-best-practices/SKILL.md` — blob `c75eeab2ce737de3ce56c4a775bf1569fac98d76`
  - `tests/manimce/test_all_skills.py` — blob `94435589c2be935e5ba8abfcc944c6f37cdb31ab`

**Verified findings**

The repository treats Manim Community Edition and ManimGL as incompatible domains rather than blending their APIs. Each skill has explicit activation cues, a small router-style `SKILL.md`, topic files under `rules/`, complete examples, and starter templates. The test harness enumerates Markdown rule files, extracts/tests examples through shared utilities, parallelizes execution, and fails the process when examples fail.

**Reusable patterns**

- Split skills when two ecosystems share a name but have incompatible imports, commands, or semantics.
- Put detailed knowledge in topic files and keep the entry file as an activation/router layer.
- Mirror skill boundaries in the test layout.
- Test executable examples embedded in documentation rather than only validating frontmatter.

**Limits**

The test harness was inspected but not run. The README statement that all examples are tested is therefore not independently confirmed. The ManimGL package contains attribution and noncommercial/share-alike constraints for adapted examples, so reuse requires license-aware separation.

---

### 2. `AvdLee/SwiftUI-Agent-Skill`

- Stars observed: `3.4k`
- Category: single expert skill with maintenance and executable analysis tooling
- Skill: `swiftui-expert-skill`
- README: present
- Main structure: `swiftui-expert-skill/{SKILL.md,references/,scripts/}`, plugin manifests, tests, and a separate API-maintenance skill.
- Files read:
  - `README.md` — blob `341e529fc2c7d7c47a04e7119d22d0b53c0ce3df`
  - `swiftui-expert-skill/SKILL.md` — blob `21df4309f88594b0a5968f87447fe07ce4114b45`
  - `swiftui-expert-skill/scripts/analyze_trace.py` — blob `250dbfdfb262f09301d097b597be3c92c5b6dc6e`

**Verified findings**

The entry file is a workflow and topic router rather than a monolithic reference. It separates correctness rules from optional performance advice, requires the current API reference to be read first, and routes tasks to focused references. The repository also extends beyond prose: `analyze_trace.py` parses Instruments traces, supports scoped windows and discovery modes, analyzes multiple lanes, correlates results, and emits structured JSON/Markdown.

**Reusable patterns**

- Pair an authoritative checklist with on-demand topic references.
- Separate “always a bug” rules from optional improvements.
- Use machine-readable diagnostic output when raw tool output is too large for reliable agent reasoning.
- Maintain time-sensitive API guidance through a separate maintenance workflow instead of mixing update logic into the user-facing skill.

**Limits**

No trace file was processed and the test suite was not executed. Runtime correctness of the parser and the currency of all iOS API statements remain unverified in this run.

---

### 3. `Brandon030722/ark-ui-skill`

- Stars observed: `216`
- Category: design/implementation skill with assets and heuristic validation
- Skill: `ark-ui`
- README: present
- Main structure: root `SKILL.md`, `references/`, `scripts/`, reusable `assets/`, examples/showcases, tokens, and promotional render sources.
- Files read:
  - `README.md` — blob `66dfedd138bd1d4aa9d277b597802abc2b330241`
  - `SKILL.md` — blob `ef798dca9f41fe4fcc2dd0f64ff51f8f029bb8e8`
  - `scripts/audit-ark-ui.mjs` — blob `c53844d2c323fa5f2acddefa959c43b55515366a`

**Verified findings**

The skill models design selection with two orthogonal dimensions: visual family and implementation depth. It includes explicit provenance/legal boundaries, responsive and accessibility constraints, starter code, React assets, token data, and deterministic screenshot/audit workflows. The zero-dependency audit script checks source files for responsive behavior, visible focus, reduced motion, semantic HTML, unresolved selectors/ARIA references, prohibited asset patterns, and uncontrolled literal colors.

**Reusable patterns**

- Represent independent design decisions as independent contract axes instead of a large combined preset matrix.
- Keep source provenance and legal constraints in the execution workflow, not as an afterthought.
- Ship starter assets and tokens only when they are paired with validation that catches broken DOM wiring and accessibility regressions.
- Treat visual depth as implementation coverage, not decoration density.

**Limits**

The heuristic audit and screenshot scripts were inspected but not run. Visual quality claims and the mapping from public evidence to each style family were not independently reproduced.

---

### 4. `chrisvoncsefalvay/claude-d3js-skill`

- Stars observed: `217`
- Category: single documentation-heavy domain skill
- Skill: `d3-viz`
- README: absent at repository root
- Main structure: root `SKILL.md`, `references/`, and supporting assets.
- Files read:
  - `SKILL.md` — GitHub content read during this run
  - `references/d3-patterns.md` — blob `0b36a0b531b65551ef7bdd12f8ef4b73852454a2`

**Verified findings**

The skill contains a broad D3 workflow, integration choices for imperative versus framework-driven rendering, responsive sizing patterns, and many complete chart/layout examples. The reference file extends the entry document with hierarchical and network visualization implementations. No repository-level README, test directory, executable validator, or evaluation harness was found in the inspected structure.

**Reusable patterns**

- Explain when a specialist library is appropriate and when a simpler alternative is better.
- Separate reusable implementation recipes from the activation document.
- Document integration choices explicitly for frameworks that can conflict with direct DOM manipulation.

**Limits**

The skill is large and example-heavy, increasing context cost and making freshness harder to maintain. Code examples were not executed. There is no inspected automated mechanism proving examples compile against the current D3 release.

---

### 5. `cloudflare/security-audit-skill`

- Stars observed: `2.8k`
- Category: multi-phase audit skill with structured output validation
- Skill: `security-audit`
- README: present
- Main structure: `skills/security-audit/` contains the entry file, phase documents, domain companions, a JSON schema, and a validator.
- Files read:
  - `README.md` — blob `871e44ddfafc8d4ec875c3e7e317f90a92e4a3c1`
  - `skills/security-audit/SKILL.md` — blob `3484ac89fd84f3e1c5c01e7941466155e6fcb5bf`
  - `skills/security-audit/validate-findings.cjs` — blob `9e9e38ad42f9ee8a8faf0f9753370bc8f63645f4`

**Verified findings**

The skill defines six ordered phases: reconnaissance, focused investigation, independent falsification, reporting, schema-validated structured output, and fresh verification. It explicitly distinguishes exploitable findings from hardening notes and requires concrete impact. The validator reads the repository schema at runtime, implements the needed JSON Schema subset, adds semantic constraints, and returns a failing exit code for invalid output.

**Reusable patterns**

- Make independent disproof a mandatory phase, not an optional reviewer prompt.
- Use one machine-readable schema as the output contract and validate it mechanically.
- Preserve rejected findings in structured form so future runs do not repeatedly rediscover the same false positives.
- Separate general orchestration from domain-specific companion documents.

**Limits**

No target codebase was audited and no validator run was executed. Repository statements about average coverage across repeated runs are self-reported and were not independently verified.

---

### 6. `disler/agent-sandbox-skill`

- Stars observed: `378`
- Category: operational skill plus bundled CLI
- Skill: `Agent Sandboxes`
- README: present
- Main structure: Claude-oriented skill under `.claude/skills/agent-sandboxes/`, bundled `sandbox_cli/`, browser cookbook, prompts, and cross-agent instruction files.
- Files read:
  - `README.md` — blob `ab623b730d557d3f0cb1f1411dfbb0b6d8aab83f`
  - `.claude/skills/agent-sandboxes/SKILL.md` — blob `d83baa43f45bd432b7a22f6435f37922a8d6fcdb`
  - `.claude/skills/agent-sandboxes/sandbox_cli/README.md` — blob `367365fe7848019a27089ff9583d1829ab613df1`

**Verified findings**

The skill is an operational runbook around an actual E2B CLI rather than prose alone. It establishes preflight credential checks, explicit sandbox-ID ownership, timeouts, multi-agent isolation rules, file/binary transfer, command execution, browser automation, and lifecycle management. The repository also carries platform-specific command wrappers and substantial example prompts.

**Reusable patterns**

- Require an explicit resource identifier to be captured and reused across turns.
- Define multi-agent collision rules for shared files, environment variables, ports, and lifecycle operations.
- Keep binary transfer and browser validation as first-class operations.
- Separate the concise skill contract from detailed CLI documentation and cookbooks.

**Limits**

No E2B sandbox was created and no CLI command was executed. Some timeout guidance differs between the main skill and the bundled CLI README, indicating documentation drift that should be normalized before reuse.

---

### 7. `distil-labs/distil-cli-skill`

- Stars observed: `178`
- Category: product-specific workflow skill
- Skill: `distil-cli` version `4.5.0`
- README: present
- Main structure: plugin metadata plus `skills/distil-cli/{SKILL.md,references/,workflows/}`.
- Files read:
  - `README.md` — blob `7026783fb8fbac868d7175249a4d838fd4b368cb`
  - `skills/distil-cli/SKILL.md` — blob `c0b1241ed0a01ba6c18324757f3abffdac6fae63`
  - `skills/distil-cli/workflows/dataset-to-model.md` — blob `936d9aeb35c14a6584f0906b602eda68b7f6ef9e`

**Verified findings**

The entry file is an intent router to task references and three end-to-end workflows. The dataset workflow separates deterministic steps from judgment-heavy steps, establishes preflight/auth checks, data quality gates, train/test leakage checks, structured status retrieval, report checkpoints, and an explicit confirmation gate before starting costly long-running training.

**Reusable patterns**

- Put irreversible or credit-consuming operations behind an explicit user gate.
- Route specific lookup questions directly to references while routing end-to-end requests to workflows.
- Maintain a run log across long workflows and require visible report checkpoints.
- Use machine-readable command output and canonical polling logic instead of parsing human text.

**Limits**

No CLI authentication, upload, evaluation, or training job was executed. Product capability and performance claims in the README are vendor claims, not independently validated here.

---

### 8. `maquina-app/rails-upgrade-skill`

- Stars observed: `82`
- Category: versioned migration workflow skill
- Skill: `rails-upgrade-assistant`
- README: absent at repository root
- Main structure: root `SKILL.md`, version guides, workflows, templates, examples, references, detection patterns, and script templates.
- Files read:
  - `SKILL.md` — blob `5fbfdff0361a82d6570e1b69cf899040da693c3a`
  - `detection-scripts/templates/detection-script-template.sh` — blob `98bed8320b58ab3203109e91d56954c727593195`

**Verified findings**

The skill enforces a sequential upgrade path and uses a two-stage evidence loop: generate a detector, obtain actual findings from the target project, then generate reports from those findings. The script template contains explicit placeholders, severity sections, project statistics, affected-file collection, configuration reminders, and a nonzero-work follow-up loop.

**Reusable patterns**

- For migrations, generate evidence from the target project before producing detailed remediation.
- Encode supported upgrade edges explicitly and split multi-hop work into independently verifiable stages.
- Keep version-specific facts in data/reference files and keep report generation in workflows/templates.
- Include rollback and re-run verification in migration output contracts.

**Limits**

The repository has no root README. The template is not executable until placeholders are fully replaced. Claims such as “90%+ accuracy” and stated time savings are self-reported and were not verified.

---

### 9. `twostraws/SwiftUI-Agent-Skill`

- Stars observed: `4.4k`
- Category: concise expert review skill
- Skill: `swiftui-pro` version `1.1`
- README: present
- Main structure: `swiftui-pro/SKILL.md`, focused references, plugin metadata, assets, and mirrored installation packaging.
- Files read:
  - `README.md` — blob `81fff7cec980cdb7c2d312c56a8b669d48037011`
  - `swiftui-pro/SKILL.md` — blob `f6015f2bfbd7c11ed4457a32ceba05e23ef340ee`
  - `swiftui-pro/references/performance.md` — blob `72c5a037df7f903880d61520632682f51719ddaf`

**Verified findings**

The skill keeps the entry file short, defines an ordered review process, supports partial loading of references, and requires findings to be organized by file with concrete before/after fixes. The performance reference targets structural identity, view decomposition, expensive body work, lazy containers, async lifecycle, and stale-cache risks.

**Reusable patterns**

- Optimize entry-file token cost by delegating every review domain to a focused reference.
- Require issue-level evidence and skip files without genuine findings.
- Standardize review output by file, line, violated rule, and minimal fix.
- State supported platform/language baselines explicitly.

**Limits**

No Swift project was reviewed and no examples were compiled. Some rules are prescriptive and should be applied with project-specific measurement rather than as universal performance facts.

---

### 10. `yantoumu/adsense-site-auditor-skill`

- Stars observed: `174`
- Category: policy-compliance audit skill
- Skill: `adsense-site-auditor`
- README: present
- Main structure: packaged skill with `SKILL.md`, exhaustive requirements reference, usage prompts, agent metadata, and a distributable archive.
- Files read:
  - `README.md` — blob `4df3b7a87d7d3be742a594551f0135128dea4ef1`
  - `adsense-site-auditor/SKILL.md` — blob `a0e9e6f19099b2ffe9c48f5bfa338cc76a3a1849`
  - `adsense-site-auditor/references/adsense-requirements.md` — GitHub content read; source snapshot dated `2026-06-16`

**Verified findings**

The skill defines official Google documentation as the authority, requires live refresh for serious audits, and forbids sampling the checklist. Each requirement must receive exactly one of four statuses with evidence and next action. The reference is organized by stable IDs, severity, requirement, and check procedure, enabling completeness counting.

**Reusable patterns**

- Give every mutable policy rule a stable ID and canonical source.
- Make completeness mechanically countable instead of relying on narrative coverage.
- Use `Unknown` rather than inventing evidence, and reserve `N/A` for justified non-applicability.
- Explicitly state that the skill cannot guarantee a third-party approval decision.

**Limits**

No website was audited, official Google pages were not refreshed during this repository-structure review, and policy freshness beyond the repository’s `2026-06-16` snapshot is not verified.

## Individual skill reports

### `manimce-best-practices`

- Activation: Manim Community imports, CLI, scene classes, and related APIs.
- Knowledge model: topic router → rule files → executable examples/templates.
- Validation: repository provides a Markdown example test harness.
- Strong point: prevents confusion with ManimGL using explicit negative scope.
- Reuse candidate: domain-disambiguation frontmatter plus mirrored tests.
- Status: `structure-reviewed`; tests not executed.

### `manimgl-best-practices`

- Activation: `manimlib`, `manimgl`, `InteractiveScene`, interactive/checkpoint workflows.
- Knowledge model: rule files for scenes, text, camera, interactivity, 3D, and CLI.
- Validation: analogous repository test structure is present.
- Strong point: operationally distinguishes APIs and development workflow from ManimCE.
- Reuse constraint: adapted examples include attribution/noncommercial/share-alike obligations.
- Status: `structure-reviewed`; tests not executed.

### `swiftui-expert-skill`

- Activation: SwiftUI writing, review, refactoring, performance, accessibility, and Instruments traces.
- Knowledge model: correctness checklist plus topic router and current-API reference.
- Tooling: trace recorder/parser with structured multi-lane output.
- Strong point: combines reference guidance with executable diagnostics.
- Reuse candidate: separate maintenance skill for fast-changing platform APIs.
- Status: `structure-reviewed`; scripts not executed.

### `ark-ui`

- Activation: original interfaces inspired by specified public visual families without copying protected assets.
- Knowledge model: family + depth contract, references, starter assets, tokens, showcases.
- Tooling: heuristic source audit, evidence analyzer, and screenshot capture scripts.
- Strong point: integrates provenance, accessibility, responsive behavior, and visual QA.
- Reuse candidate: orthogonal design-contract axes and deterministic screenshot gates.
- Status: `structure-reviewed`; visual validation not executed.

### `d3-viz`

- Activation: custom interactive D3 visualizations requiring fine control.
- Knowledge model: long entry document plus implementation-pattern references.
- Tooling/evals: none found in the inspected repository structure.
- Strong point: explicit integration patterns across imperative D3 and UI frameworks.
- Risk: large static examples may become stale and consume excessive context.
- Status: `structure-reviewed`; examples not executed.

### `security-audit`

- Activation: source-code security review requests.
- Knowledge model: ordered phases with domain companions and adversarial validation.
- Tooling: JSON schema and zero-dependency validator.
- Strong point: requires impact evidence and independent falsification.
- Reuse candidate: accepted/rejected structured findings with a machine-enforced contract.
- Status: `structure-reviewed`; no target audit or validator execution.

### `Agent Sandboxes`

- Activation: isolated execution, package testing, file operations, and browser validation.
- Knowledge model: operational rules plus CLI cookbook.
- Tooling: bundled E2B CLI and browser interface.
- Strong point: explicit multi-agent ownership of sandbox IDs and shared resources.
- Risk: inconsistent timeout examples across documents.
- Status: `structure-reviewed`; no external sandbox created.

### `distil-cli`

- Activation: Distil CLI, data preparation, evaluation, training, deployment, and model iteration.
- Knowledge model: intent router → references or end-to-end workflows.
- Tooling: external CLI; repository supplies deterministic command and reporting procedures.
- Strong point: explicit confirmation before costly long-running training.
- Reuse candidate: workflow checkpointing, run logs, JSON-only status handling.
- Status: `structure-reviewed`; no platform operation executed.

### `rails-upgrade-assistant`

- Activation: Rails 7.0–8.1 upgrade planning and analysis.
- Knowledge model: version edges, pattern data, detector generation, actual-findings reports.
- Tooling: generated Bash detector template and report templates.
- Strong point: target evidence precedes detailed remediation.
- Risk: unresolved placeholders make the base template non-executable; quality depends on generation.
- Status: `structure-reviewed`; no Rails project scanned.

### `swiftui-pro`

- Activation: modern SwiftUI writing and review.
- Knowledge model: concise ordered router to nine focused references.
- Output contract: report by file and line with rule and minimal before/after fix.
- Strong point: low entry-file context cost and explicit “no nitpicking” rule.
- Reuse candidate: partial-review reference loading and issue-only output.
- Status: `structure-reviewed`; no Swift project compiled or reviewed.

### `adsense-site-auditor`

- Activation: AdSense readiness, rejection, policy, crawlability, ownership, and privacy audits.
- Knowledge model: canonical-source rule plus exhaustive stable-ID checklist.
- Output contract: readiness decision, severity-ordered findings, and complete status table.
- Strong point: forbids sampling and supports mechanically countable coverage.
- Risk: policy snapshots age; live official documentation must remain authoritative.
- Status: `structure-reviewed`; no website audit or policy refresh performed.

## Cross-repository conclusions

### Verified recurring design patterns

1. **Thin entry, deep references** is the dominant scalable structure. It is implemented most cleanly by both SwiftUI repositories, Distil, Cloudflare, and the Manim collection.
2. **Executable validation materially improves trust.** The strongest examples pair prose with tests, schemas, parsers, or heuristic audits.
3. **Evidence gates reduce hallucinated output.** Rails requires target findings, Cloudflare requires concrete impact and falsification, and AdSense requires every stable checklist ID to have evidence.
4. **Irreversible operations need explicit gates.** Distil’s training confirmation and sandbox lifecycle rules are reusable beyond their domains.
5. **Fast-changing knowledge should be isolated.** AvdLee separates API maintenance; AdSense declares official live sources authoritative.

### Integration candidates for `idaibin/skills`

- Add a shared `evidence_status` vocabulary: `verified`, `inference`, `not_verified`.
- Require each review/audit skill to declare whether validation was inspected, executed, or unavailable.
- Standardize machine-readable output schemas for findings-heavy skills.
- Keep `SKILL.md` as routing and execution policy; place large domain material under `references/`.
- Add explicit side-effect gates for paid, destructive, publishing, deployment, or long-running actions.
- Add a reusable completeness mechanism based on stable requirement IDs.
- Add license/provenance fields where examples or assets may carry non-default obligations.

## Completion record

All 10 repositories were read beyond metadata and each counted repository has an actual skill entry file reviewed. This batch does not claim runtime correctness, current policy correctness, or test success because no repository test/evaluation command was executed.
