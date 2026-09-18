from enum import StrEnum


class IncidentTemplateSeverityBindingV1MergeStrategy(StrEnum):
    FIRST_WINS = "first-wins"
    MAX = "max"

    def __str__(self) -> str:
        return str(self.value)
