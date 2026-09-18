from enum import StrEnum


class WebhookIncidentV2Visibility(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
