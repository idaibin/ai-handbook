# Handbook — Knowledge & Reference Hub

- **维护定位：** 为 Forgeway 与 Craftway 提供可追溯的方案、UI、工具、Skills、Prompt 和创作参考。
- **本轮核对：** 2026-10-27（北京时间）；仓库保留 `idaibin/ai-handbook`，不改名。
- **范围：** 来源、主题地图、研究结论和验证状态。源码、实现、运行配置与内容运营仍由原 owner 维护。

Handbook、Forgeway、Craftway 是长期保留的三条主线，不被临时任务替代。

- **Forgeway：** 完整 IT 研发交付，覆盖 PRD、架构、UI、代码、测试、构建与部署；管理调度，不复制各仓执行能力。
- **Handbook：** Knowledge & Reference Hub，维护资料完整索引与地图，以及来源、版本、许可、取舍、证据和下游映射。
- **Craftway：** 以 AI 内容和个人 IP 为主，后续规划教育、健康内容与变现；规划不构成平台发布授权。

Craftway 为 2026-10-27 用户确认的当前名称，先前称 Creatorway，更早资料使用 Createway。此次仅同步显示名与解释；稳定 ID、仓库地址、目录及账号不变，历史记录保留原名。
资料维护不自动启动旧项目、安装工具、扩大资产授权或发布内容；Tokyo、Story Studio 等暂停项目不因补索引而恢复。

## 从哪里查

| 需要 | 既有入口 | 证据边界 |
| --- | --- | --- |
| 按主题找方案、UI、工具、Skills、Prompt | [主题地图](maps/README.md) | 导航到现有资料，不代表全部内容已验证 |
| 查原始来源、固定版本和阅读状态 | [来源目录](sources/README.md) | 候选、已读、运行验证分开 |
| 查项目、路由、外部资产及 owner 关系 | [Registry](registry/README.md) | 历史关系与当前运行状态分开 |
| 查已执行实验及局限 | [实验入口](experiments/README.md) | 仅采用具体运行记录支持的结论 |
| 查当前 Skills 精简建议 | [Skills 优化记录](research/agent-skills/skills-optimization.md) | 建议不等于实施或已证实收益 |
| 查配置归属与协作经验 | [Codex 配置与协作图](maps/codex-configuration-collaboration-map.md) | 脱敏观察；声明、已安装、实际加载与行为验证分开 |

## 使用与维护

复用现有来源台账、索引和地图；按明确问题补证、去重、追一手来源，记录日期、固定版本、许可、成本与验证状态。未知项保留未知。Skills、CLIs、Plugins 的执行能力真源留在各维护仓；借鉴优先，非必需不新增 Skill。旧批量研究的 [paused 边界](research/stage-reviews/2026-08-11-repository-research-stage-closure.md)仍有效，不恢复 Top20 重跑或顺序深研。

入口存在、链接有效或本地校验通过，不等于资产全验、项目可用或生产已发布。
私人 Library 不全量搬入仓库，也不自动同步收藏；大型、私有或受版权限制的原始资料保留在原 owner。
已完成的逻辑改动批次应在当前授权环境本地 Git 提交，不长期只保留 dirty。周内工作分支仅按明确授权同步远端；周结按下文约定审验后 squash 到 `main`；本地提交不等于已 push，也不自动推送或部署。

### 周分支与周结

- 以北京时间（`Asia/Shanghai`）的 ISO 自然周为单位：周一 00:00 至下周一 00:00（不含）；每周最多一个工作分支 `content/<ISO周所属年>-W<两位周数>`。本次为 `content/2026-W44`（2026-10-26 至 2026-11-01），承接已审三提交；原提交与保全包保留。
- 该周首个已授权改动前先核远端 `main`、同周分支、owner 和 dirty；已有同周分支则核清后复用，不重复创建。不接管其他 writer 或吸收旧分支的独有内容；前周未结算时先明确归属，不悄悄跨周搬运。新周从已同步的 `main` 开始，逻辑批次继续单独提交。
- 周结先冻结 `main` 基线、周分支 tip、本周精确路径/差异和审查测试证据，并保全原提交。只把该周已验 scope squash 为 `main` 上的一个提交；不提前结算、不夹带未审内容，也不重写原审查记录。若远端基线或候选变化，重新核差异并审查/测试受影响范围，不强推或覆盖。
- 远端写入须在明确授权范围内；成功回读远端 `main` 的提交、父链与预期内容后，才标记周结已同步，再安全同步本地；失败或结果未知时保留候选并核状态，不盲目重发。
- 清理周分支前必须确认无活跃 writer、无未交付独有内容、工作区干净且可从保全包恢复；核对冻结本周差异与 squash 结果，而不只依赖祖先关系。清理仅限获准的已结算周分支，不自动删除其他历史分支。

Prompt 内容范围包含独立的 `idaibin/prompts-hub`，见[主题地图中的 Prompt 入口](maps/README.md#prompt)。
保留独立仓、原 owner 和既有资产上传／allowlist／WebP quality 82／真实 URL 回读约束；一般内容维护不扩大资源发布授权。

## 历史执行记录

以下保留历史证据，不再作为三条长期主线的当前总入口或启动指令：

- [2026-08-22 v0.1 冻结与 v0.2 重启决定](decisions/2026-08-22-ai-engineering-lab-v0.1-freeze-and-v0.2-reset.md)
- [当时的唯一 MVP brief 与证据](mvp/story-studio-banchao-toubi-10s-v0.2.md)
- [v0.2 最小工作流的历史门禁](workflows/ai-engineering-system/README.md)
- [本次澄清前的 README 固定版本](https://github.com/idaibin/ai-handbook/blob/1859577953ae342dadf265a7e1172d4e62574c5f/README.md)

历史状态仍按原日期与范围解释。索引更新不改写既有实验结果、解冻其他项目或授权历史 next_action。
