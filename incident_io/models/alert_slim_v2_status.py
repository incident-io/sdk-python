from enum import StrEnum


class AlertSlimV2Status(StrEnum):
    FIRING = "firing"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
