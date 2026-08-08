# Agent Skills Deep Analysis — Batch 042

- Batch: `2026-08-08-batch-042`
- Phase: deep analysis
- Queue source: existing deterministic Agent Skills repository index
- Completed repository identities: **10**
- Repository README files directly read: **10**
- `SKILL.md` files directly read: **49**
- Unique pinned Git content trees represented: **6**
- Unique skill bodies directly reviewed: **45**
- New batch-local individual skill reports: **43**
- Runtime/build/test/eval execution: **not executed**
- Completion rule: a repository is counted only after identity/stars/revision verification plus direct content reading; metadata-only hits are never marked complete.

## Executive result

Batch 042 completed 10 qualified repository identities from the existing queue. Five identities are exact mirrors of the already-reviewed `c15f73db...` Anthropic Cybersecurity Skills lineage; they were still subjected to identity-level README and representative `SKILL.md` content gates, but did not create duplicate canonical reports. `VastFuture/dreamina-cli-skill` is also an already-reviewed exact content lineage and created no duplicate report.

The four repositories that contributed new batch-local reports were:

- `daonhan/Agentskills` — 10 business-methodology skills;
- `withcrux/agentHack-skills` — 20 cybersecurity training skills plus real lab/MCP/validation implementation;
- `thunderstormwang/AgentSkills` — 12 engineering/workflow skills with references and some eval definitions;
- `shengxuan-create/interview-skill` — 1 interview-preparation skill with progressive references, Python helpers, and eval definitions.

The strongest engineering findings are not about prompt quality. They are implementation-contract defects: `withcrux/agentHack-skills` declares substantially more lab environments than exist at the pinned revision and its MCP lab manager derives the Docker Compose project identifier inconsistently between start and later operations; `thunderstormwang/AgentSkills` contains a direct cross-skill contradiction over whether `git commit` requires explicit user confirmation; `shengxuan-create/interview-skill` advertises historical trigger-accuracy results that are not reproducible from the repository's current `evals/evals.json`, and one helper references an artifact absent from the pinned tree.

## Completed repositories

| # | Repository | Stars observed | Pinned revision | Content result |
|---:|---|---:|---|---|
| 1 | `solophoenixdev/Anthropic-Cybersecurity-Skills` | 0 | `c15f73db46149587e31df83c2f9d92a3b578ef21` | exact reviewed mirror lineage; README + representative skill read |
| 2 | `Bendjou18/anthropic-cybersecurity-skills` | 0 | `c15f73db46149587e31df83c2f9d92a3b578ef21` | exact reviewed mirror lineage; README + representative skill read |
| 3 | `daonhan/Agentskills` | 0 | `dda3ec9475644b5691529d7bfd8f4a9bc2db8e93` | 10/10 local skill bodies read |
| 4 | `withcrux/agentHack-skills` | 4 | `41919ab09e539a43b9365c37e9b0b8583d855d86` | 20/20 indexed skill bodies read; scripts/labs/MCP inspected |
| 5 | `themaulanas/Anthropic-Cybersecurity-Skills` | 0 | `c15f73db46149587e31df83c2f9d92a3b578ef21` | exact reviewed mirror lineage; README + representative skill read |
| 6 | `APhuongKMA/Anthropic-Cybersecurity-Skills` | 0 | `c15f73db46149587e31df83c2f9d92a3b578ef21` | exact reviewed mirror lineage; README + representative skill read |
| 7 | `inessaGit/Anthropic-Cybersecurity-Skills` | 0 | `c15f73db46149587e31df83c2f9d92a3b578ef21` | exact reviewed mirror lineage; README + representative skill read |
| 8 | `thunderstormwang/AgentSkills` | 0 | `3b3915440a0122da4e702e163c72fa2da5924df2` | 12/12 local English skill bodies read; eval/reference surfaces inspected |
| 9 | `shengxuan-create/interview-skill` | 4 | `41a4f4c0c388ef32debf8f74dcdff90390ba7489` | root skill, references/tooling/evals structure inspected |
| 10 | `VastFuture/dreamina-cli-skill` | 0 | `75e0a69a99f21a9c706045a0f6227b1b0804f886` | exact already-reviewed Dreamina wrapper lineage |

Observed Stars are point-in-time repository metadata and are not treated as quality evidence.

## 1. Anthropic Cybersecurity Skills mirror lineage

Five repository identities in this batch pin exactly to `c15f73db46149587e31df83c2f9d92a3b578ef21` / tree `a7c34f7c9035ab32a23f532fb30c1cbaf5d28dbf`. Each identity was verified separately and its README plus a representative `SKILL.md` was directly read before completion.

### Verified structure

- README presents a 753-skill cybersecurity collection with Agent Skills-style frontmatter and references.
- Representative skill content is identical across the five identities inspected in this batch.
- The exact content revision was already canonical-reviewed in earlier batches, so repository coverage increases but canonical skill-body reports are not duplicated.

### Residual issues retained from the canonical review

- Repository documentation contains inconsistent domain counts (`26` vs `38`).
- Structural validation/helper code does not constitute behavioral or security-quality evaluation of all 753 skills.
- Large inventory counts must not be converted into deep-analysis completion counts without body-level reads.

### Verdict

`qualified mirror / content already canonical-reviewed`.

## 2. `daonhan/Agentskills`

Pinned revision: `dda3ec9475644b5691529d7bfd8f4a9bc2db8e93`.

### Structure verified

The repository is a fork lineage centered on ten local business-advice skills. The pinned tree contains ten `skills/*/SKILL.md` bodies and plugin/README material; no repository-local scripts, references, tests, or eval harness were found for these ten skills.

Directly read skills:

1. `company-values`
2. `find-community`
3. `first-customers`
4. `grow-sustainably`
5. `marketing-plan`
6. `minimalist-review`
7. `mvp`
8. `pricing`
9. `processize`
10. `validate-idea`

### What is useful

- Narrow trigger boundaries and concrete output contracts make each skill easy to route.
- Several skills turn broad business advice into a repeatable decision checklist, which is useful as a Skill design pattern.
- The collection demonstrates domain decomposition: idea validation, community, MVP, pricing, sales, marketing, culture, and growth are separated rather than combined into one oversized instruction file.

### Weaknesses

- The collection is overwhelmingly derived from one business philosophy and associated examples, so it lacks source diversity and counterexamples.
- Numeric heuristics and historical business examples are presented as general guidance without local evidence that they transfer across industries, countries, or business models.
- Many statements are normative defaults rather than tested decision rules; a robust reusable skill should expose them as hypotheses or optional heuristics and request context before applying them.
- No repository-local behavioral evals test whether the advice improves decisions or even whether routing/output contracts are followed consistently.

### Verdict

`useful decomposition pattern; methodology claims need qualification and evaluation`.

## 3. `withcrux/agentHack-skills`

Pinned revision: `41919ab09e539a43b9365c37e9b0b8583d855d86`.

### Structure verified

This is materially more than a prompt collection. At the pinned revision it contains:

- 20 indexed `skills/*/SKILL.md` bodies, all directly read in this batch;
- repository validation/generation scripts and a CI workflow;
- an `agentlab` MCP/CLI Python package;
- Docker-based lab material;
- a generated `index.json`.

The batch report intentionally records the cybersecurity skill bodies at a high level only. No operational exploitation steps, credentials, payloads, or target instructions are reproduced here.

### Strong engineering patterns

- The repository attempts to bind risky training content to isolated labs rather than leaving environment control entirely to prose.
- A sampled Docker Compose lab uses an internal-only network, drops capabilities by default, adds only selected capabilities, enables `no-new-privileges`, and uses read-only mounts for DNS data.
- CI validates skill structure/safety markers and checks generated-index drift.
- The MCP layer caps output size and has session timeout/cleanup concepts.

### High-severity implementation defects

1. **MCP session/project identifier mismatch.** `start_lab()` derives the Docker Compose project name from `agent_id`, while later execution and cleanup derive it from `session_id`. The session object does not preserve the original project name. On normal sessions those identifiers differ, so follow-up operations can target a different Compose project. This is a deterministic code-level defect, not a hypothetical style issue.

2. **Declared lab coverage does not match the pinned tree.** The 20 Skill documents reference numerous distinct lab IDs, but `labs/` contains only three actual lab directories at this revision: one network lab, one privilege-escalation lab, and one web-application lab. For example, multiple network Skill declarations have no matching lab directory. This means many documented workflows cannot be treated as runnable merely because a `lab_environment` field exists.

### Additional findings

- Safety validation is mostly textual/structural. Requiring phrases such as educational-use and authorization language is useful linting, but it does not prove sandbox enforcement.
- The generated index/package metadata is hardcoded to a different repository identity (`mukul975/...`), producing provenance drift in this fork.
- `pyproject.toml` declares pytest configuration and development dependencies, but no repository-local test suite was surfaced during this review; no tests were executed.
- A sampled isolated lab attempts dependency installation at container startup while attached to an internal-only network. Without cached packages, that setup step can fail even though the container process continues; runtime verification is required.
- The MCP command filter is a small forbidden-pattern list around a general shell execution capability. The meaningful safety boundary therefore remains Docker isolation and host/runtime policy, not the string filter itself.

### Verdict

`high-value architecture, but current revision is not runtime-ready as claimed; requires lab/registry reconciliation and MCP lifecycle fixes before trust`.

## 4. `thunderstormwang/AgentSkills`

Pinned revision: `3b3915440a0122da4e702e163c72fa2da5924df2`.

### Structure verified

The pinned `.agents/skills/` tree contains 12 skill directories; all 12 English `SKILL.md` bodies were read:

- `coding-style`
- `doc-coauthoring`
- `file-translator`
- `garmin-running-export`
- `gen-task-in-plan`
- `git-commit`
- `implementation`
- `mcp-builder`
- `my-code-review`
- `playwright-cli`
- `sd-design`
- `skill-creator`

The repository also includes references and eval definitions for selected skills. `gen-task-in-plan/evals/evals.json` contains three fixture-oriented scenarios covering compatible, violating, and ambiguous follow-up-task requests. `git-commit/evals/evals.json` contains three synthetic change scenarios. They are test definitions/expected outcomes, not observed pass results in this batch.

### Strong patterns

- `sd-design` separates requirement clarification, pre-design decisions, design contracts, and test-plan artifacts with explicit gates.
- `my-code-review` correctly pushes reviewers beyond diff-only inspection and separates intent/completeness from code correctness/impact tracing.
- `gen-task-in-plan` is one of the clearer examples in this queue of eval inputs tied to workflow invariants.
- `garmin-running-export` explicitly treats browser state as credential material and limits the intended operation to data export rather than account mutation.

### High finding: authorization contract conflict

`git-commit` requires presenting the proposed commit and waiting for explicit approval before performing the commit. `implementation`, however, says its workflow is pre-authorized and instructs the agent to commit without confirmation. Because both skills can participate in the same workflow, local Skill activation order can change whether an external side effect requires confirmation.

This is a reusable design lesson: authorization and side-effect policy must live at a higher-precedence project/agent policy layer; individual skills should reference that policy instead of redefining it incompatibly.

### Other findings

- `file-translator` defaults to overwriting an existing target. A safer general-purpose contract is collision-safe output or explicit overwrite authorization.
- `garmin-running-export` handles personal fitness/authentication data; credential handling is better than average, but destination, retention, and privacy-minimization rules should be explicit.
- `skill-creator` describes an extensive eval/iteration workflow, but the presence of instructions is not proof that this repository has executed those evaluations.
- Several general-purpose skills appear to be upstream-derived or adapted; historical cross-repository canonical reconciliation remains pending, so this batch records the directly observed revisions rather than inferring exact equivalence from names.

### Verdict

`strong workflow ideas; blocked from being a clean reusable policy stack until side-effect authorization is unified`.

## 5. `shengxuan-create/interview-skill`

Pinned revision: `41a4f4c0c388ef32debf8f74dcdff90390ba7489`.

### Structure verified

The repository contains a compact root `SKILL.md` router, bilingual workflow references, prompt templates, Python helper tools, example prep artifacts, architecture documentation, and `evals/evals.json` with 13 current cases.

### Strong patterns

- Progressive disclosure is implemented well: the root Skill routes modes and tells the agent which reference section to load instead of embedding the full workflow in the root file.
- Evidence discipline explicitly distinguishes sourced facts from gaps and discourages inventing company-specific claims.
- The current eval set covers sparse-evidence research, mock interview scoring, debrief/update flows, story-bank use, time-sensitive preparation, and company-specific question grounding.

### Verification gaps and drift

1. The README advertises a historical `100%` trigger-accuracy result, but the current `evals/evals.json` only contains prompts and expected outputs; it explicitly says assertions are added during eval runs. No run artifacts or repeated-trial results were found in the inspected tree, so the headline metric is **not reproducible from current repository evidence**.
2. `company_intel.py` generates search-query plans rather than retrieving/validating company facts itself. It instructs downstream use of `result_evaluator.md`, but a repository search did not find that artifact at the pinned revision.
3. The root Skill labels a section “Four Core Disciplines” while the current body enumerates only three, a small but concrete documentation drift signal.
4. The tooling still depends on host web search and model judgment for source selection/synthesis; helper scripts should not be described as deterministic research adapters.

### Verdict

`good progressive-disclosure and evidence-oriented design; eval/result claims need reproducible run artifacts and stale references need repair`.

## 6. `VastFuture/dreamina-cli-skill`

Pinned revision: `75e0a69a99f21a9c706045a0f6227b1b0804f886`.

The exact content is an older forked Dreamina wrapper lineage already reviewed in previous batches. This identity was still independently gated with repository metadata, README, and root `SKILL.md` reads. The content uses thin Python wrappers, normalized JSON output, local-path validation, and a dry-run surface. Because the body revision is already represented in the catalog analysis, no duplicate skill report was created.

Verdict: `qualified exact duplicate / prior canonical content retained`.

## Reclassified queue entries — not completed

The following index-stage candidates were directly inspected and were **not** counted toward the ten completions because real repository content did not satisfy the catalog's local-skill criterion:

- `TheJShaner/agentskills`
- `BlockLab-Protocol/agentskills`
- `guthubcloudittogether/agentskills`
- `SkyrookieYu/agentskills_agentskills`
- `favelasquez/agentskills`
- `pl018/agentskills`
- `v2nic/agentskills`
- `Takk8IS/agentskills`
- `ghosolutions/agentskills`
- `takk-innovate-studio/agentskills`
- `ranjithsrajan/agentskills`
- `macifyer/agentskills`

Most are Agent Skills specification/reference-SDK copies; `favelasquez/agentskills` is tooling/installer-oriented rather than a repository-scoped Skill collection. They remain excluded from deep-analysis completion rather than being promoted from index metadata.

## Batch-level lessons

### 1. “Has evals” is not the same as “evaluated”

Both `thunderstormwang/AgentSkills` and `shengxuan-create/interview-skill` contain useful eval definitions, but this run found definitions/expected outputs rather than observed run evidence. The catalog should preserve three states: `eval_defined`, `eval_executed`, and `eval_passed`.

### 2. Side-effect authorization is a cross-skill contract

The direct contradiction between `git-commit` and `implementation` demonstrates that confirmation semantics cannot safely be owned by individual skills. Project/agent policy must be authoritative, and skills should declare their side effects rather than silently overriding authorization.

### 3. Executable infrastructure needs identity-level invariants

`withcrux/agentHack-skills` has more real engineering than most prompt-only repositories, but the MCP project-name mismatch shows why content review must trace identifiers across start/execute/cleanup paths. A repository can have Docker, MCP, CI, and safety text and still fail its basic lifecycle contract.

### 4. Declared resources must be reconciled against the tree

A `lab_environment`, reference, or helper path in `SKILL.md` is a claim. It becomes verified only when the path exists at the pinned revision. Batch 042 found both missing lab declarations and a missing helper-reference target.

### 5. Mirrors still require identity-level content gates

The five cybersecurity mirrors were not marked complete from metadata or matching names. Each had content read at its pinned revision first; only after that was exact-lineage deduplication applied.

## Progress update

- Previous structure-reviewed total: **410**
- Completed this batch: **10**
- New structure-reviewed total: **420**
- Frozen canonical eligible basis: **2088**
- Arithmetic remaining estimate: **1668**
- Previous skill-report total: **2853**
- New batch-local individual reports: **43**
- Updated report total: **2896**

`1668` is only `2088 - 420` on the frozen basis. Historical/canonical reconciliation is still pending, so it must not be presented as the final unique repository remainder.

## Next queue boundary

The next not-yet-completed index candidate after this batch boundary is `MarkkuPekkarinen/skills` from the deterministic `2026-04-06` shard. It must undergo the same content qualification gate before being counted.
