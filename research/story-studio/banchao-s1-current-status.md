# Story Studio — 班超 S1 Current Status

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `task_key`: `story-studio/banchao/s1-final-gate`
- `project_id`: `banchao`
- `status_revision`: `4`
- `as_of_utc`: `2026-08-26T03:38:27Z`
- `current_stage`: `S1_CANDIDATE_FINAL_GATE`
- `current_status`: `blocked_pending_media_spec_audit_and_visual_canon`
- `asset_policy`: `candidate_not_canonical`
- `canonical`: `0`
- `production_ready`: `0`

## Conclusion

EP01–EP24 narrative and candidate storyboard coverage are complete. The season retains a unique 194-frame candidate mapping and continuous storyboard animatic, but it is not approved as Visual Canon and is not production-ready.

Current work is restricted to:

```text
full active-media specification audit for 194 mapped PNG refs
→ Visual Canon closure for 6 remaining blocked boundaries
→ final confirmation of 15 PASS_CANDIDATE boundaries
→ minimal world-foundation review
→ season final gate rerun
```

Do not expand the workflow, create new episodes, regenerate the whole season, or resume the historical EP01 G07 work order.

## Verified structural facts

| Item | Result |
|---|---:|
| Episodes | 24 |
| Logical keyframes | 194 |
| Unique `shot_id` | 194/194 |
| Unique `frame_key` | 194/194 |
| Unique active Drive refs | 194/194 |
| Package-only refs | 0 |
| Boundary records | 23 |
| `PASS_CANDIDATE` | 15 |
| `PASS_INTENTIONAL_CUT` | 2 |
| `REVIEW_REQUIRED` | 4 |
| `REVIEW_REQUIRED_AFTER_REPAIR` | 2 |
| `MAPPING_BLOCKED` | 0 |
| Canonical assets | 0 |
| Production-ready assets | 0 |

Structural validation confirms mapping/manifest SHA alignment, episode counts, Character State and Location resolution, Episode Foundation alignment, and unique active refs.

## Mechanical validation correction

The previous global statement that all 194 active PNGs were already verified as `1920×1080 RGB/sRGB` is invalid.

During boundary 02, the actual active files were read as:

```text
EP05-B01: 1672×941 RGB
EP05-B02: 1672×941 RGB
```

Both were deterministically re-exported with RGB `LANCZOS` resize, no crop and no content edits:

```text
EP05-B01-v2: Drive 1JiXt-mZuFdO93jsBNiTNrbufeqeRJt0q
SHA-256 383052ab14c4004ffa9de337c4cdc9a4ee095115f7cd12e4d4d63842d0a8fbf0

EP05-B02-v2: Drive 1sRh1aG_fI55CsFHvljoIYcyiIq6MN7Wj
SHA-256 959c3ce1c8aa87b9e0672dd0d334a27bb84d6ac41e1cb0e8f1426f262fe408bf
```

The original files were renamed and moved to `90-archive/boundary-02-ep04-ep05-spec-repair`.

Current mechanical result:

```text
mapping / ID / reference structure: PASS
full 194-file decode / dimensions / color-mode audit: NOT_VERIFIED_FULL_SET
```

## Closed Visual Canon decisions

| Boundary | Decision | Evidence | Asset change |
|---|---|---|---|
| `EP01→EP02` | `PASS_INTENTIONAL_CUT` | Drive decision `1RlBfSCU94SMiWbcRnzvGuMxq2OVVS1bm` | none |
| `EP04→EP05` | `PASS_INTENTIONAL_CUT` | Drive decision `14xstpvogW9evDfN7tRpnAwxdJ7LgF4l-`; contact sheet `1NGgu8JssyGS6VtjbMAD9KKtA7vRNo0ie`; face comparison `1bJVmutgTEaxgL6tycKQJGHX9KWjlgCjZ` | B01/B02 replaced by deterministic 1920×1080 v2 exports |

`EP04-B08` closes the Shanshan mission. `EP05-B01` intentionally resets into a Khotan court establishing shot, and `EP05-B02` remains in that court while hospitality recedes. Young age, clean-shaven face, black high topknot and restrained dark layered clothing remain compatible. Court architecture and ornate local dress remain bounded adaptations pending L4 review.

## Remaining blocked boundaries

```text
EP05→EP06
EP11→EP12
EP15→EP16
EP16→EP17
EP20→EP21
EP23→EP24
```

The remaining 15 `PASS_CANDIDATE` boundaries also require final promotion to `PASS_CANON` or `PASS_INTENTIONAL_CUT` before season release.

## Current authority

1. Drive Task `1CJEoK7VTDAOAMosU92NaDqruGKkaxuJOJ_kx8FiLVjw`;
2. Drive current status Markdown `1ZrtDrFQaizTUQgauNg9K78H7OVXgDYg4` and JSON `19CyI4SnxUKkfjwI3hut_1J19bhAfCZRw`;
3. candidate manifest `1L-6SgE_3VINfxPuz6VQECJ_-pSDvY6WK`;
4. shot mapping `1U_pXUo1qD0D8rDELWvqUDUevpfoXClwa`;
5. Visual Canon Gate v1 `1ZkJYbbHUxC5tDZEL9Kqsx7CoHpya9KiL`;
6. Character State, Location, Episode Foundation and 24-episode treatment contracts;
7. current decision and audit evidence;
8. archived history.

Current evidence hashes:

```text
mapping revision: 4
mapping SHA-256: 78181c78e509a5615e900f7dc8518330eb8ddcad577fa80ad6182871f45ef5be
manifest revision: 4
manifest SHA-256: 548c2e695be07b6e4230eba9fb5615f849897d1479abcde18a288ea2f4c870fb
```

## Next action

Execute `SEASON_ACTIVE_MEDIA_SPEC_AUDIT_194`.

This gate unit takes priority over `VISUAL_CANON_BOUNDARY_REVIEW_03_EP05_TO_EP06`, because new evidence invalidated the previous season-wide media-spec claim. Do not promote another boundary until active-file decode, dimensions and color-mode status are truthful.