from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="APIKeyActorV2")


@_attrs_define(kw_only=True)
class APIKeyActorV2:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}

    Attributes:
        id (str): Unique identifier for this API key Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): The name of the API key, for the user's reference Example: My test API key.
    """

    id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        api_key_actor_v2 = cls(
            id=id,
            name=name,
        )

        api_key_actor_v2.additional_properties = d
        return api_key_actor_v2

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
