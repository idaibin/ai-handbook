# 班超｜小红书历史动漫试播 P01-KF01 视觉 Review

```yaml
task_identifier: TASK — Story Studio — 班超 小红书历史动漫三集试播验证
task_key: story-studio/banchao/xhs-history-anime-3ep-pilot
execution_unit: PILOT_EP01_KF01_RETURN_REVIEW_AND_KF02_AUTHORIZATION
asset_id: P01-KF01_SCRIBE_STATE
result: PASS_CANDIDATE_WITH_HOLDS
asset_status: visual_candidate_accepted_lineage_incomplete
canonical: false
production_ready: false
publication_ready: false
reviewed_at_utc: 2026-09-03T06:02:28Z
```

## 结论

用户返回的 PNG 是第一张可用的 P01 人物关键帧，不是报告页、Dashboard 或信息图。画面满足单人物、佣书动作、简牍、低案、朴素服装、无可读文字和竖屏构图要求。

本轮判定为 `PASS_CANDIDATE_WITH_HOLDS`，可作为 P01 内部视觉候选并授权准备 `P01-KF02_LONG_LABOR_STATE`。它不等于 Gate B 通过；Gate B 仍需三张关键帧完成后统一执行。

## 原始返回文件

```yaml
source: user_returned_attachment
file_name: BANCHAO-XHS-P01-KF01-SCRIBE-STATE-CANDIDATE-01.png
chat_file_id: file_00000000105881f5ba346b61db2aeb32
format: PNG
dimensions: 941x1672
mode: RGBA
bytes: 3825728
sha256: 5a0358c4c90826c14c3eeb882864c2d65c95b1cdfe3ac2bc0fce771304bfc881
aspect_ratio_observed: 0.562799
aspect_ratio_target: 0.562500
aspect_ratio_delta: 0.000299
provider: not_verified
provider_generation_metadata: absent
reference_binding_metadata: absent
drive_asset_file_id: 1G9igwcGXes_KLPrt8ZG41EOyw3UN6kVp
drive_receipt_file_id: 1N5ZP8_th4hBSmFeQXPPR1pik7u4HhSSC
```

原始字节必须保留。后续需要 1080×1920 时只能建立派生文件，不能覆盖本文件或把派生文件标记为 provider-native。

## 验收结果

| 检查项 | 结果 | 依据与限制 |
|---|---|---|
| exactly_one_independent_image | PASS | 只有一个完整画面，无拼版、边框或说明区 |
| aspect_ratio_9_16 | PASS_WITH_TOLERANCE | 941×1672，距精确 9:16 仅约 0.053% |
| single_clear_subject | PASS | 唯一清晰人物为班超候选 |
| identity_same_person | PASS_VISUAL | 窄椭圆脸、略高颧骨、平直浓眉、狭长眼、中等鼻梁、薄唇与参考一致 |
| face_anchor_preserved | PASS_VISUAL_WITH_MINOR_DRIFT | 额纹与面部粗粝感使年龄略显更成熟，但未达到换脸 |
| hair_anchor_preserved | PASS_WITH_HOLD | 高束发髻成立；发髻比四视图更大、更松，后续不得继续放大 |
| body_proportion_preserved | PARTIAL_PASS | 坐姿与宽袖遮挡全身比例；上身未出现明显武将化 |
| civilian_copyist_state | PASS | 低案、持笔、整理简牍和低头专注共同建立佣书身份 |
| hand_brush_surface_continuity | PASS | 双手结构可读；笔毫接触简牍，左手稳定书写面 |
| brush_no_metal_ferrule | PASS | 木/竹直杆与柔性笔毫，无现代金属套口 |
| writing_surface | PASS_CANDIDATE | 窄条简牍与捆束状态清楚；墨迹不可辨识 |
| plain_unpatterned_clothing | PASS | 棕灰交领叠穿、无纹样、无铠甲、无金属装饰 |
| no_obvious_modern_object | PASS | 未见现代纸张、装订书、现代桌椅、玻璃、电灯或现代文具 |
| no_readable_text | PASS | 简牍有抽象墨痕，但没有可确认的可读文字 |
| no_report_layout | PASS | 无表格、UI、标题、状态标签或说明文字 |
| visual_direction | PASS_CANDIDATE | 手绘线条、纸纤维质感和低饱和矿物色成立；更接近纹理化历史插画而非扁平赛璐璐 |

## Holds

### Verified

当前附件没有 Provider receipt、generation metadata 或显式 reference-binding 证明，因此只验证了视觉连续性，未验证模型层面的父图绑定。

### Inference

人物与 Variant B 在脸型、眉眼、鼻唇、发髻和服装系统上高度一致，推断参考图大概率实际参与了生成；该推断不能替代 Provider 元数据。

画面可被理解为中国古代佣书场景，但发髻体量、宽大外袍和木格窗仍带有“泛东亚古装”倾向。后续必须明确排除 Edo / ronin / samurai / kimono / shoji 视觉语汇，避免三集逐步偏向日式时代剧。

## KF02 连续性冻结

`P01-KF02_LONG_LABOR_STATE` 必须同时使用 Variant B 四视图作为身份根锚点、本 KF01 作为场景与画风连续性锚点。

只允许变化：时间进入傍晚、肩背更低、持笔动作暂停、一只手活动僵硬手指、未完成简牍适度增加、疲惫程度增加但不老化、不换脸。

不得变化：脸型、眉眼、鼻唇、发髻基线、服装系统、房间结构、低案位置、简牍系统、画风和色彩体系。

## Gate 状态

```yaml
visual_valid_keyframes: 1/3
evidence_complete_keyframes: 0/3
kf01_visual_result: PASS_CANDIDATE_WITH_HOLDS
kf02_authorized: true
kf03_authorized: false
gate_a: PASS_WITH_VISUAL_HOLDS
gate_b: BLOCKED_NOT_RUN
```

Gate B 只能在 KF01、KF02、KF03 三张有效候选完成后执行人物盲测、状态梯度检查与整体物质文化 Review。
