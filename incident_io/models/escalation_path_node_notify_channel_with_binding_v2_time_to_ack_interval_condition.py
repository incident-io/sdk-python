from enum import StrEnum


class EscalationPathNodeNotifyChannelWithBindingV2TimeToAckIntervalCondition(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
