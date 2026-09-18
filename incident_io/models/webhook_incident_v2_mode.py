from enum import StrEnum


class WebhookIncidentV2Mode(StrEnum):
    RETROSPECTIVE = "retrospective"
    STANDARD = "standard"
    TEST = "test"
    TUTORIAL = "tutorial"

    def __str__(self) -> str:
        return str(self.value)
