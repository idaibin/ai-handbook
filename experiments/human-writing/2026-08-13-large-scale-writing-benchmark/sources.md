# Corpus sources and redistribution policy

Date basis: 2026-08-13  
Scope: source selection for 12 families x 100 cases  
Current materialization: local candidate smoke test (5 families x 10 cases)

## Decision

WritingBench is the only source materialized in the first wave. Its fixed 1,000-row
snapshot has candidate bilingual breadth for five families, but not for
source-grounded rewriting, summaries, delegated task briefs, or incident records. It is not
treated as sufficient evidence for all 1,200 cases. Later waves must add the locked
source-grounded corpora below, especially for summaries, task delegation, tutorials,
and incident writing.

Every source is pinned by an immutable revision or a dated release contract. A source
without a downloaded content hash remains `locked_not_materialized`; it cannot produce
a case until its bytes and fields pass the builder's validation. Licenses are recorded
per source, not inferred from a hosting platform.

## Included sources

| Source ID | Fixed version | Rows / fields used | License | Redistribution | Intended use | Current state |
| --- | --- | --- | --- | --- | --- | --- |
| `writingbench` | commit `ae2d5176449b7b769815482641d35926f26793eb`, blob `2d04c2d4c82f8c2d615e963393c7808f64b97129` | 1,000; `index`, `domain1`, `domain2`, `lang`, `query`, `checklist` | Apache-2.0 | review required before publishing embedded material | bilingual broad writing prompts and per-case criteria | 50 candidate cases materialized locally |
| `govreport` | Hugging Face revision `4e21184e01ae8017e2c036e180fe5e541fef60a0`; dataset release 1.0 | 17,517 train / 973 validation / 973 test; `id`, `report`, `summary` | CC BY 4.0 | allowed with attribution | long source-grounded summaries and rewrites | 200-row test slice downloaded, hashed, selector implemented |
| `dolly_15k` | revision `bdd27f4d94b9c1f951818a7da7fd7aeea5dbff1a`, dataset version 1.0 | 15,011; `instruction`, `context`, `response`, `category` | CC BY-SA 3.0 | allowed with attribution and ShareAlike | human-authored instructions, handoffs, collaboration briefs | full JSONL downloaded, hashed, selector implemented |
| `github_docs` | commit `729fe5d6b03b2c9a01e91a8d203b4b4c349d300b` | Markdown front matter, path, title, body | CC BY 4.0 for `assets`, `content`, `data`; MIT for code | source-specific review required | product and technical documentation, tutorial adaptation | archive downloaded and hashed; reader removes fenced code only |
| `mdn_content` | commit `8a10694edf44bde124fa8f18af65651855f632dc` | Markdown front matter, path, title, body | CC BY-SA 2.5+ for prose; CC0/MIT rules for code examples | source-specific review required | technical explanations and tutorials | archive downloaded and hashed; reader removes fenced code only |
| `ntsb_aviation` | official `avall.zip` snapshot dated 2026-07-01 | event ID, narrative, probable cause, findings and coded event fields | US federal public domain for NTSB-authored material | allowed; exclude identified third-party text | incident and operational writing | locator locked, bytes pending |
| `ifeval` | Hugging Face revision `966cd89545d6b6acfd7638bc708b98261ca58e84` | 541; `key`, `prompt`, `instruction_id_list`, `kwargs` | Apache-2.0 | allowed with notice | deterministic constraint overlays and format gates | locked, bytes pending |
| `natural_instructions` | release tag `v2.8`, commit `e0fd31052b21acea5bd95fb00253e1ee1f5d8259` | 1,616 task definitions; definition and instance input/output fields | Apache-2.0 | allowed with notice, subject to task-source metadata | task-spec diversity and instruction structure | locked, bytes pending |
| `govuk_content` | Content API snapshot contract, retrieval date 2026-08-13 | `content_id`, `document_type`, `public_updated_at`, `title`, `details/body` | Open Government Licence v3.0 unless a page says otherwise | allowed with attribution; exclude third-party and personal data | public notices, short-form adaptation, source-grounded rewrite | locked, per-item revision/hash pending |
| `openai_cookbook` | commit `4a85c3018d20ceef48bf7549450c567896501bf9` | MDX/notebook path, title/metadata, prose cells | MIT; third-party inclusions require separate review | allowed with notice after per-file review | AI explanations and tutorials | locked, bytes pending |

Source counts are evidence about the available pools, not a claim that every item is
suitable. `families.yaml` fixes the target allocation and the implemented WritingBench
filter. Other sources remain plan slots until a source-specific deterministic selector
and candidate-pool byte hash are implemented; the builder records that status explicitly.

## Explicit exclusions

| Excluded source | Reason |
| --- | --- |
| AESLC / raw Enron email text | The public dataset card reports `license: unknown`; messages also contain personal and confidential-looking material. Real email text must not be copied into this experiment. Collaboration cases use openly licensed factual briefs instead. |
| X / Twitter post text | Tweet datasets commonly redistribute IDs rather than text, and deletion/access state is unstable. The benchmark may request an X-style output, but it does not persist scraped post text. |
| WritingPreferenceBench responses | The dataset card metadata says Apache-2.0 while its body says ODC-BY and also describes research/educational use. Until the conflict is resolved, neither chosen nor rejected responses are copied or transformed here. |
| Unlicensed blogs, vendor postmortems, and public GitHub issues | Public visibility is not a redistribution license. They may be discovery leads only. |

## Case materialization rules

1. Fetch only the exact revision in `locks/sources.yaml`.
2. Verify the file/blob hash when one is available. If bytes are not present, emit a
   pending plan slot rather than a placeholder case or commitment.
3. Normalize Unicode and whitespace only for hashing and duplicate detection. Preserve
   the original prompt bytes in materialized development cases.
4. Keep source attribution in each case's `provenance`. CC BY-SA adaptations must retain
   the applicable ShareAlike notice when published.
5. Never select an upstream record twice across families or splits.
6. Reject exact normalized duplicates. Reject near duplicates above the threshold in
   the builder; do not silently keep the first matching holdout variant.
7. Holdout plan slots contain no prompt or upstream row index. Holdout prompts are not
   materialized until the final Skill revision is frozen.

## Apache notice and embedded-material review

WritingBench must be attributed as `X-PLUG/WritingBench`, commit
`ae2d5176449b7b769815482641d35926f26793eb`, under Apache License 2.0, with a copy or
link to its `LICENSE`. The fixed repository has no root `NOTICE` file. This attribution
does not erase upstream rights: several prompts include paper excerpts, templates,
financial material, lyrics, or other quoted sources. Before any case prompt is pushed
to a public branch, record whether the embedded passage is openly licensed, public
domain, short enough for a defensible quotation, or must remain locator-only. Until
that review completes, `review_required` is the controlling redistribution status.

## Current gap

The local smoke test is a real, runnable 50-case WritingBench candidate pool, not the completed
1,200-case corpus. F02, F03, F05, F06, F07, F09 and F11 were removed rather than filled
with construct-invalid prompts. Acquired sources still require source-to-case
construction, bilingual construct review, license notice generation and deterministic
selection before their planned slots can be emitted. Sources not listed in the
acquisition checkpoint remain byte-level pending.

## 2026-08-13 acquisition checkpoint

Byte acquisition is no longer the main blocker. Exact artifacts were downloaded and
hash-locked for WritingBench, a 200-row GovReport test slice, Dolly 15K, IFEval,
GitHub Docs, MDN Content, Natural Instructions, OpenAI Cookbook, and the three current
NHTSA SGO incident CSV files. `corpus/acquisition-report.json` records byte sizes and
hashes; raw archives remain gitignored cache inputs.

`corpus/source_selectors.py` now implements hash-checked readers for WritingBench,
GovReport, Dolly, GitHub Docs, MDN and NHTSA. It removes fenced Markdown code, never
exposes reference responses, selects latest NHTSA report versions, and rejects
CBI-marked NHTSA narratives. It is not a full Markdown parser: inline code and indented
code can remain in GitHub Docs and MDN excerpts. Those two sources therefore stay
blocked on source-specific prose/code license review before any case is materialized.

This does **not** change the corpus completion count: 50 schema-valid smoke cases are
still materialized. The missing work is now source-to-case construction, bilingual
construct review, deterministic family allocation, and sealed holdout creation—not
download availability. Natural Instructions and OpenAI Cookbook remain downloaded but
unselected pending item-level provenance review. NHTSA reporting-entity narratives
remain `locator_only` because publication by a federal agency does not make private
submissions federal public-domain works.
