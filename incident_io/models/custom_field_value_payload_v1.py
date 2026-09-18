from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldValuePayloadV1")


@_attrs_define
class CustomFieldValuePayloadV1:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}

    Attributes:
        id (str | Unset): Unique identifier for the custom field value Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        value_catalog_entry_id (str | Unset): ID of the catalog entry. You can also use an ExternalID or an Alias of the
            catalog entry. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        value_link (str | Unset): If the custom field type is 'link', this will contain the value assigned. Example:
            https://google.com/.
        value_numeric (str | Unset): If the custom field type is 'numeric', this will contain the value assigned.
            Example: 123.456.
        value_option_id (str | Unset): ID of the custom field option Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        value_text (str | Unset): If the custom field type is 'text', this will contain the value assigned. Example:
            This is my text field, I hope you like it.
        value_timestamp (str | Unset): Deprecated: please use incident timestamp values instead
    """

    id: str | Unset = UNSET
    value_catalog_entry_id: str | Unset = UNSET
    value_link: str | Unset = UNSET
    value_numeric: str | Unset = UNSET
    value_option_id: str | Unset = UNSET
    value_text: str | Unset = UNSET
    value_timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value_catalog_entry_id = self.value_catalog_entry_id

        value_link = self.value_link

        value_numeric = self.value_numeric

        value_option_id = self.value_option_id

        value_text = self.value_text

        value_timestamp = self.value_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value_catalog_entry_id is not UNSET:
            field_dict["value_catalog_entry_id"] = value_catalog_entry_id
        if value_link is not UNSET:
            field_dict["value_link"] = value_link
        if value_numeric is not UNSET:
            field_dict["value_numeric"] = value_numeric
        if value_option_id is not UNSET:
            field_dict["value_option_id"] = value_option_id
        if value_text is not UNSET:
            field_dict["value_text"] = value_text
        if value_timestamp is not UNSET:
            field_dict["value_timestamp"] = value_timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        value_catalog_entry_id = d.pop("value_catalog_entry_id", UNSET)

        value_link = d.pop("value_link", UNSET)

        value_numeric = d.pop("value_numeric", UNSET)

        value_option_id = d.pop("value_option_id", UNSET)

        value_text = d.pop("value_text", UNSET)

        value_timestamp = d.pop("value_timestamp", UNSET)

        custom_field_value_payload_v1 = cls(
            id=id,
            value_catalog_entry_id=value_catalog_entry_id,
            value_link=value_link,
            value_numeric=value_numeric,
            value_option_id=value_option_id,
            value_text=value_text,
            value_timestamp=value_timestamp,
        )

        custom_field_value_payload_v1.additional_properties = d
        return custom_field_value_payload_v1

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
