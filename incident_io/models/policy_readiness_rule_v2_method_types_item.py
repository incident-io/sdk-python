from enum import StrEnum


class PolicyReadinessRuleV2MethodTypesItem(StrEnum):
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
