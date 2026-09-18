from enum import StrEnum


class CallRouteTargetV2ScheduleMode(StrEnum):
    ALL_USERS = "all_users"
    ALL_USERS_FOR_ROTA = "all_users_for_rota"
    CURRENTLY_ON_CALL = "currently_on_call"
    CURRENTLY_ON_CALL_FOR_ROTA = "currently_on_call_for_rota"
    NEXT_ON_CALL = "next_on_call"
    NEXT_ON_CALL_FOR_ROTA = "next_on_call_for_rota"
    VALUE_6 = ""

    def __str__(self) -> str:
        return str(self.value)
