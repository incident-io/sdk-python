from enum import StrEnum


class IncidentV1Mode(StrEnum):
    REAL = "real"
    TEST = "test"
    TUTORIAL = "tutorial"

    def __str__(self) -> str:
        return str(self.value)
