# human-writing semantic-unit follow-up

Date: 2026-08-13
Status: completed pilot follow-up; no promotion to `stable`

This experiment explains the 0.734-point repair-case gap between `Humanizer-zh` and the earlier `human-writing`, then tests a focused change to semantic-unit grouping. All prompts, raw outputs, judge sheets, deterministic criteria, adjudications, and exploratory failures are retained in this directory.

## Why the earlier score differed by 0.734

The earlier four-Skill benchmark scored six repair cases with three blind judges. `Humanizer-zh` averaged 4.856 and `human-writing` 4.122. The difference was not factual accuracy: `human-writing` had perfect fidelity (5.000) and no hard-issue flags, slightly ahead of `Humanizer-zh` (4.889, one hard issue). The gap came from list structure and editorial restraint.

| Dimension | Humanizer-zh | human-writing | Difference |
| --- | ---: | ---: | ---: |
| Fidelity | 4.889 | 5.000 | human-writing +0.111 |
| Instruction / structure | 5.000 | 3.667 | Humanizer-zh +1.333 |
| Clarity | 4.944 | 4.667 | Humanizer-zh +0.277 |
| Naturalness | 4.667 | 3.667 | Humanizer-zh +1.000 |
| Restraint | 4.778 | 3.611 | Humanizer-zh +1.167 |
| Overall | 4.856 | 4.122 | Humanizer-zh +0.734 |

The per-case pattern was concentrated in C01–C04. `human-writing` often treated each sentence or clause as a separate “fact,” splitting a policy from its exception, a capability from its limit and remaining caller duty, or a primary source from the role of alternatives. `Humanizer-zh` more often kept those dependent parts in one bullet. C05 tied; `human-writing` won C06 because it preserved claim strength better.

## Change under test

The candidate adds one execution rule and matching diagnostics/evals:

- sentence and clause boundaries are not item boundaries;
- keep rule + boundary, capability + resulting responsibility, primary choice + alternative roles, and stopping condition + mandated next action together;
- keep independently triggered actions at different lifecycle stages and parallel checklist items separate.

Fixed `idaibin/skills` revisions:

- baseline: `aa73fec2f8630886b7d60b066f1de4deff96b60a`
- final candidate: [`aeb4a29e4f3646806542a5eb3891a44b91138f82`](https://github.com/idaibin/skills/commit/aeb4a29e4f3646806542a5eb3891a44b91138f82) (same tree as locally reviewed commit `23b47664e3077c8324167e928df58e0d5398add1`)

## Evaluation results

### Original ten-case rerun

One isolated baseline run and one isolated candidate run on the original ten inputs were nearly identical and both correctly grouped C01–C04. This showed no regression but was not sensitive enough to establish an improvement. Raw runs are under `outputs/*-original-cases.md`.

### Adversarial iteration

Six harder cases moved dependent clauses into separate source sentences and added independent-list guardrails. The first candidate improved target grouping but over-merged one lifecycle case and under-edited one inline checklist. Three blind judges exposed those two boundaries. Every intermediate output and judge sheet is retained under `results/iteration/`; these are development evidence, not the final estimate.

### Frozen holdout before the final wording

The six holdout inputs and criteria were frozen before generation. Three baseline and three candidate executions produced 18 decisions per variant.

| Variant | H01 | H02 | H03 | H04 | H05 | H06 | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline | 0/3 | 0/3 | 0/3 | 3/3 | 3/3 | 3/3 | **9/18 (50.0%)** |
| Candidate iteration | 2/3 | 0/3 | 3/3 | 3/3 | 3/3 | 3/3 | **14/18 (77.8%)** |

The candidate iteration improved capability/limit/responsibility and policy/exception grouping without regressing the three guardrails. It still split H02 into three bullets rather than the frozen expected two; that failure is retained, not reclassified.

The intermediate candidate Skill tree used here was not retained as an immutable commit or content-addressed snapshot. The inputs, criteria, outputs, and decisions remain auditable, but the 14/18 result cannot be reproduced against the exact implementation. It is therefore observational development evidence, not the primary reproducible comparison and not attributable to the final candidate.

### Fixed-revision direct comparison

After independent review tightened the primary-choice rule and made the checklist format explicit, the published final candidate and immutable baseline were each run three times on the same six target and guardrail cases. The criteria file was written after the candidate outputs to make the intended closure decision executable, so this is a fixed-revision repeated regression comparison, not a preregistered holdout.

| Case | Intended behavior | Baseline | Final candidate |
| --- | --- | ---: | ---: |
| R01 | two policy bundles | 0/3 | 2/3 |
| R02 | one capability/limit/responsibility bundle | 0/3 | 2/3 |
| R03 | one cache/limit/responsibility bundle without adding causality | 0/3 | 0/3 |
| R04 | stopping policy together; lifecycle actions separate | 0/3 | 3/3 |
| R05 | four independent numbered actions | 3/3 | 3/3 |
| R06 | primary choice + alternative roles; evidence boundary separate | 0/3 | 3/3 |
| **Total** |  | **3/18 (16.7%)** | **13/18 (72.2%)** |

This is the primary reproducible result: both variants resolve to immutable Skill commits, and all 36 outputs plus the common adjudication are retained. Two otherwise well-grouped R03 outputs failed because they inserted `so`, making an implicit adjacency into an explicit causal relation; the strict score keeps those failures. The result supports a limited conclusion that the focused rule improves the observed failure mode and preserves the tested checklist guardrail, but target grouping remains stochastic and relation-preserving phrasing still needs work. It does not show that the issue is solved, that the candidate has caught `Humanizer-zh` on the original benchmark, or that `human-writing` should move from `pilot` to `stable`.

## Reproduction map

- `manifest.yaml`: immutable repository/model/run metadata
- `protocol.md`: isolation, scoring, and claim rules
- `original-generator-inputs.md`: original benchmark inputs
- `adversarial-generator-inputs.md`: development cases
- `holdout-inputs.md` and `holdout-criteria.md`: preregistered holdout materials
- `closure-inputs.md` and `closure-criteria.md`: final repeated regression materials
- `outputs/`: selected generation records
- `results/iteration/`: all exploratory outputs and three blind judge sheets
- `results/holdout/holdout-adjudication.md`: corrected deterministic holdout decision table
- `results/closure/closure-fixed-comparison.md`: immutable baseline-versus-final-candidate decision table

## Limits

- One model family and one host were used; sampling controls were not exposed.
- The corpus is small and dominated by technical-policy prose.
- No independent human editorial panel was used in this follow-up.
- AI detectors were not used; they are not an objective measure of authorship or writing quality.
- The fixed holdout measures structural criteria, not the full five-dimension score from the earlier four-Skill benchmark.
