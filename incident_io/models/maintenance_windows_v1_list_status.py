from enum import StrEnum


class MaintenanceWindowsV1ListStatus(StrEnum):
    ACTIVE = "active"
    PAST = "past"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
