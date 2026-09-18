from enum import StrEnum


class StepProgressV2WebhookDeliveryState(StrEnum):
    AVAILABLE = "available"
    EXPIRED = "expired"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
