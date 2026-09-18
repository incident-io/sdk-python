from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertAttributesUpdatePayloadV2")


@_attrs_define
class AlertAttributesUpdatePayloadV2:
    """
    Example:
        {'array': False, 'emoji': 'fire', 'name': 'service', 'required': False, 'type':
            'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}

    Attributes:
        array (bool): Whether this attribute is an array Example: False.
        name (str): Unique name of this attribute Example: service.
        type_ (str): Engine resource name for this attribute Example: CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"].
        emoji (str | Unset): The emoji to display alongside this attribute in chat messages, stored without colons
            Example: fire.
        required (bool | Unset): Whether this attribute is required. If this field is not set, the existing setting will
            be preserved. Example: False.
    """

    array: bool
    name: str
    type_: str
    emoji: str | Unset = UNSET
    required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        array = self.array

        name = self.name

        type_ = self.type_

        emoji = self.emoji

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "name": name,
                "type": type_,
            }
        )
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        array = d.pop("array")

        name = d.pop("name")

        type_ = d.pop("type")

        emoji = d.pop("emoji", UNSET)

        required = d.pop("required", UNSET)

        alert_attributes_update_payload_v2 = cls(
            array=array,
            name=name,
            type_=type_,
            emoji=emoji,
            required=required,
        )

        alert_attributes_update_payload_v2.additional_properties = d
        return alert_attributes_update_payload_v2

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
