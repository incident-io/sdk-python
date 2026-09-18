from enum import StrEnum


class PayReportV2OverlappingShifts(StrEnum):
    PAID_ONCE = "paid_once"
    PAID_PER_SCHEDULE = "paid_per_schedule"

    def __str__(self) -> str:
        return str(self.value)
