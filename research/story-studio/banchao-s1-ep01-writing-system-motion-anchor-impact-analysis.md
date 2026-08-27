# 班超 S1 — EP01 洛阳书写系统 Motion Anchor 影响分析

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `execution_unit`: `EP01_WRITING_SYSTEM_MOTION_ANCHOR_REPAIR_IMPACT_ANALYSIS`
- `performed_at_utc`: `2026-08-27T01:51:32Z`
- `precondition_status_revision`: `17`
- `decision`: `OPTION_A_KEEP_NARRATIVE_CANON`
- `evidence_folder_id`: `1GCpdL1t93bdOGj6aVPVoAazUvspgOMCj`

## 结论

选择 **方案 A**：

```text
F08–F10 保留为 canonical_storyboard_reference
F03 / F06–F10 不作为 production_motion_anchor
另建 K1–K5 静态物理状态锚点
canonical: 194（不变）
production_ready: 0（不变）
mapping revision: 10（不变）
manifest revision: 10（不变）
ChangeRecord: 不需要
EP01→EP02 boundary rerun: 不需要
```

关键纠偏：当前 active screenplay 的动作不是单纯“放笔后不再拿笔”，而是：

```text
把笔放下
→ 又捡起
→ 最终没有继续落字
```

因此 `F08→F09` 的“放下后重新拿起”本身并不构成叙事 Canon 冲突。真正失败的是 **物理动作锚点质量**：F08 没有明确稳定承托和手指释放，F09 又回到书写姿态，F10 没有锁定“停止落字 + 抬眼决断”的终态。它们不能直接作为视频插值的起止状态。

## Verified

1. Drive Current Status、GitHub projection 均仍为 revision 17；`canonical=194`、`production_ready=0`。
2. mapping revision 10 与 manifest revision 10 已回读，EP01-F01–F10 均解析为当前活动 Drive PNG。
3. 10 张活动源图均完成直接下载、PNG 解码、尺寸和色彩模式检查：`1920×1080 / RGB / PASS`。
4. 当前 active screenplay 明确列出 `PROP_HERO_BRUSH`、`PROP_WRITING_SURFACE`，没有 `PROP_BRUSH_REST`。
5. F08–F10 像素复核：
   - F08：毛笔横置于书写面/案面附近；没有稳定承托终态，手未完成脱离；
   - F09：重新持笔，恢复书写姿态；
   - F10：笔尖呈硬锥/硬笔感，仍为持笔状态，未形成明确决断终态。

## Source inventory

| Frame | Drive file ID | Mechanical validation | SHA-256 |
|---|---|---|---|
| `EP01-F01` | `1sYNi4U-MbP-EjR_ggqamzKa196Ifq7Tc` | 1920×1080 / RGB | `ecc2c27acdc44517296f3b7454a34a107eddbfddbfc1fd8c7aae109b6f76e473` |
| `EP01-F02` | `1WxCeBlaK2Pt2Xn6tv3fvhpb9iqd7vNLW` | 1920×1080 / RGB | `f55d36e6737dba0630ecd7ec1c4303724cf1eec1d26998c5bf2a6815c282372d` |
| `EP01-F03` | `1gJncAcSeSNvCw55bRNDcSuO9PHExa2m4` | 1920×1080 / RGB | `089b7df429f671d9bd172b02eb8bd5bea6a1e64254572d1cf86510b2c78a55b3` |
| `EP01-F04` | `1Ouu9xmkSvj-ZJr1-5c9Kd-GBGuB8eTPj` | 1920×1080 / RGB | `0ecc3161400363767114b668910c6669bb0961eab749c05681da30a32d943188` |
| `EP01-F05` | `1_XFqyhXLfJXeR6laVHUiA6r_vVPysUp_` | 1920×1080 / RGB | `95ac1ca2df342cf2bd8fbf6404cc826092ae7b7090aa8c34166cb1ac26c3dae3` |
| `EP01-F06` | `16Rn6FlDgwX5oBQie_pw0_aesYY83KRK1` | 1920×1080 / RGB | `f512f0344b302c7fcf3277b597a62644b79cec05720438c5d3220dd82dff3c6c` |
| `EP01-F07` | `1zMeW7DUzUf4gIsKG10ODXshXHVBdZRjv` | 1920×1080 / RGB | `970ef77b8ce3dc8f420f332e052f0c073b457d50389e2e0d4ef9c381488b6070` |
| `EP01-F08` | `1eQzaBxET7zK2g20GFPuA7UtQusat2isH` | 1920×1080 / RGB | `b60c366ffce87b1e723cda63cf471d9bcc3bee7e9561cd4e8ec557e3419ea5ea` |
| `EP01-F09` | `17UGtcj055Iyv52L1mfDTOgqOKkJqYT_o` | 1920×1080 / RGB | `94b66e82ef623dc6dff4829b7193b5b1b5eb3439cef4119465cbdf463a1daa85` |
| `EP01-F10` | `1qspGO7xHOGCP3JnlAoMeviXwl_LyGiDb` | 1920×1080 / RGB | `3bc6977a98c362b2a2d6afce871d44e15d9f5952b1ebeff130306dc79dfdb3db` |

## Motion-anchor eligibility

| Frame | Decision | Reason |
|---|---|---|
| `EP01-F01` | reference only | 正常书写构图，可作视觉参考，但不是锁定动作状态 |
| `EP01-F02` | reference only | 与 F01 变化较弱 |
| `EP01-F03` | `false` | 前景主体身份歧义 |
| `EP01-F04` | reference only | 叙事书写状态，没有停笔终态 |
| `EP01-F05` | reference only | 继续书写 |
| `EP01-F06` | `false` | 视线变化与手部状态未同步 |
| `EP01-F07` | `false` | 回到活跃书写，不是悬笔终态 |
| `EP01-F08` | `false` | 错误放置接触、无稳定承托、无完整释放 |
| `EP01-F09` | `false` | 重新书写，不能承担放笔后状态 |
| `EP01-F10` | `false` | 毛笔构造和笔尖不稳定，终态未锁定 |

## Contract decisions

### `PROP_HERO_BRUSH`

只锁定单一构造、连续杆体、柔软聚锋毛毫、固定手部接触区。禁止金属 ferrule、环形结构、硬塑料锥、马克笔/钢笔笔尖和跨帧几何变化。

不声明某一种现代命名的“五指执笔法”为东汉唯一标准；这里只锁定可见物理关系。

### `PROP_WRITING_SURFACE`

视频阶段只允许低对比、非语义墨迹。需要准确文字时，使用后期确定性合成。AI 伪文字直接判定失败。

### Brush Rest 纠偏

当前 active screenplay 与资产清单没有 `PROP_BRUSH_REST`。因此本轮不静默新增历史形制不明的笔搁，而使用生产控制角色：

```text
BRUSH_LAYDOWN_ZONE
```

即现有低书案上的干燥、清晰、稳定放置区。若后续必须采用独立笔搁，应先完成来源核实和 ChangeRecord。

## K1–K5

```text
K1 正常书写
K2 笔锋离开书写面
K3 横向移动，笔锋悬空
K4 笔杆接触稳定放置区，手指开始松开
K5 手与笔完全分离，毛笔静止，人物抬眼决断
```

## Not verified / missing media

以下内容来自交接描述，但原始字节没有出现在当前 sandbox，File Library 搜索也没有定位到对应 MP4/审片图，因此本轮不把它们登记为已回读证据：

- Gemini 10 秒原始 MP4；
- 该 MP4 的原始 `ffprobe` 输出；
- 1fps 审片拼版；
- 交接中提到的旧 EP01-F01–F10 审计拼版；
- Gemini 水印/平台标记的逐帧复核；
- 1280×720、24fps、240 帧、AAC 等媒体规格的本会话独立复核。

通用模板已从 File Library 读取文本；其中“角色卡复用、一个镜头一个任务、先测 3–5 镜头、检查连续性”可作为参考，但不具项目权威性。

## Validation level

```text
Authority readback: PASS
Mapping/manifest readback: PASS
Direct source-media decode: PASS 10/10
Semantic/physical state review: PASS
Impact decision: PASS_OPTION_A
Motion-anchor contract: DESIGN_APPROVED
Gemini media evidence intake: BLOCKED_MISSING_BYTES
Static K1–K5 generation: NOT_STARTED
Video regeneration: NOT_STARTED
```

## Next action

```text
REGISTER_GEMINI_10S_VIDEO_AND_REVIEW_MEDIA_EVIDENCE
resume_after_pass:
EP01_WRITING_SYSTEM_K1_K5_STATIC_ANCHOR_GENERATION
```
