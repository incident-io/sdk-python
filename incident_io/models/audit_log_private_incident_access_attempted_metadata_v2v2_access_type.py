from enum import StrEnum


class AuditLogPrivateIncidentAccessAttemptedMetadataV2V2AccessType(StrEnum):
    DIRECT_MEMBERSHIP = "direct_membership"
    GLOBAL_ACCESS = "global_access"
    NA = "N/A"
    TEAM_MEMBERSHIP = "team_membership"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "AuditLogPrivateIncidentAccessAttemptedMetadataV2V2AccessType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
