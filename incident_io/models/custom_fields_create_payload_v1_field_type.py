from enum import StrEnum


class CustomFieldsCreatePayloadV1FieldType(StrEnum):
    LINK = "link"
    MULTI_SELECT = "multi_select"
    NUMERIC = "numeric"
    SINGLE_SELECT = "single_select"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "CustomFieldsCreatePayloadV1FieldType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
