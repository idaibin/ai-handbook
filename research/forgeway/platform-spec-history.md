# Platform Spec 历史

## 研究对象

这里的“Platform Spec”指当前 Forgeway Git 历史中的初始阶段；该阶段产生时仓库 slug
仍为 `project-delivery-system`。固定基线为：

```text
repository: /Users/daibin/Codex/repos/forgeway
commit: 6c5f234a8d3a7a3d46dca3a086bb8b3b6d55b348
date: 2026-08-09 08:53 +08:00
tree: README.md plus docs/ (five Markdown files)
```

本文件不把“Platform Spec”升级成独立仓库名称。当前证据只支持“同一仓库中的一个
初始设计阶段”；没有独立 remote、release 或 runtime 证据。

## 当时解决的问题

初始 README 将脚手架定位为脱敏、Markdown-first 的规格与验证起点，目标是把目标、
当前实现、证据和未决事项放在一条可复查链路上。它强调：

- 目标轴描述“应该怎样工作”，实现轴描述“现在怎样工作”；
- owner、固定 basis 和 ID 让事实可以被复查；
- 源码存在、构建成功和运行时正确不能互相冒充；
- 证据不足时必须保持 `Not verified`；
- 没有真实消费者时不增加额外 Schema、YAML、生成器或独立仓库。

这些是从该 commit 的 README 直接读取到的设计约束，不是对目标项目行为的验证。

## 五文件阶段的优点与限制

### 保留的语义

后续 PDS 和 Forgeway 仍保留了以下核心语义：固定 basis、目标 / 实现 authority
分离、owner、状态、Gap、变更记录和分层 Evidence。这些语义被迁移到更大的交付
合同中，而不是继续维护一套平行旧文件。

### 被替代的部分

仅靠五个 Markdown 文件无法承载后续阶段需要的：

- Requirement、Task、Change、Evidence 和 Portfolio 的机器可校验元数据；
- 正向 / 负向 fixtures 和可重复的 validation command；
- 多仓 / 多组件的 basis、owner 和 gate 聚合；
- Artifact handoff、结果封套和可恢复的执行记录。

因此 `7d4037b` 选择替换五文件布局，而不是在旁边再维护一棵兼容目录。这个取舍来自
`CHG-PDS-001` 的变更记录；没有证据表明旧脚手架被某个外部消费者继续作为运行时依赖。

## 不应从历史推断的内容

- 不能从占位符或模板推断具体项目、组织或生产系统已经采用 Platform Spec；
- 不能从五文件的状态词推断已经发生真实运行时验证；
- 不能从名称推断存在一个叫 platform-spec 的独立仓库；
- 不能把后续 PDS / Forgeway 的 Schema 和 workflow 复制回 handbook，形成第二套
  当前规范。

## 后续去向

`evolution.md` 记录了从此阶段到 PDS 和 Forgeway 的完整路径。Platform Spec 的有效
思想进入 Forgeway 当前产品合同；阶段名称和选择理由留在本目录。Forgeway 执行时不
读取本历史，也不需要安装或加载一个 Platform Spec runtime。
