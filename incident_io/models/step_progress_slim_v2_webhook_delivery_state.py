from enum import StrEnum


class StepProgressSlimV2WebhookDeliveryState(StrEnum):
    AVAILABLE = "available"
    EXPIRED = "expired"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
