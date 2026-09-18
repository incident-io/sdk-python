from enum import StrEnum


class PayConfigsUpdatePayloadV2RateTimeUnit(StrEnum):
    DAY = "day"
    HOUR = "hour"

    def __str__(self) -> str:
        return str(self.value)
