from enum import StrEnum


class CallRoutesCreateOptionPayloadV2Digit(StrEnum):
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
