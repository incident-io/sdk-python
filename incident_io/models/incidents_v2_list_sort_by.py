from enum import StrEnum


class IncidentsV2ListSortBy(StrEnum):
    CREATED_AT_NEWEST_FIRST = "created_at_newest_first"
    CREATED_AT_OLDEST_FIRST = "created_at_oldest_first"

    def __str__(self) -> str:
        return str(self.value)
