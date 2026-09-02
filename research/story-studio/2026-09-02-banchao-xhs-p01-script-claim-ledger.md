# 班超｜小红书历史动漫试播 P01《佣书者》脚本与 Claim Ledger v0.1

```yaml
task_identifier: TASK — Story Studio — 班超 小红书历史动漫三集试播验证
task_id: story-studio-banchao-xhs-history-anime-3ep-pilot
task_key: story-studio/banchao/xhs-history-anime-3ep-pilot
execution_unit: PILOT_EP01_SCRIPT_DRAFT_AND_FACT_CHECK
episode_id: P01
episode_title: 佣书者
result: PASS_WITH_VISUAL_HOLDS
status: internal_candidate
canonical: false
production_ready: false
publication_ready: false
platform: Xiaohongshu
format: 9:16
target_duration_seconds: 72
shots: 7
major_locations: 1
speaking_roles: 2
narration: third_person_documentary
dialogue: minimal
historical_label: 基于史实的动漫化演绎
completed_at: 2026-09-02T12:51:46+09:00
source_basis:
  github_ref_at_execution_start: a7472475910ea2706981b1139953c1ae56e36c22
  pilot_baseline_commit: 77c5cb5b44ac21b7b1716d8cc9b94fa948b93175
  drive_task_doc_id: 1XbzjUTeUJLm92_fwkHrDFmC5rs-ZxieQ0ThhMreKrAE
  drive_story_bible_id: 1F-DnHftRIN5F4-o2M0i10EZ_d2HjL-6P
  drive_treatment_id: 1wlDngVD09q7sbL4IPtAKMiwaV-a9HP88
  primary_source: 《后汉书》卷四十七《班超传》
```

## 1. 结论

P01《佣书者》的 60–75 秒脚本、7 镜 Beat Sheet、Claim Ledger 和 Gate A 史实检查已经完成。

本集只回答一个问题：

> 成为后来出使西域的班超以前，他是谁？

脚本把班超的“佣书—久劳苦—投笔明志”作为主线，并明确阻断以下错误因果：

```text
投笔 → 当天从军 → 立即成名
```

当前脚本可进入视觉身份合同与三张关键身份帧设计，但仍不得冻结未经考据的书写材质、官府抄书空间、服饰、灯具、货币和道具细节。

## 2. 叙事合同

```yaml
opening_state: 洛阳，为官佣书以维持家计
desire: 不愿长期困在笔墨劳作中，希望立功异域
resistance: 贫困、重复劳作、旁人嘲笑，以及命运并未因一句志向立即改变
choice: 停下工作，投笔并公开说出志向
change: 从沉默承受转为明确表达行动方向
ending_hook: 投笔之后，他还要走多久才真正走向西域
```

## 3. 72 秒完整脚本

> **旁白**
>
> 成为那个后来出使西域的班超以前，他在洛阳替官府抄书。
>
> 永平五年，兄长班固被召任校书郎；班超随母亲来到洛阳。
>
> 家里贫困，他靠替官府抄书维持家计。史书对那段劳作只留下三个字：久劳苦。
>
> 史书没有写下每个黄昏。发僵的手指和磨旧的袖口，是我们为表现“久劳苦”所做的演绎。
>
> 终于有一天，他停下工作，投下手中的笔——
>
> **班超**
>
> 大丈夫……安能久事笔研间乎？
>
> **旁白**
>
> 旁人笑他。班超只回了一句——
>
> **班超**
>
> 小子安知壮士志哉！
>
> **旁白**
>
> 但史书没有写他当天从军。“久之”，他才被任为兰台令史，后来又因事免官。
>
> 投笔不是命运已经改变，只是他把志向说出了口。
>
> 下一集：他还要走多远，才真正走向西域？

### 台词边界

- “大丈夫……安能久事笔研间乎？”是史料原句的节选，省略号代表省略中段，不得把节选误标为完整原句。
- “小子安知壮士志哉！”沿用一手文本。
- 其余文字为第三人称纪录式旁白；其中演绎内容已在 Claim Ledger 标记。
- 目标时长 72 秒是静态编辑估算，不等于已完成 TTS 或真人配音计时。

## 4. 7 镜 Beat Sheet

| 镜头 | 时间 | 画面与动作 | 声音 | 标签 | 当前边界 |
|---|---:|---|---|---|---|
| P01-S01 | 00:00–00:05 | 书写动作微距；画面先不展示可辨识文字，也不锁定纸、帛或简牍材质 | 旁白第一句；笔触与室内底噪 | `[F+A]` | 只建立“佣书”处境，不冻结书写材料 |
| P01-S02 | 00:05–00:13 | 同一抄书空间内，以低细节墨色叠影表现班固受召、班超随母到洛阳 | 旁白第二句 | `[F+A]` | 叠影是时间压缩，不新增实体地点 |
| P01-S03 | 00:13–00:23 | 班超持续抄写；交付与家计仅用动作暗示，不出现未经核实的币制细节 | 旁白第三句 | `[F+I]` | “维持家计”不扩写具体收入与支付方式 |
| P01-S04 | 00:23–00:33 | 黄昏光线变化；手指发僵、袖口磨旧，明确作为劳动状态演绎 | 旁白第四句 | `[A+V]` | 不宣传为史料记载的具体外貌或伤势 |
| P01-S05 | 00:33–00:46 | 班超停笔；从伏案状态起身，投下手中笔；不做英雄化慢动作 | 旁白引入 + 班超史料台词 | `[F+A]` | 笔落点、手势和空间调度需在视觉合同中锁定 |
| P01-S06 | 00:46–00:54 | 同室人物在画外或虚焦处发笑；班超不转成怒吼，只作克制回应 | 旁人笑声 + 班超史料台词 | `[F+A]` | 群像不新增有姓名角色 |
| P01-S07 | 00:54–01:12 | 笔留在案上；画面不跳入军旅，以时间留白和片尾钩子结束 | 旁白纠正“当天从军”错误因果，并预告 P02 | `[F+I+A]` | 不提前生成军旅服装、兵器或战场 |

机械检查：

```text
duration: 72 seconds
shot_count: 7
major_location_count: 1
speaking_roles: narrator + Ban Chao
background_ensemble: unnamed / no independent dialogue
```

## 5. Claim Ledger

| Claim ID | 脚本主张 | 标签 | 来源或依据 | 处理结论 |
|---|---|---|---|---|
| P01-C01 | 永平五年，班固被召任校书郎 | `[F]` | 《后汉书》卷四十七《班超传》起首段 | 保留为确定性主张 |
| P01-C02 | 班超与母亲随至洛阳 | `[F]` | 同上：“超与母随至洛阳” | 保留为确定性主张 |
| P01-C03 | 家贫，班超常为官佣书以供养 | `[F]` | 同上：“家贫，常为官佣书以供养” | 旁白收敛为“维持家计”，不扩写具体收入 |
| P01-C04 | 佣书经历“久劳苦” | `[F]` | 同上：“久劳苦” | 保留为本集处境核心 |
| P01-C05 | 班超曾辍业投笔并表达立功异域、不久事笔研的志向 | `[F]` | 同上：“尝辍业投笔叹曰……” | 使用史料原句节选，明确省略中段 |
| P01-C06 | 旁人笑他，他回答“小子安知壮士志哉” | `[F]` | 同上 | 保留为唯一第二段直接对白 |
| P01-C07 | 投笔后不是当天从军；“久之”后任兰台令史，后因事免官 | `[F+I]` | 《班超传》先写“久之……除兰台令史，后坐事免官”，到永平十六年才进入窦固军旅叙事 | 明确阻断“投笔即从军”的错误因果 |
| P01-C08 | 把长期劳作压缩进一个黄昏 | `[A]` | 来自“久劳苦”的短视频叙事压缩 | 旁白主动说明为演绎 |
| P01-C09 | 手指发僵、袖口磨旧、具体停笔动作 | `[V]` | 用于把长期劳动转化为可见动作 | 不宣传为史料明文 |
| P01-C10 | 投笔是他第一次把志向说出口 | `[I]` | 仅限《班超传》现存叙事中的首次明确表达 | 脚本用“只是他把志向说出了口”，避免绝对化其一生 |
| P01-C11 | 精确书写材料、官府抄书空间、服装、灯具、货币、笔墨器具形制 | `[待核实]` | 当前 Story Bible 已登记物质文化门禁；本 Unit 未完成专项考据 | 不进入确定性旁白；视觉生成前必须 resolve / bound / exclude |

## 6. Gate A｜史实与脚本

| 检查 | 结果 | 依据 |
|---|---|---|
| 主张追溯 | `PASS` | 所有确定性主张已定位至《班超传》起首段及后续时间顺序 |
| 演绎标记 | `PASS` | 黄昏压缩、疲劳动作、镜头调度均已标记 `[A]/[V]` |
| 时间因果 | `PASS` | 明确写出投笔并非当天从军，并保留“久之—兰台令史—免官”的中间阶段 |
| 人物与数量 | `PASS_NOT_APPLICABLE_TO_LATER_CAST` | 本集只出现班超、班固、母亲与无名同室群像；未进入郭恂、鄯善王广或三十六吏士 |
| 单集叙事 | `PASS` | 只回答“成为班超以前，他是谁”，形成处境—愿望—选择—变化 |
| 平台合同 | `PASS_STATIC` | 9:16、72 秒、7 镜、1 个主要地点、2 个说话角色 |
| 实际配音计时 | `NOT_VERIFIED` | 尚未生成 TTS 或真人配音，不用静态估算替代运行证据 |

最终结论：

```text
GATE_A = PASS_WITH_VISUAL_HOLDS
```

## 7. 视觉前置 Hold

进入图片生成前，只允许先建立最小视觉身份合同并生成三张身份关键帧。以下内容不得从通用古装模板中猜测：

1. 班超在洛阳佣书阶段的年龄感、脸部识别特征与劳动体态；
2. 官府佣书空间的最小可信结构；
3. 书写材料、笔墨器具、灯具、服装和发式；
4. “投笔”动作的笔、手、案面和落点连续性；
5. 与既有 S1 canonical storyboard reference 的关系：本试播是独立 `candidate_not_canonical`，不得覆盖 194 张现有 reference。

## 8. 未验证项

```text
actual_voice_duration
visual_distinctiveness
cross_episode_identity_consistency
material_culture_accuracy
blind_visual_review
audience_comprehension
actual_production_cost
xiaohongshu_publication_performance
```

## 9. 下一执行单元

```text
PILOT_EP01_VISUAL_IDENTITY_CONTRACT_AND_THREE_KEYFRAMES
```

输出必须包括：

- P01 班超最小身份合同；
- 三张 9:16 独立关键身份帧：
  1. 佣书状态；
  2. 久劳苦状态；
  3. 投笔后克制回应状态；
- 每张图的 Prompt、生成记录和原始文件身份；
- 同一人物识别盲测；
- 物质文化现代元素门禁；
- Gate B 的首轮真实结论，不预设百分比分数。
