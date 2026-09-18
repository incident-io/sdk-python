from enum import StrEnum


class PolicyFindingScheduleImpactedUserV2Cause(StrEnum):
    NO_ON_CALL_SEAT = "no_on_call_seat"
    USER_DEACTIVATED = "user_deactivated"

    def __str__(self) -> str:
        return str(self.value)
