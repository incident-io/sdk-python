from enum import StrEnum


class ActionsUpdatePayloadV3Status(StrEnum):
    COMPLETED = "completed"
    DELETED = "deleted"
    NOT_DOING = "not_doing"
    OUTSTANDING = "outstanding"

    def __str__(self) -> str:
        return str(self.value)
