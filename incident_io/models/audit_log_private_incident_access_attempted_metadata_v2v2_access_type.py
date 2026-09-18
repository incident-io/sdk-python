from enum import StrEnum


class AuditLogPrivateIncidentAccessAttemptedMetadataV2V2AccessType(StrEnum):
    DIRECT_MEMBERSHIP = "direct_membership"
    GLOBAL_ACCESS = "global_access"
    NA = "N/A"
    TEAM_MEMBERSHIP = "team_membership"

    def __str__(self) -> str:
        return str(self.value)
