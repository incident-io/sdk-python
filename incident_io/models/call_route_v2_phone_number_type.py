from enum import StrEnum


class CallRouteV2PhoneNumberType(StrEnum):
    LOCAL = "local"
    MOBILE = "mobile"
    NATIONAL = "national"
    TOLL_FREE = "toll_free"

    def __str__(self) -> str:
        return str(self.value)
