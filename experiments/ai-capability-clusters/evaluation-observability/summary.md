# Summary

baseline 在错误 trace 上能判 fail，却把安全违规、security+process unknown、缺 telemetry 和“仅 trace incomplete”的正常表象判成 pass，macro-F1 为 0.277777778、false-pass 为 4、security masking 为 2。treatment 先判 security fail，再让任何非 `true` 的 trace completeness（非安全失败）保持 unknown，六条 truth 全部匹配，macro-F1 为 1.0；输出 axes 保留 completeness，unknown 指标命名为 unknown_recall。

验证器不再信任 result 中回显的 axes 或 metrics：它由冻结 fixture 重建轴真相，并对每一轴字段、ID 集和派生指标 fail closed。结果只覆盖冻结 JSON trace 的判定逻辑；没有证明 telemetry collector 完整性、跨进程时序、真实安全事件或第三方 evaluator 的生产行为。
