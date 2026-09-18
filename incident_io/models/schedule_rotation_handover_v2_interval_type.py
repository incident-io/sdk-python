from enum import StrEnum


class ScheduleRotationHandoverV2IntervalType(StrEnum):
    DAILY = "daily"
    HOURLY = "hourly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
