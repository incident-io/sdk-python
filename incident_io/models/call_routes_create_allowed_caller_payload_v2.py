from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallRoutesCreateAllowedCallerPayloadV2")


@_attrs_define
class CallRoutesCreateAllowedCallerPayloadV2:
    """
    Example:
        {'name': 'Regulator duty desk', 'phone_number': '+15551234567'}

    Attributes:
        phone_number (str): The number to allow, in international format Example: +15551234567.
        name (str | Unset): Label for whose number this is Example: Regulator duty desk.
    """

    phone_number: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_number = self.phone_number

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone_number": phone_number,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        phone_number = d.pop("phone_number")

        name = d.pop("name", UNSET)

        call_routes_create_allowed_caller_payload_v2 = cls(
            phone_number=phone_number,
            name=name,
        )

        call_routes_create_allowed_caller_payload_v2.additional_properties = d
        return call_routes_create_allowed_caller_payload_v2

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
