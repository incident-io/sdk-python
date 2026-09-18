from enum import StrEnum


class StepProgressV2Status(StrEnum):
    COMPLETE = "complete"
    ERROR = "error"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
