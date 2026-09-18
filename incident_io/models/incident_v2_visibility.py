from enum import StrEnum


class IncidentV2Visibility(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
