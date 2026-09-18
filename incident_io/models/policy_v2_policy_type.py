from enum import StrEnum


class PolicyV2PolicyType(StrEnum):
    DEBRIEF = "debrief"
    FOLLOW_UP = "follow_up"
    ON_CALL_READINESS = "on_call_readiness"
    POST_MORTEM = "post_mortem"
    SCHEDULE = "schedule"
    SHIFT_CONFLICT = "shift_conflict"
    VACATION_CONFLICT = "vacation_conflict"

    def __str__(self) -> str:
        return str(self.value)
