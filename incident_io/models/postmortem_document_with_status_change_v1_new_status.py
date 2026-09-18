from enum import StrEnum


class PostmortemDocumentWithStatusChangeV1NewStatus(StrEnum):
    COMPLETE = "complete"
    CREATED = "created"
    NOT_STARTED = "not_started"
    REVIEW = "review"

    def __str__(self) -> str:
        return str(self.value)
