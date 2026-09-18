from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogActorMetadataV2")


@_attrs_define
class AuditLogActorMetadataV2:
    """
    Example:
        {'alert_source_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'api_key_roles': 'abc123', 'external_resource_external_id':
            'q1234', 'external_resource_type': 'pager_duty_incident', 'user_base_role_slug': 'admin',
            'user_custom_role_slugs': 'engineering,security'}

    Attributes:
        alert_source_id (str | Unset): The alert source the alert fired on (if it's an alert actor) Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        api_key_roles (str | Unset): The roles that the API key has, separated by commas (if it's an API key actor)
            Example: abc123.
        external_resource_external_id (str | Unset): The ID of the external resource in the 3rd party system (if it's an
            external resource actor) Example: q1234.
        external_resource_type (str | Unset): The type of the external resource (if it's an external resource actor)
            Example: pager_duty_incident.
        user_base_role_slug (str | Unset): The base role slug of the user (if it's a user actor) Example: admin.
        user_custom_role_slugs (str | Unset): The custom role slugs of the user, separated by commas (if it's a user
            actor) Example: engineering,security.
    """

    alert_source_id: str | Unset = UNSET
    api_key_roles: str | Unset = UNSET
    external_resource_external_id: str | Unset = UNSET
    external_resource_type: str | Unset = UNSET
    user_base_role_slug: str | Unset = UNSET
    user_custom_role_slugs: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_source_id = self.alert_source_id

        api_key_roles = self.api_key_roles

        external_resource_external_id = self.external_resource_external_id

        external_resource_type = self.external_resource_type

        user_base_role_slug = self.user_base_role_slug

        user_custom_role_slugs = self.user_custom_role_slugs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_source_id is not UNSET:
            field_dict["alert_source_id"] = alert_source_id
        if api_key_roles is not UNSET:
            field_dict["api_key_roles"] = api_key_roles
        if external_resource_external_id is not UNSET:
            field_dict["external_resource_external_id"] = external_resource_external_id
        if external_resource_type is not UNSET:
            field_dict["external_resource_type"] = external_resource_type
        if user_base_role_slug is not UNSET:
            field_dict["user_base_role_slug"] = user_base_role_slug
        if user_custom_role_slugs is not UNSET:
            field_dict["user_custom_role_slugs"] = user_custom_role_slugs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alert_source_id = d.pop("alert_source_id", UNSET)

        api_key_roles = d.pop("api_key_roles", UNSET)

        external_resource_external_id = d.pop("external_resource_external_id", UNSET)

        external_resource_type = d.pop("external_resource_type", UNSET)

        user_base_role_slug = d.pop("user_base_role_slug", UNSET)

        user_custom_role_slugs = d.pop("user_custom_role_slugs", UNSET)

        audit_log_actor_metadata_v2 = cls(
            alert_source_id=alert_source_id,
            api_key_roles=api_key_roles,
            external_resource_external_id=external_resource_external_id,
            external_resource_type=external_resource_type,
            user_base_role_slug=user_base_role_slug,
            user_custom_role_slugs=user_custom_role_slugs,
        )

        audit_log_actor_metadata_v2.additional_properties = d
        return audit_log_actor_metadata_v2

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
