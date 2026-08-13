# Public pilot F04-D01-D10

Date: 2026-08-13
Status: complete forward-development batch; not a headline or holdout result

## Fixed basis

- Cases: ten WritingBench-derived general, review, and blog-writing tasks, F04-D01 through F04-D10
- Languages: five Chinese and five English
- Input commitment SHA-256: `bb7a8ae06c3c1c81eb550880eb7bcc9baa4e3a0d09d4f0a6e1c8a2d1efb77468`
- Evaluation: public WritingBench case criteria, common five-leaf rubric, and frozen hard gates
- Runtime: current ChatGPT/Codex entitlement only; no paid API or paid reviewer
- Judges: three fresh anonymous contexts in the same available model environment
- Blind mapping SHA-256: `d11389fe163343b12e98ba6daf3f92c5e80dfee8a7becd3b848eaba66fe33e7c`

Raw prompts are withheld because some WritingBench rows contain third-party material
requiring per-case redistribution review. Fixed upstream locators, revision, and
hashes remain in the corpus ledger.

## Results

| Skill | Fixed revision | Mean | First share | Eligible cases | Unified hard rate |
| --- | --- | ---: | ---: | ---: | ---: |
| `human-writing` candidate | `2448a0f20626438d3765a986d2878b49fec4d340` | **4.553** | **60.00%** | **9/10** | 70% |
| `humanizer` | `523374dee72d67c7b2b5f858ea0094ffda49c3ac` | 3.965 | 6.67% | 4/10 | 80% |
| `Humanizer-zh` | `91f3d394db8419c20d67ebe22a96cf8fee0a404b` | 3.930 | 20.00% | 3/10 | 80% |
| `stop-slop` | `8da1f030185bdfe8471220585162991eaeb970e9` | 3.903 | 13.33% | 3/10 | 80% |

All-case mean differences for the candidate were +0.588 over `humanizer`, +0.623
over `Humanizer-zh`, and +0.650 over `stop-slop`. The high unified-hard rates include
non-material instruction findings from any one judge; only material findings block
preference eligibility.

## Forward-test decision

Decision: `accepted`.

The unseen explicit-range task F04-D06 required 2,000-2,500 English words. The
candidate produced 2,100 measured words and received a 4.96/5 median weighted score
for the explicit-length slice. It remained the highest-scoring Skill overall and had
9/10 materially eligible cases, so the length-contract change showed the intended
behavior without a batch-level regression.

The review also preserved an unresolved tension: six candidate answers used visible
placeholders or omitted requested personal experience/citations when the prompt did
not provide the evidence. Judges often marked those as non-material instruction
shortfalls. No rule was added because converting placeholders into plausible facts
would violate the higher-priority grounding contract.

## Integrity anchors

- aggregate SHA-256: `fb05fc6833f1c62339d45f05fca5083fd3833885f72faceb28ca02bc94e3e36a`
- aggregate file SHA-256: `cbeccc7eaa775c0a66e6e4d15bb5a54241ba27fffcd670230858229621c4fc24`
- input evidence SHA-256: `9456114f9e91254cf34a582d4cb9eaa0283f63547b54c0cbab6c3bce16e33d35`

## Private evidence package

Detailed outputs, blind judgments, mappings, gate reports, and aggregates are stored
privately in Google Drive and are not linked from this public repository. Resolve the
package through the private AI Engineering Registry using asset ID
`human-writing-public-pilot-30-cases-20260813-v01`.

Limit: all judges are isolated contexts in one available model environment, not
independent providers, model families, or human reviewers.
