# 《班超》S1 活动媒体规格全量审计

- `audit_id`: `BANCHAO-S1-ACTIVE-MEDIA-SPEC-AUDIT-20260826`
- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `executed_at_utc`: `2026-08-26T05:19:25Z`
- `scope`: `EP01–EP24 / 194 active mapped PNG refs`
- `mapping_sha256`: `78181c78e509a5615e900f7dc8518330eb8ddcad577fa80ad6182871f45ef5be`
- `audit_json_sha256`: `6de85bac71b6802d5650ec430f065a5794d29c1c393469622ffda854f24aae18`
- `result`: `PASS_SOURCE_MEDIA_WITH_CONTRACT_CORRECTION_REQUIRED`

## 结论

194 个活动 `frame_key` 已全部纳入审计：

```text
解码成功：194/194
PNG：194/194
8-bit truecolor RGB：194/194
1920×1080：72
1672×941：122
其他尺寸：0
显式 ICC / sRGB / gAMA 标记：0
损坏文件：0
非 RGB 文件：0
活动资产变更：0
```

现行 Visual Canon Gate v1 将“视觉基准源文件”与“下游生产输出规格”混为同一门禁，要求所有活动源图必须精确为 `1920×1080 RGB/sRGB`。按实际资产证据，该规则会将 122 张可用、可解码、接近严格 16:9 的原生候选图错误判为资产失败。

本轮分类为：

```text
failure_class: FAIL_CONTRACT
not: FAIL_IMPLEMENTATION
```

不应为了获得 Visual Canon 身份而批量放大并替换 122 张源图。

## 已验证事实

### 媒体规格

- `1920×1080`：72 张，严格 16:9。
- `1672×941`：122 张，相对 16:9 偏差约 `0.053135%`。
- 所有文件均为 PNG `bit_depth=8 / color_type=2 / RGB / non-interlaced`。
- 所有 194 张均没有嵌入 ICC profile、PNG sRGB chunk 或 gAMA chunk，因此准确口径是 `RGB_8BIT_UNTAGGED`，不能继续声明已经显式验证为 sRGB。

### 证据覆盖

- 43 张：本轮或直接前序门禁已读取当前 Drive 原始字节。
- 151 张：从权威 episode/chapter/repair/rebuild package 中解码，并通过 manifest 的 Drive file ID、SHA-256，或 Drive 文件夹的文件名/唯一大小与当前 mapping 绑定。
- 194 个 mapping Drive ID 均被对账。
- 109 条 package manifest SHA 与解码字节完全一致。
- `EP10-B05` 的旧分集 manifest 存在一条 65 位 malformed SHA；当前 Drive 原始字节与 package 字节完全一致，正确 SHA-256 为：

```text
e1bbbb8d060aec9c88f17885b45cd923bbf6bc98c7e815784bf9d42d4b38c3e1
```

该问题是旧证据字段错误，不是媒体损坏。

## 门禁修正

### Visual Canon Source Media Gate

当前 S1 的 canonical storyboard source 接受：

```text
1920×1080 / 8-bit RGB PNG
或
1672×941 / 8-bit RGB PNG
```

并必须满足：

1. PNG 可解码；
2. `bit_depth=8`、`color_type=2`、Pillow mode=`RGB`；
3. 尺寸属于当前已验证的两个 S1 原生类别；
4. 相对 16:9 的比例偏差不超过 `0.1%`；
5. 记录原生尺寸、文件大小、SHA-256 和 Drive file ID；
6. 同一 `frame_key` 只有一个活动源文件。

按此合同，本轮为：

```text
PASS_SOURCE_MEDIA: 194/194
```

### Production Derivative Gate

进入 Remotion、image-to-video 或正式镜头生产前，再生成确定性派生文件：

```text
target: 1920×1080
mode: 8-bit RGB
profile: embedded sRGB
crop: forbidden unless shot contract explicitly authorizes
lineage: source file ID + source SHA + derivative SHA
```

当前预计：

```text
122 张：需要无裁切 resize + sRGB profile
72 张：只需要写入/规范化 sRGB profile
```

这些派生文件不应反向覆盖 Visual Canon 源文件。

## 分集规格分布

| Episode | Frames | 1920×1080 | 1672×941 | Decode/RGB |
|---|---:|---:|---:|---:|
| EP01 | 10 | 10 | 0 | 10/10 |
| EP02 | 8 | 8 | 0 | 8/8 |
| EP03 | 8 | 8 | 0 | 8/8 |
| EP04 | 8 | 8 | 0 | 8/8 |
| EP05 | 8 | 4 | 4 | 8/8 |
| EP06 | 8 | 0 | 8 | 8/8 |
| EP07 | 8 | 2 | 6 | 8/8 |
| EP08 | 8 | 0 | 8 | 8/8 |
| EP09 | 8 | 0 | 8 | 8/8 |
| EP10 | 8 | 1 | 7 | 8/8 |
| EP11 | 8 | 0 | 8 | 8/8 |
| EP12 | 8 | 3 | 5 | 8/8 |
| EP13 | 8 | 0 | 8 | 8/8 |
| EP14 | 8 | 0 | 8 | 8/8 |
| EP15 | 8 | 1 | 7 | 8/8 |
| EP16 | 8 | 8 | 0 | 8/8 |
| EP17 | 8 | 0 | 8 | 8/8 |
| EP18 | 8 | 8 | 0 | 8/8 |
| EP19 | 8 | 8 | 0 | 8/8 |
| EP20 | 8 | 0 | 8 | 8/8 |
| EP21 | 8 | 1 | 7 | 8/8 |
| EP22 | 8 | 0 | 8 | 8/8 |
| EP23 | 8 | 1 | 7 | 8/8 |
| EP24 | 8 | 1 | 7 | 8/8 |

## 状态影响

```text
mapping rows: 194
active asset changes: 0
canonical: 0
production_ready: 0
```

媒体规格审计已闭合，但 Visual Canon 仍受以下内容阻断：

- 6 个未关闭边界；
- 15 个此前 `PASS_CANDIDATE` 边界的最终确认；
- 五个最小世界基础域；
- 全季最终门禁重跑。

## 验证限制

本轮没有将 194 个 Drive 文件逐个重新下载一遍。43 个当前活动文件使用了当前 Drive 原始字节；其余 151 个使用权威 package 原始字节，并通过 manifest 或 Drive folder listing 与当前 mapping 绑定。该证据足以闭合媒体规格和结构审计，但不替代后续逐帧视觉语义审核。
