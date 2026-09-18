from enum import StrEnum


class ExpressionOperationV2OperationType(StrEnum):
    BRANCHES = "branches"
    CAST = "cast"
    CONCATENATE = "concatenate"
    COUNT = "count"
    FILTER = "filter"
    FIRST = "first"
    MAX = "max"
    MIN = "min"
    NAVIGATE = "navigate"
    PARSE = "parse"
    RANDOM = "random"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
