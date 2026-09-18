from enum import StrEnum


class EscalationPathNodeLevelWithBindingPayloadV2TimeToAckIntervalCondition(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
