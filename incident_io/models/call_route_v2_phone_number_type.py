from enum import StrEnum


class CallRouteV2PhoneNumberType(StrEnum):
    LOCAL = "local"
    MOBILE = "mobile"
    NATIONAL = "national"
    TOLL_FREE = "toll_free"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "CallRouteV2PhoneNumberType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
