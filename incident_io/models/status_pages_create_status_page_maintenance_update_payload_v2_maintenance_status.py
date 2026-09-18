from enum import StrEnum


class StatusPagesCreateStatusPageMaintenanceUpdatePayloadV2MaintenanceStatus(StrEnum):
    MAINTENANCE_COMPLETE = "maintenance_complete"
    MAINTENANCE_IN_PROGRESS = "maintenance_in_progress"
    MAINTENANCE_SCHEDULED = "maintenance_scheduled"

    def __str__(self) -> str:
        return str(self.value)
