# T11

## A

- Fidelity: 2/5
- Instruction/structure: 2/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 4/5
- Hard issue: true
- Evidence: 指令要求“每项对应一个事实”，但 A 将“官方来源优先”与“官方自述不能替代独立运行验证”合并为一项，又将“保留一个主来源”与“其他来源的用途”合并为一项，属于可见的明确结构指令违反；依 rubric，Fidelity 与 Instruction/structure 封顶 2。
- Reason: 四个事实均仍可辨认，转折和用途关系也清楚自然，但两项承载四个事实，没有做到一事实一条。

## B

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 四个源句分别成为四个条目，未增删事实，也未改变条件、用途或主张强度。
- Reason: 精确满足一事实一项，改动仅限必要的列表化。

Ranking: B > A

# T12

## A

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 三个 claim 各占一项；`Agent` 与 `run identity/history` 均逐字保留，caller、plain in-process runs 及持久化对象也全部保留。
- Reason: 事实、受保护文本和一项一 claim 的结构均完整准确。

## B

- Fidelity: 2/5
- Instruction/structure: 2/5
- Clarity: 4/5
- Naturalness: 4/5
- Restraint: 4/5
- Hard issue: true
- Evidence: B 只给出一个 bullet，却在其中合并 durability 的性质、非自动属性以及 caller 的持久化要求三个 claim，明确违反“one item per claim”；依 rubric，Fidelity 与 Instruction/structure 封顶 2。受保护文本本身均有逐字保留。
- Reason: 内容可读且事实未被改写，但结构没有执行核心指令，分号串联也使信息更密。

Ranking: A > B

# T13

## A

- Fidelity: 5/5
- Instruction/structure: 4/5
- Clarity: 3/5
- Naturalness: 3/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 四个动作及其顺序、编号均完整保留；packet 中没有可指认为被遗漏的具体事实或受保护文本。其不足是把四个编号项继续压在同一行，列表边界主要依靠分号重建。
- Reason: 忠实且克制，但成品仍像原始的行内枚举，去模板化后的编辑可读性提升有限。

## B

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 四个编号项、动作和先后顺序均原样保留，只把每项独立排版，没有增加解释或删除事实。
- Reason: 独立分行使编号列表立即可扫读，同时没有不必要的文字改写。

Ranking: B > A

# T14

## A

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 扩大候选池、在无新模式或证据时停止并转向实践、课前标明 Output 缺口、完成后更新证据四组决策均保留；停止条件与其后果被放在同一项中。
- Reason: 条件、动作与后续转向的关系清楚，同时把课前和完成后的独立动作分开。

## B

- Fidelity: 5/5
- Instruction/structure: 3/5
- Clarity: 4/5
- Naturalness: 4/5
- Restraint: 3/5
- Hard issue: false
- Evidence: 可见事实均保留，也没有改变条件或时序；但第一项合并“可以扩大”、条件性停止和“转向实践”，第二项又合并课前说明缺口与完成后更新两项时点不同的独立动作。
- Reason: 两个生命周期式长条目仍可理解，但过度合并独立决策，尤其弱化了课前与完成后的操作边界。

Ranking: A > B

# T15

## A

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 恰为两个条目；`Apache-2.0`、`MODEL_LICENSE`、`function tools` 均逐字保留。代码许可、专有模型例外与审查要求构成第一项，房间访问、工具授权区别与审批层构成第二项。
- Reason: 两个主题分组准确，“但”明确呈现代码许可与模型许可之间的限制关系。

## B

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 4/5
- Naturalness: 4/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 同样恰为两个条目，全部事实和三个 protected span 均保留；与 A 相比，第一项以分号和逗号连接许可范围、例外及审查要求，逻辑仍准确但关系提示略弱。
- Reason: 完全合规且忠实，只是第一项的标点衔接稍显拥挤，不如 A 的显式转折自然清楚。

Ranking: A > B

# T16

## A

- Fidelity: 4/5
- Instruction/structure: 5/5
- Clarity: 4/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 恰为三个 bullets，六个可见陈述均保留；但第二项把源文明确的“Nothing was executed ... so runtime correctness remains unvalidated”因果连接拆成两个独立句，因果仍可由相邻位置推知，却不再明示。
- Reason: 分组和事实覆盖正确，唯一弱点是一个明确关系需要读者自行重建。

## B

- Fidelity: 5/5
- Instruction/structure: 5/5
- Clarity: 5/5
- Naturalness: 5/5
- Restraint: 5/5
- Hard issue: false
- Evidence: 恰为三个 bullets；每项分别保留 provider breadth 与跨 provider 行为限制、工程信号与未执行所导致的未验证状态、approval waitpoints 与 prompt wording 限制。第二项用“because”明确保留源文的因果关系。
- Reason: 三组相互依赖的主张分别成项，事实、限制及因果关系均立即清楚。

Ranking: B > A
