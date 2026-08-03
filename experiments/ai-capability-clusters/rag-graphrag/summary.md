# Summary

词项 baseline 在多跳问题上返回 `d1`，不能直接证明 Paris；treatment 仅从问题文本识别多跳并沿 `d1 -> d2` 等冻结边扩展证据，故意扰动的 `kind` 标签不参与路由。结果拆分 lexical Recall@k、graph/path recall、扩展步数预算和 direct-only accuracy，并报告 baseline/treatment direct regression；oracle 逐题检查推断类型、答案、证据、路径及 expansion steps，且 budget keys 必须完整对应问题 ID。
