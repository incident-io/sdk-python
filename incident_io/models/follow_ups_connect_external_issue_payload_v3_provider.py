from enum import StrEnum


class FollowUpsConnectExternalIssuePayloadV3Provider(StrEnum):
    ASANA = "asana"
    AZURE_DEVOPS = "azure_devops"
    CLICK_UP = "click_up"
    FRESHSERVICE = "freshservice"
    GITHUB = "github"
    GITLAB = "gitlab"
    JIRA = "jira"
    JIRA_SERVER = "jira_server"
    LINEAR = "linear"
    NOTION = "notion"
    SALESFORCE = "salesforce"
    SERVICE_NOW = "service_now"
    SHORTCUT = "shortcut"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "FollowUpsConnectExternalIssuePayloadV3Provider":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
