from enum import StrEnum


class PayReportV2ErrorCode(StrEnum):
    INVALID_REQUEST = "invalid_request"
    TIMED_OUT = "timed_out"

    def __str__(self) -> str:
        return str(self.value)
