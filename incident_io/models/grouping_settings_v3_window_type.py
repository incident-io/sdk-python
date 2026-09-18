from enum import StrEnum


class GroupingSettingsV3WindowType(StrEnum):
    FIXED = "fixed"
    ROLLING = "rolling"

    def __str__(self) -> str:
        return str(self.value)
