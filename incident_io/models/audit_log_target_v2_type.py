from enum import StrEnum


class AuditLogTargetV2Type(StrEnum):
    ACTIVITY_LOG = "activity_log"
    ALERT = "alert"
    ALERT_CHAT_MESSAGE_TEMPLATE = "alert_chat_message_template"
    ALERT_PRIORITY = "alert_priority"
    ALERT_ROUTE = "alert_route"
    ALERT_SCHEMA = "alert_schema"
    ALERT_SOURCE = "alert_source"
    ANNOUNCEMENT_POST_TEMPLATE = "announcement_post_template"
    ANNOUNCEMENT_RULE = "announcement_rule"
    API_KEY = "api_key"
    CATALOG_ATTRIBUTE = "catalog_attribute"
    CATALOG_ENTRY = "catalog_entry"
    CATALOG_TYPE = "catalog_type"
    CONNECTOR_CONFIG = "connector_config"
    CUSTOM_FIELD = "custom_field"
    DEBRIEF_INVITE_RULE = "debrief_invite_rule"
    ESCALATION = "escalation"
    ESCALATION_PATH = "escalation_path"
    ESCALATION_PATH_TEMPLATE = "escalation_path_template"
    EXTENSION_CONNECTOR = "extension_connector"
    EXTENSION_CONNECTOR_TOOL = "extension_connector_tool"
    FOLLOW_UP_CATEGORY = "follow_up_category"
    FOLLOW_UP_PRIORITY = "follow_up_priority"
    HOLIDAY_USER_FEED = "holiday_user_feed"
    HRIS_TIME_OFF_POLICY = "hris_time_off_policy"
    INCIDENT = "incident"
    INCIDENT_CALL_SETTING = "incident_call_setting"
    INCIDENT_CALL_TRANSCRIPTION_SESSION = "incident_call_transcription_session"
    INCIDENT_DURATION_METRIC = "incident_duration_metric"
    INCIDENT_ROLE = "incident_role"
    INCIDENT_STATUS = "incident_status"
    INCIDENT_TEMPLATE = "incident_template"
    INCIDENT_TIMESTAMP = "incident_timestamp"
    INCIDENT_TIMESTAMP_SET_BY_RULE = "incident_timestamp_set_by_rule"
    INCIDENT_TYPE = "incident_type"
    INTEGRATION = "integration"
    INTERNAL_STATUS_PAGE = "internal_status_page"
    IP_ALLOWLIST = "ip_allowlist"
    MAINTENANCE_WINDOW = "maintenance_window"
    NUDGE = "nudge"
    ON_CALL_NOTIFICATION_METHOD = "on_call_notification_method"
    ON_CALL_UPSELL_REQUEST = "on_call_upsell_request"
    ORGANISATION = "organisation"
    ORGANISATION_SETTINGS = "organisation_settings"
    POLICY = "policy"
    POLICY_REPORT_SCHEDULE = "policy_report_schedule"
    POSTMORTEM_TEMPLATE = "postmortem_template"
    POSTMORTEM_TEMPLATE_SECTION = "postmortem_template_section"
    POST_INCIDENT_TASK = "post_incident_task"
    PRIVATE_INCIDENT_MEMBERSHIP = "private_incident_membership"
    RBAC_ROLE = "rbac_role"
    SCHEDULE = "schedule"
    SCHEDULE_OVERRIDE = "schedule_override"
    SCHEDULE_SYNC_RULE = "schedule_sync_rule"
    SCHEDULE_SYNC_TARGET = "schedule_sync_target"
    SCIM_GROUP = "scim_group"
    SECRET = "secret"
    SEVERITY = "severity"
    STATUS_PAGE = "status_page"
    STATUS_PAGE_SUB_PAGE = "status_page_sub_page"
    STATUS_PAGE_TEMPLATE = "status_page_template"
    TEAM_ROLE = "team_role"
    TEAM_SETTINGS = "team_settings"
    TELEMETRY_DATA_SOURCE = "telemetry_data_source"
    TIMELINE_ITEM = "timeline_item"
    USER = "user"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "AuditLogTargetV2Type":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
