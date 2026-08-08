# Agent Skills Repository Deep Analysis — Batch 039

- Batch ID: `2026-08-08-batch-039`
- Scope: next **10 qualified repository identities** from the deterministic indexed queue
- Repository completion rule: identity + observed Stars + pinned revision + actual repository content read; metadata-only completion is prohibited
- Repositories completed: **10**
- Unique Git commit trees represented: **4**
- Direct unique skill bodies reviewed: **6**
- New canonical individual skill reports: **6**
- Runtime/build/test/eval execution: **not_executed**

## Queue selection

The queue continued after Batch 038. `magicoolx/typewriter-video` remains held because the deterministic index classifies it as `adjacent_search_hit`; it was not used to fill the quota and is not counted complete. The next ten qualified identities were selected instead.

| Repository | GitHub ID | Stars observed | Pinned revision | Queue class | Content gate |
|---|---:|---:|---|---|---|
| `dhassell007/daily-briefing-skill` | 1199991058 | 0 | `f29c2aaedfbfb1b839414366afe587493c70e717` | single_skill_or_domain_package | README + SKILL + scripts/config read |
| `mperkins0155/wondelai-skills` | 1199052333 | 0 | `dd37ee506ff558e939b3d421557987cced49b866` | skill_collection | README + marketplace + representative skills/references/tooling read |
| `annayug1985-wq/skills_Cloude_Na_osnove_knig` | 1199491502 | 0 | `955115316fdf18eaef1ba6e7a9860704215e172f` | skill_collection | README + marketplace + representative skills/reference read |
| `ibernal-git/Anthropic-Cybersecurity-Skills` | 1199694737 | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | skill_collection | README + representative SKILL + collection index/workflow read |
| `minhnhat6/Anthropic-Cybersecurity-Skills` | 1199636417 | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | skill_collection | README + representative SKILL read directly from this identity |
| `vince6699me/Anthropic-Cybersecurity-Skills` | 1199503272 | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | skill_collection | README + representative SKILL read directly from this identity |
| `Acczdy/Anthropic-Cybersecurity-Skills` | 1199236751 | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | skill_collection | README + representative SKILL read directly from this identity |
| `dcollaoa/Anthropic-Cybersecurity-Skills` | 1199949411 | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | skill_collection | README + representative SKILL read directly from this identity |
| `paleon2010/Anthropic-Cybersecurity-Skills` | 1199130562 | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | skill_collection | README + representative SKILL read directly from this identity |
| `MacroscopeBenchmark/Anthropic-Cybersecurity-Skills` | 1199177680 | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | skill_collection | README + representative SKILL read directly from this identity |

Observed Stars are point-in-time GitHub repository-search observations made during this batch. They are not historical values.

## 1. `dhassell007/daily-briefing-skill`

### Actual structure and implementation

The repository is a single operational briefing skill rather than a prompt-only package. The pinned revision contains a README, root `SKILL.md`, Python scripts for market/news collection, `config.example.yaml`, and `requirements.txt`.

The skill combines three concerns:

1. market data collection;
2. headline/RSS collection and lightweight topic classification;
3. scheduled daily output formatting.

`market_briefing.py` calls external market sources and scrapes precious-metals HTML. `headlines_briefing.py` fetches RSS/web content and applies heuristic topic grouping. Configuration documentation describes ETF, treasury, news-source, and API-key settings.

### Findings

- **Critical secret/configuration defect:** the implementation contains a committed hard-coded Alpha Vantage API credential. The secret value is intentionally not copied into this report. Documentation recommends environment/config based key management, so implementation and documentation disagree. Rotate/remove the credential and scan history before reuse.
- **Configuration is not authoritative:** `config.example.yaml` describes configurable symbols and an environment variable, while the inspected implementation uses fixed symbols/settings in code. This creates false confidence that user configuration is effective.
- **Dependency/config drift:** `requirements.txt` includes dependencies that the inspected scripts do not clearly consume, while the scripts rely heavily on standard-library HTTP/XML handling.
- **Scraping is brittle:** precious-metals extraction depends on external HTML shape and broad error handling. A markup change can silently degrade the report.
- **Source quality/freshness is weakly modeled:** headline ingestion does not provide a strong deduplication, provenance, publication-time validation, or stale-feed policy.
- **No repository-local test/eval files surfaced** from direct search for common test/eval terms. No execution was performed in this batch.

### Verdict

Useful small operational skill, but not safe to adopt unchanged because committed credential handling and configuration drift break the repository's own documented contract. Prefer environment-only secrets, one parsed configuration object, deterministic source adapters, fixture-based parser tests, and explicit freshness/provenance fields.

## 2. `mperkins0155/wondelai-skills`

### Actual structure

The current pinned revision is a multi-skill collection. Its marketplace manifest describes **62 skills**: 50 framework/expert skills plus 12 orchestration/metaskills grouped into plugin collections. The repository supports multiple agent harnesses and contains generation/synchronization tooling rather than only Markdown files.

Direct content reads in this batch included:

- repository README;
- `.claude-plugin/marketplace.json`;
- `jobs-to-be-done/SKILL.md`;
- `create-business/SKILL.md`;
- `create-business/references/artifact-templates.md`;
- `scripts/generate-codex-plugins.sh`.

The Codex-generation script explicitly treats the Claude marketplace as a single source of truth, regenerates Codex plugin manifests and skill symlinks, validates generated JSON, and checks for broken symlinks. This is concrete repository tooling rather than a README-only compatibility claim.

### Design strengths

- **Clear catalog topology:** expert skills and orchestration skills are separated while sharing a common marketplace.
- **Cross-harness generation is deterministic:** the inspected script regenerates derived Codex artifacts instead of manually maintaining duplicate manifests.
- **Metaskill artifact contracts are explicit:** `create-business` defines phase state and stable document headings, and its reference templates make cross-skill handoffs inspectable.
- **Human evidence is preserved as a gate:** `create-business` explicitly says the human talks to customers and rejects simulated interviews as evidence.

### Risks and evidence gaps

- **Framework claims are not universal facts.** `jobs-to-be-done` contains strong heuristics and scoring rules; some are useful decision aids but are presented too categorically to be treated as empirically universal.
- **Marketing-quality ratings are subjective.** Several skills use 0–10 or “world-class” rubrics. These need task-specific evals if used as quality gates.
- **No pinned workflow run evidence:** the GitHub workflow-run lookup for the pinned commit returned no runs. The generation script was read but not executed here.
- **No dedicated eval/test harness surfaced** from repository search in this batch. Structural generation checks are not evidence of behavioral skill quality.
- **Large catalog means partial body-depth in this batch:** the 62-skill inventory is verified from the marketplace, but this repository-level completion is based on direct representative body reads plus actual collection/tooling inspection; it does not claim all 62 skill bodies were reread line-by-line in Batch 039.

### Verdict

Strong catalog/packaging reference, especially for single-source marketplace generation and resumable cross-skill artifact contracts. Adopt structural ideas, but keep framework assertions, scoring rubrics, and marketing claims separate from verified behavioral evidence.

## 3. `annayug1985-wq/skills_Cloude_Na_osnove_knig`

### Actual structure and lineage

The pinned repository is an older Wondel.ai-derived skill snapshot. Its README and marketplace point back to Wondel upstream branding/provenance, while the pinned marketplace contains **41 unique skills** in nine collections rather than the current Wondel repository's 62-skill set.

Direct reads included:

- README;
- `.claude-plugin/marketplace.json`;
- `jobs-to-be-done/SKILL.md` (version `1.1.1` at this revision);
- `top-design/SKILL.md` (version `1.2.0`);
- `top-design/references/typography.md`.

The `jobs-to-be-done` blob differs from the current Wondel repository's body, so this is not treated as an exact content mirror. `top-design` also contains repository-specific/versioned guidance.

### Findings

- **Useful historical snapshot, not the current upstream authority.** The repository should be compared against its upstream source before adopting rules.
- **Subjective scoring is encoded as normative policy.** `top-design` defines weighted 0–10 aesthetic scoring and several absolute visual rules. These can be useful critique prompts but are not objective quality measurements.
- **Accessibility and performance appear as constraints, but some aesthetic rules can conflict with them.** For example, extreme typography/motion guidance requires contextual accessibility and device-performance gates.
- **Reference material is substantive:** typography references contain concrete pairing/scale/loading guidance rather than only placeholder links.
- **No dedicated test/eval harness surfaced** in direct search. No runtime/browser evaluation was executed.

### Verdict

Valuable as a versioned design/product-framework snapshot and as evidence of skill evolution over time, but not a source to merge blindly with the current Wondel catalog. Preserve upstream/version provenance and validate subjective design rules against accessibility, performance, and project-specific goals.

## 4–10. Seven `Anthropic-Cybersecurity-Skills` repository identities

The seven selected identities are exact Git-content mirrors at the same pinned commit `2c88b96cf758c8a742c5b683e02c01e84497034f`. Each identity was still opened directly: its README and the same representative `SKILL.md` were read from that repository identity before completion. This prevents metadata-only completion while allowing content-level deduplication.

### Collection structure verified

The shared pinned content includes:

- README describing an Agent Skills cybersecurity collection;
- `.claude-plugin/marketplace.json` version `1.1.0`;
- generated `index.json` with `total_skills: 753` and 753 name/description/path records;
- `skills/<slug>/SKILL.md` packages;
- a GitHub validation workflow for structural metadata checks.

The representative body read in each identity was `skills/performing-memory-forensics-with-volatility3/SKILL.md`. The same blob was observed across all seven mirrors. The body is a detailed operational cybersecurity skill; this report deliberately records only its structure, prerequisites model, and safety/verification concerns rather than reproducing operational attack instructions.

### Collection-level findings

- **Exact mirror density is high.** Seven repository identities collapse to one Git content tree. Repository coverage and canonical skill content must remain separate counters.
- **`index.json` provides a machine-readable catalog of 753 skills**, but metadata quality is uneven: numerous descriptions in the generated index are malformed placeholder-like values such as `>` / `>-`, and multiple descriptions are visibly truncated. “753 production-grade skills” is therefore a repository claim, not a verified quality conclusion.
- **README domain counts are internally inconsistent:** prose refers to 26 domains while another section/heading reports 38. Catalog metrics need one generated authority.
- **Structural validation is real but limited.** The inspected GitHub workflow walks `SKILL.md` files and checks frontmatter fields, naming, duplicate names, and related structural constraints. It does not execute task behavior, verify cybersecurity correctness, prove safe authorization boundaries, or measure false positives/negatives.
- **Pinned workflow success was not observed:** the workflow-run lookup for the pinned commit returned no runs. No CI success is asserted.
- **Commit history shows selective content upgrades.** A prior v1.1.0 commit explicitly upgraded five skills that had weaker/stub content. This is further evidence that collection-size claims should not substitute for per-skill quality evidence.
- **Risk classification is necessary.** The catalog mixes defensive operations, governance/compliance, forensics, and offensive/red-team topics. High-risk operational skills require explicit authorization and scoped environments before execution. Batch 039 did not execute any cybersecurity procedure.
- **Representative skill-local `references/` / `scripts/` paths were not found at the checked memory-forensics skill path.** README describes optional structure, so their presence must be verified per skill rather than assumed collection-wide.

### Verdict

High-value taxonomy and large machine-readable skill corpus, but it should be ingested as a **catalog requiring per-skill quality/risk gates**, not as 753 already-validated production skills. The strongest reusable idea is the generated index + structural schema validation; the largest gaps are metadata quality, behavioral evals, safety/authorization tiers, and canonical deduplication of mirrors.

## Held/not completed

- `magicoolx/typewriter-video` — deterministic index classification `adjacent_search_hit`; not counted complete.
- `HsinTsao/Anthropic-Cybersecurity-Skills` — remains a qualified queued identity after the ten-repository batch boundary; not inspected deeply and remains pending.

## Validation boundary

### Verified in Batch 039

- 10 repository identities and observed Stars;
- 10 pinned revisions;
- actual repository content for every completed identity;
- four unique Git content trees;
- direct representative `SKILL.md` bodies, collection manifests/indexes, scripts/references/workflows when surfaced;
- exact mirror relationship for the seven cybersecurity identities by shared pinned Git commit and matching directly read content.

### Not verified / not executed

- no Python/Bash script execution;
- no network API calls from repository code;
- no browser/runtime behavior tests;
- no workflow success at the pinned revisions unless separately observed;
- no claim that every body in the 62-, 41-, or 753-skill collections was reread line-by-line in this batch;
- no claim that README quality/performance/security statements are externally validated.

Repository-level completion is therefore **content-gated structure/deep review**, not runtime certification.