# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1621`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1625`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1524`
- Exact duplicates removed across current inputs: `101`
- New unique repositories collected in this run: `19`
- Net catalog delta versus the previous published manifest: `+19`
- Provisionally eligible for later deep analysis: `1157`
- Held as adjacent or unclear search hits: `367`

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
- `"agent skills eval" in:name,description`, page `1`, `20` results per page

## Composition

The composed catalog consists of the `304`-repository base catalog plus verified delta batches. The completed `agent skills standard` portion is:

| Batch | Raw | Duplicates | New |
| --- | ---: | ---: | ---: |
| `agent-skills-standard-page-1.json` | 20 | 2 | 18 |
| `agent-skills-standard-page-2.json` | 20 | 0 | 20 |
| `agent-skills-standard-page-3.json` | 20 | 0 | 20 |
| `agent-skills-standard-pages-4-6.json` | 60 | 0 | 60 |
| `agent-skills-standard-page-7.json` | 20 | 0 | 20 |
| `agent-skills-standard-page-8.json` | 20 | 0 | 20 |
| `agent-skills-standard-pages-9-10.json` | 40 | 0 | 40 |

Current evaluation-query batch:

| Batch | Raw | Duplicates | New |
| --- | ---: | ---: | ---: |
| `agent-skills-eval-page-1.json` | 20 | 1 | 19 |

The full machine-readable composition, including all earlier batches and their commit references, is stored in [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## This run

Query:

```text
"agent skills eval" in:name,description
```

This run collected page `1`, using `per_page=20`.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Duplicates against the prior catalog: `1`
- Added as new repositories: `19`
- Previous composed catalog: `1505`
- Updated composed catalog: `1524`

`darkrishabh/agent-skills-eval` was already present in [`batches/agent-skill-pages-1-10.json`](batches/agent-skill-pages-1-10.json), so it was not added again. All 20 returned repositories are provisionally classified as `skill_tooling` from repository identity and query context only. The complete page order, GitHub IDs, default branches, sizes, classification, and deduplication state are stored in [`batches/agent-skills-eval-page-1.json`](batches/agent-skills-eval-page-1.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 162 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 484 | Identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 87 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Identity indicates a curated Skill index. |
| `skill_tooling` | 388 | Identity indicates validation, linting, evaluation, packaging, discovery, registry, marketplace, management, or runtime tooling. |
| `adjacent_search_hit` | 136 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 231 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and query context only. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed.

## Validation

- `agent skills eval` page `1` batch commit: `1d4ec765bf679ebd135b4a1169413ff48610e1bb`.
- Composed latest-manifest commit: `21139d8e0356be25e97fb43821108f01a0d0ffff`.
- `1505 + 19 = 1524` current unique repositories.
- `1625 - 101 = 1524` raw-to-unique reconciliation.
- Classification totals resolve to `1524`.
- `1157 + 367 = 1524`, matching the eligible and held partitions.
- No README, `SKILL.md`, scripts, references, evaluations, stars, or implementation contents were read during this index-only run.
- The next index run should continue `"agent skills eval" in:name,description` from page `2` with `per_page=20`.
