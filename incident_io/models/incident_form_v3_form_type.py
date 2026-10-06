from enum import StrEnum


class IncidentFormV3FormType(StrEnum):
    ACCEPT = "accept"
    CUSTOM_FIELDS = "custom-fields"
    DECLARE = "declare"
    RESOLVE = "resolve"
    RETROSPECTIVE = "retrospective"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "IncidentFormV3FormType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
