> Historical combined workflow. Superseded by the Createway Content Creation, Story
> Studio Media Production and Forgeway Product Delivery Maps plus
> `registry/routes.yaml`. Retained as experiment history; do not use it to assign a
> mixed-route Task.

# AI Creative & Product Experience Workflow

- Version: v0.1
- Status: Historical / superseded
- Effective date: 2026-08-16
- Scope: AI Creative & Media and AI Product Experience
- Authority: ai-handbook workflow; project-specific facts and current user instructions override this document.

## Purpose

Provide a provider-neutral route for turning an idea or product requirement into a verified creative asset or shippable product experience.

This workflow is not a model catalogue. It separates creative intent, executable production, artifact evidence, and review.

## Current ownership

Forgeway is the mandatory lifecycle coordinator for both domains. Product UI and Creative outputs are recorded as `urn:forgeway:audience-artifact:v1` records; provider-specific generators, renderers and editors are replaceable capabilities. GitHub stores contracts and metadata, while private/large binaries remain in Google Drive. A separate Creative repository and a standalone Product UI Skill are not approved by default.

## Domain routing

### Creative & Media

Use for image, video, audio, animation, poster, social content, storyboards, and product launch media.

Primary artifact chain:

Brief -> Script/Shotlist -> Storyboard -> Asset generation -> Assembly/editing -> Render -> Frame/audio inspection -> Export -> Archive

### Product Experience

Use for product strategy, UX, UI, design systems, prototypes, frontend implementation, AI interfaces, and visual/data presentation.

Primary artifact chain:

Intent -> Requirements -> Flow -> Design system -> Prototype/direction -> Implementation -> Browser/runtime verification -> Review -> Commit

## Shared contract

Every run must record:

- run_id;
- domain;
- input references;
- selected workflow;
- tools/providers and exact versions when relevant;
- generated or modified artifacts;
- verification level;
- evidence paths;
- unresolved issues;
- final disposition: accepted, revise, rejected, or not verified.

No generated image, screenshot, video, build, or README is sufficient proof by itself. Verification must match the claim.

## Creative workflow

1. Freeze the brief: audience, purpose, format, aspect ratio, duration, brand constraints, prohibited elements, and acceptance criteria.
2. Produce a structured shotlist or storyboard before generation when the output has multiple scenes, characters, or timed events.
3. Choose the smallest adequate production path:
   - deterministic code rendering for exact text, layout, timing, charts, and product demos;
   - generative image/video/audio for visual material that cannot be specified efficiently as code;
   - hybrid rendering when generated assets are inputs to a deterministic composition.
4. Save prompts, model/provider, parameters, source assets, and output metadata.
5. Render or export the result.
6. Inspect representative frames, dimensions, alpha/channel behavior, text, identity consistency, audio sync, and prohibited content.
7. Revise only against named failures.
8. Store final output and review package in Drive; store reusable workflow rules and distilled findings in ai-handbook.

Default quality gate:

- format and dimensions correct;
- required objects/counts correct;
- text and logos readable when required;
- no forbidden objects or accidental artifacts;
- continuity acceptable across a sequence;
- output opens and renders correctly;
- provenance and licensing state recorded.

## Product Experience workflow

1. Freeze product intent, users, core journey, constraints, and non-goals.
2. Inspect the current product before proposing a redesign: pages, tokens, components, interaction patterns, and implementation constraints.
3. Choose one design direction before expanding into variants.
4. Extract or define a portable design system: typography, color, spacing, radii, elevation, motion, component states, and accessibility rules.
5. Prototype the smallest critical flow.
6. Translate the accepted direction into implementation with existing project conventions.
7. Verify in the browser or target runtime at representative viewport sizes.
8. Review visual hierarchy, density, interaction states, responsive behavior, accessibility, and factual capability scope.
9. Record the changed files, runtime evidence, and remaining gaps.

Default quality gate:

- no invented product capability;
- primary journey is executable;
- visual hierarchy and density are intentional;
- states include loading, empty, error, success, and disabled where applicable;
- keyboard/focus/contrast behavior is checked;
- implementation matches the accepted design direction;
- browser/runtime readback is available.

## Provider and tool policy

A repository is eligible for adoption only if it has:

- an inspectable skill or workflow entrypoint;
- explicit inputs and outputs;
- executable commands or code paths;
- failure handling or verification guidance;
- a license and maintenance signal that are understood;
- no requirement to expose secrets in prompts or committed files.

High-level catalogues and model aggregators are discovery sources, not automatically reusable Skills.

## Current candidate roles

### Creative execution candidates

- Remotion official skills: deterministic React-based video rendering and implementation guidance.
- PixVerse Skills: structured CLI model selection, flags, JSON outputs, and composable media workflows.
- each::labs skills: broad provider-backed generation workflows; requires API and cost review.
- image-gen-plugin: prompt planning, self-review, post-processing, and metadata sidecars; requires verifying current model names and scripts.
- product-launch-video-skill: storyboarded product launch workflow with Remotion companion.
- remotion-clone-video: reverse-engineer a reference video into editable, verifiable Remotion code.

### Product experience candidates

- Superdesign skill: design-system extraction, reference gathering, draft branching, and iteration.
- Google Stitch skills: Stitch MCP-oriented design/build/utilities workflow; version drift must be checked before adoption.
- Figma MCP workflow skills: design node grounding and design-to-code handoff.
- UI Craft: acceptance-oriented design engineering and polish routing; inspect implementation before adopting its quality bar.
- design-agent-skills: catalogue/index only until individual skills are separately inspected.

## Non-goals

- Do not install every candidate.
- Do not treat generated visual quality claims as verified without output inspection.
- Do not replace existing project design systems automatically.
- Do not make provider-specific API calls part of the core workflow before cost, access, licensing, and reproducibility are verified.
- Do not promote this experimental workflow to a stable standard until it has been run on at least one real creative asset and one real product UI change.

## Forgeway handoff

Before generation, resolve the accepted Requirement plus Product UI authority or Creative brief. After generation, register exact hashes, dimensions/duration, provenance and opaque asset references. Apply class-specific review Gates and require publication readback. Product UI images remain candidates until interaction/browser evidence exists; event updates require factual sources and expiry.

## Promotion gate

Promote v0.1 to a stable workflow only after:

1. one image or video production run has a saved review package;
2. one product UI run has browser/runtime evidence;
3. failure recovery has been exercised;
4. the resulting method is shorter or more reliable than the current ad hoc process;
5. all provider-specific assumptions are isolated behind adapters or optional skills.
