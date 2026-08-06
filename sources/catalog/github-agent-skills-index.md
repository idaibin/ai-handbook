# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1715`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1719`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1617`
- Exact duplicates removed across current inputs: `102`
- New unique repositories collected in this run: `9`
- Net catalog delta versus the previous published manifest: `+9`
- Provisionally eligible for later deep analysis: `1242`
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
- `"agentskills sdk" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`

## Composition

The composed catalog consists of the `304`-repository base catalog plus verified delta batches. Recent evaluation, benchmark, testing, and SDK query batches are:

| Batch | Raw | Duplicates | New |
| --- | ---: | ---: | ---: |
| `agent-skills-eval-page-1.json` | 20 | 1 | 19 |
| `agent-skills-eval-page-2.json` | 20 | 1 | 19 |
| `agent-skills-eval-page-3.json` | 4 | 0 | 4 |
| `agent-skills-benchmark-search.json` | 16 | 0 | 16 |
| `agent-skills-test-search.json` | 45 | 0 | 45 |
| `agentskills-sdk-search.json` | 9 | 0 | 9 |

The full machine-readable composition, including all earlier batches and commit references, is stored in [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## This run

Query:

```text
"agentskills sdk" in:name,description
```

This run requested `50` repositories on page `1`, received `9`, then queried page `2` and received `0`, completing the accessible result set at this pagination size.

- Raw repository identities on page 1: `9`
- Page 2 repository identities: `0`
- Internal batch duplicates: `0`
- Duplicates against the prior catalog: `0`
- Added as new repositories: `9`
- Previous composed catalog: `1608`
- Updated composed catalog: `1617`

The nine identities were checked against the `304`-repository base catalog, the broad `agent skill` pages `1-10` batch, the existing `agentskills cli` and `agentskills specification` batches, the current AI-handbook code-search snapshot, and the immediately preceding benchmark/test batches. No exact case-insensitive `owner/repository` match was found.

All nine candidates are provisionally classified as `skill_tooling` because their repository identities and the search query identify Agent Skills SDK/tooling packages. Complete GitHub IDs, default branches, repository sizes, archived flags, ordering, eligibility, and deduplication state are stored in [`batches/agentskills-sdk-search.json`](batches/agentskills-sdk-search.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 488 | Identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 89 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Identity indicates a curated Skill index. |
| `skill_tooling` | 466 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, or runtime tooling. |
| `adjacent_search_hit` | 137 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 238 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- `agentskills sdk` batch commit: `665338816d22abb26dc2aa479d2474ef4e47bba3`.
- Composed latest-manifest commit: `233fd5b594cd6dc71faadfe4f61e6f956879bb66`.
- `1608 + 9 = 1617` current unique repositories.
- `1719 - 102 = 1617` raw-to-unique reconciliation.
- Classification totals resolve to `1617`.
- `1242 + 375 = 1617`, matching the eligible and held partitions.
- GitHub search page `2` returned zero repositories, so the accessible `"agentskills sdk"` query is complete at this pagination size.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
