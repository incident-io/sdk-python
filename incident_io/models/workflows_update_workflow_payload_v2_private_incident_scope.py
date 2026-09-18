from enum import StrEnum


class WorkflowsUpdateWorkflowPayloadV2PrivateIncidentScope(StrEnum):
    ALL = "all"
    NONE = "none"
    OWNING_TEAMS = "owning_teams"

    def __str__(self) -> str:
        return str(self.value)
