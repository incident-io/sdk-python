from enum import StrEnum


class PolicyDueDateConfigV2CalculationType(StrEnum):
    SEVEN_DAYS = "seven_days"
    WEEKDAYS = "weekdays"

    def __str__(self) -> str:
        return str(self.value)
