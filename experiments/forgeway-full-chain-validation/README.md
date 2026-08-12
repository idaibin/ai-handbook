# Forgeway full-chain cloud validation — 2026-08-13

This is an execution ledger, not a source-review memo and not a production receipt.
It records real community-project scans, one red-green feature slice, browser runtime
evidence, Delivery Graph projection, package-install consumption, and honest runtime
stops. A contract test is never substituted for a behavior result in this ledger.

## Fixed basis

| Subject | Fixed basis |
| --- | --- |
| AI Engineering System | `fb101496f52bbc1a403f825c8825622c080b3a42` |
| Forgeway input | `09bf602bc1ed7a37f313f29c70af7cb9ee66267e` plus the candidate changes described below |
| Skills input | `495892c335886d750dd62af989e1cab20c47ff3a` plus the candidate changes described below |
| Epic Stack canary | `da819d69af1bb66b19cfee35ad81aa8502d0be05` |
| Spring Petclinic canary | `88e37c15cf6fc8490b01bc3e8e2c800cec1ac272` |
| ripgrep canary | `3fce3b5bb0236da2df6d99672afb8a719642eca7` |
| Domain Driven Hexagon canary | `5c2d15a7e2d69e83dfddf28468ee9f30e02c30de` |
| Host | Linux cloud workspace; Node.js 24; OpenJDK 17; no Docker, Cargo/Rust toolchain, desktop-client control, or named external-model CLI |

## Outcome

The candidate is **locally verified through reviewed** for one bounded community
frontend slice. A separate Forgeway validation probe was delivered and deployed to a
real production host with terminal host readback; it remains production-not-verified
because no post-deploy application probe was executed against that live URL. Forgeway's
own deterministic suite and the Skills suite pass. The community canary proves a real
workflow and real browser behavior; it does not prove universal cross-project or
production behavior.

The cloud run found nine reproducible defects and fixed them before rerunning the
affected path:

1. duplicate Graph issue IDs could crash a large scan;
2. scan-local metadata made semantic diff report every unchanged asset as changed;
3. arbitrary TypeScript classes/interfaces were misclassified as domain entities;
4. a deleted tracked regular file was mislabeled as a symlink;
5. React Router `app/routes/**` modules were not recognized as pages/routes;
6. the DESIGN contract test could parse trailing npm output as a false green;
7. `ui-spec` forced first-time `DESIGN.md` adoption for a local semantics-preserving change;
8. one generic command Observation could satisfy both implemented and locally-verified;
9. `.java` was inventory-only, so Spring endpoints and JPA entities were not queryable.

The ninth fix adds bounded `regex-java/1` extraction. On Spring Petclinic it changed
Java files from inventory-only to parsed and returned 17 Spring endpoints and eight
domain entities with zero active Graph issues. Reflection, generated registrations,
and runtime-only calls remain explicit coverage gaps.

## Real product-to-review canary

The Epic Stack home page contained 21 technology-logo links whose nested images were
decorative and whose links therefore had no accessible name. The executed workflow was:

| Stage | Real input | Real output and result |
| --- | --- | --- |
| Map/discovery | clean Epic Stack checkout plus Graph scan | 370 files covered; React Router marketing index resolved as page and route `/`; tracked and untracked coverage distinguished |
| Product | current logo model, route source, and accessible-name defect | bounded requirement: every technology link exposes the model's existing `alt` text as its accessible name; no new product behavior |
| UI | accepted current surface at 1280x720 | local Feature Spec; `DESIGN.md: Not adopted (not required for this slice)`; no visual-semantic or token change |
| Architecture | existing `logos` model and route composition | KISS/YAGNI decision: reuse `logo.alt`; no registry, helper, component, state, or schema added |
| Task/TDD | public link role/name/href seam | focused Testing Library test observed red for all 21 unnamed links before implementation |
| Development | two-file task scope | added `aria-label={logo.alt}` and the focused regression test; same test then passed |
| Validation | target commands and isolated focused command | typecheck passed after Prisma client generation; lint passed with three pre-existing import-order warnings; build passed; `git diff --check` passed; focused test passed |
| Browser/a11y | built application served locally; real headless Chromium | all 21 role/name/href queries passed at 1280x720; axe-core scoped to the technology grid reported zero violations and `link-name` passed |
| Review | exact two-file Worktree basis | Standards pass; Spec pass; zero in-scope findings |

The repository's original full Vitest command did **not** pass: its global setup failed
during Prisma reset before the focused test ran. The focused config removed only that
unrelated database setup and is evidence for this UI slice, not a replacement claim
for the full suite. Whole-page axe also found a separate pre-existing unnamed brand
link. It was reported as out of task scope rather than hidden or counted against the
two-file result.

## Delivery Graph execution

A real PackageManifest was created from the clean input and another from the candidate
Worktree. Ignored run-local evidence files did not enter the result package; only the
route source and its new test changed. The run used:

- Run `run:epic-accessible-technology-links`;
- Attempt `attempt:epic-accessible-technology-links-1`, attempt number 1, succeeded;
- six typed Observations for discovery, specification, implementation, focused test,
  Chromium runtime, and fixed-basis review;
- explicit not-verified Delivery and Deployment receipts with no invented host
  authorization or target readback;
- 15 append-only events;
- policy-derived GateProjection, never caller-authored status.

| Gate | Projection | Evidence boundary |
| --- | --- | --- |
| discovered | satisfied | source query Observation |
| specified | satisfied | product/UI/architecture/task bundle Observation |
| implemented | satisfied | exact result package plus `gate:implemented` claim |
| locally-verified | satisfied | focused test plus target-like Chromium Observation; separate claim refs required |
| reviewed | satisfied | fixed two-file basis and zero in-scope findings |
| delivered | not-verified | no authorized delivery receipt/readback |
| deployed | not-verified | no authorized host deployment receipt/readback |
| production-verified | not-verified | no production probe/readback |

The `claim_refs` policy addition is deliberately selective, not authorizing: a policy
can require an implementation claim, a local-test claim, and a browser-runtime claim,
but each Observation still has to pass its own trust, actor, package, outcome, and
staleness checks.

### Real host delivery canary

A separate one-route Forgeway validation probe was built, previewed, committed and
pushed by the hosting lifecycle, then published as an immutable production version.
The host's direct terminal readback returned `succeeded` and the literal URL
<https://forgeway-validation-probe.dh2qqfpgxy.chatgpt.site>. Its independent Delivery
Graph run used package `pkg:bc4922ce6cb6b616ed3f2107a6f1fc2079f45224837cf452f5a9a30804256672`,
one succeeded Attempt, a confirmed Git delivery receipt bound to source commit
`92551b3dac470bee26e108ab736ec9eb35dcec3f`, a confirmed production deployment
receipt bound to the exact host deployment identity, and eight append-only events.
The policy projection was `delivered=satisfied`, `deployed=satisfied`, and
`production-verified=not-verified`.

This is intentionally a different Run from the Epic feature slice. A deployment of
the probe cannot upgrade the Epic package's delivery or deployment gates, and a host
status readback cannot substitute for a post-deploy application/UX probe.

## Skill behavior matrix

“Stop pass” means the Skill returned or was expected to return its declared recoverable
state before unauthorized or unevidenced action. It is not an implementation pass.

| Skill | Actual behavior exercise | Result |
| --- | --- | --- |
| `repo-map` | scanned Epic Stack, Domain Driven Hexagon, Spring Petclinic, and ripgrep; queried routes/endpoints/entities; exercised rename, tombstone, history, dirty/untracked, export/import, and diff | Pass |
| `product-spec` | bounded the Epic accessible-name requirement and non-goals from current source | Pass |
| `ui-spec` | produced a local UI slice from an accepted surface without inventing shared design authority | Pass after fix |
| `domain-modeling` | resolved the sample's User/Wallet terms, aggregate/invariant language, domain-vs-integration event distinction, and boundary ownership from the fixed DDD repository | Pass; no source artifact write |
| `dev-frontend` | observed red, implemented the minimal vertical slice, then observed green and browser behavior | Pass |
| `audit-frontend` | read-only accessibility/runtime audit on the selected grid; separated the unrelated whole-page defect | Pass |
| `dev-java` | resolved Petclinic's Maven/Gradle roots, JDK 17, Spring parent, source/tests, and attempted the repository Wrapper without editing | Stop pass: dependencies could not resolve because Maven Central was unreachable; Baseline not verified |
| `audit-java` | read-only build/architecture and API/persistence evidence on Petclinic; Graph returned 17 endpoints and eight entities | Partial: source audit executed; build/runtime profiles not verified |
| `dev-rust` | resolved ripgrep workspace, edition 2024, MSRV declarations, members, CI commands, features, and target matrix before edit | Stop pass: Cargo is unavailable; no source edit; Baseline not verified |
| `audit-rust` | read-only architecture/baseline inventory on the fixed ripgrep snapshot | Partial: source profile executed; Cargo/runtime evidence not verified |
| `repo-review` | fixed-basis Standards/Spec review of the Epic two-file result | Pass |
| `repo-delivery` | delivered the probe's exact source commit through the hosting Git lifecycle and bound a confirmed receipt to its package/ref readback | Pass for probe; Forgeway/Skills/handbook GitHub delivery still pending |
| `ops-browser` | real Chromium role/name/href and scoped axe operation | Pass for headless page operation; desktop session/group and two-pass visual closure not verified |
| `ops-client` | host capability inventory found no real desktop-client controller/target | Stop pass: `CAPABILITY_MISSING`; no simulated client receipt |
| `ask-ai` | provider inventory found no named external model CLI/key/verified provider route for a live benchmark campaign | Stop pass: provider unavailable; no fabricated external verdict |
| `human-writing` | converted raw run facts into this source-grounded evidence ledger while preserving gaps and attribution | Pass |

Repository package validation also passed for all 16 Skill packages, exact routing
passed 51/51 with zero contract errors/regressions, and 228 deterministic tests passed.
Six existing entrypoint context-budget warnings remain non-blocking; they are not
silently upgraded to passes or treated as behavior failures.

## Installed consumption

The candidate Forgeway package was packed, installed into a fresh temporary npm
project, and executed from the installed binary. `forgeway version` returned
`forgeway-cli/1` and `repo-graph/1`. The installed binary loaded the real Skills v3
registry and exact lookup of `repository.asset.query` version `1.0.0` returned one
capability owned by `repo-map`, with `static_manifest_authorizes=false`.

## Community and benchmark alignment

The validation design follows primary projects instead of inventing one synthetic
score:

- [SWE-bench](https://github.com/swe-bench/SWE-bench) supplies real issue/patch tasks
  and a Docker evaluator; SWE-bench Verified is the appropriate later coding-agent
  generalization gate, but Docker and the required image budget were unavailable here.
- [SWE-Skills-Bench](https://github.com/GeniusHTX/SWE-Skills-Bench) supplies paired
  skill/no-skill tasks; its provider and Docker requirements were unavailable, so no
  benchmark score is claimed.
- [BrowserGym](https://github.com/ServiceNow/BrowserGym) and
  [WebArena](https://github.com/web-arena-x/webarena) inform browser-task evaluation;
  this run used a smaller deterministic Chromium/axe canary because the benchmark
  sites and containers were not available.
- [Agent Skills](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)
  informs portable Skill packaging, while provider/model/CLI attribution stays
  runtime-only.
- [GitHub Spec Kit](https://github.com/github/spec-kit) supports executable
  spec-to-plan-to-task discipline; Forgeway keeps those human decisions distinct from
  machine evidence and receipts.

No SWE-bench, SWE-Skills-Bench, BrowserGym, or WebArena score is inferred from the
community canaries.

## Human and machine information model

No single file format should own every concern.

| Concern | Durable authority | Why |
| --- | --- | --- |
| project overview, product intent, feature behavior, ADRs, UI slices | concise Markdown with stable links and IDs | fastest human onboarding, review, and Git history |
| shared UI semantics | repository-native owner; `DESIGN.md` only after explicit adoption and independent approval | avoids duplicate token/component authority |
| API/interface contract | OpenAPI/JSON Schema/Proto when the project has a real producer, validator, and consumer | both humans and machines can validate the interface; [OpenAPI](https://github.com/OAI/OpenAPI-Specification) explicitly supports machine and human discovery |
| repository assets/relations/coverage | SQLite current machine store plus immutable JSONL snapshots | queryable, diffable, history-isolated, and importable |
| delivery history and status | append-only JSON events plus policy-derived projection | traceable and prevents executor-authored completion |
| architecture decisions | Markdown ADRs; see the maintained [ADR examples](https://github.com/joelparkerhenderson/architecture-decision-record) | decision context and consequences stay reviewable |
| architecture topology | derived Mermaid for small reviewed relationships or [Structurizr DSL](https://github.com/structurizr/dsl) when C4-as-code has a real owner | diagrams remain reproducible views, not a parallel source of truth |
| service/catalog navigation | existing catalog owner such as [Backstage](https://github.com/backstage/backstage) when already adopted | Forgeway should link/query it, not create a competing catalog |
| Draw.io | only when an existing human owner requires editable freeform diagrams | binary/XML drawing is not a machine gate or repository authority by default |

The minimal AI path is: query the Graph for task scope and authorities; read only the
relevant human contracts and live source; resolve a capability through the host's
global Skill/capability mechanism; execute the smallest behavior slice; attach typed
Observations to the exact result package; let policy calculate Gates; render Markdown
or diagrams only as derived navigation. Forgeway does not import remembered Skill
packages or bind provider/model/CLI identity into portable records.

## Validation levels and triggers

| Trigger | Minimum validation | Full/target validation |
| --- | --- | --- |
| Markdown-only wording, no behavior/authority change | link/lint/schema as applicable; `git diff --check` | none unless claims or navigation changed |
| local source behavior | focused red-capable test, static/type/build owner, exact diff | repository baseline when dependencies are available |
| shared UI semantics or new `DESIGN.md` | independent named human approval bound to exact hash, lint, consumer diff | required viewports/states, two same-state passes, browser computed evidence, accessibility |
| API/schema/DTO | authority validator, producer/consumer checks, compatibility | integration/conformance and deployed consumer readback |
| persistence/migration | forward migration against representative engine/data, recovery decision | staging rehearsal, backup/restore or rollback/reconciliation proof |
| auth/security/permissions | negative authorization tests and trust-boundary review | target-runtime security workflow and readback |
| runtime/config/package/deploy change | build/package plus target-like runtime probe | authorized staging deployment and target readback |
| delivery claim | immutable result package, fixed-basis review, authorized remote receipt/readback | branch/PR/CI policy proof |
| deployed claim | authorized host receipt plus exact target/version readback | staging/production environment evidence as declared |
| production-verified claim | post-deploy production probe bound to deployment result | monitoring/SLO/rollback evidence required by risk |

Risk adds overlays; it never lets a broad “full test” label erase a failed focused
check. Conversely, a focused check cannot be promoted into a repository-wide or
production pass.

## Commands and residual gaps

Forgeway candidate: `npm test` passed (16 Schemas, 82 validation cases, Forgeway
validator, Graph core/CLI, Delivery Graph v2) and `git diff --check` passed. Skills:
`bash scripts/check-skills.sh` passed (16 packages, 51/51 routing, 228 tests) with six
non-blocking context warnings.

Still not verified in this ledger:

- GitHub branch CI on the final candidate commits;
- staging-host behavior (Sites checkpoints are production deployments, not staging);
- post-deploy production application verification, even though production deployment
  and host status readback passed for the separate probe;
- real desktop assistive-technology software such as VoiceOver, NVDA, or JAWS;
- desktop browser session/group behavior and two-pass visual comparison;
- Java compilation/tests because Maven Central was unreachable;
- Rust compilation/tests because Cargo was absent;
- Docker/model-backed SWE-bench, SWE-Skills-Bench, BrowserGym, or WebArena campaigns;
- additional language/framework extractors beyond the bounded Java addition.

Those gaps must remain `Not verified` until their actual host/tool/provider boundary is
available. They must not be converted to warnings or local success Observations.
