from enum import StrEnum


class EscalationPathNodeNotifyChannelWithBindingPayloadV2TimeToAckIntervalCondition(
    StrEnum
):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
