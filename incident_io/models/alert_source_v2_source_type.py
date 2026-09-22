from enum import StrEnum


class AlertSourceV2SourceType(StrEnum):
    ALERTMANAGER = "alertmanager"
    APP_OPTICS = "app_optics"
    AZURE_DEVOPS = "azure_devops"
    AZURE_MONITOR = "azure_monitor"
    BIG_PANDA = "big_panda"
    BUGSNAG = "bugsnag"
    CHECKLY = "checkly"
    CHRONOSPHERE = "chronosphere"
    CLOUDFLARE = "cloudflare"
    CLOUDWATCH = "cloudwatch"
    CORALOGIX = "coralogix"
    CRONITOR = "cronitor"
    CROWDSTRIKE_FALCON = "crowdstrike_falcon"
    DASH0 = "dash0"
    DATADOG = "datadog"
    DYNATRACE = "dynatrace"
    ELASTICSEARCH = "elasticsearch"
    EMAIL = "email"
    EXPEL = "expel"
    GITHUB_ISSUE = "github_issue"
    GOOGLE_CLOUD = "google_cloud"
    GRAFANA = "grafana"
    HEARTBEAT = "heartbeat"
    HONEYCOMB = "honeycomb"
    HTTP = "http"
    HTTP_CUSTOM = "http_custom"
    ICINGA2 = "icinga2"
    INCOMING_CALLS = "incoming_calls"
    JIRA = "jira"
    JSM = "jsm"
    MONTE_CARLO = "monte_carlo"
    NAGIOS = "nagios"
    NEW_RELIC = "new_relic"
    OPSGENIE = "opsgenie"
    PAGER_DUTY = "pager_duty"
    PANTHER = "panther"
    PINGDOM = "pingdom"
    PRTG = "prtg"
    RUNSCOPE = "runscope"
    SALESFORCE_CASE = "salesforce_case"
    SENTRY = "sentry"
    SENTRY_METRIC = "sentry_metric"
    SERVICE_NOW = "service_now"
    SNS = "sns"
    SPLUNK = "splunk"
    STATUS_CAKE = "status_cake"
    STATUS_PAGE_VIEWS = "status_page_views"
    SUMO_LOGIC = "sumo_logic"
    UPTIME = "uptime"
    VERCEL = "vercel"
    WIZ = "wiz"
    ZENDESK = "zendesk"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "AlertSourceV2SourceType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
