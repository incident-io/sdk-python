from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogIPAllowlistUpdatedMetadataV2")


@_attrs_define
class AuditLogIPAllowlistUpdatedMetadataV2:
    """
    Example:
        {'additions': '["192.0.2.0","192.0.2.0/24"]', 'additions_count': '2', 'enabled': 'true', 'removals':
            '["192.0.2.1"]', 'removals_count': '1', 'version': '2'}

    Attributes:
        additions (str | Unset): A comma-separated array of newly added IPs/CIDRs. Max 500 characters Example:
            ["192.0.2.0","192.0.2.0/24"].
        additions_count (str | Unset): The number of IPs/CIDRs added to the allowlist Example: 2.
        enabled (str | Unset): Whether or not the IP allowlist is enabled after the update Example: true.
        removals (str | Unset): A comma-separated array of newly removed IPs/CIDRs. Max 500 characters Example:
            ["192.0.2.1"].
        removals_count (str | Unset): The number of IPs/CIDRs removed from the allowlist Example: 1.
        version (str | Unset): The version of the IP allowlist after the update Example: 2.
    """

    additions: str | Unset = UNSET
    additions_count: str | Unset = UNSET
    enabled: str | Unset = UNSET
    removals: str | Unset = UNSET
    removals_count: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additions = self.additions

        additions_count = self.additions_count

        enabled = self.enabled

        removals = self.removals

        removals_count = self.removals_count

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additions is not UNSET:
            field_dict["additions"] = additions
        if additions_count is not UNSET:
            field_dict["additions_count"] = additions_count
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if removals is not UNSET:
            field_dict["removals"] = removals
        if removals_count is not UNSET:
            field_dict["removals_count"] = removals_count
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        additions = d.pop("additions", UNSET)

        additions_count = d.pop("additions_count", UNSET)

        enabled = d.pop("enabled", UNSET)

        removals = d.pop("removals", UNSET)

        removals_count = d.pop("removals_count", UNSET)

        version = d.pop("version", UNSET)

        audit_log_ip_allowlist_updated_metadata_v2 = cls(
            additions=additions,
            additions_count=additions_count,
            enabled=enabled,
            removals=removals,
            removals_count=removals_count,
            version=version,
        )

        audit_log_ip_allowlist_updated_metadata_v2.additional_properties = d
        return audit_log_ip_allowlist_updated_metadata_v2

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
