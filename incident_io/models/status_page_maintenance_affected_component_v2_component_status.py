from enum import StrEnum


class StatusPageMaintenanceAffectedComponentV2ComponentStatus(StrEnum):
    OPERATIONAL = "operational"
    UNDER_MAINTENANCE = "under_maintenance"

    def __str__(self) -> str:
        return str(self.value)
