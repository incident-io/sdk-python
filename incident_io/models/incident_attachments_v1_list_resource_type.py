from enum import StrEnum


class IncidentAttachmentsV1ListResourceType(StrEnum):
    ARBITRARY_URL = "arbitrary_url"
    ATLASSIAN_STATUSPAGE_INCIDENT = "atlassian_statuspage_incident"
    DATADOG_MONITOR_ALERT = "datadog_monitor_alert"
    GITHUB_PULL_REQUEST = "github_pull_request"
    GITLAB_MERGE_REQUEST = "gitlab_merge_request"
    GOOGLE_CALENDAR_EVENT = "google_calendar_event"
    JIRA_ISSUE = "jira_issue"
    JSM_ALERT = "jsm_alert"
    OPSGENIE_ALERT = "opsgenie_alert"
    OUTLOOK_CALENDAR_EVENT = "outlook_calendar_event"
    PAGER_DUTY_INCIDENT = "pager_duty_incident"
    SALESFORCE_CASE = "salesforce_case"
    SCRUBBED = "scrubbed"
    SENTRY_ISSUE = "sentry_issue"
    SLACK_FILE = "slack_file"
    STATUSPAGE_INCIDENT = "statuspage_incident"
    ZENDESK_TICKET = "zendesk_ticket"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "IncidentAttachmentsV1ListResourceType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
