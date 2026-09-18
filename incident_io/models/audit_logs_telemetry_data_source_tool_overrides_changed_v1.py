from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_log_actor_v2 import AuditLogActorV2
    from ..models.audit_log_entry_context_v2 import AuditLogEntryContextV2
    from ..models.audit_log_target_v2 import AuditLogTargetV2
    from ..models.audit_log_telemetry_data_source_tool_overrides_changed_metadata_v2 import (
        AuditLogTelemetryDataSourceToolOverridesChangedMetadataV2,
    )


T = TypeVar("T", bound="AuditLogsTelemetryDataSourceToolOverridesChangedV1")


@_attrs_define
class AuditLogsTelemetryDataSourceToolOverridesChangedV1:
    """
    Example:
        {'action': 'telemetry_data_source.tool_overrides_changed', 'actor': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'metadata': {'user_base_role_slug': 'admin', 'user_custom_role_slugs': 'engineering,security'}, 'name': 'John
            Doe', 'type': 'user'}, 'context': {'location': '1.2.3.4', 'user_agent': 'Chrome/91.0.4472.114'}, 'metadata':
            {'after': '{"surfaces":{"chat":{"value":{"type":"deny"},"set_at":"2026-01-
            02T00:00:00Z","set_by":"01FCNDV6P870EA6S7TK1DSYDG0"}}}', 'before': '{"surfaces":{"chat":{"value":{"type":"allow"
            },"set_at":"2026-01-01T00:00:00Z","set_by":"01FCNDV6P870EA6S7TK1DSYDG0"}}}', 'change_id':
            '01JD8ZQK9X0000000000000000', 'tool': 'restart_service'}, 'occurred_at': '2021-08-17T13:28:57.801578Z',
            'targets': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Acme Deploy', 'type': 'extension_connector'}, {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'restart_service', 'type': 'extension_connector_tool'}], 'version': 1}

    Attributes:
        action (str): The type of log entry that this is Example: telemetry_data_source.tool_overrides_changed.
        actor (AuditLogActorV2):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'metadata': {'user_base_role_slug':
            'admin', 'user_custom_role_slugs': 'engineering,security'}, 'name': 'John Doe', 'type': 'user'}.
        context (AuditLogEntryContextV2):  Example: {'location': '1.2.3.4', 'user_agent': 'Chrome/91.0.4472.114'}.
        metadata (AuditLogTelemetryDataSourceToolOverridesChangedMetadataV2):  Example: {'after': '{"surfaces":{"chat":{
            "value":{"type":"deny"},"set_at":"2026-01-02T00:00:00Z","set_by":"01FCNDV6P870EA6S7TK1DSYDG0"}}}', 'before': '{"
            surfaces":{"chat":{"value":{"type":"allow"},"set_at":"2026-01-
            01T00:00:00Z","set_by":"01FCNDV6P870EA6S7TK1DSYDG0"}}}', 'change_id': '01JD8ZQK9X0000000000000000', 'tool':
            'restart_service'}.
        occurred_at (datetime.datetime): When the entry occurred Example: 2021-08-17T13:28:57.801578Z.
        targets (list[AuditLogTargetV2]): The custom field that was created Example: [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Acme Deploy', 'type': 'extension_connector'}, {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'restart_service', 'type': 'extension_connector_tool'}].
        version (int): Which version the event is Example: 1.
    """

    action: str
    actor: AuditLogActorV2
    context: AuditLogEntryContextV2
    metadata: AuditLogTelemetryDataSourceToolOverridesChangedMetadataV2
    occurred_at: datetime.datetime
    targets: list[AuditLogTargetV2]
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        actor = self.actor.to_dict()

        context = self.context.to_dict()

        metadata = self.metadata.to_dict()

        occurred_at = self.occurred_at.isoformat()

        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "actor": actor,
                "context": context,
                "metadata": metadata,
                "occurred_at": occurred_at,
                "targets": targets,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_log_actor_v2 import AuditLogActorV2
        from ..models.audit_log_entry_context_v2 import (
            AuditLogEntryContextV2,
        )
        from ..models.audit_log_target_v2 import AuditLogTargetV2
        from ..models.audit_log_telemetry_data_source_tool_overrides_changed_metadata_v2 import (
            AuditLogTelemetryDataSourceToolOverridesChangedMetadataV2,
        )

        d = dict(src_dict)
        action = d.pop("action")

        actor = AuditLogActorV2.from_dict(d.pop("actor"))

        context = AuditLogEntryContextV2.from_dict(d.pop("context"))

        metadata = AuditLogTelemetryDataSourceToolOverridesChangedMetadataV2.from_dict(
            d.pop("metadata")
        )

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = AuditLogTargetV2.from_dict(targets_item_data)

            targets.append(targets_item)

        version = d.pop("version")

        audit_logs_telemetry_data_source_tool_overrides_changed_v1 = cls(
            action=action,
            actor=actor,
            context=context,
            metadata=metadata,
            occurred_at=occurred_at,
            targets=targets,
            version=version,
        )

        audit_logs_telemetry_data_source_tool_overrides_changed_v1.additional_properties = d
        return audit_logs_telemetry_data_source_tool_overrides_changed_v1

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
