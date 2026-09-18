from enum import StrEnum


class EscalationPathNodeDelayV2DelayIntervalCondition(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
