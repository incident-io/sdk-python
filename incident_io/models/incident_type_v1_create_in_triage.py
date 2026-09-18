from enum import StrEnum


class IncidentTypeV1CreateInTriage(StrEnum):
    ALWAYS = "always"
    OPTIONAL = "optional"

    def __str__(self) -> str:
        return str(self.value)
