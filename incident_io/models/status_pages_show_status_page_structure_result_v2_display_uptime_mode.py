from enum import StrEnum


class StatusPagesShowStatusPageStructureResultV2DisplayUptimeMode(StrEnum):
    CHART_AND_PERCENTAGE = "chart_and_percentage"
    CHART_ONLY = "chart_only"
    NOTHING = "nothing"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "StatusPagesShowStatusPageStructureResultV2DisplayUptimeMode":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
