from enum import StrEnum


class StatusPageIncidentComponentImpactV2ComponentStatus(StrEnum):
    DEGRADED_PERFORMANCE = "degraded_performance"
    FULL_OUTAGE = "full_outage"
    PARTIAL_OUTAGE = "partial_outage"

    def __str__(self) -> str:
        return str(self.value)
