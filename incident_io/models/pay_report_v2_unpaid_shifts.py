from enum import StrEnum


class PayReportV2UnpaidShifts(StrEnum):
    EXCLUDED = "excluded"
    INCLUDED = "included"

    def __str__(self) -> str:
        return str(self.value)
