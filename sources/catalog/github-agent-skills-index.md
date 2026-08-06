# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1661`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1665`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1563`
- Exact duplicates removed across current inputs: `102`
- New unique repositories collected in this run: `16`
- Net catalog delta versus the previous published manifest: `+16`
- Provisionally eligible for later deep analysis: `1196`
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
- `"agent skills eval" in:name,description`, complete accessible pages `1-3`, `20` requested results per page; page `4` returned `0`
- `"agent skills benchmark" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`

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

Completed evaluation and benchmark query batches:

| Batch | Raw | Duplicates | New |
| --- | ---: | ---: | ---: |
| `agent-skills-eval-page-1.json` | 20 | 1 | 19 |
| `agent-skills-eval-page-2.json` | 20 | 1 | 19 |
| `agent-skills-eval-page-3.json` | 4 | 0 | 4 |
| `agent-skills-benchmark-search.json` | 16 | 0 | 16 |

The full machine-readable composition, including all earlier batches and their commit references, is stored in [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## This run

Query:

```text
"agent skills benchmark" in:name,description
```

This run requested `50` repositories on page `1`, received `16`, then queried page `2` to verify the terminal boundary.

- Raw repository identities on page 1: `16`
- Page 2 repository identities: `0`
- Internal batch duplicates: `0`
- Duplicates against the prior catalog: `0`
- Added as new repositories: `16`
- Previous composed catalog: `1547`
- Updated composed catalog: `1563`

Case-insensitive full-name searches against the current AI-handbook indexed artifacts found no prior match for any of the sixteen repository identities. The result set contains benchmark and evaluation-oriented repositories such as `claudekit/skillmark`, `milesgoscha/skillbench`, `djm204/agent-skills-benchmarks`, `GeorgeQLe/agentic-skills-benchmarks`, and `RohanT766/skill-test-generator`, plus related benchmark forks returned by the same repository search. All sixteen are provisionally classified as `skill_tooling` from repository identity and query context only. Complete GitHub IDs, default branches, sizes, ordering, classification, and deduplication state are stored in [`batches/agent-skills-benchmark-search.json`](batches/agent-skills-benchmark-search.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 162 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 484 | Identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 87 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Identity indicates a curated Skill index. |
| `skill_tooling` | 427 | Identity indicates validation, linting, evaluation, packaging, discovery, registry, marketplace, management, benchmark, or runtime tooling. |
| `adjacent_search_hit` | 136 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 231 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and query context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- `agent skills benchmark` batch commit: `be28b04abc3fceb3c03e87d6172af6e15f8214ac`.
- Composed latest-manifest commit: `4bb54d22e8ab0ec97cabbfa99e74d43187aac05a`.
- `1547 + 16 = 1563` current unique repositories.
- `1665 - 102 = 1563` raw-to-unique reconciliation.
- Classification totals resolve to `1563`.
- `1196 + 367 = 1563`, matching the eligible and held partitions.
- GitHub search page `2` returned zero repositories, so the accessible `"agent skills benchmark"` query is complete at this pagination size.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
