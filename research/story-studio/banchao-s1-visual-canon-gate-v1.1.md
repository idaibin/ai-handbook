# Story Studio — 班超 S1 Visual Canon Gate v1.1

- `gate_id`: `story-studio/banchao/s1-visual-canon-v1.1`
- `project_id`: `banchao`
- `effective_date`: `2026-08-26`
- `change_class`: `FAIL_CONTRACT_CORRECTION`
- `supersedes_section`: `v1 / L1 exact 1920×1080 RGB/sRGB source requirement`
- `evidence`: `BANCHAO-S1-ACTIVE-MEDIA-SPEC-AUDIT-20260826-DIRECT-CLOSURE`
- `audit_json_sha256`: `5fc75fed58ec94832c15742e52fd62acf45b7e418f874ff778ecd9674785e835`

## 1. Purpose

Visual Canon Gate decides whether current candidate storyboard keyframes are stable enough to become the season's approved visual reference set:

```text
candidate_not_canonical → canonical_storyboard_reference
```

It does not itself authorize `production-ready video`.

## 2. L1A — Selection Integrity

All 194 mapping rows must satisfy:

- unique `shot_id` and `frame_key`;
- one active Drive file ID per `frame_key`;
- `package-only=0`;
- mapping / manifest / file ID alignment;
- Drive bytes correspond to the expected frame content, not another frame;
- superseded files are excluded;
- native SHA-256 is relocatable.

Result values:

```text
PASS_SELECTION
FAIL_REFERENCE_CONTENT_IDENTITY
NOT_VERIFIED
```

## 3. L1B — Canonical Source Media Integrity

Accepted S1 source classes:

```yaml
accepted_dimensions:
  - 1920x1080
  - 1672x941
format: PNG
bit_depth: 8
color_type: 2
mode: RGB
aspect_ratio_relative_tolerance_from_16_9: 0.1%
```

Each source records Drive file ID, native dimensions, file size, SHA-256 and color-tag state.

```text
RGB_TAGGED_SRGB
RGB_UNTAGGED
OTHER_OR_INVALID
```

`RGB_UNTAGGED` may be canonical storyboard source, but is not production sRGB normalization.

## 4. L1C — Production Derivative Integrity

Created only when a shot enters production:

```yaml
dimensions: 1920x1080
format: PNG
bit_depth: 8
mode: RGB
icc_profile: embedded_sRGB
crop: forbidden_by_default
lineage:
  source_drive_file_id: required
  source_sha256: required
  derivative_sha256: required
  transform_receipt: required
```

- `1672×941`: no-crop resize + embedded sRGB.
- `1920×1080`: profile normalization only when needed.
- Derivatives must not silently overwrite canonical sources.

## 5. L2 — Frame Semantic Integrity

Each active frame must match its subject, treatment role, Character State, Location and prohibited-content rules.

Results:

```text
PASS_FRAME
PASS_INTENTIONAL_CHANGE
REPAIR_REQUIRED
NOT_VERIFIED
```

## 6. L3 — Boundary Continuity

Every adjacent episode boundary reviews exactly:

```text
previous exit → next entry → next second frame
```

Dimensions: identity, state, costume, space, light, direction, shot function and narrative cause.

Results:

```text
PASS_CANON
PASS_INTENTIONAL_CUT
REPAIR_REQUIRED
NOT_VERIFIED
```

## 7. L4 — Minimal World Foundation

Review only visible elements in the active 194-frame set:

1. architecture and spatial material;
2. costume, age and status silhouette;
3. weapons and armour;
4. horse tack and travel gear;
5. route, region and direction.

No new world encyclopedia is required.

## 8. Season Exit Criteria

Promotion requires:

- L1A `194/194 PASS_SELECTION`;
- L1B `194/194 PASS`;
- all 23 boundaries `PASS_CANON` or `PASS_INTENTIONAL_CUT`;
- five world domains have no unresolved `REPAIR_REQUIRED`;
- final decision and changed file IDs are recorded;
- Drive, GitHub and Registry agree.

Until then:

```text
canonical = 0
production_ready = 0
```

## 9. Current Gate Result

Local rerun on `2026-08-26T07:37:20Z`:

```text
L1A selection integrity: PASS_SELECTION 194/194
L1B source media integrity: PASS 194/194
L2 semantic aggregate: PASS
L3 boundary continuity: 23/23 PASS
L4 minimal world foundation: 5/5 PASS_WITH_BOUNDED_ADAPTATIONS
remote Drive/GitHub/Registry/Task agreement: PENDING
canonical: 0
production_ready: 0
```

All content and visual blockers are locally closed. Promotion is deferred only because Season Exit Criteria requires remote authority synchronization and readback.

## 10. Next Action

```text
REMOTE_AUTHORITY_SYNC_AND_READBACK_REVISION_14
→ PROMOTE_CANONICAL_STORYBOARD_REFERENCE_194
```
