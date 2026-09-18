from enum import StrEnum


class CallRouteV2CurrentState(StrEnum):
    ACTIVE = "active"
    PENDING = "pending"
    PENDING_NUMBER = "pending_number"
    PENDING_REGULATORY_INFORMATION = "pending_regulatory_information"

    def __str__(self) -> str:
        return str(self.value)
