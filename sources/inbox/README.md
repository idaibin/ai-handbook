# Source Inbox

本目录保存尚未进入正式来源目录的高优先级候选。Inbox 记录只代表“已发现”，不代表已经阅读、验证或推荐。

进入正式来源目录前必须：

1. 解析 canonical identity 并去重；
2. 确定领域、来源类型和来源角色；
3. 检查官方身份、许可证和访问边界；
4. 说明它要解决的问题和预期输出；
5. 按实际阶段填写 `discovery_status`，允许值以[既有状态合同](../../workflows/ai-engineering-system/state-model.yaml)为准；尚未决定采用时记录待核原因，不默认升级为 `selected`。

“待观察”可以写在说明中，但 `watchlist` 不是该合同中的 `discovery_status` 值，不新增一套状态枚举。是否已完成初筛、实际阅读或验证分别依各维度证据判断；收藏或列入 Inbox 不会自动提高阅读／验证状态。

同一地址重复提供只更新 `origins` 或重复记录，不新增唯一来源。
