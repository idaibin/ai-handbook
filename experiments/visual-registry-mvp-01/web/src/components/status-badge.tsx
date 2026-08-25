import type { RegistryStatus, ResultStatus } from "@/data/registry";

interface StatusBadgeProps {
  readonly status: RegistryStatus | ResultStatus;
}

export function StatusBadge({ status }: StatusBadgeProps) {
  return <span className={`statusBadge status-${status}`}>{status}</span>;
}
