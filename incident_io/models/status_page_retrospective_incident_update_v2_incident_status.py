from enum import StrEnum


class StatusPageRetrospectiveIncidentUpdateV2IncidentStatus(StrEnum):
    IDENTIFIED = "identified"
    INVESTIGATING = "investigating"
    MONITORING = "monitoring"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
