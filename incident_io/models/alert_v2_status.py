from enum import StrEnum


class AlertV2Status(StrEnum):
    FIRING = "firing"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
