from enum import StrEnum


class EscalationPathNodeLevelWithBindingV2AckMode(StrEnum):
    ALL = "all"
    FIRST = "first"

    def __str__(self) -> str:
        return str(self.value)
