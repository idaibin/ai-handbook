# AI Creative & Product Experience Repository Review

- Research date: 2026-08-16 Asia/Tokyo
- Scope: public GitHub repositories containing reusable Agent Skills, design workflows, or executable creative-production pipelines
- Decision: establish a provider-neutral experimental workflow; do not install a broad bundle yet
- Completion: Complete with gaps

## Conclusion

The most reusable pattern is a staged workflow, not a single model or provider:

- Creative work benefits from structured brief/storyboard, provider execution, deterministic assembly, and post-render inspection.
- Product experience work benefits from current-code inspection, portable design-system extraction, branchable prototypes, implementation, and browser verification.
- Provider-specific generation repositories are useful adapters, but should remain optional until access, cost, licensing, current API behavior, and real output quality are verified.

## Candidate findings

| Candidate | Domain | Direct evidence inspected | Reusable value | Adoption status |
|---|---|---|---|---|
| superdesigndev/superdesign-skill | Product | README workflow: inspect codebase, extract/create design system, gather references, branch drafts, iterate | Design-system-first product UI workflow | Candidate for real UI trial |
| google-labs-code/stitch-skills | Product | README describes Agent Skills and plugins for Stitch MCP; issue evidence shows possible product/workflow drift | MCP-grounded design/build utilities | Candidate; version drift check required |
| figma/mcp-server-guide | Product | Official guide describes frame/node grounding and design-to-code MCP context | Precise design handoff context | Reference workflow, not standalone Skill |
| educlopez/ui-craft | Product | README describes routing by intent and a 10-item visual acceptance bar | Quality gate for AI-generated UI | Candidate; implementation evidence still needed |
| podo/design-agent-skills | Product | README describes catalogue of 151 installable skills | Discovery/index layer | Do not treat catalogue as one Skill |
| remotion-dev/remotion | Creative/Product | Official repository and docs describe React-based deterministic video rendering | Exact text, timing, layout, reusable compositions | Core deterministic renderer candidate |
| PixVerseAI/skills | Creative | README describes decision trees, flag tables, model constraints, JSON schemas, exit codes, examples | Strong machine-oriented provider adapter pattern | Candidate after CLI/runtime test |
| adamd9/skill-image-gen | Creative | README describes OpenAI/Gemini image generation plugin and onboarding | Simple provider adapter | Candidate; runtime/API verification required |
| harshkedia177/image-gen-plugin | Creative | README describes prompt strategy, model selection, self-review, post-processing, metadata sidecar | Complete image workflow pattern | Candidate for image trial |
| memex-lab/product-launch-video-skill | Creative | README describes brief/screenshots/assets to storyboarded Remotion launch video | Product media workflow | Candidate for launch-video trial |
| crafter-station/remotion-clone-video | Creative | README describes ffprobe/frame survey/storyboard/color sampling/code rebuild/render comparison | Reference-to-editable-video workflow | Candidate for reverse-engineering trial |
| eachlabs/skills | Creative | README describes multi-provider media workflows and Agent Skills structure | Broad provider aggregation | Optional only; cost and dependency surface are risks |

## Claim-evidence ledger

| ID | Claim | Status | Evidence | Limitation |
|---|---|---|---|---|
| C1 | Deterministic React video rendering is a useful foundation for exact product media | Verified | remotion-dev/remotion repository and docs | This verifies the rendering approach, not the quality of a specific generated video |
| C2 | PixVerse exposes machine-readable workflow guidance including schemas and exit codes | Verified | PixVerseAI/skills README | Current CLI behavior and model availability were not executed in this pass |
| C3 | Superdesign proposes a codebase-grounded, design-system-first UI workflow | Verified | superdesigndev/superdesign-skill README | Current service access and generated output quality were not independently tested |
| C4 | Figma MCP provides node/frame grounding for implementation workflows | Verified | figma/mcp-server-guide | Authentication and a real implementation run were not executed |
| C5 | Image generation Skills commonly combine prompting, generation, self-review, and post-processing | Verified | harshkedia177/image-gen-plugin README | README claims were not promoted to runtime verification |
| C6 | Provider-neutral workflows reduce lock-in and make evidence comparable | Inference | Cross-candidate comparison | Needs a real comparative run |
| C7 | The current repository landscape supports one shared workflow with optional adapters | Inference | Multiple repository structures and role differences | Requires adoption trial in the user's projects |
| C8 | Stitch skill assumptions may drift with product changes | Verified | google-labs-code/stitch-skills issue #40 | Issue content is evidence of reported drift, not proof every skill is currently broken |

## Risks and gaps

- GitHub search snippets and README content do not prove executable success.
- Many candidates depend on external APIs, credits, login, or changing model names.
- Current stars and activity are discovery signals, not quality evidence.
- No real generation or browser implementation run was executed in this research pass.
- The creative candidates differ substantially in licensing, provider coupling, and local reproducibility.

## Next validation

Run exactly two bounded pilots:

1. Creative: generate one product-launch asset using a storyboard, deterministic Remotion assembly, frame inspection, and Drive review package.
2. Product: apply the design-system-first workflow to one existing RustZen or Forgeway UI surface and verify the result in the browser.

Only after those pilots should a provider-specific Skill be copied into the permanent Skills repository.
