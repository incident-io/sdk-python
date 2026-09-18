from enum import StrEnum


class ManagementMetaV2ManagedBy(StrEnum):
    DASHBOARD = "dashboard"
    EXTERNAL = "external"
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
