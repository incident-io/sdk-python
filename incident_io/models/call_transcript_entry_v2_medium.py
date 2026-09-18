from enum import StrEnum


class CallTranscriptEntryV2Medium(StrEnum):
    CALL_CHAT = "call_chat"
    SPOKEN = "spoken"

    def __str__(self) -> str:
        return str(self.value)
