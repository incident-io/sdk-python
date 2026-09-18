from enum import StrEnum


class IncidentsCreatePayloadV1Mode(StrEnum):
    REAL = "real"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
