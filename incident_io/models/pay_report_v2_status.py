from enum import StrEnum


class PayReportV2Status(StrEnum):
    COMPLETE = "complete"
    FAILED = "failed"
    GENERATING = "generating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
