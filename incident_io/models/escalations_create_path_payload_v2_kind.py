from enum import StrEnum


class EscalationsCreatePathPayloadV2Kind(StrEnum):
    STANDALONE = "standalone"
    TEMPLATED = "templated"

    def __str__(self) -> str:
        return str(self.value)
