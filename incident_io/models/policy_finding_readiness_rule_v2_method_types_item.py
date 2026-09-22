from enum import StrEnum


class PolicyFindingReadinessRuleV2MethodTypesItem(StrEnum):
    APP = "app"
    EMAIL = "email"
    LIVE_CALL = "live_call"
    MICROSOFT_TEAMS = "microsoft_teams"
    MICROSOFT_TEAMS_CHANNEL = "microsoft_teams_channel"
    PHONE = "phone"
    SLACK = "slack"
    SLACK_CHANNEL = "slack_channel"
    SMS = "sms"
    WHATSAPP_MESSAGE = "whatsapp_message"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "PolicyFindingReadinessRuleV2MethodTypesItem":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
