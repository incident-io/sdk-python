from enum import StrEnum


class APIKeyTeamRoleV1Name(StrEnum):
    API_KEYS_MANAGE = "api_keys_manage"
    CATALOG_EDITOR = "catalog_editor"
    ESCALATION_CREATOR = "escalation_creator"
    HEARTBEATS_PING = "heartbeats_ping"
    ON_CALL_EDITOR = "on_call_editor"
    PRIVATE_WORKFLOWS_EDITOR = "private_workflows_editor"
    SCHEDULES_EDITOR = "schedules_editor"
    SCHEDULES_READER = "schedules_reader"
    SCHEDULE_OVERRIDES_EDITOR = "schedule_overrides_editor"
    SECRETS_MANAGE = "secrets_manage"
    SECRETS_USE = "secrets_use"
    TELEMETRY_DATA_SOURCE_UPDATE = "telemetry_data_source_update"
    TELEMETRY_QUERY_RESTRICTED = "telemetry_query_restricted"
    WORKFLOWS_EDITOR = "workflows_editor"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "APIKeyTeamRoleV1Name":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
