from enum import StrEnum


class StepProgressSlimV2Status(StrEnum):
    COMPLETE = "complete"
    ERROR = "error"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
