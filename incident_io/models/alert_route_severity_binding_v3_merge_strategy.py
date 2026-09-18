from enum import StrEnum


class AlertRouteSeverityBindingV3MergeStrategy(StrEnum):
    FIRST_WINS = "first-wins"
    MAX = "max"

    def __str__(self) -> str:
        return str(self.value)
