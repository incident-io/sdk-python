from enum import StrEnum


class EscalationPathNodePayloadV2Type(StrEnum):
    DELAY = "delay"
    ESCALATION_PATH = "escalation_path"
    IF_ELSE = "if_else"
    LEVEL = "level"
    NOTIFY_CHANNEL = "notify_channel"
    REPEAT = "repeat"
    VOICEMAIL = "voicemail"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "EscalationPathNodePayloadV2Type":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
