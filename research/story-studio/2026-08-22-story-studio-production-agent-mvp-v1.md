# Story Studio Production Agent MVP v1

## Status

Design baseline created. This document defines the next validation unit, not a completion claim.

## Objective

Validate whether Story Studio can execute a repeatable production unit:

Episode Contract
→ Shot Plan
→ Asset Requirement
→ Asset Lock
→ Generation Attempt
→ Review
→ Evidence Update

## Scope

Project: banchao
Episode: EP01
Validation Unit: STORY_STUDIO_PRODUCTION_AGENT_MVP_01

Assets:

- CHAR_BAN_CHAO_STATE_01_LUOYANG_SCRIBE
- PROP_HERO_BRUSH
- PROP_WRITING_SURFACE
- GROUP_LUOYANG_WRITING_SYSTEM

## Rules

- Agent may generate plans and execution proposals.
- Canonical assets and production state require evidence-based updates.
- Asset existence does not equal approved production status.
- Dailies/review results do not automatically upgrade Canon or Production Ready.

## Acceptance Criteria

1. Asset requirements can be derived from a shot contract.
2. Assets have stable identifiers and continuity relationships.
3. Generation attempts produce traceable evidence.
4. Review failures can be classified.
5. A passing unit can authorize the next execution unit.

## Failure Classification

- IMPLEMENTATION_FAILURE
- CONTRACT_FAILURE
- DEPENDENCY_FAILURE
- ARCHITECTURE_CHANGE_REQUIRED

## Next Action

Execute MVP asset lock validation against the current EP01 G07 baseline.
