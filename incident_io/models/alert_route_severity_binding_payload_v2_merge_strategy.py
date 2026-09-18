from enum import StrEnum


class AlertRouteSeverityBindingPayloadV2MergeStrategy(StrEnum):
    FIRST_WINS = "first-wins"
    MAX = "max"

    def __str__(self) -> str:
        return str(self.value)
