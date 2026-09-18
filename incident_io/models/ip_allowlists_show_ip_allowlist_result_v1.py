from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ip_allowlist_v1 import IPAllowlistV1


T = TypeVar("T", bound="IPAllowlistsShowIPAllowlistResultV1")


@_attrs_define
class IPAllowlistsShowIPAllowlistResultV1:
    """
    Example:
        {'ip_allowlist': {'allowlist': [{'label': 'London HQ', 'value': '192.0.2.0'}], 'enabled': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'version': 1}}

    Attributes:
        ip_allowlist (IPAllowlistV1):  Example: {'allowlist': [{'label': 'London HQ', 'value': '192.0.2.0'}], 'enabled':
            True, 'updated_at': '2021-08-17T13:28:57.801578Z', 'version': 1}.
    """

    ip_allowlist: IPAllowlistV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_allowlist = self.ip_allowlist.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_allowlist": ip_allowlist,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_allowlist_v1 import IPAllowlistV1

        d = dict(src_dict)
        ip_allowlist = IPAllowlistV1.from_dict(d.pop("ip_allowlist"))

        ip_allowlists_show_ip_allowlist_result_v1 = cls(
            ip_allowlist=ip_allowlist,
        )

        ip_allowlists_show_ip_allowlist_result_v1.additional_properties = d
        return ip_allowlists_show_ip_allowlist_result_v1

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
