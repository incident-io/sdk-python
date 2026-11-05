from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_customer_page_component_v2 import (
        StatusPageCustomerPageComponentV2,
    )


T = TypeVar("T", bound="StatusPageCustomerPageGroupV2")


@_attrs_define(kw_only=True)
class StatusPageCustomerPageGroupV2:
    """
    Example:
        {'components': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard',
            'display_uptime': True, 'name': 'App', 'status': 'operational'}], 'description': 'Services hosted in our EU data
            center', 'display_aggregated_uptime': True, 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}

    Attributes:
        components (list[StatusPageCustomerPageComponentV2]): Array of components belonging to this group Example:
            [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard', 'display_uptime': True,
            'name': 'App', 'status': 'operational'}].
        display_aggregated_uptime (bool): Whether the page shows uptime aggregated across the group's components
            Example: True.
        id (str): Unique ID of this component group Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        name (str): The name of this component group Example: EU Data center.
        description (str | Unset): A description shown under the group's name Example: Services hosted in our EU data
            center.
    """

    components: list[StatusPageCustomerPageComponentV2]
    display_aggregated_uptime: bool
    id: str
    name: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        display_aggregated_uptime = self.display_aggregated_uptime

        id = self.id

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "components": components,
                "display_aggregated_uptime": display_aggregated_uptime,
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_customer_page_component_v2 import (
            StatusPageCustomerPageComponentV2,
        )

        d = dict(src_dict)
        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = StatusPageCustomerPageComponentV2.from_dict(
                components_item_data
            )

            components.append(components_item)

        display_aggregated_uptime = d.pop("display_aggregated_uptime")

        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        status_page_customer_page_group_v2 = cls(
            components=components,
            display_aggregated_uptime=display_aggregated_uptime,
            id=id,
            name=name,
            description=description,
        )

        status_page_customer_page_group_v2.additional_properties = d
        return status_page_customer_page_group_v2

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
