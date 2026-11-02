# 来源卡：<来源名称>

本模板用于新增或按证据更新单条来源卡。来源规则见[来源管理](../workflows/ai-engineering-system/source-management.md)，状态字段与允许值以[既有状态合同](../workflows/ai-engineering-system/state-model.yaml)为准；本模板不另定义枚举，也不批量迁移历史记录。

- `id`：
- `url`：canonical URL；发现入口与实际支持结论的原始来源分开
- 来源类型、领域与角色：
- 固定版本、commit 或章节／locator：
- 来源发布日期／修订日期：未知时注明未知，不以访问日替代
- `checked_at`：实际访问日期与时区
- 许可、版权或访问边界：未知时注明未知，不以公开可读推定可再分发
- 成本：公开阅读／实际运行／外部服务分别记录；未测不填 0

## 状态

分别填写以下六个维度；允许值从状态合同选取，不以一个“完成”状态代替。尚无证据支持的维度标注“待核原因”，不要把该说明当作新增枚举值或自动填写 `current`、`runtime_verified`。

| 维度 | 本条状态值 | 对应证据或待核原因 |
| --- | --- | --- |
| `discovery_status` | | |
| `reading_status` | | |
| `verification_status` | | |
| `freshness_status` | | |
| `workflow_status` | | |
| `handoff_status` | | |

历史卡中的 `source_verification`、`learning_status` 保留原值与原日期，不自动映射或升级。`source_checked`／`metadata_checked` 不能直接当作独立验证、运行验证或生产验证；旧 `read`／`reproduced`／`applied`／`distilled` 也不能替代六维证据。

## Input

- 当前阶段与待填补的 Output 缺口：
- 前置知识、数据、环境、版本：

## Output

- 这个来源应带来的最小产出：
- 产出文件/命令/接口：

## 证据

- 来源归属与版本：
- 实际阅读范围／实际运行记录（分开记录，未运行明确注明）：
- 成功结果：
- 失败、反例、支持边界与未验证项：
- 证据文件或链接：

## 判断

- 是否保留为主来源：是 / 否
- 与现有来源的重复点：
- 适用范围与不适用范围：
- 下一条 Pull：
