from enum import StrEnum


class WorkflowV2State(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"
    DRAFT = "draft"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
