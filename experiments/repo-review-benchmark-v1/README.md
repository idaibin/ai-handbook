# repo-review Benchmark v1

Status: frozen protocol; dataset construction in progress  
Basis date: 2026-08-13 (Asia/Tokyo)  
Authoritative workflow: `idaibin/ai-handbook@0ebee60b6f99da21be46e4789ba44e494ad3f2c9`, `workflows/ai-engineering-system/` v0.3.0

## Decision

Evaluate whether `repo-review` finds more real, material defects with fewer false
positives than three fixed public review skills. The benchmark does not evaluate
writing style, number of comments, or repository popularity.

Primary endpoint: material-finding precision. Recall is reported only for cases whose
defect set has been fully adjudicated. A maintainer comment, linked issue, or later
commit is evidence for adjudication, not ground truth by itself.

## Fixed candidates

| ID | Repository and path | Commit | Content SHA-256 |
| --- | --- | --- | --- |
| R0 | `idaibin/skills/skills/repo-review` | `f044b8b9256dc0b8b4caee87647b17a88bca4ae0` | `c6d42cc29620e66873bd4b552d23892ed328f6b88593842c0f7d43370c1e0f19` |
| R1 | `addyosmani/agent-skills/skills/code-review-and-quality` | `be42637c5af93fdc8526b68ec2f2651b930f316c` | `8f3cabca581bbf7cb5f0add3f7454e7a4523f9d4353a6a4a217e6fa515309612` |
| R2 | `getsentry/skills/skills/code-review` | `24fdb833b9e67670a027e3b482189100a69ff7f9` | `ec5fc8855cb4648b4f2c79b608f8c8824a2da6a683330524c4d6283e4a3954c4` |
| R3 | `obra/superpowers/skills/requesting-code-review` plus `code-reviewer.md` | `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` | `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8` + `5eca5fcfd48a50e0a526ce5ffd64bf625d6b81bb46d11795274dae451fe6ffd4` |

R3 is evaluated as the repository's documented composite review package. Candidates
that require multiple parallel reviewers to preserve their native semantics are
excluded from this single-reviewer comparison.

## Dataset

Exactly 100 public GitHub PR-derived cases. Case provenance is fixed as:

| Case provenance | Count | Review basis |
| --- | ---: | --- |
| Bug-introducing commit traced from a later fix PR | 60 | parent of introducing commit → introducing commit |
| Intermediate PR revision corrected later in the same PR | 20 | PR base → pre-correction revision |
| Negative control | 20 | PR base → final merged head |

For bug-introducing cases, blame/SZZ-style tracing is discovery evidence only. The
introducing commit is accepted after the later fix, regression test or reproducer,
affected code path, and parent behavior jointly establish that the reviewed commit
introduced the target defect. If introduction cannot be distinguished from older
debt, the case is rejected.

| Language | Development | Sealed holdout | Total |
| --- | ---: | ---: | ---: |
| Rust | 27 | 7 | 34 |
| React/TypeScript | 27 | 6 | 33 |
| Java | 26 | 7 | 33 |

| Change type | Development | Sealed holdout | Total |
| --- | ---: | ---: | ---: |
| Bug fix | 24 | 6 | 30 |
| Refactor | 12 | 3 | 15 |
| API or contract | 12 | 3 | 15 |
| Persistence or migration | 12 | 3 | 15 |
| Concurrency or async | 12 | 3 | 15 |
| Integration or build | 8 | 2 | 10 |

Selection limits:

- 5-800 non-generated changed lines and no more than 30 changed files;
- size strata are fixed to 30 small cases (5-49 lines), 40 medium cases (50-199),
  and 30 large cases (200-800), distributed across development and holdout;
- immutable base and review-head SHAs must remain fetchable;
- repository guidance and the smallest necessary caller/contract context must be
  available at the review head;
- bot-only dependency bumps, formatting-only diffs, generated-only changes, and PRs
  whose decisive evidence is private are excluded;
- 80 cases contain at least one adjudicable material defect at the review head; 20
  are negative controls with no confirmed actionable defect after adjudication;
- no repository contributes more than 15 cases and no author contributes more than 3.

Positive cases use either a verified bug-introducing commit or an intermediate PR
revision. Later review comments, corrective commits, tests, fixes, and linked issue
conclusions stay sealed until all candidate outputs are locked. Negative controls use
the final merged head.

## Leakage controls

Each generation package contains only:

- repository, immutable `base_sha..review_head_sha`, PR title and pre-existing body;
- files at those SHAs, repository instructions, and relevant pre-existing spec;
- CI results that existed at or before `review_head_sha`.

It excludes review comments, review decisions, commits after `review_head_sha`, later
CI results, issue conclusions written later, benchmark labels, and oracle notes.
Network access is disabled during generation. One fresh context is used for each
candidate/case pair. Candidate labels are randomly mapped per case and output hashes
are written before any oracle is opened.

The runner prompt supplies the same task and evidence package to every candidate. It
does not add review rules beyond the selected Skill. Tool availability, model,
temperature/reasoning setting, timeout, and maximum output budget are fixed and
recorded for every run.

## Finding normalization and adjudication

A candidate statement is a finding only when it asserts a concrete, reachable defect
introduced, expanded, exposed, or relied on by the reviewed range. Style preferences,
general advice, praise, missing-runtime-evidence statements, and optional refactors
are not material findings.

A predicted finding matches an adjudicated defect only when all are substantially the
same:

1. root cause;
2. trigger or affected state;
3. concrete impact;
4. relevant code path or contract.

Nearby line overlap alone is insufficient. Duplicate findings from one candidate are
collapsed to one prediction. One broad prediction may not claim several oracle
defects unless it identifies each root cause.

Oracle construction uses maintainer feedback and later history as leads, then verifies
each proposed defect against the fixed source, tests, contracts, and reachable
behavior. Each case is independently adjudicated twice. Disagreements are resolved
without seeing candidate identity. Cases lacking enough evidence remain
`not_adjudicable` and are replaced before the dataset is frozen. The oracle is a set
of known, verified target defects; it is not assumed to enumerate every possible
defect in the reviewed change.

## Metrics

Reported overall and by language/change type:

- material-finding precision: `TP / (TP + FP)`;
- known-defect finding recall: `TP / (TP + FN)` over the verified oracle defects;
- case detection rate: positive cases with at least one matched target defect;
- false positives per case and percentage of cases with at least one false positive;
- evidence accuracy: correct file/path, code behavior, and claimed trigger;
- severity calibration: exact agreement and over/under-severity distance;
- actionable-remediation rate: proposed fix addresses the verified root cause without
  expanding scope;
- no-op accuracy on negative controls;
- process failure rate: contaminated basis, missing immutable identity, fabricated
  execution evidence, unreadable output, or mutation attempt.

Precision is the primary rank. Recall, false-positive burden, evidence accuracy,
severity, and remediation are reported separately; they are not hidden inside one
subjective weighted score. Bootstrap 95% confidence intervals are computed by case.

## Development and holdout rules

- Run development cases in eight batches of ten.
- After each batch, modify `repo-review` only for repeated failures (same root cause in
  at least three cases) or one severe failure with demonstrated P0/P1 impact.
- Never rewrite old outputs or scores after a change. A new candidate commit starts a
  new result series.
- After case 80, freeze the Skill, runner, prompts, adjudication rubric, and holdout
  manifest hashes.
- Run all 20 holdout cases once. No modification, retry, cherry-picking, or replacement
  is allowed after unsealing, except a documented infrastructure failure that affected
  every candidate equally.

## Acceptance rule

`repo-review` may be promoted by this benchmark only if, on sealed holdout:

- its precision is not lower than the best comparator by more than 3 percentage points;
- its known-defect recall is higher than every comparator or within 5 percentage
  points of the best;
- it has no more false positives per case than the best comparator by more than 0.10;
- it has zero basis contamination, mutation, fabricated evidence, or false completion
  claims;
- no language or change-type stratum exposes a repeated severe failure.

This benchmark can support `pilot` or continued `stable` status. It cannot establish
cross-model generalization or human-review equivalence because one model family and
public GitHub evidence are used.

## Current execution evidence

- `skills/main` cloned cleanly at `f044b8b9256dc0b8b4caee87647b17a88bca4ae0`.
- Package validation: 17 packages passed.
- Routing evaluation: 55/55 passed, 0 contract errors, 0 regressions.
- Repository unit tests: 348 passed.
- Full validation entry point remains incomplete: the unrelated `ui-spec`
  Design.md contract attempted to create npm state under an unavailable root path.
- GitHub sample discovery began, then stopped on a GitHub secondary rate limit as
  required by the bounded-retry policy. No failed search is counted as an empty result.
- Model-based candidate generation has not started; a fresh-context runner with
  reproducible model settings is still required.

Completion state: Incomplete. Protocol and deterministic baseline are fixed; the
100-case manifest, isolated model runs, adjudication, and holdout result remain open.
