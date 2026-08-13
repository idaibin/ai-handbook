# Four-skill parity benchmark after human-writing optimization

Date: 2026-08-13  
Status: completed pilot; measured parity on this corpus, not a cross-model or cross-genre stability claim

## Result

On the same ten-case source-grounded benchmark that previously put Humanizer-zh 0.734 points ahead, the release-candidate `human-writing` reached the same top tier in the final comparison. It scored **4.789/5 on the six repair cases**, with **5.000 fidelity and zero judge-flagged semantic hard issues**. Humanizer scored 4.800; Humanizer-zh scored 4.467 with three hard-issue flags. The 0.011 gap to humanizer is not meaningful at this pilot's resolution, while `human-writing` had the largest blind first-place share.

This establishes parity on the fixed benchmark: `human-writing` exceeded Humanizer-zh on repair mean, fidelity, structure, restraint, and blind first-place share in the final comparison. It does not establish that any skill is universally superior; one generation per revision and three judges from one model family leave substantial run-to-run uncertainty.

| Skill | Repair mean / 5 | Fidelity | Structure | Clarity | Naturalness | Restraint | Hard issues / 18 | Repair first share / 18 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| humanizer | **4.800** | 4.667 | **5.000** | 4.889 | 4.778 | 4.667 | 3 | 5.083 |
| human-writing | 4.789 | **5.000** | 4.667 | 4.944 | 4.667 | **4.667** | **0** | **7.750** |
| stop-slop | 4.589 | 3.889 | **5.000** | **5.000** | **4.889** | 4.167 | 9 | 2.417 |
| Humanizer-zh | 4.467 | 4.667 | 4.278 | 4.889 | 4.500 | 4.000 | 3 | 2.750 |

All four skills preserved every explicitly protected span in 10/10 cases and returned all four already-compact controls exactly unchanged. The controls used an explicit conditional no-op instruction, so they test instruction following rather than spontaneous restraint.

## What changed

The original benchmark showed that `human-writing` preserved facts but split related conditions and limits into too many bullets. Directness was already part of its contract; the semantic-unit revision selectively adopted the useful new behavior observed in Humanizer-zh: grouping by complete meaning. It did not adopt Humanizer-zh instructions that invite invented personality, first-person experience, emotion, or unsupported detail.

The first fresh comparison found the structure problem fixed, but one judge caught a dropped `主要` in C03. The next revision added a private qualifier ledger and an explicit item-by-item check for frequency, priority, exclusivity, extent, lower bounds, confidence, and evidence-status terms. A preflight generation still dropped `主要`; that failed artifact is saved. Independent review then clarified that qualifier restoration applies only to retained or transformed claims, so authorized compression can omit an entire secondary claim. The release candidate passed three isolated qualifier-boundary tasks before its final generation and blind evaluation.

| Revision/run | human-writing repair mean | Humanizer-zh repair mean | human-writing hard issues | Finding |
| --- | ---: | ---: | ---: | --- |
| Original benchmark | 4.122 | **4.856** | 0 | Faithful, but C01-C04 were over-split. |
| Semantic-unit revision | **4.878** | 3.922 | 1 | Structure reached 5.000; C03 lost `主要`. |
| Qualifier-lock revision before compression clarification | **4.900** | 4.556 | **0** | Parity measured, but contract review found an authorized-summary conflict. |
| Release candidate | 4.789 | 4.467 | **0** | Parity target met; compression boundary also passed isolated behavior checks. |

These are independent single-generation runs, not repeated samples of an invariant skill score. Humanizer-zh's change from 4.856 to 3.922 to 4.556 is direct evidence that a single leaderboard number is noisy.

The original run did not expose its model identity, while the later runs used `gpt-5.6-sol`. Therefore the score progression is descriptive history, not an isolated estimate of the Skill edits' causal effect. The parity conclusion relies only on the final fixed-output four-skill comparison. For that last comparison, the three other skills' outputs were kept fixed from the immediately preceding same-model round, only the changed `human-writing` was regenerated, and all three anonymous judge sheets were regenerated; this isolates the release-candidate change from extra comparator sampling noise.

## Per-case final result

Each value is the mean of five dimensions from three anonymous judges.

| Case | human-writing | humanizer | Humanizer-zh | stop-slop | Main finding |
| --- | ---: | ---: | ---: | ---: | --- |
| C01 | **5.000** | 4.600 | 3.267 | 4.600 | `human-writing` kept five responsibilities and their modalities together. |
| C02 | 4.000 | **5.000** | 4.000 | **5.000** | The release run separated before/after lifecycle actions; judges found the six-item result more fragmented. |
| C03 | **4.933** | **4.933** | 4.667 | 4.200 | The qualifier lock preserved `主要` and the interpretation boundary. |
| C04 | **4.933** | 4.733 | **4.933** | 4.600 | `human-writing` retained four coherent units without an evidence-ceiling flag. |
| C05 | 4.867 | **5.000** | **5.000** | 4.867 | All candidates were faithful; paragraph density created the difference. |
| C06 | **5.000** | 4.533 | 4.933 | 4.267 | `human-writing` preserved all five findings and `automatically`. |

N01-N04 were four-way 5.000 ties because every output exactly matched the already-compact input.

## Procedure

1. Reuse the fixed ten-case corpus, six controlled degradations, four controls, instructions, references, protected spans, and comparison-skill commits from the original benchmark.
2. Materialize each skill at the commit in `manifest.yaml`. Give isolated generation agents only the assigned skill and neutral `generator-inputs.md`; expected answers, source paths, labels, other skills, and prior results remain hidden. In the final release comparison, keep the unchanged three comparison outputs fixed, regenerate only the changed `human-writing`, then regenerate all judge packets and judgments.
3. Run `evaluate.py`. It fails closed if a source/reference check, protected span, or conditional no-op check fails, then emits three Latin-rotated anonymous packets.
4. Give each fresh judge only one packet containing five anchored dimensions, the hard-issue rule, a reference used as a style aid rather than a unique answer, and a case-specific semantic criterion.
5. Run `aggregate.py`; it fails unless all mappings are bijections, all 120 score rows and 30 rankings parse, A-D appears exactly once per ranking, scores are in range, and first-place shares balance.
6. Run adversarial parser regressions in `test_aggregate.py` and preserve every output, packet, mapping, judge sheet, and JSON aggregate.

The generator and judges used `gpt-5.6-sol` with high reasoning effort. Exact sampling parameters were not exposed. No AI detector score was used.

## Saved artifacts

- `outputs/`: forty final artifacts plus each agent's read constraint and actual file list
- `results/automatic.json`: deterministic gates, output hashes, and similarity diagnostics
- `results/blind-review-1.md` to `blind-review-3.md`: balanced anonymous packets
- `results/judge-1.md` to `judge-3.md`: complete anchored blind reviews
- `results/qualifier-boundary-output.md`: isolated grouping, authorized-compression, and Chinese-to-English qualifier checks
- `results/blind-mappings.json` and `results/aggregate.json`: unblinding map and machine-readable scores
- `cases.md`, `generator-inputs.md`, `protocol.md`, and `manifest.yaml`: fixed corpus and exact execution contracts
- `evaluate.py`, `aggregate.py`, and `test_aggregate.py`: reproducible gates and aggregation
- `rounds/pre-qualifier-lock/`: the 4.878 intermediate comparison with all forty outputs and three judge sheets
- `rounds/qualifier-lock-preflight-failure/`: the stopped generation that still dropped `主要`
- `rounds/pre-compression-clarification/`: the 4.900 revision that independent review rejected as the release contract

The earlier original benchmark and semantic-unit holdout remain separate immutable experiment directories. GitHub is the durable evidence store; a Google Drive duplicate is unnecessary because all inputs, outputs, judgments, scripts, hashes, and fixed commit identities fit in version control.

## Limits and decision

- The corpus is ten excerpts from one technical/research repository, not a general writing sample.
- One final generation per skill cannot estimate variance or prove stable ordering.
- Three judges from the same model family can share blind spots.
- The benchmark covers rewriting and restraint, not fiction, marketing, personal essays, or long-form narrative.

Decision: the user-requested **same-benchmark parity target is met**. Keep the package status at `pilot` until repeated multi-model runs, broader genres, and an independent human panel support a `stable` claim.

## Reproduce

```bash
python3 experiments/human-writing/2026-08-13-four-skill-parity-benchmark/evaluate.py
python3 experiments/human-writing/2026-08-13-four-skill-parity-benchmark/aggregate.py
python3 experiments/human-writing/2026-08-13-four-skill-parity-benchmark/test_aggregate.py
git diff --check
```
