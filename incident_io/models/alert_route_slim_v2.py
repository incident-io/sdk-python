from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertRouteSlimV2")


@_attrs_define(kw_only=True)
class AlertRouteSlimV2:
    """
    Example:
        {'enabled': False, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Production incidents'}

    Attributes:
        enabled (bool): Whether this alert route is enabled or not Example: False.
        id (str): Unique identifier for this alert route config Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): The name of this alert route config, for the user's reference Example: Production incidents.
    """

    enabled: bool
    id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        id = d.pop("id")

        name = d.pop("name")

        alert_route_slim_v2 = cls(
            enabled=enabled,
            id=id,
            name=name,
        )

        alert_route_slim_v2.additional_properties = d
        return alert_route_slim_v2

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
