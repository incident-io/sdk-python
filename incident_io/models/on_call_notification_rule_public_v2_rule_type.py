from enum import StrEnum


class OnCallNotificationRulePublicV2RuleType(StrEnum):
    HIGH_URGENCY = "high_urgency"
    LOW_URGENCY = "low_urgency"

    def __str__(self) -> str:
        return str(self.value)
