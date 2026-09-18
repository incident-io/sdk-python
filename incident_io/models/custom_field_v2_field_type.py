from enum import StrEnum


class CustomFieldV2FieldType(StrEnum):
    LINK = "link"
    MULTI_SELECT = "multi_select"
    NUMERIC = "numeric"
    SINGLE_SELECT = "single_select"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
