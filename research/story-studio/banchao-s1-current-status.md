# Story Studio — 班超 S1 Current Status

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `task_key`: `story-studio/banchao/s1-final-gate`
- `project_id`: `banchao`
- `status_revision`: `5`
- `as_of_utc`: `2026-08-26T05:19:25Z`
- `current_stage`: `S1_CANDIDATE_FINAL_GATE`
- `current_status`: `blocked_pending_visual_canon`
- `current_execution_unit`: `SEASON_ACTIVE_MEDIA_SPEC_AUDIT_194_COMPLETED`
- `next_action`: `VISUAL_CANON_BOUNDARY_REVIEW_03_EP05_TO_EP06`
- `asset_policy`: `candidate_not_canonical`
- `canonical`: `0`
- `production_ready`: `0`

## Conclusion

EP01–EP24 narrative and candidate storyboard coverage are complete. The active selection remains 194 unique candidate frames. The full active-media specification audit is now closed, and the incorrect exact-1920 source requirement has been corrected as a contract defect.

Current active work is only:

```text
6 unresolved boundary reviews
+ final confirmation of 15 PASS_CANDIDATE boundaries
+ five minimal world-foundation domains
+ season final gate rerun
```

Do not batch upscale the source library, regenerate whole episodes, expand the workflow, or resume the historical EP01 G07 work order.

## Verified current facts

| Item | Result |
|---|---:|
| Episodes | 24 |
| Logical keyframes | 194 |
| Unique `shot_id` | 194/194 |
| Unique `frame_key` | 194/194 |
| Unique active Drive refs | 194/194 |
| Package-only refs | 0 |
| Media decode | 194/194 PASS |
| PNG 8-bit RGB | 194/194 |
| `1920×1080` | 72 |
| `1672×941` | 122 |
| Other dimensions | 0 |
| Explicit ICC / sRGB / gAMA tag | 0 |
| `PASS_CANDIDATE` | 15 |
| `PASS_INTENTIONAL_CUT` | 2 |
| `REVIEW_REQUIRED` | 4 |
| `REVIEW_REQUIRED_AFTER_REPAIR` | 2 |
| `MAPPING_BLOCKED` | 0 |
| Canonical assets | 0 |
| Production-ready assets | 0 |

## Active-media audit result

The audit covered all 194 current mapping rows.

```text
direct current Drive bytes: 43
authoritative package bytes bound to current IDs: 151
decode failures: 0
non-RGB files: 0
corrupt files: 0
```

Evidence:

- audit Markdown — Drive `1UcImnpmnAcm2aaeQijU3TgS4mrLVB_aJ`;
- row-level audit JSON — Drive `1VMCQvoMGU_DRKojeQorKLPyTLjtMC9hz`;
- row-level JSON SHA-256 — `6de85bac71b6802d5650ec430f065a5794d29c1c393469622ffda854f24aae18`;
- GitHub audit summary commit — `9b3bd46d89e79971234eb946997cac1e9a266c5b`.

The 151 package-bound rows were decoded from authoritative episode/chapter/repair/rebuild packages and bound to current Drive IDs through manifest Drive IDs/SHA-256 or Drive folder filename/size evidence. This closes media specification verification but does not replace pixel-level semantic review.

## Visual Canon media contract correction

The v1 rule requiring every canonical source to already be exact `1920×1080 RGB/sRGB` was invalid because it conflated source canon with production output normalization.

Visual Canon Gate v1.1 now separates:

```text
L1A — selection integrity
L1B — canonical source media integrity
L1C — production derivative integrity
```

Current S1 source classes accepted by L1B:

```text
1920×1080 / 8-bit RGB PNG
1672×941 / 8-bit RGB PNG
```

Both must decode, remain within `0.1%` of 16:9, and retain native dimensions/SHA/file ID. All 194 pass L1B.

Production derivatives remain separate and unexecuted:

```text
122: no-crop resize to 1920×1080 + embedded sRGB
72: embedded-sRGB profile normalization without resize
```

They are generated only when a shot enters production. They do not replace canonical source files merely to satisfy output dimensions.

Gate evidence:

- Drive gate v1.1 — `1ZkJYbbHUxC5tDZEL9Kqsx7CoHpya9KiL`;
- GitHub gate correction commit — `109d0c08c325e75546bb2eaf7027987f52290819`.

## Evidence defect resolved

The old EP10 manifest stores a malformed 65-character SHA for `EP10-B05`. Current Drive bytes equal package bytes and decode as `1672×941 RGB`.

Correct SHA-256:

```text
e1bbbb8d060aec9c88f17885b45cd923bbf6bc98c7e815784bf9d42d4b38c3e1
```

The image is unchanged. The historical manifest remains archived evidence; the current audit supplies the corrected identity.

## Closed Visual Canon decisions

| Boundary | Decision | Asset change |
|---|---|---|
| `EP01→EP02` | `PASS_INTENTIONAL_CUT` | none |
| `EP04→EP05` | `PASS_INTENTIONAL_CUT` | B01/B02 already changed to deterministic no-crop v2 exports |

Boundary 02 normalization remains valid, but v1.1 clarifies that normalization was not required to establish visual identity. Existing v2 files remain active to avoid unnecessary churn.

## Active blockers

| Boundary | Current state | Three-frame set |
|---|---|---|
| `EP05→EP06` | `REVIEW_REQUIRED` | `EP05-B08 → EP06-B01 → EP06-B02` |
| `EP11→EP12` | `REVIEW_REQUIRED` | `EP11-B08 → EP12-B01 → EP12-B02` |
| `EP15→EP16` | `REVIEW_REQUIRED` | `EP15-B08 → EP16-B01 → EP16-B02` |
| `EP16→EP17` | `REVIEW_REQUIRED` | `EP16-B08 → EP17-B01 → EP17-B02` |
| `EP20→EP21` | `REVIEW_REQUIRED_AFTER_REPAIR` | `EP20-B08 → EP21-B01 → EP21-B02` |
| `EP23→EP24` | `REVIEW_REQUIRED_AFTER_REPAIR` | `EP23-B08 → EP24-B01 → EP24-B02` |

After these six, the 15 existing `PASS_CANDIDATE` boundaries still require final promotion decisions.

## Minimal world-foundation blocker

Review only visible elements in the active 194-frame set:

```text
architecture / space
costume / age / status silhouette
weapons / armour
horse tack / travel gear
route / region / direction
```

No new global world encyclopedia is authorized.

## Current authority order

1. `TASK — Story Studio — 班超 S1 FINAL GATE`;
2. this current status Markdown and JSON;
3. `season-candidate-manifest-current.json` revision 5;
4. `season-shot-mapping-current.json` revision 4;
5. `BANCHAO-S1-VISUAL-CANON-GATE-v1.1.md`;
6. active-media audit Markdown and JSON;
7. Character State Bible / Location Bible / Episode Foundation Matrix / 24-episode treatment;
8. current boundary/world evidence;
9. archived historical documents and assets.

## Current evidence identity

- Task document: Drive `1CJEoK7VTDAOAMosU92NaDqruGKkaxuJOJ_kx8FiLVjw`
- Current status Markdown: Drive `1ZrtDrFQaizTUQgauNg9K78H7OVXgDYg4`
- Current status JSON: Drive `19CyI4SnxUKkfjwI3hut_1J19bhAfCZRw`
- Mapping: Drive `1U_pXUo1qD0D8rDELWvqUDUevpfoXClwa`
- Mapping SHA-256: `78181c78e509a5615e900f7dc8518330eb8ddcad577fa80ad6182871f45ef5be`
- Candidate manifest: Drive `1L-6SgE_3VINfxPuz6VQECJ_-pSDvY6WK`
- Candidate manifest revision 5 SHA-256: `e4732bd31527e762e390ecead8dff99ed0ef6662abcae0abfd042d210d02ac95`
- Visual Canon Gate v1.1: Drive `1ZkJYbbHUxC5tDZEL9Kqsx7CoHpya9KiL`
- Media audit Markdown: Drive `1UcImnpmnAcm2aaeQijU3TgS4mrLVB_aJ`
- Media audit JSON: Drive `1VMCQvoMGU_DRKojeQorKLPyTLjtMC9hz`

## Next action

```text
VISUAL_CANON_BOUNDARY_REVIEW_03_EP05_TO_EP06
EP05-B08 → EP06-B01 → EP06-B02
```

Do not regenerate a frame until a specific visual dimension returns `REPAIR_REQUIRED`.
