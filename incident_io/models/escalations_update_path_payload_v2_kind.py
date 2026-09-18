from enum import StrEnum


class EscalationsUpdatePathPayloadV2Kind(StrEnum):
    STANDALONE = "standalone"
    TEMPLATED = "templated"

    def __str__(self) -> str:
        return str(self.value)
