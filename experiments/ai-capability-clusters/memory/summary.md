# Summary

Baseline 的全局 append-only 查询会把 u1 的 manager 交给 u2，并把 u2 的 team 交给 u1；删除后仍返回旧 manager，同时保留 secret。故 query receipt 实测 `query_scope_leak_count/rate` 为 2/6，而不是因 store provenance 为零误报为零。Treatment 以 `(user,key)` 作为 scope，upsert 覆盖矛盾更新、tombstone 删除，并拒绝显式 secret 与未标记但 sensitive key 的 secret；其 query 泄漏为 0。每个 answer receipt 保留 selected source user/scope，完整 store 的 source-user 不匹配单独报告为 `store_provenance_mismatch_count/rate`。

执行只读取 `fixtures.json.policy` 中预注册的 sensitive keys、forbidden returns 和期望查询值；oracle 只做独立 validation。篡改 oracle sensitive keys 不会改变 treatment 原始输出，但必定触发 validation；orphan fact、未分类 secret retain、跨用户 source 和 queried fact 篡改亦均会失败闭环。

这仍只覆盖冻结 JSON 的本地契约，不证明真实记忆系统、secret 分类器或生产租户隔离。
