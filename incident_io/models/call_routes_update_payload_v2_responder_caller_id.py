from enum import StrEnum


class CallRoutesUpdatePayloadV2ResponderCallerId(StrEnum):
    ONCALL_NUMBER = "oncall_number"
    ROUTE_NUMBER = "route_number"

    def __str__(self) -> str:
        return str(self.value)
