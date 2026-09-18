from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ip_range_v1 import IPRangeV1


T = TypeVar("T", bound="UtilitiesIPRangesResultV1")


@_attrs_define
class UtilitiesIPRangesResultV1:
    """
    Example:
        {'ip_ranges': [{'cidr': '34.91.219.113/32', 'description': 'Requests to your systems from integrations and from
            workflow "Send a webhook" steps'}]}

    Attributes:
        ip_ranges (list[IPRangeV1]): Every address our traffic to you may originate from Example: [{'cidr':
            '34.91.219.113/32', 'description': 'Requests to your systems from integrations and from workflow "Send a
            webhook" steps'}].
    """

    ip_ranges: list[IPRangeV1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_ranges = []
        for ip_ranges_item_data in self.ip_ranges:
            ip_ranges_item = ip_ranges_item_data.to_dict()
            ip_ranges.append(ip_ranges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_ranges": ip_ranges,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_range_v1 import IPRangeV1

        d = dict(src_dict)
        ip_ranges = []
        _ip_ranges = d.pop("ip_ranges")
        for ip_ranges_item_data in _ip_ranges:
            ip_ranges_item = IPRangeV1.from_dict(ip_ranges_item_data)

            ip_ranges.append(ip_ranges_item)

        utilities_ip_ranges_result_v1 = cls(
            ip_ranges=ip_ranges,
        )

        utilities_ip_ranges_result_v1.additional_properties = d
        return utilities_ip_ranges_result_v1

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
