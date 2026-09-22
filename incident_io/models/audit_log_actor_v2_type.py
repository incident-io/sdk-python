from enum import StrEnum


class AuditLogActorV2Type(StrEnum):
    API_KEY = "api_key"
    EXTERNAL_RESOURCE = "external_resource"
    SYSTEM = "system"
    USER = "user"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "AuditLogActorV2Type":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
