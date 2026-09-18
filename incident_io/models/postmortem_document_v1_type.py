from enum import StrEnum


class PostmortemDocumentV1Type(StrEnum):
    EXTERNAL = "external"
    IN_APP = "in_app"

    def __str__(self) -> str:
        return str(self.value)
