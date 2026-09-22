from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallRouteAllowedCallerV2")


@_attrs_define(kw_only=True)
class CallRouteAllowedCallerV2:
    """A phone number allowed to reach a call route.

    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Regulator duty desk', 'phone_number': '+15551234567'}

    Attributes:
        id (str): Unique identifier for this allowed caller Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        phone_number (str): The number allowed to call this route, in international format Example: +15551234567.
        name (str | Unset): Label for whose number this is Example: Regulator duty desk.
    """

    id: str
    phone_number: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        phone_number = self.phone_number

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "phone_number": phone_number,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        phone_number = d.pop("phone_number")

        name = d.pop("name", UNSET)

        call_route_allowed_caller_v2 = cls(
            id=id,
            phone_number=phone_number,
            name=name,
        )

        call_route_allowed_caller_v2.additional_properties = d
        return call_route_allowed_caller_v2

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
