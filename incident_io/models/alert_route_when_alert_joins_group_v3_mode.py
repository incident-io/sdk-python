from enum import StrEnum


class AlertRouteWhenAlertJoinsGroupV3Mode(StrEnum):
    ON_EACH_NEW_ALERT = "on_each_new_alert"
    ON_PRIORITY_INCREASE = "on_priority_increase"

    def __str__(self) -> str:
        return str(self.value)
