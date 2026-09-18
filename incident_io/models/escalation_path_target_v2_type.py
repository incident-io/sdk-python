from enum import StrEnum


class EscalationPathTargetV2Type(StrEnum):
    MSTEAMS_CHANNEL = "msteams_channel"
    SCHEDULE = "schedule"
    SLACK_CHANNEL = "slack_channel"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
