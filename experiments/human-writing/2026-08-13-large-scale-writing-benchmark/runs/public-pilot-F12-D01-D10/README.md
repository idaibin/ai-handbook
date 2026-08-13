# Public pilot F12-D01-D10

Date: 2026-08-13
Status: complete development batch; not a headline or holdout result

## Fixed basis

- Cases: ten WritingBench-derived marketing/public-copy tasks, F12-D01 through F12-D10
- Languages: five Chinese and five English
- Input commitment SHA-256: `b92fb0d391f8cbc98ade9664b2dd846dada49fc2bbdcb1a9f907ca163cc05cad`
- Evaluation: public WritingBench case criteria, common five-leaf rubric, frozen hard gates
- Runtime: current ChatGPT/Codex entitlement only; no paid API or paid reviewer
- Judges: three fresh anonymous contexts in the same available model environment
- Blind mapping SHA-256: `8d36adfa5357f9d1d2808c9d1d6c3e745ca8233c3f06a8c9ff7f1fb308c24300`

The raw case prompts are not published because some WritingBench rows contain
third-party material that still requires per-case redistribution review. Their fixed
upstream locator, revision, and hashes remain in the experiment corpus ledger.

## Results

Scores are uncapped weighted means on the preregistered 1-5 scale. `First share`
splits ties across the three anonymous rankings. This is one development family and
does not establish overall parity or superiority.

| Skill | Fixed revision | Mean | First share | Eligible cases | Unified hard rate |
| --- | --- | ---: | ---: | ---: | ---: |
| `human-writing` | `41bcc04908df1d085bda842b6df7d99ae79e8f3c` | **4.689** | **63.33%** | 9/10 | 10% |
| `humanizer` | `523374dee72d67c7b2b5f858ea0094ffda49c3ac` | 4.266 | 23.33% | 7/10 | 30% |
| `stop-slop` | `8da1f030185bdfe8471220585162991eaeb970e9` | 3.759 | 13.33% | 2/10 | 80% |
| `Humanizer-zh` | `91f3d394db8419c20d67ebe22a96cf8fee0a404b` | 3.558 | 0% | 1/10 | 90% |

All-case mean differences for `human-writing` were +0.423 over `humanizer`, +0.930
over `stop-slop`, and +1.131 over `Humanizer-zh`. Pairwise win/loss counts over only
gate-eligible pairs are not interpreted because comparator gate failures remove too
many pairs.

## Review decision

Decision: `no_change` for this batch.

The recurring comparator failure was unsupported invention: fabricated testimonials,
product specifications, operating results, and brand histories. `human-writing`
avoided that pattern. Its main weakness was F12-D09: all three judges found the answer
truthful and restrained but scored instruction/structure 2/5 because it returned only
a missing-evidence list instead of a usable product-page draft with clearly marked
placeholders. This is a plausible general defect, but it appeared once. It is carried
forward as a counterexample; the Skill changes only if a fresh batch reproduces the
same failure or exposes a safety-critical variant.

F12-D05 received one dissenting material-grounding flag for unsourced route and timing
details, while the other two judges scored it 5/5 and praised its uncertainty handling.
That disagreement is retained and is not converted into a rule change.

## Private evidence package

Detailed outputs, blind judgments, mappings, gate reports, and aggregates are stored
privately in Google Drive and are not linked from this public repository. Resolve the
package through the private AI Engineering Registry using asset ID
`human-writing-public-pilot-30-cases-20260813-v01`. Integrity anchors:

- aggregate SHA-256: `565da76a1d8a14b9b3fda30fb04f64758f570828a3f0a5a1ed7f3a01df303dea`
- aggregate file SHA-256: `783dc8cf5275ad0dfe185c514915f6ae232ac44582fc2d60d5ca64ab1534c9fb`
- input evidence SHA-256: `91217fea5a6e7c6b5bebaa54c6c1cf5780f4e4dc1d4b21f27a2a06069e21218f`

Limit: the three judges are isolated contexts, not independent model families,
providers, or human reviewers.
