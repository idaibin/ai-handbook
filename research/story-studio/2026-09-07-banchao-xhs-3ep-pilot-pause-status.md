# 班超｜小红书历史动漫三集试播：暂停状态总览

```yaml
task_identifier: TASK — Story Studio — 班超 小红书历史动漫三集试播验证
task_key: story-studio/banchao/xhs-history-anime-3ep-pilot
status: paused_visual_direction_reset
pause_requested_at: 2026-09-07T14:09:39+08:00
pause_reason: 用户明确表示当前设计均不满意，要求完整梳理、记录并暂停
canonical: false
production_ready: false
publication_ready: false
```

## 1. 当前结论

本 Task 已暂停。暂停范围覆盖 P01、P02、P03 的后续视觉设计、关键帧、Animatic、视频与发布验证。

P01 的史实与脚本工作仍有效；当前视觉方向没有通过创意验收。此前技术上可用的 KF01 不再作为活动视觉候选或 KF02 连续性基线，KF02 执行授权撤销，Gate B 回退为等待视觉方向重新选择。

当前状态不是“项目失败”，而是：

```text
内容与史实基线可保留
视觉方向未获接受
媒体生产暂停
等待重新定义并冻结美术方向
```

## 2. 已完成工作

### 2.1 三集试播基线

三集候选结构已建立：

1. P01《佣书者》：成为后来出使西域的班超以前，他是谁；
2. P02《投笔之后》：投笔后是否立刻改变命运；
3. P03《礼变》：如何从礼遇变化判断危险到来。

三集只是独立的小红书试播候选，不覆盖既有 24 集故事和 S1 资产链。

### 2.2 P01 史实与脚本

```yaml
episode: P01《佣书者》
target_duration_seconds: 72
shot_count: 7
major_location_count: 1
speaking_roles: 2
claim_ledger_items: 11
gate_a: PASS_WITH_VISUAL_HOLDS
```

已完成：

- 完整候选旁白与对白；
- 7 镜 Beat Sheet；
- 11 项 Claim Ledger；
- `[F] / [I] / [A] / [V] / [待核实]` 边界；
- 明确排除“投笔 → 当天从军 → 立即成名”的错误因果。

尚未完成真实配音计时。

### 2.3 媒体执行隔离

已经建立并落盘控制面与媒体生成面隔离：

```text
Control Project
→ Task / Research / Contract / Review / Evidence / Sync

Isolated Media Context
→ Image Generation / Image Edit / Video Generation
```

此前在控制上下文中连续产生的三张 Dashboard / 信息图均已隔离为失败证据，不得裁切、复用或进入任何 Gate。

### 2.4 P01-KF01 实际结果

用户在隔离媒体会话返回了一张独立人物图：

```yaml
asset_id: P01-KF01_SCRIBE_STATE
format: PNG
dimensions: 941x1672
sha256: 5a0358c4c90826c14c3eeb882864c2d65c95b1cdfe3ac2bc0fce771304bfc881
technical_review: PASS_CANDIDATE_WITH_HOLDS
creative_review: REJECTED_BY_USER
final_active_status: rejected_by_creative_direction
```

技术检查曾确认：单张竖屏、人物和佣书动作可读、简牍/毛笔/低案基本成立、无报告版式和可读文字。

但创意方向未通过：

- 整体偏复古纸本历史插画；
- 赭褐色、纸张纹理和密集排线过重；
- 人物年龄偏成熟、青年锐气不足；
- 发髻偏大，存在泛东亚时代剧倾向；
- 不符合用户期望的小红书现代国漫视觉吸引力。

技术通过不能覆盖用户的创意否决。因此该图只保留为负面样本和历史执行证据。

## 3. 当前资产与处置

| 资产 | 当前状态 | 后续用途 |
|---|---|---|
| Variant B 四视图 | `candidate_unconfirmed_after_reset` | 可作为历史参考，但重新设计时不得默认视为已批准身份 Canon |
| 三张 Dashboard / 信息图 | `invalid_output_quarantined` | 失败证据，仅供路由复盘 |
| P01-KF01 复古历史插画 | `rejected_by_creative_direction` | 负面风格样本，不进入连续性链 |
| P01-KF02 隔离媒体包 | `superseded_authorization_revoked` | 禁止继续执行 |
| P01-KF03 | `not_prepared_not_authorized` | 未开始 |
| P02 完整脚本与 Claim Ledger | `not_started` | 暂停 |
| P03 完整脚本与 Claim Ledger | `not_started` | 暂停 |
| P01 Animatic / 成片 | `not_started` | 暂停 |

## 4. Gate 状态

```yaml
gate_a:
  status: PASS_WITH_VISUAL_HOLDS
  scope: P01 史实与脚本

gate_b:
  status: BLOCKED_PENDING_VISUAL_DIRECTION_SELECTION
  visual_valid_keyframes: 0/3
  accepted_style_reference: none
  accepted_character_design: none

gate_c:
  status: NOT_STARTED

gate_d:
  status: NOT_STARTED

gate_e:
  status: NOT_STARTED
```

此前 KF01 的 `PASS_CANDIDATE_WITH_HOLDS` 是技术层 Review，不再计入当前有效关键帧数量。

## 5. 已否决与未决方向

### 已否决

```text
复古纸本历史插画
棕黄单色主导
密集素描排线
偏成熟文士形象
泛东亚时代剧视觉
```

### 未获批准

“仙侠国漫质感 × 东汉历史内容”只进行过方向讨论，没有生成经用户确认的风格样本，因此不是当前批准方向。

当前：

```yaml
accepted_visual_direction: null
accepted_style_reference: null
accepted_character_reference: null
```

## 6. 未验证项

- 新视觉方向和目标受众偏好；
- 班超最终人物年龄、脸型、发式、服装和气质合同；
- Provider / model 与显式参考图绑定；
- 三关键帧人物一致性；
- 跨场景物质文化准确性；
- 视觉盲测；
- 实际配音时长；
- 单集生产成本与可持续性；
- 小红书 24 小时与 7 天数据；
- 商业使用权。

## 7. 与正式 EP01 / S1 的边界

本 Task 是独立的 `9:16` 三集小红书试播验证。它没有修改正式 EP01 的 `16:9 / 105 秒 / 14 Shots / 27 Panels` 生产链，也没有修改 S1 的既有 canonical storyboard reference。

暂停本试播不代表正式 EP01 或 S1 的生产状态发生变化。

## 8. 恢复条件

恢复时不得从 KF02 继续，也不得直接批量生成三张关键帧。合法顺序为：

```text
明确恢复本 Task
→ 重新定义目标受众与视觉目标
→ 生成少量独立视觉方向测试
→ 用户选择并冻结唯一风格
→ 重新确认班超人物身份锚点
→ 重做正式 KF01
→ KF01 通过后才准备 KF02 / KF03
```

媒体生成仍必须发生在隔离媒体上下文；控制 Project 只负责合同、Review、证据与同步。

## 9. 暂停状态

```yaml
paused: true
current_execution_unit: none
last_completed_execution_unit: PILOT_EP01_CREATIVE_DIRECTION_REJECTION_AND_PAUSE
next_action: AWAIT_EXPLICIT_RESUME_FOR_VISUAL_DIRECTION_DISCOVERY_AND_STYLE_FREEZE
```
