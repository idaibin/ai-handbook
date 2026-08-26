# Story Studio — 班超 S1 Visual Canon Gate v1

- `gate_id`: `story-studio/banchao/s1-visual-canon-v1`
- `project_id`: `banchao`
- `scope`: `EP01–EP24 / 194 candidate storyboard keyframes / 23 episode boundaries`
- `status`: `active`
- `effective_date`: `2026-08-26`
- `supersedes`: prior informal uses of “VisualCanon approval” without a standalone acceptance contract

## 1. Purpose

Visual Canon Gate decides whether the current **candidate storyboard keyframes** are stable enough to become the season's approved visual reference set.

It answers only this question:

> Are character identity/state, scene/world rules, shot function, and active asset selection consistent enough that downstream production may rely on them without silently changing the story or visual identity?

A pass allows:

```text
candidate_not_canonical → canonical_storyboard_reference
```

It does **not** by itself allow:

```text
canonical_storyboard_reference → production-ready video
```

Video production still requires shot-level `Motion Contract`, rights/provider checks, audio/editing plans, and production validation.

## 2. Non-goals

The gate is not:

- a general “looks good” or style preference review;
- a demand for perfect visual similarity between every adjacent frame;
- a complete archaeology or costume encyclopedia;
- proof that the animatic is a finished episode or season video;
- permission to overwrite or delete historical evidence;
- a reason to regenerate an entire episode when one boundary frame fails.

## 3. Authority inputs

The gate must read the following current sources:

1. `season-shot-mapping-current.json` — unique active selection and shot function;
2. `season-candidate-manifest-current.json` — frozen candidate counts and hashes;
3. Character State Bible — Drive `19OF4M-aOYq7BWf31B30pVP75hjTyckNq`;
4. Location Bible — Drive `10XNmn2diswGMbSbMSXHhcVFwl2siP6mY`;
5. Episode Foundation Matrix — Drive `1rk-Hk4CqTfedYKmMVMJA_GO-VN7ohOrR`;
6. 24-episode treatment — Drive `1wlDngVD09q7sbL4IPtAKMiwaV-a9HP88`;
7. current consistency/audit evidence — Drive `1j575_IaA2ZRWxgmtqlINYetOk_VsqgS7`, `1ndRbPCilP8XzmyShSiWIfmcs443zFNx_`;
8. the actual active PNG bytes referenced by the mapping.

Old EP01 G07 status, old r24 progress files, old manifests, and archived candidates are evidence only and cannot override this order.

## 4. Validation layers

### L1 — Mechanical integrity

For all 194 mapping rows:

- one unique `shot_id`;
- one unique `frame_key`;
- one active Drive asset reference;
- no package-only reference;
- PNG can be decoded;
- expected active format is `1920×1080`, RGB/sRGB;
- mapping, manifest, and file reference agree;
- superseded versions are excluded from the active entry.

Result values:

```text
PASS_MECHANICAL
FAIL_MECHANICAL
NOT_VERIFIED
```

### L2 — Frame semantic integrity

Each active frame must satisfy:

- the depicted primary subject matches `shot_role` / subject override;
- the image performs the narrative function assigned by the treatment and mapping;
- character age, face, hair, facial hair, costume, body wear, and props fit the assigned Character State;
- scene, architecture, palette, and staging fit the assigned Location IDs;
- no modern objects, unapproved fantasy forms, readable/pseudo-readable text, arrows, prompt labels, or baked-in review annotations;
- violence is narratively legible without relying on graphic imagery;
- intentional subject or location changes are recorded rather than disguised as continuity.

Result values:

```text
PASS_FRAME
PASS_INTENTIONAL_CHANGE
REPAIR_REQUIRED
NOT_VERIFIED
```

### L3 — Boundary continuity

Every adjacent episode boundary uses exactly three frames:

```text
previous episode exit
→ next episode entry
→ next episode second frame
```

Review dimensions:

| Dimension | Pass condition |
|---|---|
| Identity | Same named character remains recognisable; a different subject is explicitly mapped |
| State | Age, fatigue, wounds, hair, costume, authority and props follow the Character State progression |
| Space | Location change is intentional; screen direction, light and establishing responsibility are explainable |
| Shot function | Exit, establishing/opening and follow-up frames perform their mapped roles |
| Narrative cause | The cut preserves the treatment’s cause-and-effect rather than merely looking similar |

A boundary passes when every difference is either continuous or explicitly documented as an intentional cut.

Result values:

```text
PASS_CANON
PASS_INTENTIONAL_CUT
REPAIR_REQUIRED
NOT_VERIFIED
```

### L4 — Minimal world-foundation subset

Only elements actually visible in the active 194-frame set are reviewed:

1. architecture and spatial material;
2. costume, age and status silhouette;
3. weapons and armour;
4. horse tack and travel gear;
5. route, region and geographic direction.

The review must distinguish:

- `SUPPORTED`: supported by current source/contract;
- `BOUNDED_ADAPTATION`: a controlled dramatic/design choice;
- `REPAIR_REQUIRED`: anachronistic, internally contradictory, modern/fantasy, or misleading;
- `NOT_VERIFIED`: insufficient source or unreadable asset evidence.

No new global world encyclopedia is required.

## 5. Boundary review procedure

For each blocked boundary:

1. fetch the three exact PNGs from `season-shot-mapping-current.json`;
2. verify file ID, decode, dimensions and colour mode;
3. place the three images side by side without altering the images;
4. record `identity / state / costume / space / light / direction / shot function / narrative cause`;
5. assign one boundary decision;
6. if failed, repair only the smallest failing frame;
7. move the superseded file to archive and update the same `frame_key` mapping;
8. repeat L1–L3 for that boundary.

A written decision must contain:

```yaml
boundary:
frames:
decision:
dimension_results:
evidence:
repair_required:
active_asset_changes:
reviewer:
reviewed_at_utc:
```

## 6. Season exit criteria

The season may be promoted to `canonical_storyboard_reference` only when:

- L1 passes for `194/194`;
- all `23/23` episode boundaries are `PASS_CANON` or `PASS_INTENTIONAL_CUT`;
- the five minimal world domains have no unresolved `REPAIR_REQUIRED`;
- every active `frame_key` points to one active file;
- manifest SHA and mapping SHA match;
- the final gate decision and changed file IDs are recorded;
- Drive, GitHub, and Registry report the same state.

Until then:

```text
canonical = 0
production_ready = 0
```

## 7. Current gate state

Mechanical structure has been revalidated on `2026-08-26T01:13:39Z`:

```text
mapping rows: 194
unique shot IDs: 194
unique frame keys: 194
unique Drive asset refs: 194
episode counts: EP01=10; EP02–EP24=8 each
character-state references: resolved
location references: resolved
episode-foundation alignment: resolved
```

This is a structural pass only. The eight outstanding boundary decisions and minimal world subset remain visually unapproved.
