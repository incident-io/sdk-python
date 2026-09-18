from enum import StrEnum


class PolicyScheduleV2RequirementType(StrEnum):
    CONTIGUOUS = "contiguous"

    def __str__(self) -> str:
        return str(self.value)
