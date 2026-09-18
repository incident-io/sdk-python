from enum import StrEnum


class PayReportsPublishPayloadV2SendUserBreakdowns(StrEnum):
    SEND = "send"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
