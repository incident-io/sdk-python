from enum import StrEnum


class AlertsTransitionIncidentAlertPayloadV2State(StrEnum):
    RELATED = "related"
    UNRELATED = "unrelated"

    def __str__(self) -> str:
        return str(self.value)
