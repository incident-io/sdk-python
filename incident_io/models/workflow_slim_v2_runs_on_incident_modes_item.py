from enum import StrEnum


class WorkflowSlimV2RunsOnIncidentModesItem(StrEnum):
    RETROSPECTIVE = "retrospective"
    STANDARD = "standard"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
