from enum import StrEnum


class IncidentsCreatePayloadV1Status(StrEnum):
    CLOSED = "closed"
    DECLINED = "declined"
    FIXING = "fixing"
    INVESTIGATING = "investigating"
    MONITORING = "monitoring"
    TRIAGE = "triage"

    def __str__(self) -> str:
        return str(self.value)
