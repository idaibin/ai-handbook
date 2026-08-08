# Agent Skills Repository Deep Analysis — Batch 040

- Batch ID: `2026-08-08-batch-040`
- Stage: repository deep analysis
- Completed repository identities: **10**
- GitHub identity + observed Stars verified before completion: **10/10**
- Repository READMEs directly read: **10/10**
- Repository `SKILL.md` files directly read: **29**
- Unique skill bodies directly reviewed: **26**
- New canonical individual skill-body reports: **24**
- Unique pinned Git commit trees reviewed: **8**
- Runtime/build/test/eval execution: **not_executed**

## Completion rule used in this batch

A repository identity is counted complete only after all of the following are true:

1. GitHub repository identity and observed Stars are verified from GitHub.
2. A pinned repository revision is resolved.
3. The repository structure is inspected at that revision.
4. README and at least one real `SKILL.md`/equivalent body are directly read from that identity.
5. Scripts, references, manifests, tests/evals are inspected when they are present and relevant.
6. Exact-tree/content mirrors are deduplicated only after direct content gating; metadata similarity alone is insufficient.
7. Inventory-only skill entries in large collections are not counted as body-reviewed individual reports.
8. No runtime/test/eval success is claimed unless actually executed.

This batch intentionally reclassified five queue candidates after content inspection. They are **not** counted as completed repositories.

## Queue qualification corrections before selecting the ten repositories

| Indexed candidate | Actual content finding | Decision |
| --- | --- | --- |
| `Duosl/AgentSkills` | Pinned tree contains `LICENSE` + README linking to external skill repositories; no local Agent Skill body | `held_not_completed` — adjacent index/awesome-list |
| `OmSatapathy/AgentSkills` | Repository embeds an external AgentSkills repository as a gitlink/submodule and contains a separate Selenium project; no local skill bodies were surfaced | `held_not_completed` — project embedding external skills |
| `intrepid-g/agentskills` | Fork of the Agent Skills specification/reference SDK; README describes the specification, docs, and SDK rather than a skill catalog | `held_not_completed` — specification/reference SDK |
| `pranamyajainn/agentskills` | Same specification/reference-SDK lineage at the inspected revision | `held_not_completed` — specification/reference SDK |
| `shitty-shit/agentskills` | Same specification/reference-SDK lineage at the inspected revision | `held_not_completed` — specification/reference SDK |

These corrections are important: an index-stage `skill_collection` label is provisional and is not sufficient evidence for deep-analysis completion.

## Completed repositories

| # | Repository | GitHub ID | Stars observed | Pinned revision | Content gate |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `HsinTsao/Anthropic-Cybersecurity-Skills` | `1199232047` | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | README + representative SKILL direct read + exact-tree canonical mapping |
| 2 | `kagura-agent/skills` | `1200164695` | 1 | `a034021bb5ceaa918fa843ccbecf1777de81df2b` | README + all 13 surfaced SKILL bodies + scripts + references |
| 3 | `ndtrongvn/agents-skills` | `1200130399` | 0 | `f5fbed26e84db1d378b4bab1b3888f0dc9fcb178` | README + all 6 surfaced SKILL bodies + audit engine |
| 4 | `Sylvia-awen/dreamina-cli-skill` | `1200196145` | 0 | `75e0a69a99f21a9c706045a0f6227b1b0804f886` | README + SKILL + wrapper implementation + command reference |
| 5 | `Marvin-Cypher/openclaw-seedance-skill` | `1200039088` | 0 | `a054285ffeacc3a6eebcc7e24248b0477f551fa4` | README + SKILL + CLI reference |
| 6 | `skbauman3/wondelai-skills` | `1200771123` | 0 | `7c71a845071e8f994253db0d26c7e36fa90e2b5e` | README + 42-skill marketplace manifest + representative new body + reference |
| 7 | `Raven5101/skills` | `1200847563` | 0 | `955115316fdf18eaef1ba6e7a9860704215e172f` | README + representative SKILL direct read + exact-tree canonical mapping |
| 8 | `B0llieball/Anthropic-Cybersecurity-Skills` | `1200088133` | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | README + representative SKILL direct read + exact-tree canonical mapping |
| 9 | `fernandezbaptiste/Anthropic-Cybersecurity-Skills` | `1200444611` | 0 | `c15f73db46149587e31df83c2f9d92a3b578ef21` | README + stable representative body + two changed/new bodies + scripts + references |
| 10 | `cautionsign/Anthropic-Cybersecurity-Skills` | `1200262968` | 1 | `c15f73db46149587e31df83c2f9d92a3b578ef21` | README + representative SKILL direct read + exact-tree mapping to inspected `c15f73d...` content |

## Repository analyses

### 1. `HsinTsao/Anthropic-Cybersecurity-Skills`

**Verified content.** The inspected revision is the same `2c88b96...` content lineage already reviewed in Batch 039. The identity was still directly opened in this batch: README and `skills/performing-memory-forensics-with-volatility3/SKILL.md` were read from this repository identity before mirror deduplication.

**Structure.** Large cybersecurity Agent Skills collection with generated index/marketplace metadata and hundreds of skill directories. Its README advertises 753 skills and contains inconsistent domain counts (`26` in narrative text versus `38` in another heading), which remains a documentation-quality warning.

**Assessment.** The representative skill is a detailed, operational security workflow with prerequisites and verification language. It is content-rich, but the collection-level claim that all entries are “production-grade” is not established by repository-local behavioral eval evidence. The previous Batch 039 structural-validation finding still applies: metadata/schema validation is not behavioral correctness.

**Canonical action.** No new body report is added for this exact old-tree representative; it maps to the canonical body already recorded in Batch 039.

### 2. `kagura-agent/skills`

**Verified structure.** The pinned tree contains 13 directly surfaced skill bodies:

`agent-memes`, `cove-ops`, `discord-ops`, `flowforge`, `gogetajob`, `kagura-canvas`, `kagura-storyteller`, `memos-memory-guide`, `moltbook-community`, `pulse-todo`, `seedling`, `self-portrait`, `team-lead`.

All 13 `SKILL.md` bodies were directly read. Supporting implementation/reference reads included `agent-memes/scripts/memes.sh`, `cove-ops/scripts/cove-webhook-send.mjs`, and `flowforge/references/setup.md`.

**Strengths.** This is one of the more concrete collections in the queue. Several skills define real host/tool contracts, state-machine or handoff rules, persistence semantics, authorization expectations, source-first fact checking, worktree isolation, acceptance checks, and explicit human approval.

**Important gaps.**

1. **README inventory drift.** The README lists only a subset of the 13 skill directories actually present.
2. **Portability is low.** Many instructions are tightly coupled to one OpenClaw workspace, account/channel IDs, local paths, named personas, companion repositories, and tools not shipped in this repository.
3. **Absolute policy language.** Examples include mandatory FlowForge routing, “never code yourself”, forced cron coupling, fixed stale thresholds, and proactive meme sending. These can be useful local policies but should not be treated as universal Agent Skill truths.
4. **External side effects need stronger centralized authorization.** Discord administration, public posting, GitHub contribution, cron scheduling, profile publishing, and webhook creation can all create external effects. Individual skills contain some safeguards, but the repository has no shared effect/authorization contract.
5. **Credential material at rest.** `cove-webhook-send.mjs` reads a Cove bot token from configuration and caches created webhook IDs/tokens in a JSON file. No explicit restrictive file-permission handling was observed in the inspected script.
6. **Broken/local dependency references.** `flowforge/SKILL.md` links to `setup.md`, while the inspected setup file is under `flowforge/references/setup.md`. It also invokes a workspace-local `goal-drift-check.sh` not surfaced in this repository tree.
7. **Content drift.** `seedling/SKILL.md` contains two “Progressive Channel Unlocks” sections with overlapping rules.
8. **No repository-local behavioral eval suite surfaced in this inspection.** Concrete scripts exist, but runtime/test/eval execution was not performed.

**Assessment.** High practical value as a real personal-agent operating system; lower value as a portable, generally reusable skills collection without extracting the host-specific contracts and authorization model.

### 3. `ndtrongvn/agents-skills`

**Verified structure.** README defines a deterministic chain of six skills: `rb-audit`, `rb-idea`, `rb-prd`, `rb-break-task`, `rb-tdd`, and `rb-agent-md`. All six bodies were directly read. `skills/rb-audit/scripts/engine.py` was also inspected.

**Strengths.**

- Strong file-gated handoffs: audit capsule → design questions → PRD → task slices → TDD.
- Deterministic JSON artifact contract for `rb-audit`.
- Explicit freshness, source priority, and “do not invent facts” rules.
- `rb-break-task` preserves dependency-aware vertical slices.
- `rb-tdd` clearly prefers behavior/public-interface testing over implementation-coupled tests.
- `rb-agent-md` distinguishes distill/render/sync modes and leaves unresolved facts explicit.

**Important gaps.**

1. **False generality in `rb-audit`.** The implementation is heavily specialized to a specific Next.js/Solana/Supabase application: fixed directories, specific dependencies, migration filenames, and project-specific source paths/rules are encoded directly in the engine.
2. **Static-pattern limits.** Regex/path-based checks can miss semantically equivalent risks and can flag benign patterns. No labeled evaluation corpus was surfaced to quantify false positives/negatives.
3. **Time TTL instead of change invalidation.** The six-hour capsule TTL is deterministic but arbitrary; repository-content hashes would provide stronger freshness semantics.
4. **Propagation risk.** Downstream skills treat the audit capsule as authoritative, so a wrong capsule can systematically contaminate later design/PRD/task outputs.
5. **Documentation defect.** `rb-prd/SKILL.md` has a malformed Markdown backtick around the required output path.
6. **No dedicated behavioral eval harness surfaced.** The engine is executable source, but this batch did not execute it or observe tests.

**Assessment.** Strong reference for deterministic artifact handoffs and anti-hallucination workflow design. Before general reuse, split project-specific audit rules from the generic engine and add fixture-based/effectiveness evals.

### 4. `Sylvia-awen/dreamina-cli-skill`

**Verified structure.** README, root `SKILL.md`, `references/commands.md`, and the central Python wrapper implementation were directly inspected. The repository packages thin scripts over an external `dreamina` CLI.

**Strengths.**

- Real input/path/model/range validation rather than prompt-only instructions.
- Structured JSON success/failure contract.
- A real `--dry-run` branch that returns expanded CLI arguments without invoking the external CLI.
- Async generation status is normalized and invalid failure status is converted into a wrapper failure.
- Capability discovery is generated from the same command-spec definitions.
- Documentation correctly says the underlying CLI help remains the final source of truth when external flags change.

**Important gaps.**

1. Installer examples pipe a remote shell installer directly into `bash` without a pinned version/checksum, reducing supply-chain reproducibility.
2. No repository-local test/eval suite was surfaced for argument normalization, JSON extraction, or external CLI drift.
3. Wrapper output includes expanded `cli_args`; a future sensitive argument would need explicit redaction.
4. Some path examples assume `.agent/skills/...`, while installation guidance is broader; portability should use a resolved skill root rather than a hard-coded registry convention.
5. Cost, credit consumption, authentication, and server-side model behavior are external and were not runtime-verified in this batch.

**Assessment.** A materially stronger integration pattern than prompt-only CLI documentation because it adds deterministic validation, dry-run, and a stable output contract. Add unit tests/fixtures and a pinned installation path before treating it as production-grade.

### 5. `Marvin-Cypher/openclaw-seedance-skill`

**Verified structure.** README, `skills/open-claw-seedance/SKILL.md`, and `references/jimeng-cli-quickstart.md` were read. The repository contains no surfaced local wrapper implementation or eval/test harness; it documents three Dreamina/Seedance workflows around the external CLI.

**Strengths.** Narrow scope, clear dependency, and explicit instruction to consult external CLI help for supported combinations.

**Gaps.** It does not provide the validation/dry-run/structured-return layer present in `dreamina-cli-skill`; external command/version drift is therefore passed directly to the agent. Remote installer examples are unpinned, and cost/auth/external write effects have no explicit confirmation gate.

**Assessment.** Useful lightweight operator guide, but substantially less deterministic than the Python-wrapper approach reviewed immediately before it.

### 6. `skbauman3/wondelai-skills`

**Verified structure.** README and `.claude-plugin/marketplace.json` were directly inspected. The marketplace declares **42 skill identities** at metadata version `1.3.0` organized across nine plugin groups. A new representative body, `37signals-way/SKILL.md`, and `37signals-way/references/shaping-work.md` were directly read.

This revision is distinct from both the older 41-skill snapshot reviewed in Batch 039 and the later/current 62-skill Wondel revision also reviewed there. It is therefore useful provenance for catalog evolution.

**Strengths.** Clear plugin grouping, broad framework coverage, cross-skill routing, deep reference material, and explicit ethical caveats in many framework skills.

**Gaps.** The representative `37signals-way` body turns a specific product-development philosophy into strong defaults such as fixed cycle sizes, small teams, no backlog, and a `10/10` adherence score. These are coherent framework assumptions, not universally validated engineering laws. The numerical score can imply precision unsupported by a repository-local eval. No executable or behavioral eval was surfaced for this intermediate snapshot in this review.

**Canonical action.** The 42-entry manifest is an inventory record only. Only the directly read new `37signals-way` body is added as a canonical body report in this batch.

### 7. `Raven5101/skills`

**Verified content.** The repository is pinned to `955115316fdf...`, the same old Wondel-derived revision already reviewed as a separate identity in Batch 039. This identity was not completed on metadata alone: its README and `jobs-to-be-done/SKILL.md` were directly opened from `Raven5101/skills`.

The direct body read confirms the older JTBD body version already preserved in the canonical reports, including its structured framework, ethical caveats, and subjective `10/10` scoring rubric.

**Canonical action.** No new body report is added; this repository identity maps to the existing old-snapshot canonical body/version.

### 8. `B0llieball/Anthropic-Cybersecurity-Skills`

**Verified content.** README and the representative `performing-memory-forensics-with-volatility3/SKILL.md` were directly read from this identity at the exact `2c88b96...` revision.

The body blob matches the old Anthropic Cybersecurity tree already canonicalized in Batch 039. The same collection-level caveats remain: very large inventory, inconsistent documentation counts, metadata-quality defects previously observed, and structural validation that does not establish behavioral correctness.

**Canonical action.** Exact-tree mirror mapping; no duplicate canonical body report.

### 9. `fernandezbaptiste/Anthropic-Cybersecurity-Skills`

**Verified content.** This identity is pinned to `c15f73db...`, which is not the old `2c88b96...` snapshot. Repository comparison shows a diverged lineage with material changes, including added/expanded skill bodies, references, scripts, and a marketplace-version workflow.

Direct reads include:

- README
- stable representative `performing-memory-forensics-with-volatility3/SKILL.md`
- changed `detecting-lateral-movement-with-zeek/SKILL.md`
- `detecting-lateral-movement-with-zeek/scripts/process.py`
- its standards and workflow references
- new `performing-cloud-native-threat-hunting-with-aws-detective/SKILL.md`
- its `scripts/process.py` and standards reference

**Strengths.** The two newer defensive skill families are more than prompt prose: they include executable Python helpers, standards references, prerequisites, verification sections, and explicit operational boundaries. The cloud helper implements pagination and JSON export; the network helper parses structured log inputs and exposes configurable detection thresholds.

**Important gaps.**

1. **Documentation/script drift in the Zeek skill.** The skill tells users to run a provided `agent.py`, while the actual surfaced helper is `scripts/process.py` with a different invocation contract.
2. **Heuristic thresholds lack a measured eval.** Detection severities/windows/thresholds are encoded in source but no fixture corpus, precision/recall result, or false-positive benchmark was surfaced.
3. **External API compatibility was not runtime-verified.** AWS/Zeek versions and cloud permissions were not executed in this batch.
4. **Large-collection quality remains heterogeneous.** Two improved bodies do not prove that all catalog entries meet the same implementation/evidence standard.
5. **Potential high-impact automation needs human gating.** Security-response recommendations should remain reviewable rather than automatically causing account/host changes.

**Canonical action.** Add two new body reports for the directly reviewed changed/new bodies. The stable memory-forensics body maps to the existing old canonical body.

### 10. `cautionsign/Anthropic-Cybersecurity-Skills`

**Verified content.** README and representative memory-forensics SKILL were directly opened from this identity at `c15f73db...`. The identity shares the exact inspected revision with `fernandezbaptiste/Anthropic-Cybersecurity-Skills`, so the deeper changed-body/script/reference analysis above is canonicalized once rather than duplicated.

**Canonical action.** Exact-revision mirror mapping to the `c15f73db...` review; no duplicate body reports.

## Cross-repository findings

### A. Content gating corrected five queue false positives

This is the most important process finding in Batch 040. Repository names and index classifications were insufficient: five candidates labeled like Agent Skills repositories were actually an external-link index, an embedded submodule project, or specification/SDK forks. None were marked complete.

### B. Exact-tree deduplication is necessary but must follow direct identity inspection

The 10 completed repository identities collapse to 8 pinned revisions because two old cybersecurity mirrors share `2c88b96...` and two newer mirrors share `c15f73db...`. Raven also matches an old Wondel revision already canonicalized in Batch 039. Direct identity reads were still performed before canonical deduplication.

### C. “Skill quality” has at least three distinct evidence levels

1. **Prompt/policy only** — e.g. thin operator guidance.
2. **Prompt + executable helper** — e.g. Dreamina wrapper, Kagura operational scripts, rb-audit, newer cybersecurity helpers.
3. **Behaviorally evaluated implementation** — not established for the new bodies in this batch.

A script existing in a repository is stronger evidence than prose, but it is still not a passing test/eval result.

### D. Portable contracts matter more than large prompt bodies

The strongest reusable patterns in this batch are deterministic handoff artifacts, dry-run, structured output, explicit source priority, human approval, and effect boundaries. The weakest portability comes from hidden host assumptions, hard-coded paths/channels, subjective scoring, and external tool dependencies without version/eval contracts.

## Runtime/eval status

**No runtime, build, external API call, integration test, or behavioral eval was executed in Batch 040.** Source-level executable paths and tests/evals were inspected when surfaced. Therefore:

- source code existence = verified;
- documented command behavior = source-level claim unless implemented in inspected code;
- test/eval pass = **not verified**;
- external service compatibility = **not verified**;
- production readiness = **not claimed**.

## Batch totals after this run

- Repositories structure-reviewed: **400**
- Repository-scoped/canonical skill-body reports: **2851**
- Frozen canonical eligible basis: **2088 repositories**
- Arithmetic remaining estimate: **1688**
- Canonical reconciliation: **pending**

The `1688` value is only the continuation of the existing frozen arithmetic basis (`2088 - 400`). It is not a reconciled count of unique remaining GitHub repositories.