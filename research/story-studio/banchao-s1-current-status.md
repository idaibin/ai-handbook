# Story Studio — 班超 S1 Current Status

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `task_key`: `story-studio/banchao/s1-final-gate`
- `project_id`: `banchao`
- `status_revision`: `2`
- `as_of_utc`: `2026-08-26T01:26:00Z`
- `current_stage`: `S1_CANDIDATE_FINAL_GATE`
- `current_status`: `blocked_pending_visual_canon`
- `asset_policy`: `candidate_not_canonical`
- `canonical`: `0`
- `production_ready`: `0`

## Conclusion

EP01–EP24 narrative and candidate storyboard coverage are complete. The season has a frozen, unique 194-frame candidate selection and a continuous storyboard animatic, but it is not approved as visual canon and is not production-ready.

The only active work now is:

```text
Visual Canon closure for 8 boundaries
+ minimal world-foundation review
+ season final gate rerun
```

Do not expand the workflow, create new episodes, regenerate the whole season, or resume the historical EP01 G07 work order from this task.

## Verified current facts

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
| `REVIEW_REQUIRED` | 6 |
| `REVIEW_REQUIRED_AFTER_REPAIR` | 2 |
| `MAPPING_BLOCKED` | 0 |
| Storyboard animatic | available, about 8m58s, no audio |
| Canonical assets | 0 |
| Production-ready assets | 0 |

Mechanical validation performed on `2026-08-26T01:14:34Z` also confirmed:

- mapping SHA matches the candidate manifest;
- EP01 has 10 frames and EP02–EP24 have 8 frames each;
- all mapped Character State IDs resolve to the Character State Bible;
- all mapped Location IDs resolve to the Location Bible;
- all row state/location assignments are within the Episode Foundation Matrix;
- no duplicate active Drive asset reference exists in the mapping.

This round did not re-open and visually approve all 194 PNG pixels. Visual approval remains a separate gate.

## Active blockers

| Boundary | Current state | Three-frame set | What remains |
|---|---|---|---|
| `EP01→EP02` | `REVIEW_REQUIRED` | `EP01-F10` → `EP02-B01` → `EP02-B02` | 青年班超锚点可接；洛阳到早期边地的状态切换需按入口/出口帧确认 |
| `EP04→EP05` | `REVIEW_REQUIRED` | `EP04-B08` → `EP05-B01` → `EP05-B02` | 发髻/脸型存在漂移；鄯善到于阗王庭需检查空间锚点 |
| `EP05→EP06` | `REVIEW_REQUIRED` | `EP05-B08` → `EP06-B01` → `EP06-B02` | 年龄/脸部比例轻微跳变；绿洲到疏勒接近空间需统一 |
| `EP11→EP12` | `REVIEW_REQUIRED` | `EP11-B08` → `EP12-B01` → `EP12-B02` | 联盟攻城到边地上疏是合理转场，但需确认状态与空间方向 |
| `EP15→EP16` | `REVIEW_REQUIRED` | `EP15-B08` → `EP16-B01` → `EP16-B02` | EP16-B01/B02 已为独立 1920×1080 RGB PNG；仍需复核人物状态、外交空间与入口镜头职责 |
| `EP16→EP17` | `REVIEW_REQUIRED` | `EP16-B08` → `EP17-B01` → `EP17-B02` | 联盟策略到诈降酒局，需确认王忠开放钩子与人物状态 |
| `EP20→EP21` | `REVIEW_REQUIRED_AFTER_REPAIR` | `EP20-B08` → `EP21-B01` → `EP21-B02` | EP21-B01 v2 已沿用 EP20 脸型/成熟度并补入秋季军装；仍需与 EP20-B08、EP21-B02 并列复核 |
| `EP23→EP24` | `REVIEW_REQUIRED_AFTER_REPAIR` | `EP23-B08` → `EP24-B01` → `EP24-B02` | EP24-B01 v3 已完成可解码的 1920×1080 RGB 重导出；EP23-B08→EP24-B01 角色连续，B01→B02 为班超→班昭的有意主体切换；保留候选级复核，不提升 canonical |

The EP15→EP16 reason in the prior mapping was stale because it still said `package-only`; EP16 is now eight independent direct PNGs. The current mapping revision removes that obsolete statement.

## Minimal world-foundation blocker

The current Character State, Location, and Episode Foundation contracts deliberately leave material culture research-gated. The final gate therefore reviews only visible items in the active 194-frame set:

```text
architecture / space
costume / age / status silhouette
weapons / armour
horse tack / travel gear
route / region / direction
```

This is a bounded verification task, not a new world-building project.

## Current authority order

1. `TASK — Story Studio — 班超 S1 FINAL GATE` — Drive `1CJEoK7VTDAOAMosU92NaDqruGKkaxuJOJ_kx8FiLVjw`;
2. this current status Markdown and JSON;
3. `season-candidate-manifest-current.json`;
4. `season-shot-mapping-current.json`;
5. `banchao-s1-visual-canon-gate-v1.md`;
6. active source contracts:
   - Character State Bible — Drive `19OF4M-aOYq7BWf31B30pVP75hjTyckNq`;
   - Location Bible — Drive `10XNmn2diswGMbSbMSXHhcVFwl2siP6mY`;
   - Episode Foundation Matrix — Drive `1rk-Hk4CqTfedYKmMVMJA_GO-VN7ohOrR`;
   - 24-episode treatment — Drive `1wlDngVD09q7sbL4IPtAKMiwaV-a9HP88`;
7. current gate evidence and consistency matrix;
8. archived progress, reviews, packages, and historical task documents.

## Drive structure after convergence

```text
banchao/
└── S1 — EP01-EP24 — candidate-final-gate/
    ├── 00-current/
    ├── 10-candidate-overrides-and-preview/
    ├── 20-evidence/
    └── 90-archive/
```

- S1 was moved out of `EP01-preproduction-candidates-2026-08-18`.
- Old files were moved, not deleted.
- Current mapping, manifest, gate, consistency matrix and delivery summary are under `00-current`.
- Reviews and repair evidence are under `20-evidence`.
- r24 progress, old gates/manifests/reviews/packages and superseded assets are under `90-archive`.

## Conflict resolution

| Previous source/state | Resolution |
|---|---|
| Historical `TASK — Story Studio — 班超 EP01` / G07 `2/10` | Remains historical EP01 evidence; it is not the S1 execution entry |
| GitHub 10-second 《投笔》 MVP | Retained only as a future video-chain test slice; it does not represent current S1 scope |
| Registry “EP01–EP21 reviewed” | Updated to EP01–EP24 / 194-frame final gate and a dedicated Task row |
| r24 progress and older continuity gate | Archived and removed from active authority |
| “VisualCanon approval” without a standalone definition | Replaced by `banchao-s1-visual-canon-gate-v1.md` |
| EP15→EP16 `package-only` reason | Corrected; EP16 direct PNGs are present |

## Current evidence identity

- Drive Task document: `1CJEoK7VTDAOAMosU92NaDqruGKkaxuJOJ_kx8FiLVjw`
- Drive current status Markdown: `1ZrtDrFQaizTUQgauNg9K78H7OVXgDYg4`
- Drive current status JSON: `19CyI4SnxUKkfjwI3hut_1J19bhAfCZRw`
- Drive Visual Canon Gate v1: `1ZkJYbbHUxC5tDZEL9Kqsx7CoHpya9KiL`
- Registry spreadsheet: `1mftSIZi57b4h4ya1lsiJwRkRcJnud2yyGQOPXQetUYY`
- Drive S1 root: `1jiJQ6s4PYMxsmR5Fap88JHrsfa4vclJY`
- Drive current folder: `1-o5w8lmP3P5800EV1IM58lpvLZAYNAeY`
- Drive mapping file: `1U_pXUo1qD0D8rDELWvqUDUevpfoXClwa`
- mapping SHA-256: `f339b2ef41fd524b345d6ff7fe72774470fd3cbff4b9224cfc44d2ab8a99b48d`
- Drive candidate manifest: `1L-6SgE_3VINfxPuz6VQECJ_-pSDvY6WK`
- candidate manifest SHA-256: `227b16d1292bbbddea850ddeb07618f39f1320eb042bff1b55719914e3ac333d`
- Drive consistency matrix: `1j575_IaA2ZRWxgmtqlINYetOk_VsqgS7`
- Drive latest gate snapshot: `1ndRbPCilP8XzmyShSiWIfmcs443zFNx_`
- Drive animatic: `1o8rH2Gvp5ofRil15osEd_JOPYZzNQwV0`
- GitHub baseline read before convergence: `idaibin/ai-handbook@eb41bd74ec4f0e9122296f227cbb57b30df26602`

## Next action

Execute the eight three-frame Visual Canon reviews in the worklist order. Do not regenerate any frame until a specific review dimension returns `REPAIR_REQUIRED`. After those decisions, review the five minimal world domains and rerun the season final gate.
