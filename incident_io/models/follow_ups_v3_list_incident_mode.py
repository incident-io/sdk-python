from enum import StrEnum


class FollowUpsV3ListIncidentMode(StrEnum):
    RETROSPECTIVE = "retrospective"
    STANDARD = "standard"
    STREAM = "stream"
    TEST = "test"
    TUTORIAL = "tutorial"

    def __str__(self) -> str:
        return str(self.value)
