from enum import StrEnum


class AuditLogActorV2Type(StrEnum):
    API_KEY = "api_key"
    EXTERNAL_RESOURCE = "external_resource"
    SYSTEM = "system"
    USER = "user"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
