# GitHub Agent Skills Catalog — Deep Analysis Batch 048

- observed_at: `2026-08-09`
- status: `structure-reviewed`
- runtime_validation: `not_executed`
- selection_policy: existing indexed queue; complete exactly 10 genuinely qualified repository identities when at least 10 remain; metadata-only completion forbidden
- completed_repositories: `10`
- README direct reads: `10`
- SKILL.md direct reads: `14`
- unique Skill bodies directly reviewed: `8`
- unique Git trees: `4`
- new repository-scoped individual Skill reports: `7`

## Summary

This batch resumed at `ColonistOne/colony-skill` and advanced through the indexed queue into the 2026-04-11 shard. Every completed repository identity passed a content gate: repository identity and current stars were observed, a fixed revision was pinned, README/root structure was inspected, and at least one actual local `SKILL.md` body was read. No repository was marked complete from index metadata alone.

No repository script, build, test suite, eval harness, authenticated API, external service, or security workflow was executed. Source-level test/workflow assets are therefore evidence of implementation only, not passing runtime evidence.

| # | Repository | Stars observed | Pinned revision | Git tree | Content gate | Report action |
|---:|---|---:|---|---|---|---|
| 1 | `ColonistOne/colony-skill` | 0 | `392b183ffb76f643312f24a6255d185c0e11b864` | `f4d6232fc516d4dfc6f52e6ac3cb5a54fa6803da` | README + full root `SKILL.md` + `scripts/colony-auth.sh` + recursive tree | 1 new repository-scoped report |
| 2 | `gmh5225/Anthropic-Cybersecurity-Skills` | 3 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative defensive `SKILL.md` + recursive tree | mapped existing exact tree |
| 3 | `Balthael/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative defensive `SKILL.md` | mapped existing exact tree |
| 4 | `jet12/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative defensive `SKILL.md` | mapped existing exact tree |
| 5 | `DominikD83/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative defensive `SKILL.md` | mapped existing exact tree |
| 6 | `gaelnite/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative defensive `SKILL.md` | mapped existing exact tree |
| 7 | `yangshenming/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative defensive `SKILL.md` | mapped existing exact tree |
| 8 | `EmmaOK/Anthropic-Cybersecurity-Skills` | 0 | `6ec7f25d89d6e2ba8d810c4adb16eb94fc86efbe` | `7ec132a1e18317ef3cf127b94845d1f595baf1f1` | README + generated `index.json` + 2 unique new `SKILL.md` bodies + skill directory inventories + validation workflow + representative `phantom/` approval code | 2 new repository-scoped reports |
| 9 | `kareemkhaled111/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative defensive `SKILL.md` | mapped existing exact tree |
| 10 | `John-Yang-2013/agentskills` | 0 | `2a612a0d5956d23013db0dc09bfff6a79caaa8c4` | `ae5e6b5f55f568ca1cc3b9024065332be28de395` | README + all 4 local `SKILL.md` bodies + all bundled scripts + all bundled references + demo script + recursive tree | 4 new repository-scoped reports |

## Queue handling

`onuraltuntaspr/project-architect` retained its existing `adjacent_search_hit` classification and was not counted as completed. The next unresolved queue identity after this batch is `rickyly/agentskills` from `sources/catalog/batches/agentskills-created-2026-04-11-deterministic.json`.

## Repository analyses

### `ColonistOne/colony-skill`

**Verified**

- The pinned repository is a single operational Skill (`the-colony`) with README, root `SKILL.md`, one authentication helper, and no repository-local tests/evals/references.
- The Skill delegates a broad set of authenticated external operations, including content/account interactions, messaging, marketplace/task actions, webhooks, and other state-changing service calls.
- `scripts/colony-auth.sh` receives the API key as an argument, interpolates JSON in shell, does not distinguish HTTP failure with `curl --fail`, has no explicit timeout/retry policy, and emits the raw response on authentication failure.
- The `SKILL.md` blob (`4bc35977eec016b03becc10f9a8ac11784865615`) differs from the current upstream `TheColonyAI/colony-skill` body, so this repository is not suppressed as an exact-body duplicate of the earlier upstream review.

**Assessment**

The main risk is authorization breadth rather than document structure. A higher-level policy should separately authorize state-changing operations; activating a Skill should not implicitly authorize all account, marketplace, messaging, webhook, or payment-related actions. Credential handling should avoid command-line exposure and fail closed on HTTP/authentication errors.

**Not verified**

External service behavior, authentication success, API contracts, webhook delivery, marketplace operations, or script runtime behavior.

### Exact-tree Anthropic Cybersecurity mirrors

The seven identities at revision `4ae0be7f4806596e94958ac343379e9c9b3111d2` resolve to the same Git tree `5dd2ce82978a50cd014d4b310f5993bf5bba6f43`. Each identity independently passed a real content gate by reading its README and a representative defensive Skill body. The shared tree had already been reviewed in Batch 047, so repository coverage advances without duplicating individual Skill reports.

This distinction is intentional: repository identity coverage and canonical content coverage are separate. Exact-tree equality is sufficient to suppress repeated content reports, but metadata equality alone is not.

### `EmmaOK/Anthropic-Cybersecurity-Skills`

**Verified**

- This repository is materially divergent from the exact-tree mirrors: pinned tree `7ec132a1e18317ef3cf127b94845d1f595baf1f1` includes the Skill database plus a substantial `phantom/` Python application/integration surface and multiple GitHub workflows.
- Root README still says `754` Skills, while the pinned generated `index.json` records `843`; this is a concrete documentation/generated-index drift.
- Two post-baseline defensive Skill bodies were directly deep-read: `byod-and-remote-access-browser-security` and `shadow-ai-and-saas-discovery`.
- Each of those two reviewed Skill directories contains only `SKILL.md`; no colocated scripts, references, tests, or eval files are present at the pinned revision.
- `.github/workflows/validate-skills.yml` validates frontmatter fields, kebab-case naming, and duplicate names. It is structural validation, not behavioral/security-quality evaluation.
- `phantom/approvals.py` implements persisted approval records and signed approval links, but its signing secret has a built-in fallback value. Production-sensitive signing configuration should fail closed rather than silently fall back to a known constant.

**Assessment**

This repository should no longer be treated as only a static Skill catalog. The Skill database, validation workflow, and `phantom/` operational application have different assurance boundaries. The current index/README count drift also shows why generated inventory should be the source of truth for quantity while direct body reads remain the gate for individual deep-analysis reports.

**Not verified**

No workflow, Python application, integration, cloud deployment, security test, or Skill behavior was executed. The two directly reviewed defensive Skills are source-reviewed only.

### `John-Yang-2013/agentskills`

**Verified**

- The pinned repository contains four local Copilot Agent Skills: `code-reviewer`, `python-env-manager`, `data-explorer`, and `api-designer`.
- All four `SKILL.md` bodies, their bundled scripts, their reference documents, and the root demo script were directly read.
- No repository-local automated test/eval suite is present in the pinned tree; `scripts/demo.sh` is a demonstrator, not an assertion-based behavioral evaluation harness.
- `code-reviewer` uses small deterministic Python checks, but they are heuristic AST/line analyses rather than a full static-analysis engine.
- `python-env-manager/scripts/check_deps.py` has limited version-constraint reasoning; its source logic does not establish general dependency-range correctness.
- `data-explorer` provides practical profiling/report helpers, but there is no fixture-based output/correctness benchmark.
- `api-designer/scripts/generate_stub.py` has a deterministic code-generation defect: optional query parameters can produce duplicate assignment syntax, while required query parameters are still emitted as `Optional[...] = Query(None)`, losing requiredness semantics.
- `api-designer/scripts/validate_openapi.py` performs focused structural checks rather than full OpenAPI conformance validation.

**Assessment**

This repository is useful as a compact example of `SKILL.md + scripts + references`, but the implementation quality is uneven and lacks executable regression evidence. The most actionable fix is to add fixture-driven tests around generated FastAPI signatures and OpenAPI required/optional parameter behavior.

**Not verified**

The demo script, generated FastAPI application, dependency checker, data profiler, or OpenAPI validator was not executed.

## Cross-batch findings

1. **Content deduplication must be content-based.** Seven different Cybersecurity repository identities share one exact tree; each still requires a real content gate, but duplicate individual reports add no evidence.
2. **Catalog inventory and application runtime need separate assurance.** `EmmaOK/Anthropic-Cybersecurity-Skills` combines 843 indexed Skills with an operational Python platform; one validation status cannot safely cover both.
3. **Structural CI is not behavioral validation.** Frontmatter/name checks prove parseability and catalog consistency, not task quality or safe execution.
4. **External side effects require a policy above individual Skills.** `the-colony` demonstrates why activation, authorization, and execution permission should be distinct concepts.
5. **Executable helper code deserves fixture-level testing.** The FastAPI generator defect in `John-Yang-2013/agentskills` is visible directly from source and is exactly the type of issue a small deterministic regression suite should catch.

## Count check

```text
completed repository identities                 10
README direct reads                              10
SKILL.md direct reads                            14
unique Skill bodies directly reviewed             8
unique Git trees                                  4
new repository-scoped individual reports          7
cumulative structure-reviewed repositories       480
cumulative repository-scoped Skill reports      2972
arithmetic remaining estimate                    1608
```

`1608` is only the frozen `2088` eligible basis minus `480` structure-reviewed repository identities. Canonical reconciliation remains pending; this number is not a final deduplicated unique-repository remainder.
