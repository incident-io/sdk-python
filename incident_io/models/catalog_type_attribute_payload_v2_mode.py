from enum import StrEnum


class CatalogTypeAttributePayloadV2Mode(StrEnum):
    BACKLINK = "backlink"
    DYNAMIC = "dynamic"
    EXTERNAL = "external"
    INTERNAL = "internal"
    MANUAL = "manual"
    PATH = "path"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
