# Summary

Baseline 的 interrupt 重执行产生重复 `charge_card`，且 blocked case 仍执行外部副作用。Treatment 以 idempotency key 去重，并在副作用前使用 blocking gate；`max_turns=1` 的负测在 interrupt 后显式 `blocked`。recovery 分母只包含 oracle 标记的真实 recovery case，`final_state_accuracy` 单独覆盖全部 case；冻结 oracle 逐项按精确事件顺序验证事件、副作用和最终状态，避免重复、反转或阶段交换被集合比较掩盖。
