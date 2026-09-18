from enum import StrEnum


class CallRouteV2CustomLanguage(StrEnum):
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
