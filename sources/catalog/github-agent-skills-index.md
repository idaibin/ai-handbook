# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1421`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1425`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1327`
- Exact duplicates removed across current inputs: `98`
- New unique repositories added in this run: `20`
- Provisionally eligible for later deep analysis: `963`
- Held as adjacent or unclear search hits: `364`

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
- `"agent skills standard" in:name,description`, page `1`, first `20` results

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
| `agent-skills-standard-page-1.json` | 20 | 0 | 20 |

## This run

Query:

```text
"agent skills standard" in:name,description
```

This batch records the first `20` GitHub repository-search results from page `1` using `per_page=20`.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Exact case-insensitive identities found in the prior `1307`-repository catalog: `0`
- Added as new repositories: `20`
- Updated composed catalog: `1327`

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 3 | 3 |
| `skill_collection` | 8 | 8 |
| `single_skill_or_domain_package` | 3 | 3 |
| `awesome_index` | 0 | 0 |
| `skill_tooling` | 0 | 0 |
| `adjacent_search_hit` | 2 | 2 |
| `unclear_search_hit` | 4 | 4 |

The complete ordered result set, provisional classifications, and per-identity deduplication status are stored in [`batches/agent-skills-standard-page-1.json`](batches/agent-skills-standard-page-1.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 7 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 469 | Identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 83 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Identity indicates a curated Skill index. |
| `skill_tooling` | 368 | Identity indicates validation, linting, evaluation, packaging, discovery, registry, marketplace, management, or runtime tooling. |
| `adjacent_search_hit` | 134 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 230 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified repository identities and accessibility. Classifications are provisional from repository identity only. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed.

## Validation

- Agent-skills-standard batch commit: `67796335a00c9f9acd006fa3818e434d513ffa24`.
- Composed latest-manifest commit: `125308257abb14b7d67c3e5086d1fea1d0057a77`.
- The current batch contains `20` unique case-insensitive repository keys.
- Prior `1307` plus `20` new repositories resolves to `1327`.
- `1425 - 98 = 1327`.
- Classification totals resolve to `1327` repositories.
- `963 + 364 = 1327`, matching the eligible and held partitions.
- Each returned `owner/repository` identity was checked against the existing AI-handbook catalog artifacts through GitHub repository code search before being recorded as new.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), continue this query from page `2` if using `per_page=20`, preserve query origins, and add only genuinely new identities.
