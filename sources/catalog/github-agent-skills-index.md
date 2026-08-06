# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1401`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1405`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1307`
- Exact duplicates removed across current inputs: `98`
- New unique repositories added in this run: `51`
- Provisionally eligible for later deep analysis: `949`
- Held as adjacent or unclear search hits: `358`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## Completed search coverage

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
- `"agent skills marketplace" in:name,description`, pages `1-10`
- `"agentskills specification" in:name,description`, page `1`
- `"skill lint" in:name,description`, complete accessible page-1 result set with `100` requested results
- `"agent skills validator" in:name,description`, complete accessible page-1 result set with `100` requested results

## Composition

The composed catalog consists of the `304`-repository base catalog plus these verified deltas:

| Batch | Raw | Duplicates | New |
| --- | ---: | ---: | ---: |
| `mcp-skills-pages-1-10.json` | 100 | 0 | 100 |
| `skill-catalog-pages-1-10.json` | 100 | 2 | 98 |
| `skill-registry-pages-1-10.json` | 100 | 5 | 95 |
| `agent-skill-pages-1-10.json` | 100 | 56 | 44 |
| `agentskills-cli-search.json` | 6 | 0 | 6 |
| `skill-marketplace-pages-1-10.json` | 100 | 4 | 96 |
| `agent-skills-hub-pages-1-2.json` | 20 | 0 | 20 |
| `skill-hub-pages-1-10.json` | 100 | 13 | 87 |
| `agent-skills-directory-pages-1-2.json` | 20 | 1 | 19 |
| `openai-skills-pages-1-10.json` | 100 | 0 | 100 |
| `anthropic-skills-pages-1-10.json` | 100 | 1 | 99 |
| `agent-skills-marketplace-pages-1-10.json` | 100 | 14 | 86 |
| `agentskills-specification-search.json` | 12 | 0 | 12 |
| `skill-lint-search.json` | 90 | 0 | 90 |
| `agent-skills-validator-search.json` | 53 | 2 | 51 |

## This run

Query:

```text
"agent skills validator" in:name,description
```

GitHub returned `53` accessible repository identities in the complete page-1 result set when requesting up to `100` results.

- Raw repository identities: `53`
- Internal batch duplicates: `0`
- Exact case-insensitive identities already present in the prior `1256`-repository catalog: `2`
- Added as new repositories: `51`
- Updated composed catalog: `1307`

Duplicates removed:

```text
swarmclawai/agent-skills-lint
kriptoburak/agent-skills-lint
```

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 2 | 2 |
| `skill_collection` | 27 | 27 |
| `single_skill_or_domain_package` | 1 | 1 |
| `awesome_index` | 0 | 0 |
| `skill_tooling` | 17 | 15 |
| `adjacent_search_hit` | 3 | 3 |
| `unclear_search_hit` | 3 | 3 |

The complete ordered result set, provisional classifications, and per-identity deduplication status are stored in [`batches/agent-skills-validator-search.json`](batches/agent-skills-validator-search.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 4 | Identity strongly indicates a Skill specification or normative guidance. |
| `skill_collection` | 461 | Identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 80 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Identity indicates a curated Skill index. |
| `skill_tooling` | 368 | Identity indicates validation, linting, evaluation, packaging, discovery, registry, marketplace, management, or runtime tooling. |
| `adjacent_search_hit` | 132 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 226 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified repository identities and accessibility. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- Agent-skills-validator batch commit: `466e0a94b4e01f73a040c0817fc3e76390b0a6cd`.
- Composed latest-manifest commit: `d2f7a6324cad6073031bb3b412d5fd48eb95d223`.
- The current batch contains `53` unique case-insensitive repository keys.
- Prior `1256` plus `51` new repositories resolves to `1307`.
- `1405 - 98 = 1307`.
- Classification totals resolve to `1307` repositories.
- `949 + 358 = 1307`, matching the eligible and held partitions.
- Deduplication used exact case-insensitive identity comparison against the GitHub-indexed `1154`-repository AI-handbook snapshot, then direct comparison with the two newer batches totaling `102` repositories.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new identities.
