from enum import StrEnum


class CallRouteOptionV2Digit(StrEnum):
    VALUE_0 = "1"
    VALUE_1 = "2"
    VALUE_2 = "3"
    VALUE_3 = "4"
    VALUE_4 = "5"
    VALUE_5 = "6"
    VALUE_6 = "7"
    VALUE_7 = "8"
    VALUE_8 = "9"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "CallRouteOptionV2Digit":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
