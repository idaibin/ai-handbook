# GitHub Skills Catalog Deep Analysis — 2026-08-07-batch-002

- Observed: `2026-08-07T02:01:49+08:00`
- Completed: `10` repositories, `13` individual skills.
- Completion gate: verified GitHub identity and displayed stars; read README/equivalent, actual `SKILL.md` or equivalent, and available scripts/references/eval assets.
- Validation status: `structure-reviewed`; runtime tests/evals were `not_executed`.
- Stars are GitHub page display values observed on 2026-08-07 and can change.

## Batch summary

| Repository | ID | Branch | Stars | Skills |
| --- | ---: | --- | ---: | ---: |
| `chuspeeism/dashi-ppt-skill` | `1264811161` | `main` | `4.8k` | 1 |
| `Cuimao777/eterna-image2image-skill` | `1281081043` | `main` | `171` | 1 |
| `dgreenheck/webgpu-claude-skill` | `1140251276` | `main` | `1.1k` | 1 |
| `ferdinandobons/startup-skill` | `1174682625` | `main` | `576` | 4 |
| `Frankieli123/grok-skill` | `1132683863` | `master` | `179` | 1 |
| `freestylefly/author-methodology-analysis-skill` | `1270344186` | `main` | `15` | 1 |
| `guangyuspace/codex-gamestudio-skill` | `1268530871` | `main` | `43` | 1 |
| `jdubois/dr-jskill` | `1157075149` | `main` | `320` | 1 |
| `Kappaemme-git/codex-first-customer-finder-skill` | `1298346646` | `main` | `953` | 1 |
| `KyrieCheungYep/ky-design-to-html-skill` | `1256980488` | `main` | `155` | 1 |

## Repository reports

### 1. `chuspeeism/dashi-ppt-skill`

- **Read:** `README.md`, `skills/dashi-ppt/SKILL.md`, `scripts/render_goal_deck.sh` (`51b42f14e3ef9de8cb1d21b04453696ec6d386a4`).
- **Structure/workflow:** A large one-skill presentation system with theme/layout libraries, generators, validators, browser editor, and HTML/PDF/PPTX export. It converts the brief into a JSON plan, confirms theme/media, scaffolds deterministic layouts, applies content/layout contracts, renders, validates, previews, and checks the installed version.
- **Finding:** Separating semantic planning from deterministic artifact generation is the strongest reusable design. The renderer uses strict shell handling and chained validators.
- **Limits:** Large dependency/asset surface, browser and network requirements, substantial runtime/token cost, AGPL plus proprietary-subcomponent boundaries. No deck was generated or exported.
- **Skill:** `dashi-ppt`.

### 2. `Cuimao777/eterna-image2image-skill`

- **Read:** `README.md` (`6fa395...`), `skill/eterna-image2image/SKILL.md` (`fbac388...`), `references/lut-workflow.md` (`1e63935...`).
- **Structure/workflow:** Compact bilingual skill with three references and example images. It preserves identity, composition, perspective, and motivated lighting before applying one of three restrained cinematic modes.
- **Finding:** Strong provenance language distinguishes inspired, reference-grade, and color-managed results; negative constraints and preservation defaults reduce uncontrolled rewrites.
- **Limits:** Examples are explicitly not benchmarks; color-check scripts are only roadmap items; quality remains subjective and model-dependent. No image was generated.
- **Skill:** `eterna-image2image`.

### 3. `dgreenheck/webgpu-claude-skill`

- **Read:** `README.md` (`9aed0ea...`), `skills/webgpu-threejs-tsl/SKILL.md` (`3115563...`), `docs/device-loss.md` (`bf4a5ce...`).
- **Structure/workflow:** One source-of-truth skill with focused docs, examples, templates, and thin Cursor `@file` shims. It covers renderer setup, TSL nodes/materials, compute, post-processing, WGSL, limits, and device-loss recovery.
- **Finding:** Progressive disclosure and cross-tool shims are highly reusable. Device-loss guidance includes preservation, recovery, and deliberate fault-injection patterns.
- **Limits:** README says aligned with r183+ but later recommends r171+, creating version ambiguity. No example was built or run.
- **Skill:** `webgpu-threejs-tsl`.

### 4. `ferdinandobons/startup-skill`

- **Read:** README plus all four `SKILL.md` files; `startup-competitors` (`d5a0903...`), `startup-positioning` (`1aa046e...`), `startup-pitch` (`cedd5a6...`), and `verification-agent.md` (`d58da12...`).
- **Structure/workflow:** Four independently triggerable skills: eight-phase startup design, competitive intelligence, positioning, and pitching. Supports fast-track/resume modes, bounded research waves, progress files, verification, and go/no-go gates.
- **Finding:** Good decomposition by user intent and strong review rules for unlabeled claims, contradictions, stale/duplicate sources, confidence, and cross-phase consistency.
- **Limits:** Browsing/context intensive; framework use is not empirical validation of a startup. No market research or eval scenario was run.
- **Skills:** `startup-design`, `startup-competitors`, `startup-positioning`, `startup-pitch`.

### 5. `Frankieli123/grok-skill`

- **Read:** `README.md` (`69c9286...`), `SKILL.md` (`38b2296...`), `scripts/grok_search.py` (`ee5d356...`).
- **Structure/workflow:** Single search skill with configuration and PowerShell helpers. The Python standard-library client loads layered config, rejects placeholders, calls `/v1/chat/completions`, parses JSON or SSE-like output, and returns content plus sources.
- **Finding:** Small implementation surface and a useful machine-readable search contract.
- **Limits:** Search behavior is endpoint/model-specific; structured extraction is best effort; aggressive triggering can add latency/cost. Script was not executed and no tests were inspected.
- **Skill:** `grok-search`.

### 6. `freestylefly/author-methodology-analysis-skill`

- **Read:** `README.md` (`75f8d3a...`), `SKILL.md`, `scripts/analyze_corpus.py` (`0521885...`), schema/templates and declared dashboard/validator pipeline.
- **Structure/workflow:** Corpus analysis for Markdown/TXT/DOCX/text PDFs. Deterministic scripts create features, fingerprints, dedupe and sensitivity signals; interpretation must cite evidence/rules/confidence; reports, JSON, CSV, dashboard, and sync metadata share one data source.
- **Finding:** Strong separation between computed facts and model interpretation, with sample-size gates below five and three items.
- **Limits:** Image-only PDFs need OCR, subjective labels still require judgment, and sync expands permissions. No corpus or validator was run.
- **Skill:** `author-methodology-analysis`.

### 7. `guangyuspace/codex-gamestudio-skill`

- **Read:** `README.md` (`6a872d6...`), `SKILL.md` (`266b104...`), `references/ui-ux-audit.md` (`ec92612...`).
- **Structure/workflow:** Reference-heavy single skill covering roles, phases, Godot, assets, mobile UI, QA, and handoffs. It explicitly uses role perspectives rather than background agents, applies minimal changes, updates `CODEX_HANDOFF.md`, and creates `DEBUG_HANDOFF.md` after repeated failed fixes.
- **Finding:** The repeated-error stop rule and mobile readability/touch-target audit are practical controls.
- **Limits:** Many gates are qualitative; store/retention scores are heuristics. No game project or test was run.
- **Skill:** `gamestudio`.

### 8. `jdubois/dr-jskill`

- **Read:** `README.md` (`60a9437...`), `SKILL.md`, `scripts/create-project-latest.mjs` (`21c6af5...`), `versions.json`, references/workshop/test structure.
- **Structure/workflow:** Large Spring Boot generation skill using central version authority and cross-platform Node scripts. It resolves a Boot version, downloads from start.spring.io, applies project files, supports multiple front ends/security/deployment paths, protects `.env`, and documents Maven/front-end validation.
- **Finding:** Centralized versions plus deterministic scaffolding is a strong pattern for large engineering skills.
- **Limits:** Opinionated and ecosystem-heavy; depends on live services/current compatibility; repository calls itself experimental. No project was generated or built.
- **Skill:** `dr-jskill`.

### 9. `Kappaemme-git/codex-first-customer-finder-skill`

- **Read:** `README.md` (`6080256...`), `SKILL.md` (`451922e...`), `research-framework.md` (`5846202...`), `generate_report.py`.
- **Structure/workflow:** Defines ICP/disqualifiers, searches public pain/timing signals, keeps an evidence ledger, scores and deduplicates candidates, drafts source-grounded openers, and renders a standalone HTML report. Outreach stays manual and private enrichment is excluded.
- **Finding:** Primary candidates require original-source evidence and dates. Scoring weights pain/fit/timing/reachability/evidence, while the renderer escapes content and restricts links to HTTP(S).
- **Limits:** Weights are heuristic and public signals do not prove purchase intent. No live research or script run occurred.
- **Skill:** `first-customer-finder`.

### 10. `KyrieCheungYep/ky-design-to-html-skill`

- **Read:** `README.md` (`1871402...`), `SKILL.md` (`b548bb1...`), `visual-error-taxonomy.md` (`77e368e...`), `screenshot_page.py` (`27eabe7...`).
- **Structure/workflow:** Compact skill that maps the page, separates code structure from assets, distinguishes reference canvas from display viewport, implements, captures a real browser screenshot, classifies errors, and iterates. Includes fixed-aspect and three-layer scaling patterns.
- **Finding:** Treating recreation as an error-reduction loop, with low-permission defaults and explicit missing-asset reporting, is directly reusable.
- **Limits:** No automated image-diff threshold; fidelity depends on assets/browser tooling. The Playwright helper was read but not executed.
- **Skill:** `ky-design-to-html`.

## Individual skill reports

| Skill | Purpose / execution contract | Key assessment |
| --- | --- | --- |
| `dashi-ppt` | Plan JSON → choose theme/media → scaffold deterministic deck → validate/render/export. | Strong content/layout separation; heavy runtime and licensing surface. |
| `eterna-image2image` | Preserve scene/identity → select cinematic mode → apply color/composition constraints → manual review. | Good provenance and preservation rules; no reproducible eval. |
| `webgpu-threejs-tsl` | Route to focused WebGPU/TSL docs, examples, templates, limits and recovery. | Excellent progressive disclosure; version guidance conflicts. |
| `startup-design` | Preflight → discovery gate → research waves → eight phases → verification → go/no-go. | Resumable evidence workflow; context intensive. |
| `startup-competitors` | Collect original sources in waves → compare pricing/features/GTM → battle cards. | Collection separated from synthesis; freshness dependent. |
| `startup-positioning` | Map alternatives/capabilities/value/segment/category → messaging implications. | Explicit intermediate artifacts; framework fit is not PMF proof. |
| `startup-pitch` | Research audience → evidence narrative → multiple pitch lengths → score/Q&A. | One evidence base, multiple renderings; real investor response unverified. |
| `grok-search` | Load config → call compatible endpoint → parse JSON/SSE → return content/sources. | Useful machine contract; endpoint-specific and best-effort. |
| `author-methodology-analysis` | Validate corpus → deterministic features → evidenced interpretation → artifacts/validation. | Computed facts remain authoritative; subjective labels remain. |
| `gamestudio` | Select relevant roles → smallest change → verify/handoff → stop blind repeated fixes. | Strong continuity and debugging gate; roles are not actual agents. |
| `dr-jskill` | Resolve versions → scaffold Spring Boot → apply options → run documented verification. | Central version authority; large live ecosystem dependency. |
| `first-customer-finder` | Define ICP → gather dated public signals → score/dedupe → manual opener/report. | Good evidence/privacy boundary; intent remains a hypothesis. |
| `ky-design-to-html` | Page map → asset split → canvas fit → implementation → screenshot → correction loop. | Strong visual verification discipline; no automated diff threshold. |

All individual skill reports have runtime status `not_executed`; none were marked complete from metadata alone.

## Cross-repository findings

1. Deterministic scripts and structured artifacts improve trust when paired with model interpretation.
2. Progressive disclosure through references is the dominant scalable layout.
3. Explicit stop/verification gates are more useful than adding more simulated roles.
4. Reproducible task fixtures with pass/fail skill evals remain uncommon in this batch.
5. Side-effect boundaries should be standardized: manual outreach, secret protection, installation consent, and network disclosure.

## Progress

- Latest index snapshot: `850` unique, `543` provisionally eligible, `307` held.
- Cumulative completion: `20` repositories and `24` skills.
- Estimated eligible remaining: `523` (`543 - 20`); this changes as indexing/reclassification continues.
- Excluded from this batch: `aiskilloftheweek/claude-ai-skill-of-the-week` (no actual skill definition located) and `alibaba-flyai/flyai-skill` (attempted root `SKILL.md` did not resolve).

## Verification boundary

Every completed repository had identity and stars verified and actual repository content read. No third-party script, test, eval, dependency installation, external model API, generated image/deck/application, browser comparison, or live prospect research was executed. Status is `structure-reviewed`, not `runtime-verified`.
