from enum import StrEnum


class CatalogCreateTypePayloadV2Icon(StrEnum):
    ALERT = "alert"
    BOLT = "bolt"
    BOX = "box"
    BRIEFCASE = "briefcase"
    BROWSER = "browser"
    BULB = "bulb"
    CALENDAR = "calendar"
    CLOCK = "clock"
    COG = "cog"
    COMPONENTS = "components"
    DATABASE = "database"
    DOC = "doc"
    EMAIL = "email"
    ESCALATION_PATH = "escalation-path"
    FILES = "files"
    FLAG = "flag"
    FOLDER = "folder"
    GLOBE = "globe"
    INCIDENT_TEMPLATE = "incident-template"
    MONEY = "money"
    SERVER = "server"
    SEVERITY = "severity"
    STAR = "star"
    STATUS_PAGE = "status-page"
    STORE = "store"
    TAG = "tag"
    USER = "user"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "CatalogCreateTypePayloadV2Icon":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
