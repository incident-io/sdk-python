from enum import StrEnum


class IncidentSlimV2StatusCategory(StrEnum):
    ACTIVE = "active"
    CANCELED = "canceled"
    CLOSED = "closed"
    DECLINED = "declined"
    MERGED = "merged"
    PAUSED = "paused"
    POST_INCIDENT = "post-incident"
    TRIAGE = "triage"

    def __str__(self) -> str:
        return str(self.value)
