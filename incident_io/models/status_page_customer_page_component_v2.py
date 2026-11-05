from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_customer_page_component_v2_status import (
    StatusPageCustomerPageComponentV2Status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageCustomerPageComponentV2")


@_attrs_define(kw_only=True)
class StatusPageCustomerPageComponentV2:
    """
    Example:
        {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard', 'display_uptime': True,
            'name': 'App', 'status': 'operational'}

    Attributes:
        component_id (str): The ID of this component. Incidents and maintenance windows refer to components by this ID.
            Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        display_uptime (bool): Whether the page shows this component's uptime Example: True.
        name (str): The name of this component Example: App.
        status (StatusPageCustomerPageComponentV2Status): The current status of this component Example: operational.
        description (str | Unset): A description shown under the component's name, if it has one Example: The web
            dashboard.
    """

    component_id: str
    display_uptime: bool
    name: str
    status: StatusPageCustomerPageComponentV2Status
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_id = self.component_id

        display_uptime = self.display_uptime

        name = self.name

        status = self.status.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_id": component_id,
                "display_uptime": display_uptime,
                "name": name,
                "status": status,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        component_id = d.pop("component_id")

        display_uptime = d.pop("display_uptime")

        name = d.pop("name")

        status = StatusPageCustomerPageComponentV2Status(d.pop("status"))

        description = d.pop("description", UNSET)

        status_page_customer_page_component_v2 = cls(
            component_id=component_id,
            display_uptime=display_uptime,
            name=name,
            status=status,
            description=description,
        )

        status_page_customer_page_component_v2.additional_properties = d
        return status_page_customer_page_component_v2

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
