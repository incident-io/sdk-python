from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertAttributeV2")


@_attrs_define(kw_only=True)
class AlertAttributeV2:
    """
    Example:
        {'array': False, 'emoji': 'fire', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'service', 'required': False,
            'type': 'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}

    Attributes:
        array (bool): Whether this attribute is an array Example: False.
        id (str): The ID of this attribute Example: 01GW2G3V0S59R238FAHPDS1R66.
        name (str): Unique name of this attribute Example: service.
        required (bool): Whether this attribute is required. If this field is not set, the existing setting will be
            preserved. Example: False.
        type_ (str): Engine resource name for this attribute Example: CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"].
        emoji (str | Unset): The emoji to display alongside this attribute in chat messages, stored without colons
            Example: fire.
    """

    array: bool
    id: str
    name: str
    required: bool
    type_: str
    emoji: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        array = self.array

        id = self.id

        name = self.name

        required = self.required

        type_ = self.type_

        emoji = self.emoji

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "id": id,
                "name": name,
                "required": required,
                "type": type_,
            }
        )
        if emoji is not UNSET:
            field_dict["emoji"] = emoji

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        array = d.pop("array")

        id = d.pop("id")

        name = d.pop("name")

        required = d.pop("required")

        type_ = d.pop("type")

        emoji = d.pop("emoji", UNSET)

        alert_attribute_v2 = cls(
            array=array,
            id=id,
            name=name,
            required=required,
            type_=type_,
            emoji=emoji,
        )

        alert_attribute_v2.additional_properties = d
        return alert_attribute_v2

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
