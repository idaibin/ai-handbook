# Public pilot F08-D01-D10

Date: 2026-08-13
Status: complete development batch; not a headline or holdout result

## Fixed basis

- Cases: ten WritingBench-derived product and business-writing tasks, F08-D01 through F08-D10
- Languages: five Chinese and five English
- Input commitment SHA-256: `2a6866e5e6f2e679adb2dcd5213c0b5634103b13947445c3be29e3ee2c15d089`
- Evaluation: public WritingBench case criteria, common five-leaf rubric, frozen hard gates
- Runtime: current ChatGPT/Codex entitlement only; no paid API or paid reviewer
- Judges: three fresh anonymous contexts in the same available model environment
- Blind mapping SHA-256: `d0a3434706bdf73b21cbb38ba8dcf43c6d06f66d23cb00868ef5fb5d1e717e0f`

Raw prompts are withheld because some WritingBench rows contain third-party material
that still requires per-case redistribution review. Fixed upstream locators, revision,
and hashes remain in the corpus ledger.

## Results

Scores are uncapped weighted means on the preregistered 1-5 scale. `First share`
splits ties across three anonymous rankings. This is one development family and does
not establish overall parity or superiority.

| Skill | Fixed revision | Mean | First share | Eligible cases | Unified hard rate |
| --- | --- | ---: | ---: | ---: | ---: |
| `human-writing` | `41bcc04908df1d085bda842b6df7d99ae79e8f3c` | **4.491** | 28.33% | 7/10 | 30% |
| `humanizer` | `523374dee72d67c7b2b5f858ea0094ffda49c3ac` | 4.414 | 10.00% | 8/10 | 20% |
| `Humanizer-zh` | `91f3d394db8419c20d67ebe22a96cf8fee0a404b` | 4.299 | **40.00%** | 5/10 | 50% |
| `stop-slop` | `8da1f030185bdfe8471220585162991eaeb970e9` | 4.224 | 21.67% | 6/10 | 40% |

All-case mean differences for `human-writing` were +0.077 over `humanizer`, +0.192
over `Humanizer-zh`, and +0.267 over `stop-slop`.

## Review decision

Decision: `candidate` revision for forward testing.

`human-writing` failed three explicit length contracts. F08-D03 exceeded the roughly
2,500-character request by about one third; F08-D04 supplied less than half of the
3,000-5,000-word range and omitted requested real cases; F08-D08 supplied roughly
half of the requested 3,000 words. This repeated across three tasks and all judges,
so it met the preregistered recurrence threshold for a Skill change.

The candidate change requires a private section budget in the requested unit and a
final measured recount/revision pass. It also replaces bare refusal with the safest
useful partial artifact or a fill-ready template when evidence is incomplete, without
authorizing invention. The original batch score is immutable; the change is evaluated
only on a later unseen batch.

## Private evidence package

Detailed outputs, blind judgments, mappings, gate reports, and aggregates are stored
privately in Google Drive and are not linked from this public repository. Resolve the
package through the private AI Engineering Registry using asset ID
`human-writing-public-pilot-30-cases-20260813-v01`. Integrity anchors:

- aggregate SHA-256: `6795dc90631e54a10a826eae030f60578a6c5359af60bdfe91f834dcf1d71e9a`
- aggregate file SHA-256: `371ca48d78d2b5b7bb771d17255ae2f39cd1a75278baa6b878e064998c8ffb02`
- input evidence SHA-256: `c27268292ea344262c94792ea90a6aab8c2fb05de3b6bcb71eac4b888104d246`

Limit: the three judges are isolated contexts, not independent model families,
providers, or human reviewers.
