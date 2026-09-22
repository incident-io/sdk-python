from enum import StrEnum


class EscalationEventV2Event(StrEnum):
    ACKED = "acked"
    CANCELLED = "cancelled"
    ENTERED_GRACE_PERIOD = "entered_grace_period"
    EXPIRED = "expired"
    NOTIFIED_CHANNELS = "notified_channels"
    NOTIFIED_USERS = "notified_users"
    RESOLVED = "resolved"
    TRIGGERED = "triggered"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "EscalationEventV2Event":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
