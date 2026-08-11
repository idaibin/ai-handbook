# Knowledge Publication Architecture

- **Status:** approved target contract; implementation pending
- **Decision date:** 2026-08-11
- **Canonical owner:** `idaibin/ai-handbook`
- **Applies to:** `idaibin/ai-handbook`, `idaibin/blog`, `idaibin/feeds-hub`

本规范重构三个独立仓库之间的内容模型、晋级门禁和数据合同，不合并仓库。

## 1. 唯一职责

| 仓库 | 唯一职责 | 明确不承担 |
| --- | --- | --- |
| `feeds-hub` | 实时事件的来源、时间、身份、去重、核验、生命周期与查询/写入合同 | 稳定知识结论、公开知识页面和自动晋级 |
| `ai-handbook` | 来源、主张、概念、实践、工作流、实验、证据、新鲜度、冲突、晋级与公开资格的权威 | 实时信息门户和面向读者的站点展示 |
| `blog` | 已批准公开知识的双语静态阅读、导航、搜索、关系展示、SEO/RSS、变更记录和旧 URL 兼容 | 研究裁决、私有 Handbook 状态和 Feed 运行时读取 |

`knowledge-distillation` 继续生产课程、文章、知识卡和媒体内容包；它不是 Blog
知识节点和关系的权威。`skills` 继续拥有生产级可执行 Skill。

## 2. 单向晋级与反馈

```text
feeds-hub event
  -> explicit knowledge_candidate handoff
  -> ai-handbook research / synthesis / validation / promotion
  -> versioned public-knowledge export
  -> blog build-time import / static publication
  -> static correction link with public entityId + revision
  -> repository-owned issue triage
  -> ai-handbook correction candidate
```

- Feed 事件不会自动进入 Handbook 源文件，也不会自动发布。
- Blog 不在运行时读取 Handbook、Feed API、Neon 或本机目录。
- 读者纠错只通过显式静态链接进入仓库拥有的 Issue 模板；Blog 没有纠错后端，也不静默提交。

## 3. Handbook 知识模型

第一版持久对象类型：

- `source`
- `claim`
- `concept`
- `practice`
- `workflow`
- `tool`
- `skill`
- `project`
- `experiment`

`claim` 与 `experiment` 是内部证据/治理记录。它们可以通过字段白名单形成公开
evidence projection，但第一版不作为独立公开页面导出。

第一版公共页面类型：

- `concept`
- `practice`
- `workflow`
- `tool`
- `skill`
- `project`
- 被公开节点引用的 `source`

第一版关系枚举：

- `relatedTo`
- `broaderThan`
- `narrowerThan`
- `dependsOn`
- `implements`
- `uses`
- `contradicts`
- `supersedes`
- `derivedFrom`

关系目标使用跨语言稳定的 `entityId`。语言版本是同一实体的内容变体，不创建
`translationOf` 关系。

## 4. 身份、语言和 URL

- `entityId`：跨语言、跨版本稳定，实体级全局唯一。
- 公共内容变体键：(`entityId`, `language`)。
- slug 唯一范围：(`language`, `type`, `slug`)。
- 每个真实存在的语言变体单独输出；缺失译文不静默回退。
- Blog URL 由 `language + type + slug` 生成，关系图由 `entityId` 连接。
- 旧 URL 在迁移清单中保留 redirect 或 canonical 映射，完成验证前不得删除。

## 5. Public Knowledge v1

Handbook 在一个固定 Git commit 下生成：

```text
public-knowledge/
├── manifest.json
├── nodes.jsonl
├── edges.json
├── redirects.json
├── changelog.json
└── content/
    └── {entityId}.{language}.md
```

公共变体最小字段：

- `schemaVersion`
- `entityId`
- `type`
- `slug`
- `title`
- `summary`
- `language`
- `visibility`
- `relations`
- `sources`
- `evidence`
- `freshness`
- `handbookRevision`
- `publishedAt`
- `updatedAt`

模型名、模型参数、Prompt 或系统指令只有在内容被明确批准公开、完成脱敏且是复现
公开 practice/workflow/skill 所必需时才进入导出。凭据、账号数据、私有配置、原始
会话、客户数据、私有 URL、本机绝对路径和环境 secret 永不进入公共字段。

### 5.1 确定性和锁定

- artifact 是 `handbookRevision` 对应 Git commit 中的 `public-knowledge/` tree。
- 除 `manifest.json` 外，每个 payload 文件统一为 UTF-8、LF，并计算 SHA-256。
- JSON payload 使用稳定 key 顺序且不含无意义空白。
- `manifest.json` 按路径 UTF-8 字节序列升序列出 payload 路径和各自 SHA-256。
- `artifactSha256` 对排序后的 UTF-8 行
  `<file-sha256><two spaces><relative-path><LF>` 计算 SHA-256。
- `manifest.json` 不参与自身 artifact hash；它自己的 SHA-256 单独记录。
- Blog 的 `knowledge.lock` 固定 repository、完整 Git commit、export path、schema
  version、manifest SHA-256、artifact SHA-256 和同步时间。

### 5.2 Freshness

- Handbook 在导出时以 `evaluatedAt` 计算并固化公开 freshness。
- Blog 验证冻结值与 artifact 一致，不使用当前时钟重新裁决。
- 独立 freshness audit 在到期时生成新 artifact；旧锁定版本仍可重现。

### 5.3 验证所有权

Handbook 出口拒绝：

- 重复 `entityId` 或公共变体键；
- 同一语言/类型内重复 slug；
- 缺失关系目标；
- public 引用 private；
- verified claim 没有来源证据；
- freshness 与 `evaluatedAt` 不一致；
- 本机路径、凭据、Token、私有 URL 或禁止字段；
- 非确定性或手工修改的生成物；
- 已迁移页面缺 redirect/canonical。

Blog 只验证锁文件、schema、manifest/artifact hash、文件计数、内容/边完整性、
语言与路由映射、redirect/canonical 闭合；不重新读取或推断私有 Handbook 状态。

## 6. Feeds Candidate v1

`feeds-hub -> ai-handbook` 是显式候选 artifact 或请求，不是自动写入：

- `feedId`
- `slug`
- `feedVersion`
- `eventKey`
- `source`
- `sourceUrl`
- `eventAt`
- `observedAt`
- `contentHash`
- `candidateReason`
- `verificationStatus`

候选幂等身份为 (`feedId`, `eventKey`, `contentHash`)；`feedVersion` 只是来源快照和
并发元数据。Feed summary/tags 是发现提示，Handbook 必须读取原始来源后才能形成
verified claim。

## 7. Blog 目标信息架构

```text
/zh|en/concepts/{slug}
/zh|en/practices/{slug}
/zh|en/workflows/{slug}
/zh|en/tools/{slug}
/zh|en/skills/{slug}
/zh|en/projects/{slug}
/zh|en/sources/{entityId}
/zh|en/explore
/zh|en/changelog
```

Graph 只是 `/explore` 中使用 `edges.json` 的局部邻域视图。无 JavaScript 时必须
保留普通关系列表和完整阅读能力。Prompt 不再作为长期顶级知识类型，迁入
practice、workflow 或 skill。

## 8. 实施顺序和门禁

1. **Phase 0 — Inventory：** 固定现有内容、URL、语言配对、入站链接、重复项和拟议 owner；不改页面。
2. **Phase 1 — Contract Canary：** 冻结 v1 合同，用 5–8 个代表节点验证；不批量迁移。
3. **Phase 2 — Deterministic Export：** 只有 Blog 这一命名消费者进入实施后，才增加 exporter、fixture 和 validator。
4. **Phase 3 — Blog Canary：** 引入锁定快照、typed loader、新路由、search/backlinks/local graph 与旧 URL 测试。
5. **Phase 4 — Content Migration：** 按 owner 迁移剩余内容；保留仍有价值的长篇 editorial 内容。
6. **Phase 5 — Candidate And Feedback：** 最后启用 Feed candidate、freshness audit 和 correction loop。

每阶段必须能退回上一份已验证 artifact 或旧路由。Phase 0–1 只建立规范和小样本，
不授权公开发布、部署、提交或推送。

## 9. 明确不做

- 不合并三个仓库。
- 不新增图数据库、向量数据库、GraphRAG 或运行时 federation。
- 不新增第二套工作流/状态机或专用 CLI。
- 不让 Blog 复制整个私有 Handbook 或连接 Feed 运行时数据库。
- 不让 AI 自动晋级、自动建立公开关系或自动发布。
- 不把全局 3D Graph 或重型 SPA 作为主要界面。
