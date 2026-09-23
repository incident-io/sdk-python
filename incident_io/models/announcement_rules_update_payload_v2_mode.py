from enum import StrEnum


class AnnouncementRulesUpdatePayloadV2Mode(StrEnum):
    INCLUDE_ALL = "include_all"
    INCLUDE_DECLINED_AND_MERGED = "include_declined_and_merged"
    INCLUDE_TRIAGE = "include_triage"
    INCLUDE_TRIAGE_AND_MERGED = "include_triage_and_merged"
    LIVE_AND_CLOSED = "live_and_closed"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "AnnouncementRulesUpdatePayloadV2Mode":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
