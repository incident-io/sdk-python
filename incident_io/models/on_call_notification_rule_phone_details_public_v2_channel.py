from enum import StrEnum


class OnCallNotificationRulePhoneDetailsPublicV2Channel(StrEnum):
    SMS = "sms"
    VOICE = "voice"

    def __str__(self) -> str:
        return str(self.value)
