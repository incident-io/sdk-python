from enum import StrEnum


class StatusPageIncidentAffectedComponentV2ComponentStatus(StrEnum):
    DEGRADED_PERFORMANCE = "degraded_performance"
    FULL_OUTAGE = "full_outage"
    OPERATIONAL = "operational"
    PARTIAL_OUTAGE = "partial_outage"

    def __str__(self) -> str:
        return str(self.value)
