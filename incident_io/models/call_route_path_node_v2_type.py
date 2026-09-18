from enum import StrEnum


class CallRoutePathNodeV2Type(StrEnum):
    LEVEL = "level"
    VOICEMAIL = "voicemail"

    def __str__(self) -> str:
        return str(self.value)
