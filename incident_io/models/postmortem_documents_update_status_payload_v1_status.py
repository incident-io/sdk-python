from enum import StrEnum


class PostmortemDocumentsUpdateStatusPayloadV1Status(StrEnum):
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"

    def __str__(self) -> str:
        return str(self.value)
