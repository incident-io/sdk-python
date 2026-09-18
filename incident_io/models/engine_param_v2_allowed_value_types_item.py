from enum import StrEnum


class EngineParamV2AllowedValueTypesItem(StrEnum):
    EXPRESSION = "expression"
    LITERAL = "literal"
    REFERENCE = "reference"

    def __str__(self) -> str:
        return str(self.value)
