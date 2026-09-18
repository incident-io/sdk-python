from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogHrisTimeOffPolicyUpdatedMetadataV2")


@_attrs_define
class AuditLogHrisTimeOffPolicyUpdatedMetadataV2:
    """
    Example:
        {'behaviour': 'visible', 'connection_name': 'default', 'previous_behaviour': 'private', 'provider_slug':
            'bamboohr'}

    Attributes:
        behaviour (str | Unset): The visibility behaviour after the update (private, visible, or ignore) Example:
            visible.
        connection_name (str | Unset): The name of the Merge.dev connection the policy belongs to Example: default.
        previous_behaviour (str | Unset): The visibility behaviour before the update (private, visible, or ignore)
            Example: private.
        provider_slug (str | Unset): The Merge.dev HRIS provider slug (e.g. bamboohr, hibob) Example: bamboohr.
    """

    behaviour: str | Unset = UNSET
    connection_name: str | Unset = UNSET
    previous_behaviour: str | Unset = UNSET
    provider_slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        behaviour = self.behaviour

        connection_name = self.connection_name

        previous_behaviour = self.previous_behaviour

        provider_slug = self.provider_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if behaviour is not UNSET:
            field_dict["behaviour"] = behaviour
        if connection_name is not UNSET:
            field_dict["connection_name"] = connection_name
        if previous_behaviour is not UNSET:
            field_dict["previous_behaviour"] = previous_behaviour
        if provider_slug is not UNSET:
            field_dict["provider_slug"] = provider_slug

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        behaviour = d.pop("behaviour", UNSET)

        connection_name = d.pop("connection_name", UNSET)

        previous_behaviour = d.pop("previous_behaviour", UNSET)

        provider_slug = d.pop("provider_slug", UNSET)

        audit_log_hris_time_off_policy_updated_metadata_v2 = cls(
            behaviour=behaviour,
            connection_name=connection_name,
            previous_behaviour=previous_behaviour,
            provider_slug=provider_slug,
        )

        audit_log_hris_time_off_policy_updated_metadata_v2.additional_properties = d
        return audit_log_hris_time_off_policy_updated_metadata_v2

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
