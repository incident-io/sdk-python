from enum import StrEnum


class CallRouteV2CurrentState(StrEnum):
    ACTIVE = "active"
    PENDING = "pending"
    PENDING_NUMBER = "pending_number"
    PENDING_REGULATORY_INFORMATION = "pending_regulatory_information"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "CallRouteV2CurrentState":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
