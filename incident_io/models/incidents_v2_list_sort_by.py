from enum import StrEnum


class IncidentsV2ListSortBy(StrEnum):
    CREATED_AT_NEWEST_FIRST = "created_at_newest_first"
    CREATED_AT_OLDEST_FIRST = "created_at_oldest_first"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "IncidentsV2ListSortBy":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
