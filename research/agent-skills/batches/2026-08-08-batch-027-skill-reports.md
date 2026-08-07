# GitHub Skills Catalog — Batch 027 individual skill reports

Observed: `2026-08-08`

Runtime validation: `not_executed`

This file records individual reports only for distinct local skill definitions directly read in Batch 027. Exact mirrors/snapshots and packaging-only variants do not receive duplicate reports.

## `zyq5428/zephyr-agent-skills`

Reviewed revision: `431ef375fadc8cd22cdbee53311ec5807d505657`

### `zephyr-index`

- **Purpose:** navigation/router for the Zephyr skill suite rather than an implementation domain itself.
- **Structure:** `SKILL.md` points to `references/quick_reference.md`, `references/decision_tree.md`, `references/skill_catalog.md`, `scripts/task_skill_match.py`, and a CSV keyword map asset.
- **Useful pattern:** keep discovery logic in a small hub and load specialized skills only after task classification.
- **Verification surface:** catalog/link consistency and representative task-to-skill routing checks are specified; not executed.

### `zephyr-foundations`

- **Purpose:** embedded-C conventions, concurrency primitives, basic Devicetree literacy, and defensive error handling.
- **Supporting surfaces:** references for macros, concurrency, Devicetree basics, and error handling; `scripts/errno_return_check.py`; driver template asset.
- **Useful pattern:** combines conceptual guidance with a narrowly scoped static checker instead of trying to automate the entire workflow.
- **Runtime:** not executed.

### `build-system`

- **Purpose:** West workspaces/manifests, Kconfig, Sysbuild, and CMake integration.
- **Supporting surfaces:** `west.md`, `kconfig.md`, `cmake.md`, `scripts/find_modules.sh`, and a West manifest template.
- **Useful pattern:** build-system guidance is separated from application/runtime skills, reducing routing ambiguity.
- **Runtime:** no `west` or build command executed.

### `devicetree`

- **Purpose:** Zephyr Devicetree syntax, bindings, overlays, HWMv2, and node/property modification.
- **Supporting surfaces:** syntax/bindings/overlay references, overlay template, and `scripts/overlay_include_check.py`.
- **Verification contract:** inspect resolved DTS and generated headers after a build; no build performed.

### `native-sim`

- **Purpose:** host-based Zephyr simulation, debugging, and CI-oriented testing with `native_sim`.
- **Supporting surfaces:** simulation/debugging references, log scanner script, CI checklist asset.
- **Boundary:** the skill describes GDB/Valgrind/Twister usage, but none was run in this review.

### `board-bringup`

- **Purpose:** custom Zephyr board definitions using Hardware Model v2.
- **Supporting surfaces:** HWMv2 structure and board-file references, `scripts/board_yaml_lint.py`, and a `board.yml` template.
- **Useful pattern:** explicitly scopes board-unique configuration and delegates chip-level configuration to SoC definitions.
- **Runtime:** no board build or hardware validation executed.

### `zephyr-module`

- **Purpose:** reusable out-of-tree Zephyr modules and West integration.
- **Supporting surfaces:** module definition/West integration references, `scripts/module_manifest_check.py`, and module manifest template.
- **Verification contract:** module discovery, Kconfig visibility, compilation/linking; not executed.

### `kernel-basics`

- **Purpose:** threads, logging, and shell command integration.
- **Supporting surfaces:** thread/logging/shell references, `scripts/log_summary.py`, shell command template.
- **Useful pattern:** keeps core observability/interactive diagnostics separate from more advanced event-driven kernel services.
- **Runtime:** no target application or log parser executed.

### `kernel-services`

- **Purpose:** Zbus, SMF, work queues, and Settings persistence.
- **Supporting surfaces:** focused references, `scripts/zbus_channel_lint.py`, SMF state-table asset.
- **Architecture pattern:** encourages decoupled event-driven modules and explicit state transitions.
- **Runtime:** no concurrency, persistence, or reboot behavior validated.

### `hardware-io`

- **Purpose:** sensors, pinctrl/GPIO, and SoC-level hardware configuration.
- **Supporting surfaces:** sensor/pinctrl/SoC references, `scripts/gpio_alias_check.py`, sensor polling template.
- **Boundary:** readiness, electrical correctness, scaling, and timing remain hardware/runtime questions and were not verified.

### `power-performance`

- **Purpose:** system/device power management, performance tuning, and code/data relocation.
- **Supporting surfaces:** power/performance references, `scripts/power_budget_estimator.py`, power-budget CSV template.
- **Verification contract:** measured power, analyzer/map evidence, and memory-region confirmation; no measurements performed.

### `connectivity-ble`

- **Purpose:** BLE GATT/GAP integration, connection tuning, and delayed/batched transmission patterns.
- **Supporting surfaces:** BLE fundamentals, send-when-idle, power references, timing helper script, GATT service template.
- **Boundary:** discoverability, connection, GATT exchange, and negotiated parameters were not runtime-tested.

### `connectivity-ip`

- **Purpose:** IP stack configuration and protocol selection among CoAP/MQTT/LwM2M, plus external SDK/module integration.
- **Supporting surfaces:** protocol-selection/IP-stack/module references, `scripts/net_config_audit.py`, minimal CoAP config asset.
- **Useful pattern:** treats memory-footprint trimming as an explicit configuration concern.
- **Runtime:** no network connectivity, DNS, cloud, or footprint measurement executed.

### `connectivity-usb-can`

- **Purpose:** USB device classes and CAN integration/bridging.
- **Supporting surfaces:** USB and bridge references, `scripts/can_filter_lint.py`, CAN-filter CSV template.
- **Boundary:** enumeration, bus traffic, buffering, and framing interoperability remain unverified runtime claims.

### `storage`

- **Purpose:** NVS persistence and flash partition/layout management.
- **Supporting surfaces:** NVS/flash references, `scripts/nvs_id_lint.py`, partition overlay template.
- **Verification contract:** mount/write/read/reset and runtime flash-map agreement; not executed.

### `testing-debugging`

- **Purpose:** Ztest, Twister, tracing, and thread-analysis workflows.
- **Supporting surfaces:** three focused references, testcase template, and `scripts/twister_smoke.py`.
- **Source finding:** the inspected helper checks for a local `twister` executable, builds a Twister command, runs it, then summarizes `twister.json` when present.
- **Runtime:** the helper and test suites were not executed; source presence is not a pass result.

### `security-updates`

- **Purpose:** secure-boot/update lifecycle, image signing, update transport, rollback policy, and cryptographic integration.
- **Supporting surfaces:** MCUboot/signing/update/rollback/crypto references, config fragment, and `scripts/mcuboot_version_guard.py`.
- **Source finding:** the inspected version guard is a local semantic-version monotonicity checker with explicit failure codes; it was not run.
- **Runtime:** image verification/update/rollback behavior not validated.

### `iot-protocols`

- **Purpose:** OpenThread, Matter, cloud SDK integration, and LoRaWAN-oriented workflows.
- **Supporting surfaces:** protocol-specific references, provisioning dataset checker, dataset template.
- **Boundary:** joins, commissioning, telemetry, and radio behavior were not executed.

### `multicore`

- **Purpose:** SMP, OpenAMP/RPMsg, IPC, and linkable extensions.
- **Supporting surfaces:** SMP/OpenAMP/IPC/LLEXT references, config checker, RPMsg channel-contract template.
- **Useful pattern:** explicitly treats IPC contracts and shared-memory design as architecture surfaces rather than incidental code.
- **Runtime:** cross-core correctness, latency, throughput, or extension loading not validated.

### `industrial`

- **Purpose:** industrial protocol integration such as Modbus and CANopen.
- **Supporting surfaces:** protocol references, register-map lint script, CSV allocation template.
- **Boundary:** communication with real peers/controllers and recovery behavior were not tested.

### `specialized`

- **Purpose:** LVGL UI, audio, watchdog/reliability, and fault-injection-oriented resilience topics.
- **Supporting surfaces:** four focused references, watchdog timing checker, health-map template.
- **Useful pattern:** groups lower-frequency specialist topics while still requiring explicit validation criteria per topic.
- **Runtime:** display/audio/watchdog/fault behavior was not executed.

## `blackwell-systems/agentskills-cli`

Reviewed revision: `31f35119e4ed0e8165313ee3f1a7e8938cb481cf`

### `progressive-disclosure-guide`

- **Purpose:** interactive guide for splitting a large Agent Skill into a compact core plus on-demand references.
- **Contract:** presents metadata/core/reference tiers, asks for assessment and preview before mutation, and describes routing/injection patterns.
- **Source-level mismatch:** the skill repeatedly invokes `agentskills upgrade`, but the reviewed executable exposes only `agentskills decompose` and `agentskills lint`; the repository README also documents `decompose`. The bundled skill therefore contains stale command instructions at this revision.
- **Supporting implementation:** `src/commands/decompose.rs` includes dry-run, interactive confirmation, provider selection, routing-style options, filesystem application, and inline unit tests. Tests were not run.
- **Recommendation for catalog consumers:** treat the conceptual progressive-disclosure guidance as useful, but do not copy the command examples without reconciling them to the current CLI.

## Duplicate/reference-only repositories

No additional individual skill reports were generated for:

- `liangyongqin/zephyr-agent-skills`: exact reviewed Zephyr skill tree plus marketplace-only packaging delta.
- `gplm0/agentskills`, `chlin1983/agentskills`, `ghwoodard/agentskills`, `puppetls/agentskills`, `xhoanggiang/agentskills`, and `camillanapoles/skills_agentskills_reference`: exact already-reviewed official Agent Skills snapshot `b5ce2a438123f9f9c9b167c5af297c048f15395b`.
- `TracyHe/agentskills`: same reviewed official snapshot plus two docs-presentation file changes only.

This avoids turning repository mirrors into synthetic duplicate skill records.
