from enum import StrEnum


class AlertRouteCustomFieldBindingPayloadV2MergeStrategy(StrEnum):
    APPEND = "append"
    FIRST_WINS = "first-wins"
    LAST_WINS = "last-wins"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "AlertRouteCustomFieldBindingPayloadV2MergeStrategy":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
