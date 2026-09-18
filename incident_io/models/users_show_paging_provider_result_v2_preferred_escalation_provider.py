from enum import StrEnum


class UsersShowPagingProviderResultV2PreferredEscalationProvider(StrEnum):
    NATIVE = "native"
    OPSGENIE = "opsgenie"
    PAGERDUTY = "pagerduty"
    SPLUNK_ON_CALL = "splunk_on_call"

    def __str__(self) -> str:
        return str(self.value)
