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

    @classmethod
    def _missing_(cls, value: object) -> "CatalogUpdateTypePayloadV3Color":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
