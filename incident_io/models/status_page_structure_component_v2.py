from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatusPageStructureComponentV2")


@_attrs_define
class StatusPageStructureComponentV2:
    """
    Example:
        {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}

    Attributes:
        component_id (str): The ID of the affected component. This may be found by calling the ShowStatusPageStructure
            endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        name (str): The name of this component Example: App.
    """

    component_id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_id = self.component_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_id": component_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        component_id = d.pop("component_id")

        name = d.pop("name")

        status_page_structure_component_v2 = cls(
            component_id=component_id,
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
