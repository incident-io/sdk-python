from enum import StrEnum


class ManagedResourcesCreateManagedResourcePayloadV2ResourceType(StrEnum):
    ALERT_ROUTE = "alert_route"
    ALERT_SOURCE = "alert_source"
    API_KEY = "api_key"
    ESCALATION_PATH = "escalation_path"
    ESCALATION_PATH_TEMPLATE = "escalation_path_template"
    INCIDENT_FORM = "incident_form"
    INCIDENT_TEMPLATE = "incident_template"
    POLICY = "policy"
    SCHEDULE = "schedule"
    SCHEDULE_SYNC_RULE = "schedule_sync_rule"
    SCHEDULE_SYNC_TARGET = "schedule_sync_target"
    SECRET = "secret"
    STATUS_PAGE_COMPONENT = "status_page_component"
    STATUS_PAGE_STRUCTURE = "status_page_structure"
    TEAM_GROUPING_PREFERENCE = "team_grouping_preference"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "ManagedResourcesCreateManagedResourcePayloadV2ResourceType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
