# GitHub Agent Skills Deep Analysis — Batch 012

## Run result

- Batch: `2026-08-07-batch-012`
- Repository completions: **10**
- Individual skill reports: **240** unique skill identities
- Completion basis: repository identity + displayed GitHub stars + actual repository content inspection. No repository was completed from metadata alone.
- Evidence model: current repository-maintained inventories were used to enumerate current skills; representative `SKILL.md` definitions were directly read in every repository, with scripts, references, validators, evals, workflows, or support code read when available.
- Runtime validation: **not_executed**. Third-party scripts, installers, cloud APIs, browser automation, external services, and test suites were inspected but not executed.
- Queue snapshot: `sources/catalog/github-agent-skills-index-latest.json`, `2502` unique repositories, `2088` deep-analysis eligible, `414` held for review.

Large collections are not represented as if every skill body was directly read. Each individual report records whether it is based on a directly read body/support artifact or the repository's current maintained catalog/tree. Repository-level completion requires actual content reading beyond metadata.

## Repository summary

| Repository | GitHub repository ID | Default branch | Stars observed | Current individual reports | Direct content evidence |
| --- | ---: | --- | ---: | ---: | --- |
| `davidpc007/openclaw-marketing-skills` | `1288093218` | `main` | 147 | 37 | README/root catalog; `product-marketing-context/SKILL.md`; `google-ads-connect/SKILL.md`; missing referenced support paths checked |
| `huangkiki/dailypaper-skills` | `1167689618` | `main` | 1.1k | 7 | README/architecture; `daily-papers/SKILL.md`; `paper-reader/SKILL.md`; deterministic fetch/scoring script |
| `itsmostafa/aws-agent-skills` | `187398354` | `main` | 1.1k | 18 | README/current service inventory; `iam/SKILL.md`; official-reference map; AWS documentation update checker/workflow |
| `jorgerosal/wordpress-skills` | `1213054856` | `main` | 66 | 18 | README/current domain inventory; `wp-performance-review/SKILL.md`; repository structural validator |
| `LambdaTest/agent-skills` | `1159911288` | `main` | 347 | 70 | `skills_index.json`; `api-analyzer/SKILL.md`; validator; Playwright eval fixture; duplicate catalog-row reconciliation |
| `WordPress/agent-skills` | `1137891086` | `trunk` | 2.0k | 17 | README/current inventory; `wp-block-development/SKILL.md`; block scanner; eval harness |
| `vibe-motion/skills` | `1184541668` | `main` | 995 | 13 | README/current tree; `pixel2motion/SKILL.md`; SVG path-audit implementation |
| `YANZHANLIN/ielts-claude-skills` | `1200004393` | `main` | 264 | 4 | README/current tree; `ielts/SKILL.md`; pure-Markdown packaging |
| `rrezartprebreza/spring-boot-skills` | `1210653721` | `main` | 202 | 19 | README/current versioned inventory; Boot 4 REST skill; Boot 3/4 parity validator |
| `vadimcomanescu/codex-skills` | `1134597713` | `main` | 24 | 37 | README/current curated+experimental inventory; `code-reviewer/SKILL.md`; repository validator |

Stars are mutable observations from public GitHub repository pages during this batch.

---

## 1. `davidpc007/openclaw-marketing-skills`

### Repository analysis

**Identity and structure.** Public repository on `main`, organized around a root marketing-skill catalog plus `skills/` packages. The current README enumerates **37** skills while the repository About text still says **38**, so the live catalog and summary metadata are not fully synchronized.

**Direct content evidence.** `skills/product-marketing-context/SKILL.md` implements a reusable context artifact under `.agents/`, with existing-state checks and guided or codebase-derived drafting. `skills/google-ads-connect/SKILL.md` defines credential setup, data acquisition, a scorecard, and a confirmation boundary before optional account mutations. During support-file verification, the skill's referenced `references/mutation-safety.md` and `scripts/audit.py` paths returned 404 from the current repository, establishing package drift rather than merely missing search results.

**Quality / risk.** The catalog has useful cross-skill composition and central marketing context, but at least one integration skill currently references absent support artifacts. Live-account connectors also create a higher-authority execution boundary, so this batch inspected instructions only and did not execute external API operations.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `product-marketing-context` | **direct body** | Shared product/marketing context workflow with existing-state checks and persistent `.agents/` context artifact. |
| `page-cro` | current README/catalog | Conversion review skill for marketing pages; body not directly read in this batch. |
| `signup-flow-cro` | current README/catalog | Signup-flow conversion review skill; body not directly read in this batch. |
| `onboarding-cro` | current README/catalog | Onboarding conversion review skill; body not directly read in this batch. |
| `form-cro` | current README/catalog | Form conversion review skill; body not directly read in this batch. |
| `popup-cro` | current README/catalog | Popup conversion review skill; body not directly read in this batch. |
| `paywall-upgrade-cro` | current README/catalog | Paywall/upgrade conversion skill; body not directly read in this batch. |
| `copywriting` | current README/catalog | Marketing-copy creation skill; body not directly read in this batch. |
| `copy-editing` | current README/catalog | Marketing-copy editing skill; body not directly read in this batch. |
| `cold-email` | current README/catalog | Cold-email workflow; body not directly read in this batch. |
| `email-sequence` | current README/catalog | Multi-message email sequence workflow; body not directly read in this batch. |
| `social-content` | current README/catalog | Social-content workflow; body not directly read in this batch. |
| `seo-audit` | current README/catalog | SEO audit workflow; body not directly read in this batch. |
| `ai-seo` | current README/catalog | AI-search/SEO workflow; body not directly read in this batch. |
| `programmatic-seo` | current README/catalog | Programmatic SEO workflow; body not directly read in this batch. |
| `site-architecture` | current README/catalog | Site-information-architecture workflow; body not directly read in this batch. |
| `schema-markup` | current README/catalog | Structured-data/schema workflow; body not directly read in this batch. |
| `content-strategy` | current README/catalog | Content-strategy workflow; body not directly read in this batch. |
| `paid-ads` | current README/catalog | Paid-ad strategy workflow; body not directly read in this batch. |
| `ad-creative` | current README/catalog | Ad-creative workflow; body not directly read in this batch. |
| `ab-test-setup` | current README/catalog | Experiment setup workflow; body not directly read in this batch. |
| `analytics-tracking` | current README/catalog | Analytics/tracking setup workflow; body not directly read in this batch. |
| `google-ads-connect` | **direct body + missing-support verification** | Live Google Ads connector/audit workflow; current body references support paths not present at the checked locations. |
| `meta-ads-connect` | current README/catalog | Meta Ads data connector workflow; body not directly read in this batch. |
| `search-console-connect` | current README/catalog | Search Console data connector workflow; body not directly read in this batch. |
| `x-twitter-connect` | current README/catalog | X/Twitter connector workflow; body not directly read in this batch. |
| `referral-program` | current README/catalog | Referral-program design workflow; body not directly read in this batch. |
| `free-tool-strategy` | current README/catalog | Free-tool/growth strategy workflow; body not directly read in this batch. |
| `churn-prevention` | current README/catalog | Retention/churn workflow; body not directly read in this batch. |
| `revops` | current README/catalog | Revenue-operations workflow; body not directly read in this batch. |
| `sales-enablement` | current README/catalog | Sales-enablement workflow; body not directly read in this batch. |
| `launch-strategy` | current README/catalog | Product-launch workflow; body not directly read in this batch. |
| `pricing-strategy` | current README/catalog | Pricing strategy workflow; body not directly read in this batch. |
| `competitor-alternatives` | current README/catalog | Competitor/alternative positioning workflow; body not directly read in this batch. |
| `marketing-ideas` | current README/catalog | Marketing ideation workflow; body not directly read in this batch. |
| `marketing-psychology` | current README/catalog | Marketing psychology/persuasion workflow; body not directly read in this batch. |
| `lead-magnets` | current README/catalog | Lead-magnet strategy workflow; body not directly read in this batch. |

---

## 2. `huangkiki/dailypaper-skills`

### Repository analysis

**Identity and structure.** Public repository on `main`. The current workflow is a seven-skill research pipeline backed by shared configuration, Python utilities, Obsidian output, optional Zotero integration, and an optional local web viewer.

**Direct content evidence.** `daily-papers/SKILL.md` is the user-facing orchestrator that sequences fetch → review → notes. `paper-reader/SKILL.md` is a substantial paper-reading workflow with input routing, template-driven notes, figure/formula/table completeness checks, image fallback handling, concept-link maintenance, and config-gated git operations. `skills/daily-papers/fetch_and_score.py` moves fetch, keyword scoring, merge/dedup, and top-N selection into deterministic Python rather than spending model tokens on those stages.

**Quality / risk.** This is a strong example of separating deterministic data processing from model judgment. The README also documents a local permission-bypass convenience with an explicit warning, so execution permissions remain an operator-controlled boundary. No dedicated model-behavior eval harness was observed in this batch.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `daily-papers` | **direct body** | User-facing orchestrator for fetch, review, and note-generation stages. |
| `paper-reader` | **direct body + references** | Deep paper-reading workflow with source fallbacks, structured note QA, concept maintenance, and optional Zotero/Obsidian integration. |
| `generate-mocs` | current README/tree | Generates Obsidian map-of-content/index artifacts; body not directly read in this batch. |
| `github-trending` | current README/tree | Produces research-oriented GitHub trending notes; body not directly read in this batch. |
| `daily-papers-fetch` | current README/tree + supporting script | Internal candidate-fetch stage; deterministic fetch/scoring code was directly inspected. |
| `daily-papers-review` | current README/tree | Internal recommendation/review stage; body not directly read in this batch. |
| `daily-papers-notes` | current README/tree | Internal prioritized-note stage; body not directly read in this batch. |

---

## 3. `itsmostafa/aws-agent-skills`

### Repository analysis

**Identity and structure.** Public repository on `main` with 18 service skills under `skills/`, shared official-documentation references, tracking state, scripts, and a scheduled documentation-update workflow.

**Direct content evidence.** `skills/iam/SKILL.md` includes `last_updated` and an official AWS doc source, then gives concepts, patterns, troubleshooting, and references. Root `REFERENCES.md` maps all service domains to official guides/API/CLI references. `scripts/check-aws-updates.py` directly parses AWS documentation RSS/What's New sources, tracks last-check state, and applies significance keywords; the weekly GitHub Actions workflow runs this checker and opens repository updates through pull requests.

**Quality / risk.** The maintenance loop is concrete code rather than a README-only freshness claim. It still uses keyword significance heuristics and this batch did not execute the feeds or validate every AWS recommendation against current upstream docs.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `iam` | **direct body + official references** | IAM knowledge skill with upstream source metadata, patterns, troubleshooting, and reference links. |
| `lambda` | current README/service inventory | AWS Lambda skill; body not directly read in this batch. |
| `dynamodb` | current README/service inventory | DynamoDB skill; body not directly read in this batch. |
| `s3` | current README/service inventory | S3 skill; body not directly read in this batch. |
| `api-gateway` | current README/service inventory | API Gateway skill; body not directly read in this batch. |
| `ec2` | current README/service inventory | EC2 skill; body not directly read in this batch. |
| `ecs` | current README/service inventory | ECS skill; body not directly read in this batch. |
| `eks` | current README/service inventory | EKS skill; body not directly read in this batch. |
| `cloudformation` | current README/service inventory | CloudFormation skill; body not directly read in this batch. |
| `cloudwatch` | current README/service inventory | CloudWatch skill; body not directly read in this batch. |
| `rds` | current README/service inventory | RDS skill; body not directly read in this batch. |
| `sqs` | current README/service inventory | SQS skill; body not directly read in this batch. |
| `sns` | current README/service inventory | SNS skill; body not directly read in this batch. |
| `cognito` | current README/service inventory | Cognito skill; body not directly read in this batch. |
| `step-functions` | current README/service inventory | Step Functions skill; body not directly read in this batch. |
| `secrets-manager` | current README/service inventory | Secrets Manager skill; body not directly read in this batch. |
| `eventbridge` | current README/service inventory | EventBridge skill; body not directly read in this batch. |
| `bedrock` | current README/service inventory | Bedrock skill; body not directly read in this batch. |

---

## 4. `jorgerosal/wordpress-skills`

### Repository analysis

**Identity and structure.** Public repository on `main`. The current architecture keeps canonical Claude-oriented packages under `claude-skills/`, a plugin-compatible `skills/` surface, parallel Codex wrappers, slash commands, docs, and a validation script. The current table lists **18** domains, while one README sentence still says the Codex wrappers cover “the same seventeen domains,” a documentation-count drift.

**Direct content evidence.** `claude-skills/wp-performance-review/SKILL.md` is a systematic WordPress performance review protocol with severity ordering, file-type-specific checks, search patterns, platform context, and report structure. `scripts/validate_repo.py` enforces frontmatter, Claude/Codex skill-set parity, plugin alias parity, shared reference presence, command metadata, and README/docs/changelog consistency.

**Quality / risk.** The dual-agent packaging and repository validator are strong maintenance mechanisms. The count drift shows prose can still lag the validated package tree; no behavior eval suite was directly observed in this batch.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `wp-performance-review` | **direct body** | Systematic WordPress performance review workflow with severity, targeted scans, and platform-aware guidance. |
| `wp-security-review` | current README/domain inventory | WordPress security review domain; body not directly read in this batch. |
| `wp-plugin-development` | current README/domain inventory | Plugin-development/review domain; body not directly read in this batch. |
| `wp-acf-and-content-modeling` | current README/domain inventory | ACF/content-modeling domain; body not directly read in this batch. |
| `wp-headless-and-wpgraphql` | current README/domain inventory | Headless/WPGraphQL domain; body not directly read in this batch. |
| `wp-block-development` | current README/domain inventory | Gutenberg block-development domain; body not directly read in this repository batch. |
| `wp-theme-development` | current README/domain inventory | Theme-development domain; body not directly read in this batch. |
| `wp-woocommerce-dev` | current README/domain inventory | WooCommerce development/review domain; body not directly read in this batch. |
| `wp-rest-api-development` | current README/domain inventory | WordPress REST API domain; body not directly read in this batch. |
| `wp-admin-ui-development` | current README/domain inventory | Admin UI domain; body not directly read in this batch. |
| `wp-migration-upgrade-review` | current README/domain inventory | Migration/upgrade review domain; body not directly read in this batch. |
| `wp-accessibility-review` | current README/domain inventory | Accessibility review domain; body not directly read in this batch. |
| `wp-test-strategy` | current README/domain inventory | WordPress testing strategy domain; body not directly read in this batch. |
| `wp-ci-cd-and-release-engineering` | current README/domain inventory | CI/CD and release domain; body not directly read in this batch. |
| `wp-site-audit-and-onboarding` | current README/domain inventory | Repository/site onboarding and routing domain; body not directly read in this batch. |
| `wp-wpcli-and-ops` | current README/domain inventory | WP-CLI and operations domain; current README marks it in progress. |
| `wp-playground-development` | current README/domain inventory | WordPress Playground domain; current README marks it in progress. |
| `wp-phpstan-review` | current README/domain inventory | PHPStan/static-analysis domain; current README marks it in progress. |

---

## 5. `LambdaTest/agent-skills`

### Repository analysis

**Identity and structure.** Public repository on `main` with framework-specific top-level skill packages, nested API/Postman/Newman packages, `evals/`, shared references, repository scripts, and a machine-readable `skills_index.json`. The index declares `total_skills: 70`.

**Catalog reconciliation.** The current `skills_index.json` contains **71 catalog rows but 70 unique skill identities**: `test-framework-migration-skill` appears twice at the same path, once with an empty reference list and once with the full migration-reference set. This batch counts it once. The repository validator checks referenced files and metadata but does not reject duplicate index records or reconcile the declared total against raw row count, explaining why this drift can survive structural validation.

**Direct content evidence.** `api-skill/api-analyzer/SKILL.md` defines a terse request-validation workflow and also mixes the functional instructions with TestMu product promotion/handoff behavior. `scripts/validate_skills.py` enforces frontmatter fields, categories, line limits, reference/playbook presence, and index file existence. `evals/playwright-skill-evals.json` contains ten concrete routing/behavior cases including negative-trigger cases; this is genuine eval material, although the evals were not executed in this batch.

**Quality / risk.** The repository has unusually broad test-framework coverage, machine-readable inventory, structural validation, and behavior fixtures. The principal observed issue is index duplication; a secondary design concern is vendor-promotion language embedded inside some skill behavior.

### Individual skill reports

The following are the **70 unique** current identities after exact-name/path deduplication of the duplicate migration record.

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `api-ai-augmented` | current `skills_index.json` | API/LLM tool-schema and agentic API workflow skill. |
| `api-analyzer` | **direct body** | Strict API-request validation workflow; includes vendor handoff/promotion after the functional verdict. |
| `api-compliance-checker` | current index | API compliance/privacy design skill. |
| `api-designer` | current index | REST API design/specification skill. |
| `api-documentation` | current index | API documentation generation skill. |
| `api-fetcher-specific-domains` | current index | Domain/platform API example lookup skill. |
| `api-graphql-grpc` | current index | GraphQL/gRPC design helper. |
| `api-health-monitoring` | current index | API health/observability design skill. |
| `api-inferrer-from-files` | current index | API endpoint inference from project structure. |
| `api-integration` | current index | API/event integration architecture skill. |
| `api-mock-helper` | current index | API mock/sandbox/fixture design skill. |
| `api-rate-limiting-helper` | current index | API rate-limit/retry/quota design skill. |
| `api-sdk-generator` | current index | Client SDK/code-generation workflow. |
| `api-security-auth-pattern` | current index | Defensive API authentication/authorization pattern skill. |
| `api-to-testcase-generator` | current index | Generates test cases from API definitions/specs. |
| `api-versioning-helper` | current index | API versioning/deprecation/migration guidance. |
| `appium-skill` | current index | Appium mobile-automation skill. |
| `behat-skill` | current index | Behat/PHP BDD skill. |
| `behave-skill` | current index | Behave/Python BDD skill. |
| `capybara-skill` | current index | Capybara/Ruby E2E skill. |
| `cicd-pipeline-skill` | current index | CI/CD pipeline generation for test automation. |
| `codeception-skill` | current index | Codeception/PHP testing skill. |
| `cucumber-skill` | current index | Cucumber/Gherkin BDD skill. |
| `cypress-skill` | current index | Cypress E2E/component testing skill. |
| `detox-skill` | current index | Detox/React Native testing skill. |
| `espresso-skill` | current index | Android Espresso UI testing skill. |
| `flutter-testing-skill` | current index | Flutter test-generation skill. |
| `gauge-skill` | current index | Gauge specification/test skill. |
| `geb-skill` | current index | Geb/Groovy browser-testing skill. |
| `hyperexecute-skill` | current index | Test orchestration configuration skill. |
| `jasmine-skill` | current index | Jasmine unit-testing skill. |
| `jest-skill` | current index | Jest unit/integration testing skill. |
| `junit-5-skill` | current index | JUnit 5 testing skill. |
| `karma-skill` | current index | Karma browser test-runner configuration skill. |
| `laravel-dusk-skill` | current index | Laravel Dusk browser-testing skill. |
| `lettuce-skill` | current index | Legacy Lettuce/Python BDD skill with replacement context. |
| `mocha-skill` | current index | Mocha/Chai/Sinon testing skill. |
| `mstest-skill` | current index | MSTest/.NET testing skill. |
| `nemojs-skill` | current index | Nemo.js browser-automation skill. |
| `newman-cicd-integration` | current index | Newman CI/CD integration skill. |
| `newman-report-analyzer` | current index | Newman result-analysis skill. |
| `newman-script-helper` | current index | Newman command/configuration helper. |
| `nightwatchjs-skill` | current index | NightwatchJS E2E testing skill. |
| `nunit-skill` | current index | NUnit/.NET testing skill. |
| `openapi-spec-generator` | current index | OpenAPI/Swagger specification-generation skill. |
| `phpunit-skill` | current index | PHPUnit testing skill. |
| `playwright-skill` | **current index + direct eval fixture** | Playwright automation skill backed by explicit positive, negative-routing, mobile, debugging, and scaffold eval cases. |
| `postman-collection-generator` | current index | Postman collection-generation skill. |
| `postman-newman-automation` | current index | Postman-to-Newman automation workflow. |
| `postman-openapi-converter` | current index | OpenAPI-to-Postman conversion skill. |
| `postman-test-script-generator` | current index | Postman assertion/pre-request script generation skill. |
| `protractor-skill` | current index | Legacy Protractor E2E skill with deprecation context. |
| `puppeteer-skill` | current index | Puppeteer browser-automation skill. |
| `pytest-skill` | current index | Pytest testing skill. |
| `robot-framework-skill` | current index | Robot Framework testing skill. |
| `rspec-skill` | current index | RSpec/Ruby testing skill. |
| `selenide-skill` | current index | Selenide/Java UI testing skill. |
| `selenium-skill` | current index | Selenium multi-language browser-automation skill. |
| `serenity-bdd-skill` | current index | Serenity BDD/Screenplay skill. |
| `smartui-skill` | current index | Visual-regression configuration skill. |
| `specflow-skill` | current index | SpecFlow/.NET BDD skill. |
| `test-framework-migration-skill` | **current index, duplicate rows deduplicated** | Cross-framework migration skill; represented twice in the raw index but counted once here. |
| `testcafe-skill` | current index | TestCafe E2E testing skill. |
| `testng-skill` | current index | TestNG/Java testing skill. |
| `testunit-skill` | current index | Ruby Test::Unit skill. |
| `unittest-skill` | current index | Python unittest skill. |
| `vitest-skill` | current index | Vitest testing skill. |
| `webdriverio-skill` | current index | WebdriverIO testing skill. |
| `xcuitest-skill` | current index | XCUITest iOS UI testing skill. |
| `xunit-skill` | current index | xUnit.net testing skill. |

---

## 6. `WordPress/agent-skills`

### Repository analysis

**Identity and structure.** Public WordPress-owned repository on `trunk`. The current README enumerates 17 skills under `skills/`, backed by references, optional scripts, shared material, docs, and an `eval/` tree.

**Direct content evidence.** `skills/wp-block-development/SKILL.md` defines inputs, deterministic triage/listing, block-model selection, metadata/registration/serialization/deprecation procedures, verification, and escalation to canonical upstream docs. Its `scripts/list_blocks.mjs` recursively discovers `block.json` files with explicit ignores/depth/file caps and emits structured JSON. `eval/harness/run.mjs` validates every skill's frontmatter/name/compatibility contract and executes a deterministic project-triage script shape check.

**Quality / risk.** This repository combines domain procedures, deterministic repository scanners, and structural evaluation. The README documents AI-assisted authorship with subsequent contributor review/testing. The harness was inspected but not executed here, so no passing-runtime claim is made.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `wordpress-router` | current README/tree | Routes WordPress tasks to specialized skills. |
| `wp-project-triage` | current README/tree + harness dependency | Deterministic project classification/triage skill used by other workflows. |
| `wp-block-development` | **direct body + script** | Detailed Gutenberg block workflow with deterministic block discovery and explicit verification. |
| `wp-block-themes` | current README/tree | Block-theme development skill. |
| `wp-plugin-development` | current README/tree | Plugin-development skill. |
| `wp-rest-api` | current README/tree | WordPress REST API skill. |
| `wp-interactivity-api` | current README/tree | Interactivity API skill. |
| `wp-abilities-api` | current README/tree | Abilities API development skill. |
| `wp-abilities-audit` | current README/tree | Abilities audit/review skill. |
| `wp-abilities-verify` | current README/tree | Abilities verification skill with supporting runtime-harness references in the repository. |
| `wp-wpcli-and-ops` | current README/tree | WP-CLI and operations skill. |
| `wp-performance` | current README/tree | WordPress performance skill. |
| `wp-phpstan` | current README/tree | PHPStan/static-analysis skill. |
| `wp-playground` | current README/tree | WordPress Playground skill. |
| `wpds` | current README/tree | WordPress design-system skill. |
| `wp-plugin-directory-guidelines` | current README/tree | Plugin-directory policy/guideline skill. |
| `blueprint` | current README/tree | Blueprint/reproducible-environment skill. |

---

## 7. `vibe-motion/skills`

### Repository analysis

**Identity and structure.** Public repository on `main` with 13 current skill directories. The README explicitly keeps a separate boids/fish project outside the skill count, so this report does not inflate the inventory with adjacent project material.

**Direct content evidence.** `pixel2motion/SKILL.md` is a large Pixel → Vector → Motion workflow with a hard smoothness gate, complexity ladder, geometric overlays/IoU evidence, motion-ready SVG contracts, reduced-motion requirements, bounded iteration budget, and explicit motion QA. `pixel2motion/scripts/svg_path_audit.py` is actual implementation code for parsing SVG path commands, measuring/visualizing segments and tangents, and producing audit artifacts.

**Quality / risk.** The strongest pattern is explicit evidence generation and bounded refinement instead of subjective endless polishing. No central model-routing eval suite was observed; supporting tools were inspected rather than executed.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `brand-launch-video-star` | current root tree | Brand-launch video skill; body not directly read in this batch. |
| `claude-typer` | current root tree | Typing/text-motion skill; body not directly read in this batch. |
| `disney-animation-rule-skill` | current root tree | Animation-principles guidance skill; body not directly read in this batch. |
| `light-spotlight-render` | current root tree | Spotlight/rendering skill; body not directly read in this batch. |
| `pixel2motion` | **direct body + script** | Evidence-heavy raster-to-vector-to-motion workflow with deterministic SVG path audit support. |
| `procedural-fish-render` | current root tree | Procedural fish-rendering skill; body not directly read in this batch. |
| `remotion-3d-ticker` | current root tree | Remotion 3D ticker skill; body not directly read in this batch. |
| `remotion-candlestick` | current root tree | Remotion candlestick visualization skill; body not directly read in this batch. |
| `remotion-vinyl-player` | current root tree | Remotion vinyl-player animation skill; body not directly read in this batch. |
| `ruler-progress-render` | current root tree | Progress/ruler rendering skill; body not directly read in this batch. |
| `svg-assembly-animator` | current root tree | SVG assembly animation skill; body not directly read in this batch. |
| `threejs-earth-render` | current root tree | Three.js Earth rendering skill; body not directly read in this batch. |
| `wechat-2d-render` | current root tree | WeChat-style 2D rendering skill; body not directly read in this batch. |

---

## 8. `YANZHANLIN/ielts-claude-skills`

### Repository analysis

**Identity and structure.** Public repository on `main`, intentionally small and stateless: four pure-Markdown skill directories with no dependency-heavy runtime, scripts, or eval harness in the current layout.

**Direct content evidence.** `ielts/SKILL.md` is the router/assessment entrypoint. It gathers target/timeline and current level, routes to writing/reading/speaking subskills, includes score/strategy tables, and states explicit boundaries about what the router itself should not do.

**Quality / risk.** The packaging is simple and low-maintenance. Domain scoring/strategy statements are authored guidance rather than independently validated facts in this batch, so completion indicates content inspection, not educational-outcome validation.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `ielts` | **direct body** | Assessment/router skill that sends users to specialized training modules and maintains scope boundaries. |
| `ielts-writing` | current root tree/README | Writing-training skill; body not directly read in this batch. |
| `ielts-reading` | current root tree/README | Reading-training skill; body not directly read in this batch. |
| `ielts-speaking` | current root tree/README | Speaking-material/training skill; body not directly read in this batch. |

---

## 9. `rrezartprebreza/spring-boot-skills`

### Repository analysis

**Identity and structure.** Public repository on `main`. It maintains mirrored `skills/spring-boot-3/` and `skills/spring-boot-4/` trees. The current catalog contains **19 logical skill identities**; the two framework-version implementations are variants of those identities, not 38 independent reports.

**Direct content evidence.** `skills/spring-boot-4/rest-api-conventions/SKILL.md` provides concrete response, status, URL, versioning, pagination, exception-handling, and Boot 4 gotcha conventions. `scripts/validate-skills.sh` checks exact Boot 3/Boot 4 folder parity, SKILL frontmatter, mandatory Gotchas sections with minimum gotcha counts, specific JWT-template semantics, README catalog coverage, and referenced local paths.

**Quality / risk.** Mirrored version trees plus parity validation are a useful pattern for framework-major-version knowledge. The validator was read but not executed, and individual technical claims were not independently replayed against running Boot projects.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `layered-architecture` | current README/catalog | Layered architecture guidance with Boot 3/4 variants. |
| `hexagonal-architecture` | current README/catalog | Hexagonal architecture guidance with Boot 3/4 variants. |
| `domain-driven-design` | current README/catalog | DDD guidance with Boot 3/4 variants. |
| `multi-module-maven` | current README/catalog | Multi-module Maven architecture skill. |
| `rest-api-conventions` | **direct Boot 4 body** | Concrete REST API conventions including Boot 4 native version routing and pagination/error gotchas. |
| `openapi-first` | current README/catalog | OpenAPI-first workflow skill. |
| `problem-details-rfc9457` | current README/catalog | Problem-details/error-contract skill. |
| `hateoas` | current README/catalog | HATEOAS API-design skill. |
| `spring-data-jpa` | current README/catalog | Spring Data JPA skill. |
| `flyway-migrations` | current README/catalog | Flyway migration skill. |
| `spring-data-redis` | current README/catalog | Redis integration skill. |
| `transactional-patterns` | current README/catalog | Transaction boundary/pattern skill. |
| `spring-batch` | current README/catalog | Spring Batch skill. |
| `spring-security-jwt` | current README/catalog + validator-specific check | JWT/security skill with extra repository validation for access-token semantics. |
| `oauth2-resource-server` | current README/catalog | OAuth2 resource-server skill. |
| `spring-ai-integration` | current README/catalog | Spring AI integration skill. |
| `mcp-server` | current README/catalog | MCP server skill. |
| `ai-observability` | current README/catalog | AI observability skill. |
| `testing-pyramid` | current README/catalog | Testing-strategy/pyramid skill. |

---

## 10. `vadimcomanescu/codex-skills`

### Repository analysis

**Identity and structure.** Public repository on `main` with two explicit tiers: **16 curated** and **21 experimental** skills, grouped under category directories. Each package is expected to carry `SKILL.md` and `LICENSE.txt`, with optional `references/`, `assets/`, and `scripts/`.

**Direct content evidence.** `skills/.curated/quality/code-reviewer/SKILL.md` defines review order (correctness, safety, maintainability, performance, tests), large-diff triage, request-change criteria, and structured output. `scripts/validate_skills.py` scans both tiers, requires exactly `name` + `description` frontmatter, folder/name agreement, lowercase naming, `LICENSE.txt`, and verifies backtick-referenced local `references/`, `assets/`, and `scripts/` paths actually exist.

**Quality / risk.** The curated/experimental split makes maturity explicit, and the validator checks the common failure mode of broken support-file references. No model-behavior eval suite was directly observed in this batch.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `frontend-design` | current curated inventory | Curated frontend-design skill. |
| `information-architect` | current curated inventory | Curated information-architecture skill. |
| `react-best-practices` | current curated inventory | Curated React best-practices skill. |
| `senior-architect` | current curated inventory | Curated software-architecture skill. |
| `senior-backend` | current curated inventory | Curated backend-engineering skill. |
| `senior-devops` | current curated inventory | Curated DevOps skill. |
| `senior-computer-vision` | current curated inventory | Curated computer-vision skill. |
| `senior-data-engineer` | current curated inventory | Curated data-engineering skill. |
| `senior-data-scientist` | current curated inventory | Curated data-science skill. |
| `code-reviewer` | **direct body** | High-signal code-review workflow with risk ordering, diff triage, actionable comments, and test-plan output. |
| `senior-qa` | current curated inventory | Curated QA skill. |
| `test-driven-development` | current curated inventory | Curated TDD workflow skill. |
| `webapp-testing` | current curated inventory | Curated web-application testing skill. |
| `security-compliance` | current curated inventory | Curated defensive security/compliance review skill. |
| `senior-secops` | current curated inventory | Curated defensive SecOps skill. |
| `senior-prompt-engineer` | current curated inventory | Curated prompt-engineering skill. |
| `accessibility-auditor` | current experimental inventory | Experimental accessibility audit skill. |
| `ui-design-system` | current experimental inventory | Experimental UI design-system skill. |
| `senior-frontend` | current experimental inventory | Experimental frontend-engineering skill. |
| `senior-fullstack` | current experimental inventory | Experimental full-stack skill. |
| `error-resolver` | current experimental inventory | Experimental error-resolution/debugging skill. |
| `gh-fix-ci` | current experimental inventory | Experimental GitHub CI remediation skill. |
| `systematic-debugging` | current experimental inventory | Experimental systematic debugging skill. |
| `audiocraft-audio-generation` | current experimental inventory | Experimental AudioCraft generation skill. |
| `agents-crewai` | current experimental inventory | Experimental CrewAI agent workflow skill. |
| `api-integration-specialist` | current experimental inventory | Experimental API integration skill. |
| `dispatching-parallel-agents` | current experimental inventory | Experimental parallel-agent coordination skill. |
| `feature-design-assistant` | current experimental inventory | Experimental feature-design/product skill. |
| `meeting-insights-analyzer` | current experimental inventory | Experimental meeting-insight analysis skill. |
| `planning-with-files` | current experimental inventory | Experimental file-backed planning skill. |
| `product-manager-toolkit` | current experimental inventory | Experimental product-management toolkit. |
| `changelog-generator` | current experimental inventory | Experimental changelog-generation skill. |
| `file-organizer` | current experimental inventory | Experimental file-organization skill. |
| `finishing-a-development-branch` | current experimental inventory | Experimental branch-completion workflow. |
| `gh-address-comments` | current experimental inventory | Experimental GitHub review-comment workflow. |
| `git-commit-helper` | current experimental inventory | Experimental commit-preparation helper. |
| `using-git-worktrees` | current experimental inventory | Experimental git-worktree workflow. |

---

## Cross-repository findings

1. **Machine-readable catalogs need self-consistency validation.** LambdaTest has a real validator and `skills_index.json`, but the index currently has 71 rows for 70 unique identities because one migration entry is duplicated. A validator should assert uniqueness and declared-count equality.
2. **Support-path validation catches real packaging regressions.** `openclaw-marketing-skills` currently references at least two checked Google Ads support paths that are absent; `codex-skills` explicitly validates referenced local paths, a reusable pattern for other skill catalogs.
3. **Deterministic code is most valuable where judgment is not needed.** DailyPaper moves fetch/scoring/dedup to Python; WordPress uses deterministic project/block scanners; Spring Boot validates mirrored version trees; these reduce token use and drift.
4. **Freshness mechanisms should be executable and reviewable.** AWS Agent Skills has an actual scheduled upstream-doc checker and PR workflow, but its significance classification remains heuristic and should not be confused with semantic revalidation of every skill.
5. **Maturity/status needs to be explicit.** WordPress and Vadim expose in-progress or experimental status rather than presenting every package as equally mature; this is preferable to silent maturity ambiguity.

## Verification boundary

All ten repositories had identity, displayed stars, and actual repository contents inspected. Every repository had at least one current skill body or equivalent definition directly read, and available support/validation/eval surfaces were inspected where present. The 240 individual reports above are inventory-complete for the current maintained catalogs used in this batch, with duplicate identities reconciled rather than double-counted. No third-party runtime command or test suite was executed, so `structure-reviewed` is the completion status and `runtime_validation` remains `not_executed`.
