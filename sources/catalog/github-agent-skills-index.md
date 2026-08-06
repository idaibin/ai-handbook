# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1601`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1605`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1505`
- Exact duplicates removed across current inputs: `100`
- New unique repositories collected in this run: `40`
- Net catalog delta versus the previous published manifest: `+40`
- Provisionally eligible for later deep analysis: `1138`
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

## Composition

The composed catalog consists of the `304`-repository base catalog plus verified delta batches. The current `agent skills standard` portion is:

| Batch | Raw | Duplicates | New |
| --- | ---: | ---: | ---: |
| `agent-skills-standard-page-1.json` | 20 | 2 | 18 |
| `agent-skills-standard-page-2.json` | 20 | 0 | 20 |
| `agent-skills-standard-page-3.json` | 20 | 0 | 20 |
| `agent-skills-standard-pages-4-6.json` | 60 | 0 | 60 |
| `agent-skills-standard-page-7.json` | 20 | 0 | 20 |
| `agent-skills-standard-page-8.json` | 20 | 0 | 20 |
| `agent-skills-standard-pages-9-10.json` | 40 | 0 | 40 |

The full machine-readable composition, including all earlier batches and their commit references, is stored in [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## This run

Query:

```text
"agent skills standard" in:name,description
```

This run collected pages `9-10`, using `per_page=20`.

- Raw repository identities: `40`
- Internal batch duplicates: `0`
- Duplicates against the prior catalog: `0`
- Added as new repositories: `40`
- Previous composed catalog: `1465`
- Updated composed catalog: `1505`

Thirty-nine returned repositories have the identity `*/agent-skills-standard` and are provisionally classified as `specification`. `ArtsiomCh/claude-skills` is provisionally classified as `skill_collection`. These classifications are based only on repository identity and query context. The complete page order, GitHub IDs, default branches, sizes, and deduplication state are stored in [`batches/agent-skills-standard-pages-9-10.json`](batches/agent-skills-standard-pages-9-10.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 162 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 484 | Identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 87 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Identity indicates a curated Skill index. |
| `skill_tooling` | 369 | Identity indicates validation, linting, evaluation, packaging, discovery, registry, marketplace, management, or runtime tooling. |
| `adjacent_search_hit` | 136 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 231 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and query context only. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed.

## Validation

- Pages `9-10` batch commit: `1cb4f8bed2cf49b9483779e43bb3e191e961a7c3`.
- Composed latest-manifest commit: `a3b225d628255ef9c4d55add9fb729483e297879`.
- `1465 + 40 = 1505` current unique repositories.
- `1605 - 100 = 1505` raw-to-unique reconciliation.
- Classification totals resolve to `1505`.
- `1138 + 367 = 1505`, matching the eligible and held partitions.
- No README, `SKILL.md`, scripts, references, evaluations, stars, or implementation contents were read during this index-only run.
- The `"agent skills standard" in:name,description` first-10-page index boundary is now complete; a subsequent index run should move to the next not-yet-covered Skills/Agent Skills repository search query.
