from enum import StrEnum


class EscalationPathTargetV2Urgency(StrEnum):
    HIGH = "high"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
