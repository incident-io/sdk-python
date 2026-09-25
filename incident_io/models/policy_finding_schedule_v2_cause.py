from enum import StrEnum


class PolicyFindingScheduleV2Cause(StrEnum):
    NOBODY_SCHEDULED = "nobody_scheduled"
    NOTIFICATIONS_PAUSED = "notifications_paused"
    NO_ON_CALL_SEAT = "no_on_call_seat"
    USER_DEACTIVATED = "user_deactivated"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "PolicyFindingScheduleV2Cause":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
