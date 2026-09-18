from enum import StrEnum


class AlertRouteCustomFieldBindingV3MergeStrategy(StrEnum):
    APPEND = "append"
    FIRST_WINS = "first-wins"
    LAST_WINS = "last-wins"

    def __str__(self) -> str:
        return str(self.value)
