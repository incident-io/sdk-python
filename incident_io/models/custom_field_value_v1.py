from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_option_v1 import CustomFieldOptionV1
    from ..models.embedded_catalog_entry_v1 import EmbeddedCatalogEntryV1


T = TypeVar("T", bound="CustomFieldValueV1")


@_attrs_define(kw_only=True)
class CustomFieldValueV1:
    """
    Example:
        {'value_catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'},
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}

    Attributes:
        value_catalog_entry (EmbeddedCatalogEntryV1 | Unset):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Primary On-call'}.
        value_link (str | Unset): If the custom field type is 'link', this will contain the value assigned. Example:
            https://google.com/.
        value_numeric (str | Unset): If the custom field type is 'numeric', this will contain the value assigned.
            Example: 123.456.
        value_option (CustomFieldOptionV1 | Unset):  Example: {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}.
        value_text (str | Unset): If the custom field type is 'text', this will contain the value assigned. Example:
            This is my text field, I hope you like it.
    """

    value_catalog_entry: EmbeddedCatalogEntryV1 | Unset = UNSET
    value_link: str | Unset = UNSET
    value_numeric: str | Unset = UNSET
    value_option: CustomFieldOptionV1 | Unset = UNSET
    value_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_catalog_entry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_catalog_entry, Unset):
            value_catalog_entry = self.value_catalog_entry.to_dict()

        value_link = self.value_link

        value_numeric = self.value_numeric

        value_option: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_option, Unset):
            value_option = self.value_option.to_dict()

        value_text = self.value_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value_catalog_entry is not UNSET:
            field_dict["value_catalog_entry"] = value_catalog_entry
        if value_link is not UNSET:
            field_dict["value_link"] = value_link
        if value_numeric is not UNSET:
            field_dict["value_numeric"] = value_numeric
        if value_option is not UNSET:
            field_dict["value_option"] = value_option
        if value_text is not UNSET:
            field_dict["value_text"] = value_text

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_field_option_v1 import CustomFieldOptionV1
        from ..models.embedded_catalog_entry_v1 import (
            EmbeddedCatalogEntryV1,
        )

        d = dict(src_dict)
        _value_catalog_entry = d.pop("value_catalog_entry", UNSET)
        value_catalog_entry: EmbeddedCatalogEntryV1 | Unset
        if isinstance(_value_catalog_entry, Unset):
            value_catalog_entry = UNSET
        else:
            value_catalog_entry = EmbeddedCatalogEntryV1.from_dict(_value_catalog_entry)

        value_link = d.pop("value_link", UNSET)

        value_numeric = d.pop("value_numeric", UNSET)

        _value_option = d.pop("value_option", UNSET)
        value_option: CustomFieldOptionV1 | Unset
        if isinstance(_value_option, Unset):
            value_option = UNSET
        else:
            value_option = CustomFieldOptionV1.from_dict(_value_option)

        value_text = d.pop("value_text", UNSET)

        custom_field_value_v1 = cls(
            value_catalog_entry=value_catalog_entry,
            value_link=value_link,
            value_numeric=value_numeric,
            value_option=value_option,
            value_text=value_text,
        )

        custom_field_value_v1.additional_properties = d
        return custom_field_value_v1

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
