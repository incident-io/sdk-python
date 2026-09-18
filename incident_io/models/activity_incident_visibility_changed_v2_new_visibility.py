from enum import StrEnum


class ActivityIncidentVisibilityChangedV2NewVisibility(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
