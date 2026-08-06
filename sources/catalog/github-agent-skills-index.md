# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1348`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1352`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1256`
- Exact duplicates removed across current inputs: `96`
- New unique repositories added in this run: `90`
- Provisionally eligible for later deep analysis: `904`
- Held as adjacent or unclear search hits: `352`

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
- `"skill lint" in:name,description`, complete accessible result set on page `1` with `100` requested results per page

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

## This run

Query:

```text
"skill lint" in:name,description
```

GitHub returned `90` accessible repository identities in the complete page-1 result set when requesting up to `100` results.

- Raw repository identities: `90`
- Internal batch duplicates: `0`
- Exact case-insensitive identities already present in the prior `1166`-repository catalog: `0`
- Added as new repositories: `90`
- Updated composed catalog: `1256`

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 0 | 0 |
| `skill_collection` | 2 | 2 |
| `single_skill_or_domain_package` | 0 | 0 |
| `awesome_index` | 0 | 0 |
| `skill_tooling` | 77 | 77 |
| `adjacent_search_hit` | 3 | 3 |
| `unclear_search_hit` | 8 | 8 |

The complete ordered result set, provisional classifications, and per-identity deduplication status are stored in [`batches/skill-lint-search.json`](batches/skill-lint-search.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 2 | Identity strongly indicates a Skill specification. |
| `skill_collection` | 434 | Identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 79 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Identity indicates a curated Skill index. |
| `skill_tooling` | 353 | Identity indicates validation, linting, evaluation, packaging, discovery, registry, marketplace, management, or runtime tooling. |
| `adjacent_search_hit` | 129 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 223 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified repository identities and accessibility. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- Skill-lint batch commit: `39d18b64b3df476536383a01b4b5f60075d9056c`.
- Composed latest-manifest commit: `6033fa60d6004a6b79feb32874f1476d94ce4f39`.
- The current batch contains `90` unique case-insensitive repository keys.
- Prior `1166` plus `90` new repositories resolves to `1256`.
- Classification totals resolve to `1256` repositories.
- `904 + 352 = 1256`, matching the eligible and held partitions.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new identities.
