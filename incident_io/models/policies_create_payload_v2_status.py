from enum import StrEnum


class PoliciesCreatePayloadV2Status(StrEnum):
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
