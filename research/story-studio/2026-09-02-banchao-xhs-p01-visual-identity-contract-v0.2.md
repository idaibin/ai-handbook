# 班超｜小红书历史动漫试播 P01《佣书者》视觉身份合同与三关键帧 Work Order v0.2

```yaml
task_identifier: TASK — Story Studio — 班超 小红书历史动漫三集试播验证
task_id: story-studio-banchao-xhs-history-anime-3ep-pilot
task_key: story-studio/banchao/xhs-history-anime-3ep-pilot
execution_unit: PILOT_EP01_VISUAL_IDENTITY_CONTRACT_AND_THREE_KEYFRAMES
episode_id: P01
episode_title: 佣书者
status: media_capsule_ready_waiting_isolated_execution
canonical: false
production_ready: false
publication_ready: false
platform: Xiaohongshu
format: 9:16
required_output_count: 3
current_asset: P01-KF01_SCRIBE_STATE
execution_surface: isolated_media_context
control_project_media_tool_calls: prohibited
visual_direction: 东汉简牍纸色 × 矿物色 × 手绘硬边二维动画
updated_at: 2026-09-02T09:22:09Z
```

## 1. 结论与范围

本合同只为 P01《佣书者》建立一个最小、可验证的班超视觉身份，并按顺序生成三张独立 9:16 关键身份帧：

1. `P01-KF01_SCRIBE_STATE`：佣书状态；
2. `P01-KF02_LONG_LABOR_STATE`：久劳苦状态；
3. `P01-KF03_RESTRAINED_REPLY_STATE`：投笔后克制回应状态。

一次只允许执行一张图。`KF01` 通过身份、构图、物质文化和版式检查后，才授权 `KF02`；`KF02` 通过后才授权 `KF03`。

本试播资产是 `candidate_not_canonical`。它不覆盖 Story Studio 既有 S1 的 194 张 canonical storyboard reference，也不修改另一条 EP01 16:9 / 105 秒生产链。历史人物外貌属于艺术设计，不宣传为真实复原。

## 2. 媒体执行边界

```yaml
execution_surface: isolated_media_context
context_isolation_required: true
single_asset_only: true
current_asset_id: P01-KF01_SCRIBE_STATE
control_project_media_tool_calls: prohibited
```

媒体生成上下文只能加载当前 `asset_id`、当前一张画面的目标、Variant B 参考图、班超身份特征、当前镜头、构图、风格和禁止项。

不得加载或转述：

```text
Task State
Gate
Registry
Execution Record
commit
SHA-256
GitHub / Drive 状态
Evidence Report
next_action
```

需要参考图时，必须先确认参考图在隔离媒体上下文中已经实际绑定。未取得绑定证据时执行 `STOP_BEFORE_TOOL`。输出出现表格、Dashboard、报告页、UI、标题、状态标签或说明文字，立即判定为 `invalid_output`，不得裁切或拆取人物区域继续使用。

## 3. 身份锚点

```yaml
source_asset:
  title: banchao__ep01__g07-char-ban-chao-state01__take02a-variant-b__provider-native.png
  drive_file_id: 1RP2qjzN0DP6hkuy2XnsA1mZCttPj8mOr
  sha256: 86f95cd86c9d05994c8756fbf520976bf40b44192c36daf3c03906cf95748ce1
  dimensions: 1672x941
  mode: RGB
  use_scope: identity_reference_only
```

Variant A 含有明显服装纹样，只作为 rejected comparison，不进入媒体生成输入。

稳定身份特征：

```text
成年东亚男性，青年后段至壮年前段的年龄感；
清瘦、结实但非武将体格；
偏长的窄椭圆脸，颧骨略高但不过度突出；
眉形平直偏浓，眼睛狭长、眼尾接近平直；
鼻梁中等、鼻头克制；
薄唇，方中带收的下颌；
暖棕肤色，保留劳动环境中的自然粗粝感；
黑发高束为简洁发髻，额前和鬓侧少量自然碎发；
无胡须、无冠冕、无官阶符号。
```

三张图必须保持同一张脸、同一身体比例、同一发髻基线和同一服装系统。状态变化只能来自姿态、肌肉张力、眼神和疲劳程度。

## 4. 人物状态梯度

### P01-KF01｜佣书状态

```text
精神状态：专注、克制、尚能维持工作节奏；
体态：坐于低案前，身体略前倾，但脊背尚未明显塌陷；
手部：一手稳定持笔，另一手整理未完成的简牍；
眼神：落在书写表面，不看镜头；
叙事功能：让观众一眼看懂“他靠抄写维持生活”。
```

### P01-KF02｜久劳苦状态

```text
精神状态：长时间劳动后的疲惫，不做夸张痛苦表情；
体态：肩背更低，持笔手暂时停下，另一只手轻微活动僵硬手指；
细节：袖口有合理磨旧，桌面工作量增加，光线进入傍晚；
眼神：短暂离开书写表面，停顿而非发呆；
叙事功能：将史料中的“久劳苦”转化为明确但被标记为演绎的可见状态。
```

### P01-KF03｜投笔后克制回应状态

```text
精神状态：从忍耐转为明确决意，平静而非怒吼；
体态：从案前半起身或已经站直，身体重心稳定；
关键连续性：同一支笔已经落在同一张低案近侧，手离开笔，案面关系清楚；
表情：下颌略收、目光转向画外嘲笑者，克制坚定；
禁止：英雄化仰拍、战场预示、武器、铠甲、强烈金色圣光；
叙事功能：表现“投笔只是把志向说出口”，不暗示当天从军。
```

## 5. 服装、书写与空间边界

服装：无纹样、磨旧、低饱和棕灰色交领叠穿布衣，实用宽袖、简单布带和简洁发髻。允许轻微褶皱、磨损、局部不对称和低对比织物质感。

禁止：服装纹样、绣金、金属饰件、铠甲、披风、武将护腕、现代鞋底、长装饰发带、统一古偶妆面和塑料皮肤。

书写与空间：

- 使用“简牍”作为宽泛书写载体，只出现窄条状、成组排列或捆束的书写单位；
- 使用木或竹质直杆毛笔和柔性笔毫，不出现现代金属 ferrule；
- 使用低矮、朴素的木质工作案与席面；
- 使用简化的官府抄书室：木构框架、低细节墙面、单侧自然光；
- 所有墨迹保持抽象、不可辨识。

主动排除：现代纸张堆、装订书册、西式书桌和椅子、卷轴式批量道具、玻璃窗、电灯、欧式烛台、明确币制和支付动作、可辨识汉字及现代文具。

## 6. 统一画面合同

```yaml
aspect_ratio: 9:16
independent_images: true
current_image_count: 1
single_clear_subject: Ban Chao
style: hand_drawn_hard_edge_2d_animation
surface: subtle_fiber_paper_texture
palette:
  base: warm_bamboo_paper
  dark: soot_ink_brown
  accent: restrained_mineral_ochre_and_blue_grey
lighting: one_side_natural_daylight
camera_language: documentary_cinematic_not_heroic
text: none
watermark: none
logo: none
```

禁止拼版、角色设定表、报告页、信息图、字幕、标题、边框和 UI 元素。

## 7. 当前唯一媒体输入：P01-KF01

当前隔离媒体包只包含：

```text
P01-KF01_REFERENCE.png
P01-KF01_MEDIA_INPUT.txt
P01-KF01_ACCEPTANCE.txt
```

媒体上下文不得加载本 Work Order、Task 文档或任何状态记录。`KF02` 和 `KF03` 的文字在本合同中保留，但在 `KF01` 通过前不得放入当前媒体上下文。

纯媒体输入：

[`2026-09-02-banchao-xhs-p01-kf01-media-input.txt`](./2026-09-02-banchao-xhs-p01-kf01-media-input.txt)

隔离 Capsule：

[`2026-09-02-banchao-xhs-p01-kf01-isolated-media-capsule.yaml`](./2026-09-02-banchao-xhs-p01-kf01-isolated-media-capsule.yaml)

## 8. Gate B 首轮验收

每张有效图必须逐项判断：

```yaml
identity_same_person:
face_anchor_preserved:
hair_anchor_preserved:
body_proportion_preserved:
costume_system_preserved:
state_is_distinguishable:
hand_prop_surface_continuity:
material_culture_no_obvious_modern_element:
no_readable_text:
no_report_layout:
aspect_ratio_9_16:
reference_binding_evidence:
```

无有效图时，Gate B 只能保持 `BLOCKED_NOT_RUN`。三张图全部生成后才做真实结论。即使 `PASS_CANDIDATE`，也只允许进入 P01 完整静态分镜 / Animatic，不自动成为 canonical、production-ready 或 publication-ready。

## 9. 当前迁移与未验证边界

已完成：最小人物身份合同、当前 `KF01` 单资产媒体输入、参考图/Prompt/验收清单的纯媒体包，以及控制面与媒体生成面的隔离迁移。

尚未验证：

```text
reference_binding_in_isolated_media_context
actual_provider_model_and_version
valid_kf01_output
cross_image_identity_consistency
material_culture_accuracy
blind_review
actual_voice_duration
actual_production_cost
publication_performance
commercial_rights
```
