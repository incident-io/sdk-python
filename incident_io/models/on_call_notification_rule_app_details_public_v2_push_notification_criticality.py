from enum import StrEnum


class OnCallNotificationRuleAppDetailsPublicV2PushNotificationCriticality(StrEnum):
    ACTIVE = "active"
    CRITICAL = "critical"

    def __str__(self) -> str:
        return str(self.value)
