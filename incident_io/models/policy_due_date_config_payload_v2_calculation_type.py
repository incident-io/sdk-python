from enum import StrEnum


class PolicyDueDateConfigPayloadV2CalculationType(StrEnum):
    SEVEN_DAYS = "seven_days"
    WEEKDAYS = "weekdays"

    def __str__(self) -> str:
        return str(self.value)
