from enum import StrEnum


class WorkflowsUpdateWorkflowPayloadV2RunsOnIncidentModesItem(StrEnum):
    RETROSPECTIVE = "retrospective"
    STANDARD = "standard"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
