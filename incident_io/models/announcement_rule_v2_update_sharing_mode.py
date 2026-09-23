from enum import StrEnum


class AnnouncementRuleV2UpdateSharingMode(StrEnum):
    NONE = "none"
    THREAD = "thread"
    THREAD_AND_CHANNEL = "thread_and_channel"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "AnnouncementRuleV2UpdateSharingMode":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
