from enum import StrEnum


class PoliciesUpdatePayloadV2PolicyType(StrEnum):
    DEBRIEF = "debrief"
    FOLLOW_UP = "follow_up"
    ON_CALL_READINESS = "on_call_readiness"
    POST_MORTEM = "post_mortem"
    SCHEDULE = "schedule"
    SHIFT_CONFLICT = "shift_conflict"
    VACATION_CONFLICT = "vacation_conflict"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "PoliciesUpdatePayloadV2PolicyType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
