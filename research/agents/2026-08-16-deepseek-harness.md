# 2026-08-16 — DeepSeek Harness：Everything is a Plugin

## 结论先行

DeepSeek Harness（`dsh`）不是“把 DeepSeek V4 接进一个 CLI”的薄壳，而是 DeepSeek 开源的一套 **Agent Runtime / Harness**：负责把模型、会话历史、工具、权限、沙箱、Skills、MCP、Hooks、Subagents、Workflow、UI/Headless 等能力组合成可运行 Agent。

它最重要的设计不是某一个工具，而是两条基础原则：

1. **Everything is a Plugin**：模型适配器、tool registry、session log、agent loop 都不是不可替换的“核心特权模块”，而是 Cordis plugin composition 的一部分。
2. **Session log + capability seams**：模型可见上下文必须能从 append-only session event log 重建；文件系统、shell、sandbox、subagent 等能力通过 Service Definition → Provider → Consumer 的 seam 解耦。

这使它更接近“可组合的 Agent 操作环境”，而不是普通的 coding-agent CLI。

但当前应把它视为 **developer preview / pre-release architecture**，不应直接等同于成熟生产框架。官方 V4-Pro 的高 Agent benchmark 也不能归因于 Harness 本身：这些结果同时受模型、prompt、tool set、effort、环境和 harness 配置影响，目前没有独立证据隔离出“换成 DeepSeek Harness”本身能带来多少收益。

**研究判断：值得深入学习其架构思想；值得做小规模真实任务验证；暂不建议把现有核心工作流整体迁移到它。**

---

## 1. 什么是 Harness？先把几个概念分开

可以把一个 AI Agent 想成“驾驶系统”：

- **Model**：负责推理与生成，相当于发动机。
- **Agent loop**：反复执行“观察 → 思考/请求模型 → 调工具 → 读结果 → 再继续”的循环。
- **Tool**：模型可以直接调用的动作，如读文件、执行 shell、搜索、创建 issue。
- **Skill**：可发现、按需加载的可复用指令/知识包，告诉 Agent “应该怎么做某类任务”。
- **Plugin**：扩展 Harness 本身的运行时组件；在 dsh 中甚至 Agent loop、模型适配器和 session log 都可以由 plugin 提供。
- **MCP**：连接外部 MCP server 的协议；它解决“外部能力怎么接进来”，并不负责整个 Agent 生命周期。
- **Hook**：生命周期拦截点上的外部回调/脚本桥接。
- **Harness**：把上面这些东西组织起来并真正执行任务的运行环境。

因此，**MCP 不是 Harness，Skill 也不是 Harness；它们只是 Harness 中的能力来源或扩展机制。**

DeepSeek Harness 的特别之处在于，它把传统框架里常见的“固定核心 + 周边插件”进一步推到“几乎所有东西都是可组合插件”。

---

## 2. 为什么 DeepSeek 要做 Harness

### Verified

DeepSeek 在 2026-07-31 的 V4-Flash 更新说明中明确写到，公开 Code Agent benchmark 使用了 **DeepSeek Harness minimal mode**，当时标注“to be released soon”。到 2026-08-13，官方 `deepseek-ai/deepseek-harness` 仓库已经公开；当前观察到的 HEAD 为：

`47f943859bef60e4160492346772ded9b24f765a`

该提交信息是 `release: dsh@0.1.0-rc.5 & publish the dsh family publicly`，时间为 2026-08-13。仓库 README 将项目定义为 open-source agent harness，口号为 **Everything is a Plugin**，并明确标记为 developer preview，未来存在 breaking changes。

同一时期 DeepSeek V4-Pro GA 的官方说明强调 Agent 能力，并给出 Terminal Bench 2.1、DeepSWE、Toolathlon 等多项 Agent benchmark 结果。这说明 Harness 并不是旁支工具，而是 DeepSeek 当前 Agent 产品化/评测链路的一部分。

### Inference

模型能力提升之后，真正影响 Agent 实际效果的已经不只是“模型聪不聪明”，还包括：

- 给模型什么上下文；
- 工具定义是否稳定；
- tool call 如何执行和回传；
- 失败如何恢复；
- shell/filesystem/sandbox 是否在同一 execution world；
- 是否能保存、fork、resume session；
- 是否能安全插入用户审批、hook、telemetry；
- 是否能在不同运行环境中复用同一 Agent 行为。

DeepSeek Harness 的核心目标可以理解为：**把这些“模型之外、但决定 Agent 能否稳定工作的部分”提升为一等架构对象。**

---

## 3. 核心架构：不是一个大 Agent，而是一棵 Plugin Tree

DeepSeek Harness 构建在 Cordis 上。Cordis 自己将可组合性拆成两个维度：

- **Temporal composability**：组件移除时，其副作用可以完整撤销；
- **Spatial composability**：组件声明依赖，并能对上下文变化做响应式管理。

Cordis 用 effect tracking、coeffect resolution、declarative loader、config reconciliation 和 HMR 实现这些目标。

在 dsh 中，plugin 向共享 context 注册 service、typed event 和 reversible effect。架构文档明确写道：模型 adapter、tool registry、session log、agent loop 都是 plugin，**不存在一个必须修改的 privileged core**。

### Profile / Bundle / Patch

运行一个 dsh profile，本质是启动一棵按层组合的 plugin tree：

```text
bundle layers
  ↓
profile patch
  ↓
home cordis.patch.yml
  ↓
CLI --patch
  ↓
最终运行时 plugin tree
```

官方提供 `web` 与 `headless` profile。基础 `dsh-base` 负责模型适配、tools、持久化、sandbox/approval、settings、credentials、telemetry；`dsh-web-app` 再加浏览器 UI；`dsh-headless` 则加一次性 runner。

这意味着“产品形态”不是另写一套 Agent，而是对同一能力树的不同 composition。

### 为什么这个设计重要

传统 Agent 框架经常出现这种演进：

```text
固定 AgentLoop
 + 一堆 if/else
 + tool hooks
 + provider adapters
 + 特殊模式
 + feature flags
```

随着 Browser、Remote Sandbox、Subagent、MCP、Approval、Hooks 增加，固定核心会越来越难改。

DeepSeek 的选择是把“替换能力”从特殊扩展点变成基础机制。好处是减少 fork；代价是 composition、event semantics 和配置系统本身会变复杂。

---

## 4. 一次真实 Turn 是怎么跑的

官方 architecture 将 **Step** 定义为“一次模型请求，以及该请求触发的工具调用”；一个 **Turn** 可以包含 0 个或多个 Step。

简化流程如下：

```text
turn/start
  ↓
claim input
  ↓
assemble system prompt + tool schemas
  ↓
agent/pre-step
  ↓
step/start
  ↓
写入 user message
  ↓
从 session log derive model history
  ↓
agent/request
  ↓
LLM stream
  ↓
assistant message/chunks
  ↓
若有 tool call
  ↓
tools pre-execute → execute → post-execute
  ↓
tool/result
  ↓
step/end
  ↓
需要继续？ → 下一 Step
  ↓
turn/end
```

这里有一个非常关键的设计：**Session log 是模型上下文的事实源。**

`core/session` 使用 append-only `SessionEvent` log；`deriveMessages()` 再把 durable events 投影成模型历史。user / assistant / tool / turn / step 等 durable facts 都从同一个事件流派生，fork、resume、transcript、telemetry、persistence 也复用这个来源。

官方给出的运行时不变量是：

> 任何模型可见内容，都必须能够从 log 重建。

这比“直接维护一个 mutable messages[]”更适合长期 Agent，因为恢复、审计、分叉、压缩、UI 展示都能围绕同一事实源工作。

---

## 5. Capability Seam：为什么 Sandbox、Shell、FS 可以换而不必改 Agent Loop

DeepSeek Harness 把关键能力抽象成：

```text
Service Definition
→ Provider
→ Consumer
```

例如 filesystem、subprocess、shell、sandbox、subagent 都通过这种 seam 接入。

最有价值的官方例子是：filesystem 与 subprocess 共享一个 execution world。如果把 provider 从 host implementation 换成 remote sandbox，Bash、PTY、LSP 可以随这个 execution world 一起迁移，而不是每个工具都做一套“remote version”。

### Inference

这个思想非常适合需要 local-first + cloud execution 共存的 Agent 系统：

- 本地项目：provider 指向本机 FS / shell；
- 云验证：provider 指向远端 sandbox；
- Agent loop、tool contract 和上层 workflow 尽量不变。

真正值得借鉴的不是 dsh 的 TypeScript API，而是 **把执行位置设计成 provider，而不是散落在每个 Tool 里面。**

---

## 6. Skills：它不是 Plugin，也不是把所有 SKILL.md 都塞进 Prompt

DeepSeek Harness 已有完整的 `skill/` capability family。

### Verified

官方定义：Skills 是 **reusable agent instructions**，通过 provider-neutral catalog 与 loader 暴露给模型。

结构是：

```text
ctx.skills
  ├─ local filesystem provider
  ├─ packaged / embedded provider
  ├─ future remote provider
  └─ ...
        ↓
model-facing skill catalog
        ↓
skill({ name }) tool 按需加载正文
```

当前本地 provider 会发现：

- `<projectRoot>/.dsh/skills`
- `<projectRoot>/.agents/skills`
- custom dirs
- user-level dsh / agents dirs
- configured bundled skills

支持目录型 `<name>/SKILL.md` 和 flat `<name>.md`。

更重要的是，它不会把 Skill 正文全部提前放进上下文。初始 session catalog 只包含模型可调用 Skill 的 `name + description`；模型真正需要时再执行 `skill({ name })` 加载完整内容。

每个 Skill 还有独立的 invocation policy：是否允许 model invocation、是否允许 user invocation。

### 为什么这值得关注

这解决了一个常见问题：Skills 越多，系统 prompt 越大。

DeepSeek 的方式是把 Skill 设计成：

```text
Discovery metadata（低成本）
→ Routing
→ On-demand full body（需要时才付 token）
```

这与 Tool schema 仍需常驻请求上下文形成鲜明对比。

### Inference

对于大型 Skills Catalog，这种“目录快照 + 按需 body loading”比“启动时拼接全部 Skill 文本”更可扩展，也更容易做 project/user scope、权限和 remote provider。

---

## 7. MCP：接入完整吗？目前不是

DeepSeek Harness 有官方 MCP client bridge，但当前边界很明确。

### Verified

`@deepseek-ai/dsh-mcp-client`：

- 支持 `stdio` 与 `streamable-http`；
- 每个 MCP server 对应一个 plugin instance；
- MCP tool 注册到 `ctx.tools`；
- 模型看到的名字形如 `mcp__github__create_issue`；
- 支持 `tools/list_changed` 重同步；
- 支持 tool-call timeout 与 abort；
- 支持断线后的指数退避重连与有限重试预算；
- tool generation 以 replace/rollback 的方式更新，避免半套工具残留；
- tool name 做稳定命名和冲突处理。

这里体现了 dsh 的一贯思路：**MCP 不是另建一套执行模型，而是一个把外部协议映射到内部 `ctx.tools` seam 的 plugin。**

### 当前明确限制

官方 README 明确列出：

- **只桥接 MCP Tools**；Resources 与 Prompts 尚无 Harness consumer，暂未实现；
- MCP non-text result 在模型上下文中的 native rendering 是有损的：image/audio/resource 等会变成 placeholder，完整 JSON 只保留在 execution-local canonical value；
- startup initialize / paginated tools/list 使用 SDK 默认 60 秒 timeout，dsh 暂未暴露单独配置；
- unsupported output-schema vocabulary 会退回 unconstrained `JsonValue`；
- Streamable HTTP 的连接失败恢复方式与 stdio supervisor 不完全相同。

因此，如果问题是“DeepSeek Harness 已经完整支持 MCP 吗”，答案是：**Tool 接入做得相当工程化，但并非完整 MCP capability coverage。**

### Token / KV Cache 的一个细节

官方文档还专门讨论了 MCP tool schema 的 token 和 KV-cache 影响：只要 MCP tools 已注册，schema cost 会进入每次模型请求；tool list/schema 改变可能从第一个变化 token 开始破坏 prefix cache reuse，而无变化的 reconnect 会生成稳定 tool definition。

这说明其设计不仅考虑“能不能连”，还考虑长 session 的上下文稳定性。

---

## 8. Hooks、ACP、SDK：不同边界，不要混在一起

### Hooks

Harness 内部真正的原生扩展面是 typed interception points。`hooks-claude-code` 与 `hooks-codex` 是 **bridge plugin**：把已有 Claude Code / Codex 外部 shell-hook 协议映射到 dsh 的内部 lifecycle extension surface。

因此：

```text
native Cordis plugin interception
≠ external shell hook
```

后者只是兼容桥。

### ACP

dsh 的 ACP（Agent Client Protocol）用于把 Harness Agent 暴露给 programmatic client，是 automation/interoperability transport，不是人机 UI 层。另有 out-of-process subagent ACP client 实现 subagent provider interface。

### SDK / JSON-RPC

仓库还包含 JSON-RPC protocol/server、TypeScript client、Python SDK/runtime。它们解决“外部程序怎样驱动 Agent”，而不是“模型怎样调用 Tool”。

把这些边界分清后，可以得到：

- MCP：外部能力 → Harness Tool
- ACP / SDK：外部程序 → Harness Agent
- Hook bridge：外部生命周期脚本 → Harness interception point
- Skill provider：可复用指令 → Harness catalog/loader
- Plugin：Harness 内部组件与扩展的统一组合单元

---

## 9. Subagent、Workflow、自修改：为什么它不只是 coding CLI

从官方仓库结构可以确认，dsh 已包含：

- `subagent` provider；
- worker-thread `workflow` provider + tool consumer；
- plan / todo；
- compaction；
- session persistence/projection/title/telemetry；
- sandbox 与 approval/permission；
- LSP、filesystem、shell、subprocess、terminal；
- self-modification：Agent 可检查并 mount 自己的 plugins；
- web/headless profiles；
- hooks / ACP / SDK / Python runtime。

这表明它的目标不是“给 DeepSeek 模型做一个终端界面”，而是尝试形成一整套 Agent runtime platform。

### 风险

尤其是 self-modification。Cordis 的 reversible effect / plugin unload 机制使动态 mount 在结构上比“运行时随便改全局状态”更可控，但它并不自动解决：

- plugin supply-chain；
- 权限扩大；
- secret exposure；
- prompt/tool injection；
- 恶意插件；
- 动态 composition 后的行为审计。

因此可逆 ≠ 安全，只是更容易恢复和治理。

---

## 10. DeepSeek V4 的效果，到底有多少是 Harness 带来的？

这是本次研究最需要避免的错误归因。

### Verified

DeepSeek 官方在 2026-08-13 V4-Pro GA 公布了多项较高 Agent benchmark，例如 Terminal Bench 2.1 87.9、DeepSWE 62.7、Toolathlon-Verified 74.1 等；2026-07-31 V4-Flash 的公开 Code Agent benchmark 则明确使用 DeepSeek Harness minimal mode。

### Not verified

目前没有找到官方或独立的严格 ablation：

```text
同一个模型
+ 同一个 benchmark
+ 同一 tools / prompt / effort / sandbox
只替换 Harness A vs Harness B
```

因此不能得出：

> “DeepSeek Harness 本身把 Terminal Bench 提升到了 87.9。”

正确说法只能是：**DeepSeek 将 Harness 作为其 Agent benchmark stack 的一部分；V4 + Harness 整体表现很强，但 Harness 的独立贡献尚未被隔离验证。**

这也是下一阶段真实验证最有价值的问题。

---

## 11. 与相关方案怎么理解

### 11.1 DeepSeek Harness vs MCP

它们不是竞争关系。

- MCP：协议层，解决外部 tools/resources/prompts 的标准连接。
- Harness：运行时层，解决 session、agent loop、context、tool execution、sandbox、approval、recovery、plugins 等。

dsh 的 MCP client 本身就是 Harness 的一个 plugin。

### 11.2 DeepSeek Harness vs Skills

也不是竞争关系。

- Skill：可复用任务知识/指令。
- Harness：决定 Skill 如何发现、路由、加载、进入 session、受什么 scope/policy 控制。

DeepSeek 的 `ctx.skills` 更像“Skill runtime substrate”。

### 11.3 DeepSeek Harness vs Codex / Claude Code 类产品

现阶段最重要的差异不是模型，而是开放程度与架构取向。

DeepSeek Harness 把自身 runtime、composition、skills、MCP、hook bridge、ACP 等大量底层机制直接开源，并允许替换 agent loop / service provider；这使它更适合研究和二次组合。

但 developer preview 的 breaking changes、较大的 TypeScript monorepo 和更复杂的 composition 模型，也意味着它目前未必比成熟产品更省维护成本。

这里不做“谁更强”的结论，因为缺少固定模型、固定任务、固定工具环境下的独立横向实测。

---

## 12. 真正值得借鉴的 5 个设计

### 1. Session Event Log 作为模型上下文事实源

不是让 `messages[]` 同时承担运行状态、审计、恢复和 UI，而是：

```text
Durable events
→ projection
→ model messages / UI / resume / fork / telemetry
```

这是长期 Agent 系统最值得直接借鉴的一点。

### 2. Capability seam，而不是到处写 provider-specific Tool

把 FS / Shell / Sandbox / Subagent 的运行位置封装在 provider 层，可减少 local/cloud 两套实现分叉。

### 3. Skill catalog 与正文分离

只把 `name + description` 放入可见 catalog，正文按需加载。这是 Skills 扩容后控制上下文成本的实用模式。

### 4. Plugin lifecycle 必须可撤销

插件不只是“注册一次 callback”，而要能在 unload/HMR/recompose 时撤销副作用。这对动态 Agent runtime 比传统 extension API 更重要。

### 5. 外部协议先映射到内部稳定 seam

MCP → `ctx.tools`，Claude/Codex hooks → interception points，ACP → agent automation surface。这样外部协议变化不会直接污染 Agent loop。

---

## 13. 不建议照搬的部分

### 1. 不要因为 Everything is a Plugin 就把所有业务逻辑插件化

dsh 是通用 Harness，需要极高可组合性。具体产品如果只有固定 runtime，过度 plugin 化会增加配置、生命周期、依赖和调试成本。

### 2. 不要把官方 benchmark 当作 Harness benchmark

当前证据不足以拆分模型与 Harness 的贡献。

### 3. 不要现在就把核心生产工作流绑定到 dsh API

官方明确是 developer preview，仓库自身也采取 pre-release、允许 breaking changes 的姿态。此时更合理的是验证架构思想和关键能力，而不是建立大量不可逆依赖。

### 4. MCP 不能假设“全能力支持”

如果实际需要 MCP Resources / Prompts 或模型侧 rich media，需要额外设计，当前官方 bridge 不覆盖。

---

## 14. 建议的真实验证，不做大迁移

下一步如果要验证 DeepSeek Harness，建议只做一个固定任务：

**同一真实仓库、同一模型、同一任务、同一工具边界，对比现有 Agent Harness 与 dsh。**

重点不是只看“任务成功没”，而是记录：

- 首次成功率；
- tool-call 次数与失败恢复；
- token/context 增长；
- Skill 加载是否准确；
- MCP tool schema 成本；
- session resume / fork 是否可靠；
- local → remote sandbox provider 切换成本；
- approval / hook / telemetry 的可观测性；
- 修改一个 capability 时是否真的无需 fork agent loop。

只有这一层真实证据出现后，才值得判断是否把其模式吸收到现有 Workflow / Skills / Agent 平台。

---

## 15. Evidence ledger

### Verified

- `deepseek-ai/deepseek-harness` 是 DeepSeek AI 官方开源 Agent Harness，MIT License。
- 观察基线 HEAD：`47f943859bef60e4160492346772ded9b24f765a`，2026-08-13，发布 `dsh@0.1.0-rc.5` family。
- 官方 README 标记 developer preview，并明确 “Everything is a Plugin”。
- 核心架构基于 Cordis；模型 adapter、tool registry、session log、agent loop 都可作为 plugin 组合。
- SessionEvent log 是 durable history；模型消息通过 projection 派生。
- Skills 使用 provider-neutral registry + catalog + on-demand loader；本地支持 `.dsh/skills` 和 `.agents/skills` 等来源。
- MCP client 当前支持 stdio / streamable-http，并将 MCP tools 注册到 `ctx.tools`；当前不桥接 MCP Resources / Prompts。
- Hook 子系统提供 Claude Code / Codex hook bridge；ACP 提供 programmatic agent transport。
- 2026-07-31 V4-Flash Code Agent benchmark 使用 DeepSeek Harness minimal mode；2026-08-13 V4-Pro 官方公布多项 Agent benchmark。

### Inference

- dsh 的架构方向更接近“Agent operating environment”而非单一 coding CLI。
- Capability seam 对 local-first / cloud execution 共存很有借鉴意义。
- Durable event log + projection 比 mutable message history 更适合作为长期 session 的可恢复事实源。
- Skill metadata/body 分离是大型 Skill Catalog 控制上下文成本的合理设计。

### Not verified / Evidence debt

- Harness 相对 Codex / Claude Code / OpenCode / Pi 等方案的独立质量收益尚无固定模型、固定任务的严格实测。
- 官方 V4 benchmark 无法隔离 Harness 的独立贡献。
- 本次未在真实项目运行 `dsh`，因此未声明安装、构建、runtime、MCP server、sandbox、hooks 等已通过实际验证。
- developer preview 的 API / plugin contract 后续稳定性尚不可预测。

---

## 一页式总结

**一句话理解**：DeepSeek Harness 是“模型之外的 Agent 运行时”，负责把 context、session、tools、sandbox、skills、MCP、hooks、subagents、workflow 等组合起来；最大特点是用 Cordis 将这些能力全部做成可动态组合和撤销的 plugins。

**最重要的架构思想**：

```text
Everything is a Plugin
+ Append-only Session Event Log
+ Capability Seams
+ Profile/Bundle Composition
+ Protocol Bridges
```

**最值得学的**：session event log 事实源、provider seam、Skill catalog/按需 loader、可撤销 plugin lifecycle、外部协议先映射到内部稳定接口。

**当前最大限制**：developer preview；MCP 目前只有 Tools；整体架构复杂度高；缺少能够隔离 Harness 独立贡献的第三方 benchmark。

**是否值得继续**：是。建议下一步做一次固定真实仓库的 Harness A/B 验证，而不是直接迁移核心工作流。

---

## 主要来源（观察日期：2026-08-16）

1. DeepSeek Harness official repository  
   https://github.com/deepseek-ai/deepseek-harness
2. Architecture  
   https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md
3. Capability seams  
   https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/capability-seams.md
4. Skills subsystem  
   https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md
5. MCP client bridge  
   https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/mcp/mcp-client/README.md
6. Hook bridges  
   https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/hooks/README.md
7. ACP  
   https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/acp/README.md
8. Cordis  
   https://github.com/cordiverse/cordis
9. DeepSeek API changelog  
   https://api-docs.deepseek.com/quick_start/pricing
   （官方 changelog / model update 页面中记录 V4-Flash/V4-Pro Agent benchmark 与 Harness minimal mode；页面结构可能后续调整。）

## Canonical research metadata

- Date: 2026-08-16
- Topic: DeepSeek Harness
- Source repository: `deepseek-ai/deepseek-harness`
- Fixed source commit: `47f943859bef60e4160492346772ded9b24f765a`
- Evidence level: static/source research; no runtime validation in this run
- Canonical location: `idaibin/ai-handbook/research/agents/2026-08-16-deepseek-harness.md`
