from enum import StrEnum


class ScheduleReplicaV2ReplicaProvider(StrEnum):
    JSM = "jsm"
    NATIVE = "native"
    OPSGENIE = "opsgenie"
    PAGERDUTY = "pagerduty"

    def __str__(self) -> str:
        return str(self.value)
