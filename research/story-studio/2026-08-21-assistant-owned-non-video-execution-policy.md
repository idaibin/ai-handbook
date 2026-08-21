# Story Studio Assistant-Owned Non-Video Execution Policy

状态：`approved`  
生效时间：`2026-08-21`  
适用范围：Story Studio 当前及后续 Task 的非视频工作

## 决策

除实际视频生成外，Research、文档、代码、图像、角色/场景/道具资产、技术图、验证、Dailies、证据打包以及 Google Drive / GitHub 同步，默认均由当前执行助手直接完成。

非视频任务不得再把“新建专用会话”“交给外部 provider”或“由用户下载后执行”作为默认推进条件。只有当前工具确实不能产生目标类型，且不存在可验证的替代执行路径时，才能记录为阻塞。

## 执行规则

- 用户无需为非视频任务下载、转发或手工执行 Work Order。
- 同一 Task 控制会话可以直接执行非视频资产，不再要求 fresh asset chat。
- 图像模型输出、确定性 renderer 输出和来源文件直接派生输出都可以形成 `execution-native` 证据；不得把 resize、重编码或 Review derivative 标记为 native。
- 几何布局、机位、灯光、流程图和其他技术型资产可以使用确定性 renderer，但必须保存源码、运行时身份、原始 bytes、精确格式/尺寸、SHA-256，并完成可复现回读。
- 生成失败或错路由的报告图、信息图和无关内容必须记为 `invalid_output`，不得进入资产清单或 Gate。
- 实际视频生成仍可路由到具备视频能力的 provider/session；视频前后的脚本、分镜、提示词、Review、证据和同步仍由助手负责。

## 证据合同

每个可计数的非视频资产执行至少保存：

1. execution-native 原始文件；
2. execution receipt；
3. 精确格式、尺寸、字节数和 SHA-256；
4. `GenerationAttempt` 或等价执行记录；
5. `Dailies` / 人工验收；
6. Drive file ID 与回读证据；
7. 必要时保存源码和 byte-identical rerender 结果。

## Gate 边界

本政策只改变执行责任和合法执行路径，不降低验收要求。任何输出均不得自行升级为 Production Canon、G07 approved、`production_ready` 或 `publication_ready`。

## 本次落地

`VERTICAL_SLICE_02_LUOYANG_MINIMAL_SET` 已按该政策执行 `TAKE_02B`：

- execution-native PNG：1920×1080 RGB；
- SHA-256：`95875a2243294872f6defd0d31bd4be51edeacb6a3ccd0de40eba85ec10d13ff`；
- deterministic renderer 源码已保存；
- 两次重渲染 byte-identical；
- 自动校验和 Dailies 通过；
- `verified_G07_asset_executions` 从 `1/10` 更新为 `2/10`；
- `VERTICAL_SLICE_03_HERO_BRUSH` 已成为当前执行单元；
- Unit 01 Camera/Lighting 仍阻塞且未被豁免。
