from enum import StrEnum


class AlertRouteChannelTargetPayloadV3ChannelVisibility(StrEnum):
    ASSISTANT = "assistant"
    DM = "dm"
    GROUP_CHAT = "group_chat"
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
