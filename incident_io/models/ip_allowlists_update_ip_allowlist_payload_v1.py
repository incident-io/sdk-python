from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ip_allowlist_item_v1 import IPAllowlistItemV1


T = TypeVar("T", bound="IPAllowlistsUpdateIPAllowlistPayloadV1")


@_attrs_define
class IPAllowlistsUpdateIPAllowlistPayloadV1:
    """
    Example:
        {'allowlist': [{'label': 'London HQ', 'value': '192.0.2.0'}], 'enabled': True, 'version': 1}

    Attributes:
        allowlist (list[IPAllowlistItemV1]): A list of IP addresses or CIDR prefixes to allow Example: [{'label':
            'London HQ', 'value': '192.0.2.0'}].
        enabled (bool): Whether this IP allowlist is enabled or not Example: True.
        version (int): The version of this IP allowlist Example: 1.
    """

    allowlist: list[IPAllowlistItemV1]
    enabled: bool
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowlist = []
        for allowlist_item_data in self.allowlist:
            allowlist_item = allowlist_item_data.to_dict()
            allowlist.append(allowlist_item)

        enabled = self.enabled

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowlist": allowlist,
                "enabled": enabled,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_allowlist_item_v1 import IPAllowlistItemV1

        d = dict(src_dict)
        allowlist = []
        _allowlist = d.pop("allowlist")
        for allowlist_item_data in _allowlist:
            allowlist_item = IPAllowlistItemV1.from_dict(allowlist_item_data)

            allowlist.append(allowlist_item)

        enabled = d.pop("enabled")

        version = d.pop("version")

        ip_allowlists_update_ip_allowlist_payload_v1 = cls(
            allowlist=allowlist,
            enabled=enabled,
            version=version,
        )

        ip_allowlists_update_ip_allowlist_payload_v1.additional_properties = d
        return ip_allowlists_update_ip_allowlist_payload_v1

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
