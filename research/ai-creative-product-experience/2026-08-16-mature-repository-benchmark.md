# Mature Repository Benchmark: Creative and Product UI

- Date: 2026-08-16
- Scope: 19 public GitHub repositories
- Research state: Complete with gaps
- Validation level: static repository/document inspection plus ImageGen pilot; no third-party CLI runtime execution

## Repository set

| Repository | Domain | Borrowed pattern | Decision |
|---|---|---|---|
| remotion-dev/remotion | Creative | deterministic React video rendering, frame-based motion | adopt as renderer option |
| remotion-dev/skills | Creative | progressive skill routing, topic rules, still-frame sanity checks | adopt workflow pattern |
| PixVerseAI/skills | Creative | decision trees, model constraints, JSON output schemas, exit codes | borrow adapter contract |
| eachlabs/skills | Creative | broad media workflows and provider aggregation | optional adapter only |
| harshkedia177/image-gen-plugin | Creative | prompt planning, self-review, post-processing, metadata sidecar | borrow image-run pattern |
| Sogni-AI/sogni-creative-agent-skill | Creative | durable runs, cost ceilings, cancellation/resume, replay records | borrow run-control ideas |
| memex-lab/product-launch-video-skill | Creative | brief-to-storyboard-to-Remotion launch workflow | borrow production stages |
| trunghaiy/appshot | Creative/Product | app scanning to store screenshots and preview video | borrow multi-format export |
| ybuild-ai/ai-game-art-pipeline-skill | Creative | runtime-oriented asset QA instead of stopping at pretty images | borrow asset acceptance model |
| SankaiAI/TwitCanva-Video-Workflow | Creative | node-based multi-model canvas and storyboard | reference only; too broad for core |
| google-labs-code/stitch-skills | Product | DESIGN.md extraction, design-system application, code/design round-trip | borrow contract boundaries |
| figma/mcp-server-guide | Product | node/frame grounding, component/variable extraction, Code Connect | optional external design adapter |
| superdesigndev/superdesign-skill | Product | codebase grounding, branchable visual drafts, design-system-first workflow | borrow ideation sequence |
| ConardLi/garden-skills | Product | context-first design engineering, v0 checkpoint, explicit critique dimensions | borrow review gates selectively |
| educlopez/ui-craft | Product | acceptance-oriented UI craft and intent routing | benchmark quality gate |
| vercel-labs/design-systems-to-agent-skills | Product | verified facts -> closed PRD -> generated Skill -> mechanical verification | adopt for Skill generation |
| shadcn-ui/ui | Product | open-code component distribution and composability | reference component model |
| ant-design/ant-design | Product | mature tokens, components, accessibility and enterprise patterns | target-project design-system source |
| storybookjs/storybook | Product | isolated component documentation and interaction/visual testing | adopt evidence source |

## Decision-critical evidence

- Remotion Skills explicitly routes into focused rule files and supports a one-frame render sanity check.
- PixVerse Skills documents decision trees, parameter constraints, structured JSON outputs, and exit-code handling.
- Stitch Skills separates design, build, and utility capabilities and treats DESIGN.md as a portable design-system artifact.
- Figma MCP exposes design context, variables, components, and Code Connect for code reuse, but rate limits and beta status make it an adapter rather than a core dependency.
- Vercel Labs' design-system pipeline persists each stage, extracts verified source facts, generates closed specifications, and mechanically verifies the resulting Skill.
- Storybook provides an isolated component environment suitable for implementation evidence.
- Ant Design and shadcn/ui are component-system references; they are not complete Product UI workflows.

## Claim-evidence ledger

| Claim | Status | Support | Limitation |
|---|---|---|---|
| Creative requires an independent implementation boundary | Inference | media-specific runtimes, adapters, rendering and QA patterns across the Creative repositories | requires a real repository pilot |
| Product UI should remain coupled to delivery artifacts and target code | Inference | Stitch, Figma, Vercel DS pipeline, Storybook and component-system evidence | must be tested in Forgeway and one product repo |
| UI Spec should be a contract rather than the whole workflow | Inference | separation of persisted artifacts and execution stages in mature pipelines | Forgeway schema compatibility not executed in this pass |
| One Style Contract can align media and UI direction | Verified for pilot | six generated outputs using a fixed palette/material/grid language | only visual consistency was tested |
| ImageGen output verifies implementability | Not verified | no coded prototype or browser comparison yet | requires selected direction and implementation |
| Provider aggregation should be core architecture | Rejected | EachLabs/Sogni/PixVerse show useful breadth but also provider, pricing and runtime coupling | keep behind optional adapters |

## Risks

- Several repositories are young even when their underlying tools are mature.
- README claims were not treated as runtime proof.
- External services may change models, pricing, authentication, and limits.
- Image generation can preserve coarse style while drifting in exact text, dates, icons, or component semantics.
- A Product UI Skill built before a real project pilot would encode assumptions instead of verified practice.

## Next validation

1. Select one of the three Product UI directions.
2. Create UI Spec and Style Contract fixtures.
3. Implement one screen in a real target project.
4. Run browser, responsive, accessibility, and visual-comparison checks.
5. Create `creative-workflows` only after the schemas and first deterministic pipeline are fixed.
