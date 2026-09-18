from enum import StrEnum


class OnCallNotificationRuleMethodTargetPublicV2Type(StrEnum):
    ALL = "all"
    SPECIFIC = "specific"

    def __str__(self) -> str:
        return str(self.value)
