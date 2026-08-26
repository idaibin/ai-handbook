# Story Studio — 班超 S1 Current Status

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `task_key`: `story-studio/banchao/s1-final-gate`
- `project_id`: `banchao`
- `status_revision`: `6`
- `as_of_utc`: `2026-08-26T06:26:11Z`
- `current_stage`: `S1_CANDIDATE_FINAL_GATE`
- `current_status`: `blocked_pending_reference_repair_5_and_visual_canon`
- `current_execution_unit`: `SEASON_ACTIVE_MEDIA_SPEC_AUDIT_DIRECT_READBACK_66_COMPLETED`
- `next_action`: `SEASON_ACTIVE_REFERENCE_REPAIR_EP03_B04_B08`
- `asset_policy`: `candidate_not_canonical`
- `canonical`: `0`
- `production_ready`: `0`

## Conclusion

EP01–EP24 narrative and 194-frame candidate coverage remain complete. Media source verification is now closed, but the season cannot advance because five EP03 mapping references point to another frame's bytes.

Current work is strictly:

```text
repair 5 EP03 references
→ rerun L1A selection integrity
→ close 6 blocked boundaries
→ promote 15 PASS_CANDIDATE boundaries
→ review 5 minimal world domains
→ rerun season final gate
```

Do not batch upscale source assets, regenerate whole episodes, expand the workflow, or resume historical EP01 G07 work.

## Verified current facts

| Item | Result |
|---|---:|
| Episodes | 24 |
| Logical keyframes | 194 |
| Unique `shot_id` / `frame_key` / Drive refs | 194 / 194 / 194 |
| Package-only refs | 0 |
| Direct current Drive readback | 194/194 |
| Decode / PNG / 8-bit RGB | 194/194 |
| Native `1920×1080` | 72 |
| Native `1672×941` | 122 |
| L1A reference-content identity | **189 PASS / 5 FAIL** |
| L1B canonical source media | **194/194 PASS** |
| L1C production derivatives | NOT_STARTED |
| `PASS_CANDIDATE` | 15 |
| `PASS_INTENTIONAL_CUT` | 2 |
| Remaining blocked boundaries | 6 |
| Canonical assets | 0 |
| Production-ready assets | 0 |

## Active Reference Blocker

| frame_key | Current ID contains | Correct Drive ID |
|---|---|---|
| `EP03-B04` | `EP03-B05` | `14Hc3VHi6r1BB9RuuvoNHY49vn5Rlf3jo` |
| `EP03-B05` | `EP03-B04` | `1Gbd1LFHwIO2AjaMR2yVNltc8Ac6PrUm5` |
| `EP03-B06` | `EP03-B07` | `1zu2BQrqnZ5iJwbdsUEj1OG1dxBZ6_nQ8` |
| `EP03-B07` | `EP03-B08` | `14sYpd4aR_S0QPnpeDqa_zgY_fExOUnrQ` |
| `EP03-B08` | `EP03-B06` | `1rGYabvWr1I-rU46uEvdRIRvfsC5s1GQg` |

All correct PNGs already exist and are `1920×1080 RGB`. Repair is mapping/manifest reassignment only; no image generation, resize or visual change.

## Media Contract State

Visual Canon Gate v1.1 separates:

```text
L1A selection integrity
L1B canonical source media integrity
L1C production derivative integrity
```

`1672×941` is an accepted native storyboard source. Future production derivatives are:

```text
122 → no-crop resize to 1920×1080 + embedded sRGB
72  → embedded-sRGB/profile normalization only
```

These are not current Visual Canon blockers and must not overwrite native canonical sources.

## Closed Boundary Decisions

| Boundary | Decision | Asset change |
|---|---|---|
| `EP01→EP02` | `PASS_INTENTIONAL_CUT` | none |
| `EP04→EP05` | `PASS_INTENTIONAL_CUT` | B01/B02 existing deterministic v2 exports remain active |

## Remaining Boundary Worklist

```text
EP05→EP06
EP11→EP12
EP15→EP16
EP16→EP17
EP20→EP21
EP23→EP24
```

After these six, 15 earlier `PASS_CANDIDATE` boundaries still require final promotion decisions.

## Minimal World-Foundation Blocker

Review only visible elements in the active set:

```text
architecture / space
costume / age / status silhouette
weapons / armour
horse tack / travel gear
route / region / direction
```

## Authority Order

1. `TASK — Story Studio — 班超 S1 FINAL GATE`;
2. this current status Markdown and JSON;
3. `season-candidate-manifest-current.json`;
4. `season-shot-mapping-current.json`;
5. `BANCHAO-S1-VISUAL-CANON-GATE-v1.1.md`;
6. direct-closure audit Markdown / JSON / CSV;
7. Character State / Location / Episode Foundation / treatment;
8. boundary and world evidence;
9. archived historical material.

## Evidence Identity

- Mapping: Drive `1U_pXUo1qD0D8rDELWvqUDUevpfoXClwa`, revision 4, SHA `78181c78e509a5615e900f7dc8518330eb8ddcad577fa80ad6182871f45ef5be`.
- Candidate manifest: Drive `1L-6SgE_3VINfxPuz6VQECJ_-pSDvY6WK`, revision 5.
- Audit Markdown: Drive `1UcImnpmnAcm2aaeQijU3TgS4mrLVB_aJ`.
- Audit JSON: Drive `1VMCQvoMGU_DRKojeQorKLPyTLjtMC9hz`, SHA `5fc75fed58ec94832c15742e52fd62acf45b7e418f874ff778ecd9674785e835`.
- Audit CSV: Drive `1kwkoB9Zgg4KfMGMuft-S-_GzcYtIqwFE`.
- Evidence ZIP: Drive `1TfaTt-aDSTQxN-19N9eiuWzOJFKYM5ea`.
- EXEC-0005 evidence: Drive `1kXOQX_EMLa4wkaf8N8aOdWAICj34R0ZZ`.
- Gate v1.1: Drive `1ZkJYbbHUxC5tDZEL9Kqsx7CoHpya9KiL`.
- GitHub audit correction: `41b35e999071c421327e25b3d1c7218e38c9391d`.
- GitHub gate current-result correction: `689772094e8e055387795433978b85a434e6bde7`.

## Next Action

```text
SEASON_ACTIVE_REFERENCE_REPAIR_EP03_B04_B08
```

After repair, rerun L1A for all 194 refs. Only a pass restores `VISUAL_CANON_BOUNDARY_REVIEW_03_EP05_TO_EP06`.
