# Visual Registry MVP 01

Status: draft baseline

## Goal

Validate a Visual Language Registry and Prompt Compiler before building any public prompt website.

## Principle

Durable assets:
- Visual Contract
- Style taxonomy
- Camera
- Lighting
- Material
- Composition

Derived assets:
- Provider prompts
- Model specific parameters

## Phase 1

- visual-contract.schema.json
- historical_han_realism
- saas_bento_dashboard
- minimal_tech_cover

## Validation

Input:
Visual Contract + Subject

Output:
- Gemini adapter prompt
- Flux adapter prompt
- Midjourney adapter prompt

Acceptance:
The generated prompts should preserve the same visual intent across providers.

## Scope Control

Not included:
- public website
- prompt marketplace
- user accounts
- large prompt collection

Next:
Implement compiler prototype and validate against Story Studio and UI Spec cases.
