# Experiments Index

`experiments/` 保存固定输入、Oracle、Baseline/Treatment、运行证据与明确边界的实验协议。
研究或设计文档不能替代实际 Trial，局部验证不能升级为通用能力结论。

## 当前实验

| 目录 | 类型 | 当前定位 |
| --- | --- | --- |
| [`ai-capability-clusters/`](./ai-capability-clusters/) | 能力聚类实验 | 固定 Fixture、Oracle、Baseline/Treatment 与应用案例。 |
| [`forgeway-full-chain-validation/`](./forgeway-full-chain-validation/) | 执行证据账本 | Forgeway 全链路社区项目验证；不等同于通用 Benchmark。 |
| [`repo-review-benchmark-v1/`](./repo-review-benchmark-v1/) | 固定 Benchmark 协议 | `repo-review` 与公开 Review Skills 的配对评测；数据集仍在构建。 |
| [`skills-forgeway-paired-evaluation-v1/`](./skills-forgeway-paired-evaluation-v1/) | 配对工程评测协议 | 基于 Harbor 与 Multi-SWE-bench 验证 A→B Skills 增益和 B→C Forgeway 增益；已定义[测试反馈与强化闭环](./skills-forgeway-paired-evaluation-v1/feedback-loop.md)，Phase 0 尚未执行。 |
| [`story-studio-60s-pilot/`](./story-studio-60s-pilot/) | 媒体生产 Pilot | Story Studio 60 秒生产链路的阶段性实验与证据。 |
| [`visual-registry-mvp-01/`](./visual-registry-mvp-01/) | Visual Contract、Prompt 1:N 与查询实验 | 保留合同、查询原型与证据；真实应用已迁出，目标仓库为 `idaibin/prompts-hub`，当前等待仓库创建。独立图片仍为 0/4。 |

## 维护规则

- 每个实验必须有固定 Basis、输入、Oracle、状态和未验证边界。
- 协议、实现、Trial 结果和最终结论必须分开标记。
- 基于测试反馈产生的修改必须建立新 Candidate 和 Result Series，不得覆盖旧 Trial。
- 大型原始日志与二进制证据可放 Google Drive，但 GitHub 必须保留不可变身份和索引。
- 开源 Harness 已提供的容器、调度、轨迹或 Verifier 能力不得在本仓库重复实现。
- 可运行产品代码必须进入对应产品仓库，不得长期存放在 `ai-handbook/experiments`。