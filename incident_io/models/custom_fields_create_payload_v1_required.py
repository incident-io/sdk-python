from enum import StrEnum


class CustomFieldsCreatePayloadV1Required(StrEnum):
    ALWAYS = "always"
    BEFORE_CLOSURE = "before_closure"
    NEVER = "never"

    def __str__(self) -> str:
        return str(self.value)
