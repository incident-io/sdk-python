from enum import StrEnum


class PayConfigsCreatePayloadV2RateTimeUnit(StrEnum):
    DAY = "day"
    HOUR = "hour"

    def __str__(self) -> str:
        return str(self.value)
