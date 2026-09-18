from enum import StrEnum


class AuditLogPrivateAlertAccessAttemptedMetadataV2Outcome(StrEnum):
    DENIED = "denied"
    GRANTED = "granted"

    def __str__(self) -> str:
        return str(self.value)
