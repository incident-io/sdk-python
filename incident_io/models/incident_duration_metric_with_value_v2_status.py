from enum import StrEnum


class IncidentDurationMetricWithValueV2Status(StrEnum):
    CALCULATING = "calculating"
    INVALID_TIMESTAMPS = "invalid_timestamps"
    SUCCESS = "success"
    TIMESTAMPS_MISSING = "timestamps_missing"

    def __str__(self) -> str:
        return str(self.value)
