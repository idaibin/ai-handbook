# 学习路径：产出驱动 v0.2

学习不按课程页数或固定周期推进，而由当前问题、可验证 Output 和证据门禁驱动。

## 双循环

```text
持续发现：发现 → 去重 → 分类 → 初筛 → 候选池
按需学习：问题 → 固定来源 → 阅读 → 汇总 → 图谱
          → 实验 → 应用 → Review → 输出 → 反馈
```

持续发现可以自动化；深度学习必须由用户委派、项目缺口或实验失败 Pull。

## 阶段

| 阶段 | Pull 条件 / Input | 必做 Output | 门禁证据 | 下一步 |
| --- | --- | --- | --- | --- |
| A. 定义问题 | 一个真实任务、能力缺口或待核实事件 | 目标、范围、I/O、约束、失败条件 | 他人可据此判断成功或失败 | 选择来源 |
| B. 发现与筛选 | 用户地址、Stars、官方索引、搜索结果 | canonical 去重候选和主来源选择 | 来源角色、身份、许可、新鲜度 | 固定版本阅读 |
| C. 阅读与汇总 | 固定主来源和明确问题 | 原子结论、边界、反例、冲突、开放问题 | locator 和实际阅读范围 | 更新知识图谱 |
| D. 图谱与假设 | 经来源支持的结论和项目上下文 | 图谱增量、方案、Prompt、实践假设 | 事实/推断/假设分开 | 最小实验 |
| E. 实验与评估 | 可证伪假设 | baseline、treatment、oracle、负例和结果 | 同环境可复跑，失败判据冻结 | 真实项目应用 |
| F. 应用 | 实验结果和明确目标仓库 | 代码或流程变更 | 固定 SHA、项目构建测试、Review | 路由输出 |
| G. 输出 | 已验证知识或方法 | Feed、知识产品、Skill 候选或工程规范 | 与证据范围匹配，权限边界明确 | 收集反馈 |
| H. 迭代 | 实际使用、错误、遗漏和过期信号 | 反馈、回归案例、候选修订 | 新 Evaluation 和独立 Review | 升级、保留或降级 |

## 每阶段最小包

```text
Input：对象、数据、约束、固定版本
Output：代码、知识、Feed 或可观察结果
Evidence：locator、命令、日志、测试、截图或评估
Scope：declared / source-resolved / local / target / runtime / production
Status：按 discovery、reading、verification、freshness、workflow、handoff 分维度记录
Residual gaps：未验证项、失败和下一条最小证据
```

统一状态定义见 [`../workflows/ai-engineering-system/state-model.yaml`](../workflows/ai-engineering-system/state-model.yaml)。

## 课程、书籍和仓库使用原则

- 课程、电子书和 Awesome List 是候选输入，不代表已经学习。
- 官方来源优先，但官方自述仍不能替代独立运行验证。
- 同一问题优先保留一个主来源；其他来源用于不同实现、冲突核对或失败案例。
- 进入课程前先写明它填补哪个 Output 缺口；完成后更新来源卡、知识图谱和实验/应用证据。
- 候选池可以很大；当新来源不再提供新模式或证据时停止扩张，转向实践。

## 输出路由

```text
实时信息       → feeds-hub
知识性对外内容 → knowledge-distillation
稳定执行方法   → idaibin/skills
项目代码与验证 → 目标项目仓库
研究与治理     → ai-handbook
```

一次本地成功不能直接形成生产 Skill 或生产完成声明。下游使用失败必须回到本路径的 H 阶段，形成反例和方法修订。
