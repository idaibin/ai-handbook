## C01

| Candidate | fidelity | instruction/structure | clarity | naturalness | restraint | hard_issue | evidence |
|---|---:|---:|---:|---:|---:|---|---|
| A | 5 | 5 | 5 | 5 | 5 | 无 | 五项职责各占一个语义单元；资产类型、唯一事实源限制、Sheets 双重限制及自动化三项禁区均完整保留。 |
| B | 3 | 5 | 5 | 5 | 3 | 将“不能自动提升证据等级”改为“不能提升证据等级”，删除了 automatic-only 范围。 | 五项结构清楚，但把只针对自动行为的禁令强化成无条件禁令。 |
| C | 5 | 3 | 4 | 3 | 3 | 无 | 内容和模态完整，但把 Sheets 限制及自动化允许/禁止项拆成多个同级 bullet，五项职责被过度碎片化。 |
| D | 5 | 3 | 4 | 3 | 3 | 无 | 内容完整，但将 Sheets 的用途与限制拆开，并把自动化责任拆成四条，语义配对弱于原文。 |

Ranking: A > C = D > B

## C02

| Candidate | fidelity | instruction/structure | clarity | naturalness | restraint | hard_issue | evidence |
|---|---:|---:|---:|---:|---:|---|---|
| A | 3 | 5 | 5 | 5 | 3 | 将“应优先保留一个主来源”改成“应保留一个主来源”，把偏好强化为无条件要求。 | 其余偏好与反限制、课程前后动作和停止条件均正确配对。 |
| B | 5 | 2 | 4 | 2 | 2 | 无 | 事实完整，但主来源与其他来源用途、课程前后动作均被拆成多条，形成明显清单节奏并削弱限定关系。 |
| C | 5 | 3 | 5 | 3 | 3 | 无 | 内容完整；官方来源与独立验证、课程前后动作、候选池与停止条件分别被拆开，配对关系仍可恢复但不够紧密。 |
| D | 5 | 5 | 5 | 5 | 5 | 无 | 五组主张及各自反限制、前后动作和停止条件均在同一语义单元内，模态完整。 |

Ranking: D > C > B > A

## C03

| Candidate | fidelity | instruction/structure | clarity | naturalness | restraint | hard_issue | evidence |
|---|---:|---:|---:|---:|---:|---|---|
| A | 5 | 3 | 5 | 3 | 3 | 无 | 设计焦点、授权边界和许可证边界均准确，但三组论证各被拆成两个 bullet，节奏机械。 |
| B | 5 | 3 | 5 | 3 | 3 | 无 | 三类边界及其限定均完整准确，但六条拆分造成不必要的碎片化。 |
| C | 5 | 5 | 5 | 5 | 5 | 无 | 用三个语义单元分别保留设计焦点与解释边界、房间权限与工具授权、代码许可与模型许可。 |
| D | 3 | 5 | 5 | 5 | 3 | 将“不能被理解为”改为“不能用作”，把解释边界强化成绝对不可用。 | 授权与许可证论证完整，但第一项出现 criterion 明确禁止的 claim-strength 变化。 |

Ranking: C > A = B > D

## C04

| Candidate | fidelity | instruction/structure | clarity | naturalness | restraint | hard_issue | evidence |
|---|---:|---:|---:|---:|---:|---|---|
| A | 5 | 3 | 4 | 3 | 3 | 无 | 四项论证和证据上限均保留，但被拆成八条；原因、限制和结论需要跨 bullet 重新配对。 |
| B | 5 | 5 | 5 | 5 | 5 | 无 | 四个 bullet 与四项论证一一对应，明确保留 durability 并非每次 Agent run 自动具备及未执行带来的证据上限。 |
| C | 3 | 4 | 4 | 5 | 3 | 省略了 durability “not an automatic property of every Agent run”的显式反限定。 | 仍说明进程内运行需由调用方持久化，但 criterion 特别要求的自动性边界只剩隐含。 |
| D | 5 | 3 | 5 | 4 | 3 | 无 | 所有主张与上限完整；前两项和 provider 论证被拆分，较原四项结构更碎，但因果仍清楚。 |

Ranking: B > D > A > C

## C05

| Candidate | fidelity | instruction/structure | clarity | naturalness | restraint | hard_issue | evidence |
|---|---:|---:|---:|---:|---:|---|---|
| A | 5 | 5 | 5 | 5 | 5 | 无 | 完整保留 commit/tree/blob 链路、SHA 复算、三类 locator 模态、反例及 fail-closed/token 行为。 |
| B | 5 | 5 | 5 | 5 | 5 | 无 | 验证链、复合 locator 全片段要求、heading/symbol/free-text 匹配规则和失败行为均完整准确。 |
| C | 5 | 5 | 5 | 5 | 5 | 无 | 所有校验步骤、匹配范围、`SECURITY.md#security` 反例及非零失败/不泄露 token 均保留。 |
| D | 5 | 5 | 5 | 5 | 5 | 无 | 三段分别组织验证链、locator 规则与反例、失败行为，信息和模态无缺失。 |

Ranking: A = B = C = D

## C06

| Candidate | fidelity | instruction/structure | clarity | naturalness | restraint | hard_issue | evidence |
|---|---:|---:|---:|---:|---:|---|---|
| A | 3 | 5 | 5 | 5 | 3 | 将“none can automatically make”改为“none can make”，删除 automatically，强化 exactly-once 限制。 | 五项发现、数量、示例及其余证据边界均完整，但 criterion 特别要求的自动化范围丢失。 |
| B | 5 | 5 | 5 | 5 | 5 | 无 | 五项发现完整；三项目、七类、五个 malformed、三个 multi-root、SSH 路径和 Golutra 正反证据均准确。 |
| C | 5 | 5 | 5 | 5 | 5 | 无 | 完整保留 automatically 范围、HITL 对照、至少七种 subtype、模板计数/风险及 README 证据上限。 |
| D | 5 | 5 | 5 | 3 | 4 | 无 | 实质内容、计数和范围完整，但首条中英文标点混用，第二条标题式改写略削弱自然度。 |

Ranking: B = C > D > A

## N01

| Candidate | fidelity | instruction/structure | clarity | naturalness | restraint | hard_issue | evidence |
|---|---:|---:|---:|---:|---:|---|---|
| A | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入逐项一致，八条事实、数字、范围和否定项均未改动。 |
| B | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入逐项一致，满足 conditional no-op。 |
| C | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入逐项一致，无增删、拆并或措辞强化。 |
| D | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入逐项一致，完整保留全部计数和限定。 |

Ranking: A = B = C = D

## N02

| Candidate | fidelity | instruction/structure | clarity | naturalness | restraint | hard_issue | evidence |
|---|---:|---:|---:|---:|---:|---|---|
| A | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，五项发现与证据边界均未改动。 |
| B | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，满足 conditional no-op。 |
| C | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，无事实、模态或结构变化。 |
| D | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，没有不必要改写。 |

Ranking: A = B = C = D

## N03

| Candidate | fidelity | instruction/structure | clarity | naturalness | restraint | hard_issue | evidence |
|---|---:|---:|---:|---:|---:|---|---|
| A | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，九项筛选问题逐项保留。 |
| B | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，满足 conditional no-op。 |
| C | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，无增删、重排或改写。 |
| D | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，所有证据、许可与复核边界均保留。 |

Ranking: A = B = C = D

## N04

| Candidate | fidelity | instruction/structure | clarity | naturalness | restraint | hard_issue | evidence |
|---|---:|---:|---:|---:|---:|---|---|
| A | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，九步流程、先后条件、字段和原子提交要求均保留。 |
| B | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，满足 conditional no-op。 |
| C | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，无事实、顺序或结构变化。 |
| D | 5 | 5 | 5 | 5 | 5 | 无 | 与已紧凑输入完全一致，没有不必要改写。 |

Ranking: A = B = C = D
