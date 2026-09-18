from enum import StrEnum


class ActionsV1ListIncidentMode(StrEnum):
    REAL = "real"
    TEST = "test"
    TUTORIAL = "tutorial"

    def __str__(self) -> str:
        return str(self.value)
