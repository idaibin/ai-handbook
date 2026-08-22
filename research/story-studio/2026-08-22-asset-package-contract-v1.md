# Story Studio Asset Package Contract v1

## Decision

`MVP_ASSET_LOCK_01` no longer produces a combined asset board as a canonical asset.

The board is a derived review artifact only.

Canonical production assets must be stored independently.

## Asset Model

```
Asset Package
├── media/
├── specification/
├── continuity/
├── generation/
└── evidence/
```

## Required Asset Types

### Character

Example:

`CHAR_BAN_CHAO_STATE_01_LUOYANG_SCRIBE`

Contains:

- identity references
- neutral turnaround
- face references
- costume rules
- continuity constraints
- generation attempts
- evidence

### Prop

Example:

`PROP_HERO_BRUSH`

Contains:

- hero view
- detail views
- dimensions
- material specification
- usage constraints

### Location

Example:

`LOC_LUOYANG_COPYING_COMPOSITE_SET`

Contains:

- master views
- camera references
- lighting rules
- layout constraints

## Relationship Layer

Composite groups do not own media.

Example:

`GROUP_LUOYANG_WRITING_SYSTEM`

Only stores:

- asset references
- scale relationship
- continuity rules
- usage constraints

## Shot Contract

Shots reference assets instead of embedding generated images.

```
Shot
 ├── requires Character
 ├── requires Props
 ├── requires Location
 └── defines Camera / Lighting / Motion
```

## State Rules

```
candidate
→ internal_candidate
→ canonical
→ production_ready
```

A review board, collage, or dashboard cannot become canonical.

## MVP Validation

Verify:

1. Asset can be reused by multiple shots.
2. Asset version can be resolved deterministically.
3. Continuity constraints can be checked before generation.
4. Evidence can trace every generated output.
