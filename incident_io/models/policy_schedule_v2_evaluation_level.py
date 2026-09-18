from enum import StrEnum


class PolicyScheduleV2EvaluationLevel(StrEnum):
    ROTATION = "rotation"
    SCHEDULE = "schedule"

    def __str__(self) -> str:
        return str(self.value)
