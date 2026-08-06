# GitHub Agent Skills Repository Index

## Current verified catalog

- Search queries completed:
  - `"agent skills" in:name,description`, pages `1-10`
  - `"codex skills" in:name,description`, pages `1-10`
  - `"claude skills" in:name,description`, pages `1-10`
  - `"mcp skills" in:name,description`, pages `1-10`
  - `"skill catalog" in:name,description`, pages `1-10`
  - `"skill registry" in:name,description`, pages `1-10`
  - `"agent skill" in:name,description`, pages `1-10`
  - `"agentskills cli" in:name,description`, page `1`
  - `"skill marketplace" in:name,description`, pages `1-10`
  - `"agent skills hub" in:name,description`, pages `1-2`
  - `"skill hub" in:name,description`, pages `1-10`
  - `"agent skills directory" in:name,description`, pages `1-2`
- Raw GitHub search hits: `946`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `950`
- Unique repositories after case-insensitive `owner/repository` deduplication: `869`
- Exact duplicates removed across current inputs: `81`
- New unique repositories added in this run: `19`
- Provisionally eligible for later deep analysis: `561`
- Held as adjacent or unclear search hits: `308`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The composed catalog currently consists of:

- Base catalog: [`github-agent-skills-index.json`](github-agent-skills-index.json), `304` repositories.
- MCP delta: [`batches/mcp-skills-pages-1-10.json`](batches/mcp-skills-pages-1-10.json), `100` new repositories.
- Skill-catalog delta: [`batches/skill-catalog-pages-1-10.json`](batches/skill-catalog-pages-1-10.json), `98` new repositories from `100` raw identities.
- Skill-registry delta: [`batches/skill-registry-pages-1-10.json`](batches/skill-registry-pages-1-10.json), `95` new repositories from `100` raw identities.
- Agent-skill delta: [`batches/agent-skill-pages-1-10.json`](batches/agent-skill-pages-1-10.json), `44` new repositories from `100` raw identities.
- AgentSkills-CLI delta: [`batches/agentskills-cli-search.json`](batches/agentskills-cli-search.json), `6` new repositories from `6` raw identities.
- Skill-marketplace delta: [`batches/skill-marketplace-pages-1-10.json`](batches/skill-marketplace-pages-1-10.json), `96` new repositories from `100` raw identities.
- Agent-skills-hub delta: [`batches/agent-skills-hub-pages-1-2.json`](batches/agent-skills-hub-pages-1-2.json), `20` new repositories from `20` raw identities.
- Skill-hub delta: [`batches/skill-hub-pages-1-10.json`](batches/skill-hub-pages-1-10.json), `87` new repositories from `100` raw identities.
- Agent-skills-directory delta: [`batches/agent-skills-directory-pages-1-2.json`](batches/agent-skills-directory-pages-1-2.json), `19` new repositories from `20` raw identities.

## This run

The focused `"agent skills directory" in:name,description` query collected pages `1-2`, with `10` repository identities per page.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Already present in the current `850`-repository catalog: `1`
- Added as new repositories: `19`
- Updated composed catalog: `869`

Exact duplicate removed:

- `heilcheng/awesome-agent-skills`

The complete ordered result set, provisional classification, and per-identity new/duplicate status are stored in the batch artifact.

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 0 | 0 |
| `skill_collection` | 10 | 10 |
| `single_skill_or_domain_package` | 1 | 1 |
| `awesome_index` | 2 | 1 |
| `skill_tooling` | 6 | 6 |
| `adjacent_search_hit` | 1 | 1 |
| `unclear_search_hit` | 0 | 0 |

## Classification totals

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 1 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 260 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 64 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 200 | Repository identity indicates Skill discovery, validation, scanning, packaging, management, marketplace, catalog, registry, hub, directory, client, CLI, or runtime tooling. |
| `adjacent_search_hit` | 106 | Search hit is related to agents or Skills but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 202 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified that repository identities existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- Agent-skills-directory batch commit: `1ed0a3096447476819a73ea046f573563d1e8f12`.
- Composed latest-manifest commit: `409fe653e768b349f7cb8fe595b99fae94de015a`.
- The current batch contains `20` unique case-insensitive keys internally.
- Exact identity comparison found `1` repository in the current `850`-repository catalog.
- Prior `850` plus `19` new repositories resolves to `869`.
- Classification totals resolve to `869` repositories.
- `561 + 308 = 869`, matching the eligible and held partitions.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new repositories.
