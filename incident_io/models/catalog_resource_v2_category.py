from enum import StrEnum


class CatalogResourceV2Category(StrEnum):
    CUSTOM = "custom"
    EXTERNAL = "external"
    PRIMITIVE = "primitive"

    def __str__(self) -> str:
        return str(self.value)
