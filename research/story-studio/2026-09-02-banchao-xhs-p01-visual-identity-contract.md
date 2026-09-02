# 班超｜小红书历史动漫试播 P01《佣书者》视觉身份合同与三关键帧 Work Order v0.1

```yaml
task_identifier: TASK — Story Studio — 班超 小红书历史动漫三集试播验证
task_id: story-studio-banchao-xhs-history-anime-3ep-pilot
task_key: story-studio/banchao/xhs-history-anime-3ep-pilot
execution_unit: PILOT_EP01_VISUAL_IDENTITY_CONTRACT_AND_THREE_KEYFRAMES
episode_id: P01
episode_title: 佣书者
status: execution_authorized
canonical: false
production_ready: false
publication_ready: false
platform: Xiaohongshu
format: 9:16
output_count: 3
visual_direction: 东汉简牍纸色 × 矿物色 × 手绘硬边二维动画
created_at: 2026-09-02T15:20:35+09:00
github_baseline: idaibin/ai-handbook@f426a07b0f489a6c72488d7a6f34e79aeb2295b0
```

## 1. 结论与范围

本合同只为 P01《佣书者》建立一个最小、可验证的班超视觉身份，并生成三张独立 9:16 关键身份帧：

1. `P01-KF01_SCRIBE_STATE`：佣书状态；
2. `P01-KF02_LONG_LABOR_STATE`：久劳苦状态；
3. `P01-KF03_RESTRAINED_REPLY_STATE`：投笔后克制回应状态。

本试播资产是 `candidate_not_canonical`。它不覆盖 Story Studio 既有 S1 的 194 张 canonical storyboard reference，也不修改另一条 EP01 16:9 / 105 秒生产链。

历史人物外貌属于艺术设计，不宣传为真实复原。

## 2. 身份锚点

### 唯一图像锚点

```yaml
source_asset:
  title: banchao__ep01__g07-char-ban-chao-state01__take02a-variant-b__provider-native.png
  drive_file_id: 1RP2qjzN0DP6hkuy2XnsA1mZCttPj8mOr
  current_conversation_file: /mnt/data/banchao__ep01__g07-char-ban-chao-state01__take02a-variant-b__provider-native.png
  sha256: 86f95cd86c9d05994c8756fbf520976bf40b44192c36daf3c03906cf95748ce1
  dimensions: 1672x941
  mode: RGB
  use_scope: identity_reference_only
```

Variant A 含有明显服装纹样，只作为 rejected comparison，不进入本试播生成输入。

### 稳定身份特征

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

三张图中必须保持同一张脸、同一身体比例、同一发髻基线和同一服装系统。状态变化只能来自姿态、肌肉张力、眼神和疲劳程度。

## 3. 人物状态梯度

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

## 4. 服装与发式边界

```text
plain worn layered matte cloth
muted brown / warm grey / faded mineral earth palette
cross-collar wrapped layers
wide but practical sleeves
simple cloth sash
minimal hair tie
```

允许：轻微褶皱、磨损、局部不对称、低对比织物质感。

禁止：服装纹样、绣金、金属饰件、铠甲、披风、武将护腕、现代鞋底、长装饰发带、统一古偶妆面、塑料皮肤。

以上是受现有角色候选与广义汉代服饰轮廓约束的艺术设计，不定格为完整考古复原。

## 5. 书写与空间边界

### 已采用

- 使用“简牍”作为宽泛书写载体表达，不区分本镜头中的竹简或木牍材质；
- 只出现窄条状、成组排列或捆束的书写单位；
- 使用木或竹质直杆毛笔和柔性笔毫，不出现现代金属 ferrule；
- 使用低矮、朴素的木质工作案与席面；
- 使用简化的官府抄书室：木构框架、低细节墙面、单侧自然光；
- 所有墨迹保持抽象、不可辨识，不生成可阅读文字。

### 主动排除

```text
现代纸张堆
装订书册
西式书桌和椅子
卷轴式批量道具
玻璃窗
电灯、蜡烛式欧式烛台
明确币制和支付动作
可辨识汉字
现代文具
```

选择“简牍”而不锁定更窄材质，是因为当前一手脚本只证明“佣书”，而国家博物馆公开资料将简牍定义为竹简与木牍的统称，并说明其是纸张普及以前的重要书写载体、汉代出土数量丰富。空间、家具和服装仍保留为 `[I/A]` 视觉边界，不作为确定史实主张。

## 6. 统一画面合同

```yaml
aspect_ratio: 9:16
independent_images: true
image_count: 3
single_clear_subject: Ban Chao
style: hand_drawn_hard_edge_2d_animation
surface: subtle_fiber_paper_texture
palette:
  base: warm_bamboo_paper
  dark: soot_ink_brown
  accent: restrained_mineral_ochre_and_blue_grey
lighting: one_side_natural_window_light
camera_language: documentary_cinematic_not_heroic
text: none
watermark: none
logo: none
```

禁止拼版、角色设定表、报告页、信息图、字幕、标题、边框和 UI 元素。

## 7. 三张生成指令

### P01-KF01_SCRIBE_STATE

```text
以唯一参考图中的同一位班超为身份锚点，将其转化为手绘硬边二维历史动漫风格。竖屏 9:16，东汉洛阳的简化官府抄书室，一位清瘦成年男性坐在低矮木案前专注佣书，身体轻微前倾，右手持一支木或竹杆毛笔，左手整理窄条状成组简牍。服装为无纹样、磨旧、低饱和棕灰色交领叠穿布衣，简洁发髻。单侧自然光，简牍纸色、矿物赭石和蓝灰色，手绘线条与局部不对称。无可辨识文字，无现代物件，无报告版式，无武器铠甲。
```

### P01-KF02_LONG_LABOR_STATE

```text
保持与第一张完全同一张脸、同一发髻、同一身体比例、同一服装和同一低案空间。竖屏 9:16，傍晚自然光，一位长期抄写后的班超肩背更低，持笔手暂时离开书写面，另一只手轻微活动僵硬手指，袖口有合理磨旧，案上的未完成简牍数量增加。表情疲惫但克制，不夸张痛苦。手绘硬边二维历史动漫，简牍纸色与低饱和矿物色，无可辨识文字，无现代纸堆、书册、玻璃窗、武器或报告版式。
```

### P01-KF03_RESTRAINED_REPLY_STATE

```text
保持与前两张完全同一张脸、同一发髻、同一身体比例、同一服装和同一低案空间。竖屏 9:16，班超从案前半起身或刚站直，同一支毛笔已落在低案近侧，手与笔完全分离，笔、手、案面落点关系清楚。他转向画外发笑者，神情平静、克制、坚定，不怒吼。镜头为平视或轻微低机位但不得英雄化，单侧自然光，手绘硬边二维历史动漫，简牍纸色与矿物赭石、蓝灰色。画面不进入军旅，不出现武器、铠甲、旗帜、金色圣光、可读文字、标题或信息图。
```

## 8. Gate B 首轮验收

每张图必须逐项判断：

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
```

Gate B 不预设百分比分数。三张图全部生成后才做真实结论：

- `PASS_CANDIDATE`：三图可盲认为同一人物，状态清楚，无硬失败；
- `REVISE`：身份基本成立但有一项可修正漂移；
- `FAIL`：换脸、年龄漂移、现代元素、错误版式、手部/笔/案面连续性错误或任一图非独立 9:16。

即使 `PASS_CANDIDATE`，也只允许进入 P01 完整静态分镜 / Animatic，不自动成为 canonical、production-ready 或 publication-ready。

## 9. 来源与未验证边界

### 已读取

- `idaibin/ai-handbook/main@f426a07b0f489a6c72488d7a6f34e79aeb2295b0`
- Drive Task：`1XbzjUTeUJLm92_fwkHrDFmC5rs-ZxieQ0ThhMreKrAE`
- P01 Script / Claim Ledger：`1c27ZCBInvWrqoYre48DKTrzPQoNsbheXoBCyAki-kgo`
- 班超 Variant B 身份参考：`1RP2qjzN0DP6hkuy2XnsA1mZCttPj8mOr`
- 中国国家博物馆《故衣留声：汉简中的服饰穿搭》：https://www.chnmuseum.cn/fw/jyhdyy/202512/t20251211_278267.shtml
- 中国国家博物馆《孙机：考古能看得见历史，也能望得见未来》：https://www.chnmuseum.cn/yj/kydt/202306/t20230621_258717.shtml

### 尚未验证

```text
exact_historical_portrait
exact_official_copying_room_layout
exact_garment_construction
exact_bamboo_vs_wood_substrate_per_shot
actual_provider_model_and_version
cross_image_identity_consistency
blind_review
actual_voice_duration
actual_production_cost
publication_performance
commercial_rights
```
