# Story Studio — 班超 S1 Visual Canon Gate v1.1 媒体合同修正

- `gate_id`: `story-studio/banchao/s1-visual-canon-v1.1`
- `project_id`: `banchao`
- `effective_date`: `2026-08-26`
- `change_class`: `FAIL_CONTRACT_CORRECTION`
- `supersedes_section`: `v1 / L1 exact 1920×1080 RGB/sRGB source requirement`
- `evidence`: `BANCHAO-S1-ACTIVE-MEDIA-SPEC-AUDIT-20260826`
- `audit_json_sha256`: `6de85bac71b6802d5650ec430f065a5794d29c1c393469622ffda854f24aae18`

## 1. 修正原因

Visual Canon Gate v1 把以下两件事混为一体：

```text
A. canonical storyboard source 是否稳定可信
B. 下游生产输入是否已归一化为 1920×1080 sRGB
```

全量审计证明当前 194 张活动源图均可解码、均为 8-bit RGB PNG，但存在两个真实原生规格：

```text
1920×1080：72
1672×941：122
```

`1672×941` 与 16:9 的相对偏差约为 `0.053135%`。单纯无裁切放大不会改善身份、剧情、构图或世界一致性，因此不能把源图未放大视为 Visual Canon 失败。

## 2. 修正后的 L1

### L1A — Selection Integrity

全部 194 个 mapping rows 必须满足：

- `shot_id` 唯一；
- `frame_key` 唯一；
- 一个活动 Drive file ID；
- `package-only=0`；
- mapping、manifest、file ID 对齐；
- superseded 文件不在活动入口；
- 原生 SHA-256 可重新定位。

### L1B — Canonical Source Media Integrity

当前《班超》S1 源图允许的规格集合：

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

每张源图必须记录：

```text
Drive file ID
native dimensions
file size
SHA-256
color tag status
evidence source
```

颜色标记值：

```text
RGB_TAGGED_SRGB
RGB_UNTAGGED
OTHER_OR_INVALID
```

`RGB_UNTAGGED` 允许作为 canonical storyboard source，但不得直接被声明为已完成 sRGB 生产归一化。

### L1C — Production Derivative Integrity

当某个镜头进入 Production ShotKeyframe、Remotion 或视频生成时，才创建确定性 production derivative：

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

规则：

- 1672×941 源图：无裁切 resize + 嵌入 sRGB。
- 1920×1080 源图：不改变构图，只进行必要的 profile 规范化。
- 派生文件不得静默覆盖 canonical source。
- canonical source 的身份由 Visual Canon 决定，不由像素放大决定。

## 3. 本轮结果

```text
L1A selection integrity: PASS 194/194
L1B source media integrity: PASS 194/194
L1C production derivatives: NOT_STARTED
```

分布：

```text
1920×1080 / RGB_8BIT_UNTAGGED: 72
1672×941 / RGB_8BIT_UNTAGGED: 122
corrupt: 0
non-RGB: 0
explicit sRGB-tagged: 0
```

## 4. 证据缺陷处理

`EP10-B05` 的旧分集 manifest 写入了 65 位 malformed SHA-256。当前 Drive 原始字节与 package 字节一致，正确 SHA-256 为：

```text
e1bbbb8d060aec9c88f17885b45cd923bbf6bc98c7e815784bf9d42d4b38c3e1
```

处理方式：

- 不替换活动图像；
- 在当前 audit 中覆盖旧错误口径；
- 旧 manifest 保留为历史证据；
- 后续当前 manifest 只引用本次审计结果，不回写覆盖历史包。

## 5. 不变项

本修正不改变：

- 194 个活动 `frame_key`；
- 当前 shot mapping；
- 已关闭的两个边界决策；
- 人物、场景或剧情语义；
- `canonical=0`；
- `production_ready=0`；
- 其余 Visual Canon 与世界基础门禁。

## 6. 下一步

媒体规格合同修正完成后，恢复边界审核：

```text
VISUAL_CANON_BOUNDARY_REVIEW_03_EP05_TO_EP06
```

只有 Visual Canon、最小世界基础和全季 final gate 全部通过，才允许将活动源图升级为 `canonical_storyboard_reference`。生产派生文件随后按需生成，不在本轮批量创建。
