from enum import StrEnum


class AlertTemplateAttributeBindingPayloadV2MergeStrategy(StrEnum):
    APPEND = "append"
    FIRST_WINS = "first_wins"
    LAST_WINS = "last_wins"
    MAX = "max"
    MIN = "min"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "AlertTemplateAttributeBindingPayloadV2MergeStrategy":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
