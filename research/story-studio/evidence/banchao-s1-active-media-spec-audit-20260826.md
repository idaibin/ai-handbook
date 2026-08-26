# 《班超》S1 活动媒体规格与引用完整性全量审计（Direct Closure）

- `audit_id`: `BANCHAO-S1-ACTIVE-MEDIA-SPEC-AUDIT-20260826-DIRECT-CLOSURE`
- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `executed_at_utc`: `2026-08-26T06:26:11Z`
- `scope`: `EP01–EP24 / 194 active mapped PNG refs`
- `contract`: `Visual Canon Gate v1.1`
- `audit_json_sha256`: `5fc75fed58ec94832c15742e52fd62acf45b7e418f874ff778ecd9674785e835`
- `result`: `FAIL_L1A_REFERENCE_CONTENT_IDENTITY_WITH_L1B_SOURCE_MEDIA_PASS`

## 结论

66/66 个此前仅由 package 绑定的待回读引用，现已逐个读取当前 direct Drive 原始字节。194 张活动源图的事实基线已经闭合：

```text
strict active-ref coverage: 194/194
decode / PNG / 8-bit RGB: 194/194
native 1920×1080: 72
native 1672×941: 122
L1A reference-content identity: 189 PASS / 5 FAIL
L1B canonical source media integrity: 194/194 PASS
L1C production derivatives: NOT_STARTED
```

`1672×941` 不再被当作 Visual Canon 源文件失败。按 v1.1，它是已批准的原生源规格之一。122 张无裁切 resize 与 72 张 sRGB profile 规范化只属于未来 `L1C` 生产派生，不应批量覆盖 canonical source。

当前真正阻断是 **5 个 EP03 mapping 引用指向了其他 frame 的字节**。因此此前的 `L1A selection integrity: PASS 194/194` 被新 direct 证据推翻。

## 5 个活动引用错位

| frame_key | 当前 Drive ID | 当前 ID 实际字节 | 正确 Drive ID |
|---|---|---|---|
| `EP03-B04` | `1Gbd1LFHwIO2AjaMR2yVNltc8Ac6PrUm5` | `EP03-B05` | `14Hc3VHi6r1BB9RuuvoNHY49vn5Rlf3jo` |
| `EP03-B05` | `14Hc3VHi6r1BB9RuuvoNHY49vn5Rlf3jo` | `EP03-B04` | `1Gbd1LFHwIO2AjaMR2yVNltc8Ac6PrUm5` |
| `EP03-B06` | `14sYpd4aR_S0QPnpeDqa_zgY_fExOUnrQ` | `EP03-B07` | `1zu2BQrqnZ5iJwbdsUEj1OG1dxBZ6_nQ8` |
| `EP03-B07` | `1rGYabvWr1I-rU46uEvdRIRvfsC5s1GQg` | `EP03-B08` | `14sYpd4aR_S0QPnpeDqa_zgY_fExOUnrQ` |
| `EP03-B08` | `1zu2BQrqnZ5iJwbdsUEj1OG1dxBZ6_nQ8` | `EP03-B06` | `1rGYabvWr1I-rU46uEvdRIRvfsC5s1GQg` |

这些正确 PNG 均已存在且为 `1920×1080 RGB`。修复类型是 `mapping_reference_only`：不生成图片、不 resize、不改变剧情或构图。

## 分层门禁结果

### L1A — Selection Integrity

```text
unique shot_id / frame_key / Drive ref structure: PASS
reference points to expected frame bytes: FAIL 189/194
```

### L1B — Canonical Source Media Integrity

```text
PNG decode: PASS 194/194
8-bit RGB: PASS 194/194
accepted native dimensions: PASS 194/194
explicit sRGB/ICC/gAMA tag: 0/194 → RGB_UNTAGGED
```

`RGB_UNTAGGED` 可作为 storyboard canonical source，但不能被声明为已完成 production sRGB 归一化。

### L1C — Production Derivative Integrity

```text
1672×941 source: 122 → future no-crop resize + embedded sRGB
1920×1080 source: 72 → future profile normalization only
current status: NOT_STARTED
```

仅当镜头进入 Production ShotKeyframe、Remotion 或视频生成时按需创建，并保留 source file ID / source SHA / derivative SHA / transform receipt。

## 其他证据缺陷

`EP10-B05` 的旧分集 manifest 保存了 65 位 malformed SHA。当前媒体字节可解码，正确 SHA-256 为：

```text
e1bbbb8d060aec9cc88f17885b45cd923bbf6bc98c7e815784bf9d42d4b38c3e1
```

历史 manifest 保留为证据；当前审计纠正身份，不修改媒体。

## 状态影响

```text
active asset changes: 0
mapping changes: 0
canonical: 0
production_ready: 0
next_action: SEASON_ACTIVE_REFERENCE_REPAIR_EP03_B04_B08
```

修复 5 个引用并重跑 L1A 后，才恢复：

```text
VISUAL_CANON_BOUNDARY_REVIEW_03_EP05_TO_EP06
```
