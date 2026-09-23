from enum import StrEnum


class APIKeyRoleV1Name(StrEnum):
    ACT_ON_BEHALF_OF_USERS = "act_on_behalf_of_users"
    API_KEYS_MANAGE = "api_keys_manage"
    CALL_TRANSCRIPTS_VIEWER = "call_transcripts_viewer"
    CATALOG_EDITOR = "catalog_editor"
    CATALOG_VIEWER = "catalog_viewer"
    DOCUMENTS_VIEWER = "documents_viewer"
    ESCALATION_CREATOR = "escalation_creator"
    GLOBAL_ACCESS = "global_access"
    HEARTBEATS_PING = "heartbeats_ping"
    INCIDENT_CREATOR = "incident_creator"
    INCIDENT_EDITOR = "incident_editor"
    INCIDENT_MEMBERSHIPS_EDITOR = "incident_memberships_editor"
    INCIDENT_WORKLOAD_PRIVATE_VIEWER = "incident_workload_private_viewer"
    INCIDENT_WORKLOAD_VIEWER = "incident_workload_viewer"
    INVESTIGATIONS_EDITOR = "investigations_editor"
    INVESTIGATION_DOWNLOAD = "investigation_download"
    MANAGE_SETTINGS = "manage_settings"
    NOTIFICATION_METHODS_MANAGE = "notification_methods_manage"
    NOTIFICATION_METHODS_UNREDACTED_VIEWER = "notification_methods_unredacted_viewer"
    ON_CALL_EDITOR = "on_call_editor"
    ON_CALL_VIEWER = "on_call_viewer"
    PAY_CONFIGS_EDITOR = "pay_configs_editor"
    PAY_CONFIGS_VIEWER = "pay_configs_viewer"
    PAY_REPORTS_EDITOR = "pay_reports_editor"
    PAY_REPORTS_VIEWER = "pay_reports_viewer"
    POLICIES_VIEWER = "policies_viewer"
    POLICY_FINDINGS_MANAGE = "policy_findings_manage"
    POSTMORTEMS_MANAGE = "postmortems_manage"
    POST_INCIDENT_FLOW_OPT_OUT = "post_incident_flow_opt_out"
    PRIVATE_ESCALATION_WORKFLOWS_EDITOR = "private_escalation_workflows_editor"
    PRIVATE_WORKFLOWS_EDITOR = "private_workflows_editor"
    SCHEDULES_EDITOR = "schedules_editor"
    SCHEDULES_READER = "schedules_reader"
    SCHEDULE_OVERRIDES_EDITOR = "schedule_overrides_editor"
    SECRETS_MANAGE = "secrets_manage"
    SECRETS_USE = "secrets_use"
    SECURITY_SETTINGS_EDITOR = "security_settings_editor"
    STATUS_PAGE_PUBLISHER = "status_page_publisher"
    STATUS_PAGE_VIEWER = "status_page_viewer"
    TEAM_MEMBERSHIPS_MANAGE = "team_memberships_manage"
    TELEMETRY_DATA_SOURCE_UPDATE = "telemetry_data_source_update"
    TELEMETRY_QUERY_RESTRICTED = "telemetry_query_restricted"
    TELEMETRY_VIEWER = "telemetry_viewer"
    VIEWER = "viewer"
    WORKFLOWS_EDITOR = "workflows_editor"
    WORKFLOWS_VIEWER = "workflows_viewer"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "APIKeyRoleV1Name":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
