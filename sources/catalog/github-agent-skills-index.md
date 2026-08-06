# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1706`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1710`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1608`
- Exact duplicates removed across current inputs: `102`
- New unique repositories collected in this run: `45`
- Net catalog delta versus the previous published manifest: `+45`
- Provisionally eligible for later deep analysis: `1233`
- Held as adjacent or unclear search hits: `375`

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

## Composition

The composed catalog consists of the `304`-repository base catalog plus verified delta batches. Recent evaluation, benchmark, and testing query batches are:

| Batch | Raw | Duplicates | New |
| --- | ---: | ---: | ---: |
| `agent-skills-eval-page-1.json` | 20 | 1 | 19 |
| `agent-skills-eval-page-2.json` | 20 | 1 | 19 |
| `agent-skills-eval-page-3.json` | 4 | 0 | 4 |
| `agent-skills-benchmark-search.json` | 16 | 0 | 16 |
| `agent-skills-test-search.json` | 45 | 0 | 45 |

The full machine-readable composition, including all earlier batches and commit references, is stored in [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## This run

Query:

```text
"agent skills test" in:name,description
```

This run requested `50` repositories on page `1`, received `45`, then queried page `2` to verify the terminal boundary.

- Raw repository identities on page 1: `45`
- Page 2 repository identities: `0`
- Internal batch duplicates: `0`
- Duplicates against the prior catalog: `0`
- Added as new repositories: `45`
- Previous composed catalog: `1563`
- Updated composed catalog: `1608`

Each candidate owner identity was checked against the indexed AI-handbook code-search snapshot. Because that search snapshot did not necessarily include the immediately preceding benchmark delta, [`batches/agent-skills-benchmark-search.json`](batches/agent-skills-benchmark-search.json) was also fetched from `main` and compared directly. No exact prior `owner/repository` match was found.

Classification remained identity-only. The 45 candidates were provisionally divided into `30 skill_tooling`, `4 skill_collection`, `2 single_skill_or_domain_package`, `1 specification`, `1 adjacent_search_hit`, and `7 unclear_search_hit`. The adjacent and unclear candidates are held rather than treated as deep-analysis qualified. Complete GitHub IDs, default branches, repository sizes, archived flags, ordering, provisional classifications, eligibility flags, and deduplication state are stored in [`batches/agent-skills-test-search.json`](batches/agent-skills-test-search.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 488 | Identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 89 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Identity indicates a curated Skill index. |
| `skill_tooling` | 457 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, or runtime tooling. |
| `adjacent_search_hit` | 137 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 238 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- `agent skills test` batch commit: `f1882a1c0727b514749f2251f80118d95088bc13`.
- Composed latest-manifest commit: `300b78f4cd29ff3f5a17eedfe1664eb65c24e383`.
- `1563 + 45 = 1608` current unique repositories.
- `1710 - 102 = 1608` raw-to-unique reconciliation.
- Classification totals resolve to `1608`.
- `1233 + 375 = 1608`, matching the eligible and held partitions.
- GitHub search page `2` returned zero repositories, so the accessible `"agent skills test"` query is complete at this pagination size.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
