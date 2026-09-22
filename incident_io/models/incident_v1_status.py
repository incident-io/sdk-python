from enum import StrEnum


class IncidentV1Status(StrEnum):
    CLOSED = "closed"
    DECLINED = "declined"
    FIXING = "fixing"
    INVESTIGATING = "investigating"
    MONITORING = "monitoring"
    TRIAGE = "triage"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "IncidentV1Status":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
