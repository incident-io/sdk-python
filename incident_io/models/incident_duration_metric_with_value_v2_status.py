from enum import StrEnum


class IncidentDurationMetricWithValueV2Status(StrEnum):
    CALCULATING = "calculating"
    INVALID_TIMESTAMPS = "invalid_timestamps"
    SUCCESS = "success"
    TIMESTAMPS_MISSING = "timestamps_missing"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "IncidentDurationMetricWithValueV2Status":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
