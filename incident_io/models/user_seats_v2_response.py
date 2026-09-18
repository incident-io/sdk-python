from enum import StrEnum


class UserSeatsV2Response(StrEnum):
    FULL_ACCESS = "full_access"
    NONE = "none"
    VIEWER_ONLY = "viewer_only"

    def __str__(self) -> str:
        return str(self.value)
