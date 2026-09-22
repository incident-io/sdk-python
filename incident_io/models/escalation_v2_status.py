from enum import StrEnum


class EscalationV2Status(StrEnum):
    ACKED = "acked"
    CANCELLED = "cancelled"
    DELAYED = "delayed"
    EXPIRED = "expired"
    PENDING = "pending"
    PENDING_REPEAT = "pending_repeat"
    RESOLVED = "resolved"
    SNOOZED = "snoozed"
    TRIGGERED = "triggered"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "EscalationV2Status":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
