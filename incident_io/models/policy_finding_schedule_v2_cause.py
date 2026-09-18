from enum import StrEnum


class PolicyFindingScheduleV2Cause(StrEnum):
    NOBODY_SCHEDULED = "nobody_scheduled"
    NO_ON_CALL_SEAT = "no_on_call_seat"
    USER_DEACTIVATED = "user_deactivated"

    def __str__(self) -> str:
        return str(self.value)
