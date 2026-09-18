from enum import StrEnum


class IncidentTemplateCustomFieldBindingV1MergeStrategy(StrEnum):
    APPEND = "append"
    FIRST_WINS = "first-wins"
    LAST_WINS = "last-wins"

    def __str__(self) -> str:
        return str(self.value)
