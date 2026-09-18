from enum import StrEnum


class StatusPageIncidentUpdateV2IncidentStatus(StrEnum):
    IDENTIFIED = "identified"
    INVESTIGATING = "investigating"
    MONITORING = "monitoring"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
