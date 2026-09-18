from enum import StrEnum


class IncidentStatusesCreatePayloadV1Category(StrEnum):
    CLOSED = "closed"
    LEARNING = "learning"
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
