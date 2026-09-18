from enum import StrEnum


class IncidentsV2ListFilterMode(StrEnum):
    ALL = "all"
    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)
