from enum import StrEnum


class ScheduleRotationV2SchedulingMode(StrEnum):
    FAIR = "fair"
    SEQUENTIAL = "sequential"

    def __str__(self) -> str:
        return str(self.value)
