from enum import StrEnum


class IncidentStatusV2Category(StrEnum):
    CANCELED = "canceled"
    CLOSED = "closed"
    DECLINED = "declined"
    LEARNING = "learning"
    LIVE = "live"
    MERGED = "merged"
    PAUSED = "paused"
    TRIAGE = "triage"

    def __str__(self) -> str:
        return str(self.value)
