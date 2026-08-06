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
  - `"openai skills" in:name,description`, pages `1-10`
  - `"anthropic skills" in:name,description`, pages `1-10`
- Raw GitHub search hits: `1146`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1150`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1068`
- Exact duplicates removed across current inputs: `82`
- New unique repositories added in this run: `99`
- Provisionally eligible for later deep analysis: `743`
- Held as adjacent or unclear search hits: `325`

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
- OpenAI-skills delta: [`batches/openai-skills-pages-1-10.json`](batches/openai-skills-pages-1-10.json), `100` new repositories from `100` raw identities.
- Anthropic-skills delta: [`batches/anthropic-skills-pages-1-10.json`](batches/anthropic-skills-pages-1-10.json), `99` new repositories from `100` raw identities.

## This run

The focused `"anthropic skills" in:name,description` query collected pages `1-10`, with `10` repository identities per page.

- Raw repository identities: `100`
- Internal batch duplicates: `0`
- Already present in the current `969`-repository catalog: `1`
- Added as new repositories: `99`
- Updated composed catalog: `1068`

Duplicate removed:

- `LeastBit/Claude_skills_zh-CN`

The complete ordered result set, provisional classification, and per-identity new/duplicate status are stored in the batch artifact.

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 1 | 1 |
| `skill_collection` | 65 | 64 |
| `single_skill_or_domain_package` | 3 | 3 |
| `awesome_index` | 0 | 0 |
| `skill_tooling` | 20 | 20 |
| `adjacent_search_hit` | 7 | 7 |
| `unclear_search_hit` | 4 | 4 |

## Classification totals

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 2 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 404 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 78 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 223 | Repository identity indicates Skill discovery, validation, scanning, packaging, management, marketplace, catalog, registry, hub, directory, client, CLI, or runtime tooling. |
| `adjacent_search_hit` | 115 | Search hit is related to agents, OpenAI, Anthropic, MCP, Claude, Codex, or Skills but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 210 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified that repository identities existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- Anthropic-skills batch commit: `e09c55a308e2facf5ef2fe97c8a018c5a81613ce`.
- Composed latest-manifest commit: `34e38345a9d1d5042ec59542786b436aaecb22a0`.
- The current batch contains `100` unique case-insensitive keys internally.
- Exact identity comparison found `1` repository in the current `969`-repository catalog.
- Prior `969` plus `99` new repositories resolves to `1068`.
- Classification totals resolve to `1068` repositories.
- `743 + 325 = 1068`, matching the eligible and held partitions.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new repositories.
