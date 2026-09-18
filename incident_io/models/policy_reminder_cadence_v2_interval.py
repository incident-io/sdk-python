from enum import StrEnum


class PolicyReminderCadenceV2Interval(StrEnum):
    DAILY = "daily"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
