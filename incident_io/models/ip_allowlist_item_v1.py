from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPAllowlistItemV1")


@_attrs_define
class IPAllowlistItemV1:
    """
    Example:
        {'label': 'London HQ', 'value': '192.0.2.0'}

    Attributes:
        value (str): An IP address or a CIDR IP prefix to allow Example: 192.0.2.0.
        label (str | Unset): A label to help identify this IP or prefix Example: London HQ.
    """

    value: str
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        value = d.pop("value")

        label = d.pop("label", UNSET)

        ip_allowlist_item_v1 = cls(
            value=value,
            label=label,
        )

        ip_allowlist_item_v1.additional_properties = d
        return ip_allowlist_item_v1

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
