# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1735`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1739`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1637`
- Exact duplicates removed across current inputs: `102`
- New unique repositories collected in this run: `20`
- Net catalog delta versus the previous published manifest: `+20`
- Provisionally eligible for later deep analysis: `1255`
- Held as adjacent or unclear search hits: `382`

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
- `"agent skills standard" in:name,description`, pages `1-10`, `20` results per page
- `"agent skills eval" in:name,description`, complete accessible pages `1-3`, `20` requested results per page; page `4` returned `0`
- `"agent skills benchmark" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agent skills test" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agentskills sdk" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agent skills template" in:name,description`, page `1`, `20` results per page; page `2` has additional results and remains pending

## Composition

The composed catalog consists of the `304`-repository base catalog plus verified delta batches.

| Recent batch | Raw | Duplicates | New |
| --- | ---: | ---: | ---: |
| `agent-skills-eval-page-3.json` | 4 | 0 | 4 |
| `agent-skills-benchmark-search.json` | 16 | 0 | 16 |
| `agent-skills-test-search.json` | 45 | 0 | 45 |
| `agentskills-sdk-search.json` | 9 | 0 | 9 |
| `agent-skills-template-page-1.json` | 20 | 0 | 20 |

The full machine-readable composition, including all earlier batches and commit references, is stored in [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## This run

Query:

```text
"agent skills template" in:name,description
```

This run requested `20` repositories on page `1` and received `20`. Page `2` was checked and contains additional results, so the query is not yet exhausted.

- Raw repository identities on page 1: `20`
- Internal batch duplicates: `0`
- Duplicates against the prior catalog: `0`
- Added as new repositories: `20`
- Previous composed catalog: `1617`
- Updated composed catalog: `1637`
- Added to provisional deep-analysis queue: `13`
- Added to held-for-review: `7`

Exact owner identities for the 20 candidates were checked against the current AI-handbook code-search snapshot; the broad `agent skill` pages `1-10` batch was also inspected. No exact case-insensitive `owner/repository` match was found.

Provisional classification for this page is `11 skill_tooling`, `2 skill_collection`, `4 adjacent_search_hit`, and `3 unclear_search_hit`. Complete GitHub IDs, default branches, repository sizes, archived flags, ordering, eligibility, and deduplication state are stored in [`batches/agent-skills-template-page-1.json`](batches/agent-skills-template-page-1.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 490 | Identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 89 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Identity indicates a curated Skill index. |
| `skill_tooling` | 477 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, or runtime tooling. |
| `adjacent_search_hit` | 141 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 241 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- `agent skills template` page-1 batch commit: `7eaf00087ce5e4fe9dc150033defa47c7dddc059`.
- Composed latest-manifest commit: `8f5e7413c1d2105223b558038cea9d5969539cea`.
- `1617 + 20 = 1637` current unique repositories.
- `1739 - 102 = 1637` raw-to-unique reconciliation.
- Classification totals resolve to `1637`.
- `1255 + 382 = 1637`, matching the eligible and held partitions.
- Page `2` contains additional results; the next persisted index boundary is `"agent skills template"`, page `2`, `per_page=20`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
