from enum import StrEnum


class ScheduleRotationUpdatePayloadV2SchedulingMode(StrEnum):
    FAIR = "fair"
    SEQUENTIAL = "sequential"

    def __str__(self) -> str:
        return str(self.value)
