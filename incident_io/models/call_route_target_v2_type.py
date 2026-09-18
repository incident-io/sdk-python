from enum import StrEnum


class CallRouteTargetV2Type(StrEnum):
    SCHEDULE = "schedule"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
