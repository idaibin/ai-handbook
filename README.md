# AI Engineering Lab v0.2

- **Status:** `ACTIVE_MVP_STORY_STUDIO_PENDING_REVIEW`
- **Effective date:** 2026-08-22
- **Previous baseline:** `v0.1` archived at `fb61beeac1ac18dba4fd064cdefd892f5b4052eb`

AI Engineering Lab v0.2 只做一件事：用最小可运行结果验证真实价值。

当前只允许一个 MVP 活动。其他既有项目、Task、研究、架构扩展、资产生产和自动化继续冻结；历史代码、文档、实验和资产只作为证据。

## 当前唯一 MVP

Story Studio：班超《投笔》10 张关键分镜 / 10 秒视频验证，状态为 `ten_storyboard_frames_ready`。

- [MVP Brief、输出与证据](mvp/story-studio-banchao-toubi-10s-v0.2.md)
- 下一门禁：按 F01—F10、每张约 1 秒调用真实视频模型，最多 3 次；随后用户只做 `keep / change / stop` 决策
- 在决策前：不恢复 30/105 秒成片、G07 十单元或 24 集扩展；Forgeway 与 Skills 保持冻结

执行循环：

`Problem → Smallest Result → Run → Evidence → Keep / Change / Stop`

禁止新建平台、通用 Registry、通用 Workflow、新项目或大规模研究；除非当前 MVP 的运行证据证明它是不可缺少的最小依赖。

## 当前记录

- [v0.1 冻结归档与 v0.2 重启基线](decisions/2026-08-22-ai-engineering-lab-v0.1-freeze-and-v0.2-reset.md)
- [v0.2 最小工作流](workflows/ai-engineering-system/README.md)

旧 v0.1 内容可通过 Git 历史读取，不再具有当前执行权。
