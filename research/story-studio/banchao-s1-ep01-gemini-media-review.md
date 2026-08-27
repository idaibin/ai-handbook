# 班超 S1 EP01 — Gemini 10 秒媒体证据注册与动作复核（Revision 19）

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `task_key`: `story-studio/banchao/s1-final-gate`
- `execution_unit`: `REGISTER_GEMINI_10S_VIDEO_AND_REVIEW_MEDIA_EVIDENCE`
- `performed_at_utc`: `2026-08-27T02:56:15Z`
- `precondition_status_revision`: `18`
- `precondition_task_revision`: `23`
- `result`: `PASS_MEDIA_EVIDENCE_REGISTERED_PRODUCTION_ACCEPTANCE_FAIL`

## 结论

用户补充的 Gemini 原始 MP4 和 EP01-F01–F10 联系图已经取得可回读字节，并完成媒体探测、完整解码、抽帧、动作接触复核和 Canon 对照。

```text
媒体证据注册：PASS
动作路径可见性：PASS_BOUNDED
笔搁接触与手部释放：PASS_BOUNDED
作为 production clip：FAIL
canonical：194（不变）
production_ready：0（不变）
mapping revision：10（不变）
manifest revision：10（不变）
```

本轮纠正一项此前交接判断：实际视频在约 `7.75–8.50s` 使用了一个带凹槽的木质承托物，毛笔获得支撑，手指随后完全离开，毛笔保持静止。因此“没有进入承托位置”与“手没有完成松开”不再成立。

但该结果仍不能进入生产：视频静默引入了当前合同未授权、历史形制未核实的独立笔搁；同时存在 Hero Brush 构造错误、伪文字、Canon 身份/服装/场景漂移、固定可见平台标记和原生 720p 等失败。

## Verified — 媒体身份与规格

```text
source_sha256:
951a15a405786fc056b84d5144c4d702191266dc42801a2211bf346e5cfe5d09

container: MP4 / isom
container_duration: 10.005s
encoder_tag: Google

video:
H.264 High
1280×720
24 fps
240 frames
10.000s
yuv420p

audio:
AAC LC
48 kHz
stereo
10.005s
128 kbps approximately

full ffmpeg decode: PASS
visible audio stream: PRESENT_AND_NON_SILENT
```

音频内容的叙事和 Foley 质量本轮未做听觉语义验收；这里只验证流存在、可解码且不是全静音。

## Verified — 动作时间线

| 时间 | 观察 | 结果 |
|---|---|---|
| `0.00–4.50s` | 持续书写，笔尖接触书写面 | `K1 PASS_BOUNDED` |
| `4.50–6.25s` | 书写停止，笔尖离开表面，人物先开始抬眼 | `K2 PASS_BOUNDED`；视线动作略早 |
| `6.50–7.50s` | 毛笔从近竖直转为水平，笔尖悬空横向移动 | `K3 PASS` |
| `7.75–8.25s` | 笔杆落到带凹槽的木质承托物上 | `K4 PHYSICAL_CONTACT_PASS`；目标道具未授权 |
| `8.25–8.50s` | 手指松开并撤离，毛笔保持静止 | `K5 RELEASE_PASS_BOUNDED` |
| `9.00–10.00s` | 人物正面抬眼，形成决断终态 | `K5 DECISION_GAZE_PASS_BOUNDED` |

## 证据纠偏

```text
“没有进入笔搁承托位置” → CONTRADICTED
“手没有完成松开—脱离” → CONTRADICTED
“放笔后没有稳定静止终态” → CONTRADICTED
```

新的准确表述是：

```text
物理接触与释放动作可以读懂；
但依赖了未授权的独立笔搁，并且毛笔本体、文字、Canon 一致性和交付规格不合格。
```

## Production acceptance matrix

| 验收项 | 结果 | 依据 |
|---|---|---|
| 视频完整解码 | `PASS` | 240/240 帧可解码；音频流可解码 |
| 原生分辨率记录 | `PASS_RECORDED / TARGET_FAIL` | 原生 `1280×720`，不是 `1920×1080` |
| 片内人物连续性 | `PASS_BOUNDED` | 抽样帧中同一人物未发生明显身份替换 |
| Canon 人物身份/服装一致性 | `FAIL` | 与 EP01-F01 Canon 对照，脸部比例、灰色服装、发型细节均发生漂移 |
| Canon 场景连续性 | `FAIL` | 书案布局、背景抄书人数量、道具和空间构图均被重建 |
| 手部结构 | `PASS_BOUNDED_AT_SAMPLED_FRAMES` | 未见明确增指/缺指；接触和释放连续；运动模糊仍存在 |
| Hero Brush 构造 | `FAIL` | 尾部环形结构、黑色 ferrule/end-cap 感、笔毫呈刚性实心锥感 |
| 执笔与动作路径 | `PASS_BOUNDED` | 书写、抬笔、横移、放置、松手均可读；握持仍偏低且硬笔感较强 |
| 承托接触 | `PASS_PHYSICALLY / FAIL_CONTRACT` | 确实使用带凹槽的木质笔搁；当前合同禁止静默引入 `PROP_BRUSH_REST` |
| 书写表面稳定 | `PASS_BOUNDED` | 主表面位置基本稳定 |
| 可见文字策略 | `FAIL` | 纸面存在高对比、可读形态的 AI 伪文字和印记 |
| 背景稳定 | `PASS_WITH_LIMITATION` | 无明显人物消失；动作重复、低细节和软化仍不满足生产验收 |
| 可见平台标记 | `FAIL` | 右下角固定四角星/菱形标记贯穿抽样帧 |
| 无水印交付 | `FAIL` | 当前原始文件不可作为无标记交付资产 |

## Failure classification

```text
FAIL_IMPLEMENTATION
- Hero Brush 几何和材质错误
- Canon 人物/服装/场景漂移
- 纸面伪文字
- 原生输出仅 1280×720

FAIL_CONTRACT / FAIL_DEPENDENCY
- 生成依赖了未授权的独立笔搁
- 当前合同要求 BRUSH_LAYDOWN_ZONE，不允许静默引入历史形制未核实的 PROP_BRUSH_REST

FAIL_RIGHTS_OR_PROVIDER
- 固定可见平台标记影响交付

NOT FAIL_ARCHITECTURE
- K1–K5 分段状态仍然有效
- 新证据反而证明“接触—释放—静止”动作可由视频模型完成
```

## Drive evidence identities

```text
Original MP4: 1-HAifRlGJydN_crLPhLEkSZMznfcH2B8
Raw ffprobe JSON: 18NEst-YnhjvERJl_-yvk2IgC7qbZQf3t
Decode receipt: 1FJZlGqMsCElAAXRGitm39064CEb-A_A9
1fps review sheet: 1rubqDEtc5spdKYLPj46yUW96T3mTaZlg
6–9s quarter-second review: 1ryolV1QODnjsNF8MvYI-je-2xDiilgYK
Brush placement close-up: 1gpjSKMswOf-ymaP0eB4n7g82svY2Z9xn
Identity comparison: 1zBdU44pvjglsdYyqM75NIyhHkJqDaXPI
Hand/brush close-ups: 1NjEmxR5MQnHR_SEoC3xGR_DNTcN5vWm2
User canonical contact sheet: 1i81ncsLVDYyateZgj-GxnPgEDblRr-Jc
Review report: 1HRARJlqm8yZiv221XK26oI4Cb59Z-qT-
Evidence JSON: 1OCWZpIyyYNhEZr3bWR2qXkaxG_hIKXKA
Checksums: 1JGcfUX9L8jKQUas-zQQqE0Ns453CUpso
Evidence package: 1HgolEWto1XQoxJ9Gqgrfti_0RWxlaiQI
```

## Unchanged assets and decisions

```text
Option A：保持
F08–F10：继续作为 canonical_storyboard_reference
F03 / F06–F10：仍不作为 production_motion_anchor
canonical：194
production_ready：0
mapping revision：10
manifest revision：10
EP01→EP02 boundary：不重跑
```

## Next action

```text
EP01_WRITING_SYSTEM_K1_K5_STATIC_ANCHOR_GENERATION
```

静态锚点必须继续使用已批准的 `BRUSH_LAYDOWN_ZONE`；不得从本视频复制未授权笔搁。先验收 K1–K5，再进入 Clip A/B/C。
