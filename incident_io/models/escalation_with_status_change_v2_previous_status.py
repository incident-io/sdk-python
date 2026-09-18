from enum import StrEnum


class EscalationWithStatusChangeV2PreviousStatus(StrEnum):
    ACKED = "acked"
    CANCELLED = "cancelled"
    DELAYED = "delayed"
    EXPIRED = "expired"
    PENDING = "pending"
    PENDING_REPEAT = "pending_repeat"
    RESOLVED = "resolved"
    SNOOZED = "snoozed"
    TRIGGERED = "triggered"

    def __str__(self) -> str:
        return str(self.value)
