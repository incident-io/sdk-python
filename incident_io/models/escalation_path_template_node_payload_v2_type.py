from enum import StrEnum


class EscalationPathTemplateNodePayloadV2Type(StrEnum):
    DELAY = "delay"
    ESCALATION_PATH = "escalation_path"
    IF_ELSE = "if_else"
    LEVEL = "level"
    NOTIFY_CHANNEL = "notify_channel"
    REPEAT = "repeat"
    VOICEMAIL = "voicemail"

    def __str__(self) -> str:
        return str(self.value)
