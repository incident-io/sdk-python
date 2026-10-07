from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_log_actor_v2 import AuditLogActorV2
    from ..models.audit_log_entry_context_v2 import AuditLogEntryContextV2
    from ..models.audit_log_extension_plugin_updated_metadata_v2 import (
        AuditLogExtensionPluginUpdatedMetadataV2,
    )
    from ..models.audit_log_target_v2 import AuditLogTargetV2


T = TypeVar("T", bound="AuditLogsExtensionPluginUpdatedV1")


@_attrs_define(kw_only=True)
class AuditLogsExtensionPluginUpdatedV1:
    """
    Example:
        {'action': 'extension_plugin.updated', 'actor': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'metadata':
            {'user_base_role_slug': 'admin', 'user_custom_role_slugs': 'engineering,security'}, 'name': 'John Doe', 'type':
            'user'}, 'context': {'location': '1.2.3.4', 'user_agent': 'Chrome/91.0.4472.114'}, 'metadata': {'after_enabled':
            'true', 'after_enabled_skill_count': '2', 'after_name': 'acme-oncall', 'after_provider': 'github',
            'after_repo_name': 'oncall-plugins', 'after_repo_owner': 'acme-forks', 'after_skill_selection_mode': 'selected',
            'after_subpath': 'plugins/acme-oncall', 'before_enabled': 'false', 'before_enabled_skill_count': '4',
            'before_name': 'oncall', 'before_provider': 'github', 'before_repo_name': 'oncall-plugins', 'before_repo_owner':
            'acme', 'before_skill_selection_mode': 'automatic', 'before_subpath': 'plugins/acme-oncall', 'changed':
            'location'}, 'occurred_at': '2021-08-17T13:28:57.801578Z', 'targets': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'acme-oncall', 'type': 'extension_plugin'}], 'version': 1}

    Attributes:
        action (str): The type of log entry that this is Example: extension_plugin.updated.
        actor (AuditLogActorV2):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'metadata': {'user_base_role_slug':
            'admin', 'user_custom_role_slugs': 'engineering,security'}, 'name': 'John Doe', 'type': 'user'}.
        context (AuditLogEntryContextV2):  Example: {'location': '1.2.3.4', 'user_agent': 'Chrome/91.0.4472.114'}.
        metadata (AuditLogExtensionPluginUpdatedMetadataV2):  Example: {'after_enabled': 'true',
            'after_enabled_skill_count': '2', 'after_name': 'acme-oncall', 'after_provider': 'github', 'after_repo_name':
            'oncall-plugins', 'after_repo_owner': 'acme-forks', 'after_skill_selection_mode': 'selected', 'after_subpath':
            'plugins/acme-oncall', 'before_enabled': 'false', 'before_enabled_skill_count': '4', 'before_name': 'oncall',
            'before_provider': 'github', 'before_repo_name': 'oncall-plugins', 'before_repo_owner': 'acme',
            'before_skill_selection_mode': 'automatic', 'before_subpath': 'plugins/acme-oncall', 'changed': 'location'}.
        occurred_at (datetime.datetime): When the entry occurred Example: 2021-08-17T13:28:57.801578Z.
        targets (list[AuditLogTargetV2]): The custom field that was created Example: [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'acme-oncall', 'type': 'extension_plugin'}].
        version (int): Which version the event is Example: 1.
    """

    action: str
    actor: AuditLogActorV2
    context: AuditLogEntryContextV2
    metadata: AuditLogExtensionPluginUpdatedMetadataV2
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
        from ..models.audit_log_extension_plugin_updated_metadata_v2 import (
            AuditLogExtensionPluginUpdatedMetadataV2,
        )
        from ..models.audit_log_target_v2 import AuditLogTargetV2

        d = dict(src_dict)
        action = d.pop("action")

        actor = AuditLogActorV2.from_dict(d.pop("actor"))

        context = AuditLogEntryContextV2.from_dict(d.pop("context"))

        metadata = AuditLogExtensionPluginUpdatedMetadataV2.from_dict(d.pop("metadata"))

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = AuditLogTargetV2.from_dict(targets_item_data)

            targets.append(targets_item)

        version = d.pop("version")

        audit_logs_extension_plugin_updated_v1 = cls(
            action=action,
            actor=actor,
            context=context,
            metadata=metadata,
            occurred_at=occurred_at,
            targets=targets,
            version=version,
        )

        audit_logs_extension_plugin_updated_v1.additional_properties = d
        return audit_logs_extension_plugin_updated_v1

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
