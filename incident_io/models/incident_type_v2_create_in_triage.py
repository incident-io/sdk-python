from enum import StrEnum


class IncidentTypeV2CreateInTriage(StrEnum):
    ALWAYS = "always"
    OPTIONAL = "optional"

    def __str__(self) -> str:
        return str(self.value)
