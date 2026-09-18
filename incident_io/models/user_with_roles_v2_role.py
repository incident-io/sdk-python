from enum import StrEnum


class UserWithRolesV2Role(StrEnum):
    ADMINISTRATOR = "administrator"
    OWNER = "owner"
    RESPONDER = "responder"
    UNSET = "unset"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
