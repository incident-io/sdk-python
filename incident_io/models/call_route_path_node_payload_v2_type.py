from enum import StrEnum


class CallRoutePathNodePayloadV2Type(StrEnum):
    LEVEL = "level"
    VOICEMAIL = "voicemail"

    def __str__(self) -> str:
        return str(self.value)
