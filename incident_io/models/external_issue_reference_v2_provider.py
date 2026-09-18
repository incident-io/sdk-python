from enum import StrEnum


class ExternalIssueReferenceV2Provider(StrEnum):
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
