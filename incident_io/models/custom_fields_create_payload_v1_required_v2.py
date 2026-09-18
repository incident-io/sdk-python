from enum import StrEnum


class CustomFieldsCreatePayloadV1RequiredV2(StrEnum):
    ALWAYS = "always"
    BEFORE_RESOLUTION = "before_resolution"
    NEVER = "never"

    def __str__(self) -> str:
        return str(self.value)
