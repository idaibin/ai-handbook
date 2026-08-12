# Changelog

## 0.4.0-candidate.1 — 2026-08-12

- 根据“局部小改仍默认完整构建”的反例，新增验证预算候选规范。
- 验证在修改完成后按需触发，按主张、风险和影响边界选择最小充分层级，不把长规则复制进 `AGENTS.md`。
- 明确构建、运行时与浏览器验证的升级条件，以及完整仓库构建的有限适用范围。
- 增加验证预算回归案例；等待更多真实任务试运行和独立 Review 后再决定是否合并并晋级为正式 MINOR。

## 0.3.0 — 2026-08-11

- 明确 `feeds-hub`、`ai-handbook`、`blog` 保持独立，只重构内容模型、晋级门禁和数据合同。
- 增加 Handbook 权威知识模型、确定性 Public Knowledge v1 导出和 Blog 固定快照消费边界。
- 增加 `knowledge_candidate` 与 `public_knowledge_export` 交接模板。
- 固定双语实体身份、Feed 候选幂等键、freshness 评估时点、artifact hash 和读者纠错边界。
- 明确不引入图/向量数据库、运行时跨仓库读取、第二套状态机、自动晋级或自动发布。

## 0.2.0 — 2026-08-03

- 将 `ai-handbook` 明确为学习与治理控制面。
- 建立持续发现与按需深研双循环。
- 固定 `feeds-hub`、`knowledge-distillation`、`skills` 和目标项目仓库的职责边界。
- 增加来源治理、存储、状态、Skill 验证和跨仓库交接合同。
- 明确 Google Drive、ChatGPT Library、Project Sources 和 Google Sheets 的非重叠用途。
- 增加 fail-closed 外部写入、证据范围和受控自我迭代规则。
- 保存 ChatGPT Work 项目指令的版本化副本。

## 0.1.0 — 2026-08-03

- 建立来源台账、学习地图、阶段门禁、固定来源覆盖和 AI 能力簇实验基础。
