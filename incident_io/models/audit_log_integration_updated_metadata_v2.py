from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogIntegrationUpdatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogIntegrationUpdatedMetadataV2:
    """
    Example:
        {'changed_fields': 'connector_config_id,personal_access_token', 'connector_config_id_from':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'connector_config_id_to': '01FCNDV6P870EA6S7TK1DSYDG1', 'host_from':
            'https://jira.example.com', 'host_to': 'https://jira.internal.example.com', 'integration_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        changed_fields (str): Comma-separated names of the fields that changed, such as connector_config_id, host,
            tls_root_cert, ca_certificate, personal_access_token, app_id, private_key or auth_type Example:
            connector_config_id,personal_access_token.
        integration_id (str): ID of the GitLab installation, GitHub Enterprise app or Jira Server config that changed
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        connector_config_id_from (str | Unset): ID of the connector requests went through before the change, absent when
            there was none Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        connector_config_id_to (str | Unset): ID of the connector requests go through after the change, absent when
            there is none Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        host_from (str | Unset): The host before the change, absent when there was none Example:
            https://jira.example.com.
        host_to (str | Unset): The host after the change Example: https://jira.internal.example.com.
    """

    changed_fields: str
    integration_id: str
    connector_config_id_from: str | Unset = UNSET
    connector_config_id_to: str | Unset = UNSET
    host_from: str | Unset = UNSET
    host_to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed_fields = self.changed_fields

        integration_id = self.integration_id

        connector_config_id_from = self.connector_config_id_from

        connector_config_id_to = self.connector_config_id_to

        host_from = self.host_from

        host_to = self.host_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changed_fields": changed_fields,
                "integration_id": integration_id,
            }
        )
        if connector_config_id_from is not UNSET:
            field_dict["connector_config_id_from"] = connector_config_id_from
        if connector_config_id_to is not UNSET:
            field_dict["connector_config_id_to"] = connector_config_id_to
        if host_from is not UNSET:
            field_dict["host_from"] = host_from
        if host_to is not UNSET:
            field_dict["host_to"] = host_to

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        changed_fields = d.pop("changed_fields")

        integration_id = d.pop("integration_id")

        connector_config_id_from = d.pop("connector_config_id_from", UNSET)

        connector_config_id_to = d.pop("connector_config_id_to", UNSET)

        host_from = d.pop("host_from", UNSET)

        host_to = d.pop("host_to", UNSET)

        audit_log_integration_updated_metadata_v2 = cls(
            changed_fields=changed_fields,
            integration_id=integration_id,
            connector_config_id_from=connector_config_id_from,
            connector_config_id_to=connector_config_id_to,
            host_from=host_from,
            host_to=host_to,
        )

        audit_log_integration_updated_metadata_v2.additional_properties = d
        return audit_log_integration_updated_metadata_v2

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
