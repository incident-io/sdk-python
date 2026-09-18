from enum import StrEnum


class AlertEventsCreateHTTPPayloadV2Status(StrEnum):
    FIRING = "firing"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
