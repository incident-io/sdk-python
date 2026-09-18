from enum import StrEnum


class IncidentRoleV1RoleType(StrEnum):
    CUSTOM = "custom"
    LEAD = "lead"
    REPORTER = "reporter"

    def __str__(self) -> str:
        return str(self.value)
