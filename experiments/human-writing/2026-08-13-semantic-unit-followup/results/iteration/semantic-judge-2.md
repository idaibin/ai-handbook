# Semantic Blind Review — T11–T16

## T11

### A

- Fidelity: 2/5
- Instruction/structure: 2/5
- Clarity: 4/5
- Naturalness: 5/5
- Restraint: 4/5
- Hard issue: true
- Evidence: 指令要求“每项对应一个事实”，但 A 将“官方来源优先”与“官方自述不能替代独立运行验证”合并为一项，又将“保留一个主来源”与“其他来源的用途”合并为一项，属于明确的结构指令违反；因此 Fidelity 和 Instruction/structure 按 rubric 封顶为 2。
- 理由: 四项事实均可辨认且逻辑关系清楚，文字也自然，但两条各承载两个事实，未满足核心粒度要求。

### B

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 四个源句分别成为四个条目，没有增删事实、改变限定或引入新关系。
- 理由: 逐事实拆分准确、清晰，改动仅限于完成所要求的列表化。

Ranking: B > A

## T12

### A

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 三个 claim 分列为三项，且 `Agent` 与 `run identity/history` 均逐字保留。
- 理由: 完整保留事实、主语、责任主体和 protected spans，同时严格做到一项一个 claim。

### B

- Fidelity: 2/5
- Instruction/structure: 2/5
- Clarity: 3/5
- Naturalness: 3/5
- Restraint: 3/5
- Hard issue: true
- Evidence: 指令明确要求“one item per claim”，B 却把三个独立 claim 压入一个条目，属于明确指令违反；因此 Fidelity 和 Instruction/structure 按 rubric 封顶为 2。两个 protected spans 虽然均有保留，但不能消除该 hard issue。
- 理由: 事实仍在且语法可读，但单个长条目需要读者自行拆解三层断言，核心结构要求未完成。

Ranking: A > B

## T13

### A

- Fidelity: 5/5
- Instruction/structure: 3/5
- Clarity: 3/5
- Naturalness: 3/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 四个动作及其顺序均保留，编号 1–4 也存在；但所有编号仍挤在同一行，列表边界不够显著。packet 中没有可见证据表明其删改了事实或明确遗漏了 protected 内容。
- 理由: 内容准确且改动克制，但几乎原样返回，未充分改善编号列表的可读性，成品感较弱。

### B

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 四个动作、原顺序和 1–4 编号全部保留，每个编号独立成行；没有新增或删减事实。
- 理由: 在不改写有效措辞的前提下，将编号列表整理成自然、清楚的成品，格式调整具有直接阅读收益。

Ranking: B > A

## T14

### A

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 候选池扩张、停止条件、停止后的转向、进入课程前的要求以及完成后的更新均被保留；停止条件与其后果合并在同一条，两个独立的前后续动作则分开列出。
- 理由: 每项都形成可独立执行或判断的完整决策，相关条件与后果紧邻，独立动作没有被不必要地捆绑。

### B

- Fidelity: 5/5
- Instruction/structure: 3/5
- Clarity: 4/5
- Naturalness: 4/5
- Restraint: 3/5
- Hard issue: false
- Evidence: 所有事实仍然可见；但第一项合并“可以继续扩大”“满足条件时停止”“停止后转向实践”，第二项又合并进入课程前与完成后的两个阶段性动作，条目粒度过大。
- 理由: 逻辑大体清楚，但把多个独立决策或不同阶段动作压在同一项中，弱化了“每项表达一个完整决策”的结构效果。

Ranking: A > B

## T15

### A

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 恰为两个条目；许可范围及模型审查构成第一组，房间访问、工具授权与审批层构成第二组；`Apache-2.0`、`MODEL_LICENSE`、`function tools` 均逐字保留。
- 理由: 分组与源文的两个主题完全一致，限制、后续要求和区别关系都清晰自然。

### B

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 4/5
- Naturalness: 4/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 同样恰为两个条目，全部事实和三个 protected spans 均保留；第一项后半以逗号衔接“使用这些模型前需……”稍弱于 A 的分号层级，但未改变关系。
- 理由: 实质上完整合规，仅第一项的内部标点层次略显拥挤，使许可例外与审查要求的边界不如 A 立即清楚。

Ranking: A > B

## T16

### A

- Fidelity: 4/5
- Instruction/structure: 4/5
- Clarity: 4/5
- Naturalness: 5/5
- Restraint: 4/5
- Hard issue: false
- Evidence: 恰为三项且六个事实全部可见；不过第二项把源文明确的“so”因果衔接改为句号并列，第三项也用句号弱化了同一人类门控对比的显式衔接。
- 理由: 读者仍能从同一条目恢复两组关系，内容自然易读，但两处关系的显式程度略有下降。

### B

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 恰为三项；每项分别组合一组相关断言。“because nothing was executed…”保留了未执行与运行时正确性未验证之间的因果关系，第三项以分号维持显式审批等待点与仅靠 prompt wording 之间的门控对照。
- 理由: 事实、因果、限制和对比都完整保留，并以三条清楚且自然地呈现。

Ranking: B > A
