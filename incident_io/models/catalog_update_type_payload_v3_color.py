from enum import StrEnum


class CatalogUpdateTypePayloadV3Color(StrEnum):
    BLUE = "blue"
    CYAN = "cyan"
    GREEN = "green"
    ORANGE = "orange"
    PINK = "pink"
    VIOLET = "violet"
    YELLOW = "yellow"

    def __str__(self) -> str:
        return str(self.value)
