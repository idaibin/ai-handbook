# Story Studio MVP_ASSET_LOCK_01 Asset State Update

Date: 2026-08-22

## Decision

MVP_ASSET_LOCK_01 is corrected from composite board generation to independent Asset Package validation.

The previous dashboard/board images are classified as:

- artifact_type: derived_review_artifact
- canonical_asset: false

They must not be used as production assets, model references, or shot inputs.

## Canonical Asset Units

```text
CHAR_BAN_CHAO_STATE_01_LUOYANG_SCRIBE
PROP_HERO_BRUSH
PROP_WRITING_SURFACE
LOC_LUOYANG_COPYING_COMPOSITE_SET
GROUP_LUOYANG_WRITING_SYSTEM
```

## Asset Package Contract

Each asset package requires:

- canonical media files
- specification
- continuity rules
- generation metadata
- evidence manifest
- status lifecycle

## Group Rule

GROUP_LUOYANG_WRITING_SYSTEM stores relationships only:

- asset references
- scale relationships
- usage constraints
- continuity rules

It does not replace individual assets.

## MVP Execution Order

1. Character Asset Package
2. Hero Brush Asset Package
3. Writing Surface Asset Package
4. Writing System relationship validation
5. Shot reference resolution test
6. Evidence manifest update

## Current Status

Architecture correction completed.

Next execution must create or validate independent asset packages. No composite asset board may become canonical.
