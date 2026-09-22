from enum import StrEnum


class CallRoutesUpdatePayloadV2CustomLanguage(StrEnum):
    DE_DE = "de-DE"
    EN_GB = "en-GB"
    EN_US = "en-US"
    ES_ES = "es-ES"
    FR_FR = "fr-FR"
    NL_NL = "nl-NL"
    PT_BR = "pt-BR"
    PT_PT = "pt-PT"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "CallRoutesUpdatePayloadV2CustomLanguage":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
