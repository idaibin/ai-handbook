# Agents Index Run — agent-framework first partition

- run_id: `agents-index-20260809T151450Z`
- observed_at: `2026-08-09T15:14:50Z`
- query: `AI agent framework stars:>=1000`
- authority_basis: `idaibin/ai-handbook@da9416532852bb8e8a5398b8bcfea6cb9d8ac6f1`
- evidence_level: `metadata_verified`

## Pagination evidence

| Page | Per page | Returned |
| ---: | ---: | ---: |
| 1 | 100 | 100 |
| 2 | 100 | 21 |
| 3 | 100 | 0 |

The first empty page is the deterministic terminal condition. Pages 4–10 were not requested.

## Reconciliation

| Result | Count |
| --- | ---: |
| Search hits | 121 |
| Normalized unique identities | 121 |
| Duplicates against canonical index | 0 |
| Eligible | 94 |
| Held | 6 |
| Rejected | 21 |

The GitHub search query verified the `stars:>=1000` floor. The connector projection did not expose exact star, fork, issue, fork-status, disabled, license, or repository-description fields; unsupported values are recorded as `null`, and descriptions are explicitly synthesized from root READMEs.

## First deep-analysis candidates

- `agent0ai/agent-zero@5ff106a2d489d17c2a3b378521a8f29fb29cf77d`
- `microsoft/agent-framework@5eb3eb745e16324ac7bffb1dbe006d8f13c8d993`
- `microsoft/autogen@027ecf0a379bcc1d09956d46d12d44a3ad9cee14`
- `zai-org/Open-AutoGLM@86f55382982fb054e8fc98ca80609dff8a2cdc3c`
- `TEN-framework/ten-framework@1b78cb725910d6f63389ef4ae69b182854d5b9d9`
- `pydantic/pydantic-ai@fc6a3ac506513150e2016ee5ba9785d792795150`
- `openai/openai-agents-python@e3d7c1727bf43761afbb7954651b7f908a973a3b`
- `alibaba/spring-ai-alibaba@9aee0f1a86f59fcf284628a922d68ef71a4e2c85`
- `livekit/agents@02569a40794645195bd92003431e5197ea413922`
- `FoundationAgents/MetaGPT@11cdf466d042aece04fc6cfd13b28e1a70341b1f`

## Held

- `humanlayer/12-factor-agents`: Primary source for agent engineering principles with scaffolding, but the root repository is not itself an agent runtime.
- `agi-inc/agent-protocol`: Agent communication specification is relevant infrastructure, but executable runtime ownership is unclear in this index pass.
- `open-mercato/open-mercato`: 主要是AI工程基础/业务框架，agents作为代码辅助与技能执行层而非核心产品。
- `CommandCodeAI/BaseAI`: README明确曾是可组合智能体框架但已宣告弃用并迁移到Langbase primitives；get_repo却未标记archived。
- `truefoundry/cognita`: Archived and no longer maintained; primarily production RAG infrastructure rather than a current agent runtime.
- `dot-agent/nextpy`: Self-modifying software framework is described, but README marks it an early friends-stage project and the agent execution boundary is unclear in an index pass.

## Rejected

- `obra/superpowers`: Coding-agent skills and development methodology, not a repository-owned agent runtime.
- `pestphp/pest`: General PHP testing framework marketed to developers and agents; no agent loop or agent-specific evaluation runtime.
- `SerpentAI/SerpentAI`: Archived game-agent framework outside the LLM/generative-agent scope.
- `heygen-com/hyperframes`: Deterministic video-rendering framework consumed by agents; it does not implement an agent loop.
- `caramaschiHG/awesome-ai-agents-2026`: Curated awesome list; no repository-owned agent implementation.
- `steel-dev/awesome-web-agents`: README identifies a curated awesome list, not an agent implementation or framework.
- `antvis/AVA`: README's primary scope is visual analytics and visualization generation, not general agent construction or execution.
- `e2b-dev/awesome-ai-sdks`: Curated awesome list; no repository-owned agent runtime.
- `xbtlin/ai-berkshire`: Agent skill collection rather than a repository-owned agent loop.
- `deanpeters/Product-Manager-Skills`: Product-management skill collection rather than an agent runtime.
- `Ar9av/obsidian-wiki`: Agent-operated knowledge and skills collection rather than an agent runtime.
- `Farama-Foundation/Arcade-Learning-Environment`: 这里的agent是Atari强化学习/游戏代理，不属于LLM或生成式AI智能体主题。
- `Meirtz/Awesome-Context-Engineering`: Curated context-engineering survey/resources; no repository-owned agent runtime.
- `victordibia/autogen-ui`: Example UI over AutoGen teams; topic rules exclude UI-only repositories.
- `trycua/acu`: Curated awesome list; no repository-owned agent runtime.
- `wondelai/skills`: Agent Skills collection; no repository-owned agent loop or runtime in scope.
- `mukul975/Anthropic-Cybersecurity-Skills`: Cybersecurity skill library, not an implemented agent loop.
- `datopian/portaljs`: Data portal framework assisted by external coding-agent skills; not an agent runtime.
- `alpic-ai/skybridge`: MCP Apps and server UI framework; no implemented agent loop is established by the root README.
- `cirosantilli/china-dictatorship`: Unrelated repository; root README unavailable and repository identity is outside the Agents topic.
- `gege-circle/.github`: Organization profile content unrelated to AI agents.

## Published snapshot

`agents-agent-framework-20260809T151450Z` contains 94 fixed default-branch HEAD candidates. This index pass did not inspect implementation paths, tests, builds, or runtime behavior.

## Next shard

`coding-agent:first-partition`
