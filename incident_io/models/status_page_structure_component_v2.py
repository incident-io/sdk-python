from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatusPageStructureComponentV2")


@_attrs_define(kw_only=True)
class StatusPageStructureComponentV2:
    """
    Example:
        {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'display_uptime': True, 'hidden': False, 'name': 'App'}

    Attributes:
        component_id (str): The ID of the affected component. This may be found by calling the ShowStatusPageStructure
            endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        display_uptime (bool): Whether the page shows this component's uptime Example: True.
        hidden (bool): Whether the component is hidden from the page Example: False.
        name (str): The name of this component Example: App.
    """

    component_id: str
    display_uptime: bool
    hidden: bool
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_id = self.component_id

        display_uptime = self.display_uptime

        hidden = self.hidden

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_id": component_id,
                "display_uptime": display_uptime,
                "hidden": hidden,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        component_id = d.pop("component_id")

        display_uptime = d.pop("display_uptime")

        hidden = d.pop("hidden")

        name = d.pop("name")

        status_page_structure_component_v2 = cls(
            component_id=component_id,
            display_uptime=display_uptime,
            hidden=hidden,
            name=name,
        )

        status_page_structure_component_v2.additional_properties = d
        return status_page_structure_component_v2

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
