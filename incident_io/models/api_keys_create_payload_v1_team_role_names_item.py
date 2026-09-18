from enum import StrEnum


class APIKeysCreatePayloadV1TeamRoleNamesItem(StrEnum):
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
