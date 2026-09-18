from enum import StrEnum


class PolicyFindingV2State(StrEnum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    DISMISSED = "dismissed"
    PENDING = "pending"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
