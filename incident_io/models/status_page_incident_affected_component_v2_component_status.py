from enum import StrEnum


class StatusPageIncidentAffectedComponentV2ComponentStatus(StrEnum):
    DEGRADED_PERFORMANCE = "degraded_performance"
    FULL_OUTAGE = "full_outage"
    OPERATIONAL = "operational"
    PARTIAL_OUTAGE = "partial_outage"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "StatusPageIncidentAffectedComponentV2ComponentStatus":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
