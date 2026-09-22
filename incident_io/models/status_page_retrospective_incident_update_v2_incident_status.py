from enum import StrEnum


class StatusPageRetrospectiveIncidentUpdateV2IncidentStatus(StrEnum):
    IDENTIFIED = "identified"
    INVESTIGATING = "investigating"
    MONITORING = "monitoring"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "StatusPageRetrospectiveIncidentUpdateV2IncidentStatus":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
