from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldOptionsCreatePayloadV1")


@_attrs_define(kw_only=True)
class CustomFieldOptionsCreatePayloadV1:
    """
    Example:
        {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}

    Attributes:
        custom_field_id (str): ID of the custom field this option belongs to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        value (str): Human readable name for the custom field option. Values must not start or end with whitespace, or
            contain tabs or newlines. Example: Product.
        sort_key (int | Unset): Sort key used to order the custom field options correctly Default: 1000. Example: 10.
    """

    custom_field_id: str
    value: str
    sort_key: int | Unset = 1000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_field_id = self.custom_field_id

        value = self.value

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field_id": custom_field_id,
                "value": value,
            }
        )
        if sort_key is not UNSET:
            field_dict["sort_key"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        custom_field_id = d.pop("custom_field_id")

        value = d.pop("value")

        sort_key = d.pop("sort_key", UNSET)

        custom_field_options_create_payload_v1 = cls(
            custom_field_id=custom_field_id,
            value=value,
            sort_key=sort_key,
        )

        custom_field_options_create_payload_v1.additional_properties = d
        return custom_field_options_create_payload_v1

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
