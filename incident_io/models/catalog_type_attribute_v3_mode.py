from enum import StrEnum


class CatalogTypeAttributeV3Mode(StrEnum):
    API = "api"
    BACKLINK = "backlink"
    DASHBOARD = "dashboard"
    DYNAMIC = "dynamic"
    EXTERNAL = "external"
    INTERNAL = "internal"
    PATH = "path"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "CatalogTypeAttributeV3Mode":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
