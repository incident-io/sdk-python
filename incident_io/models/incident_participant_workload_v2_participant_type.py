from enum import StrEnum


class IncidentParticipantWorkloadV2ParticipantType(StrEnum):
    COLLABORATOR = "collaborator"
    OBSERVER = "observer"
    RESPONDER = "responder"

    def __str__(self) -> str:
        return str(self.value)
