from enum import StrEnum


class IncidentParticipantV2ParticipantType(StrEnum):
    COLLABORATOR = "collaborator"
    OBSERVER = "observer"
    RESPONDER = "responder"

    def __str__(self) -> str:
        return str(self.value)
