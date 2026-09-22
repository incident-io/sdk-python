from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_maintenance_affected_component_v2_component_status import (
    StatusPageMaintenanceAffectedComponentV2ComponentStatus,
)

T = TypeVar("T", bound="StatusPageMaintenanceAffectedComponentV2")


@_attrs_define(kw_only=True)
class StatusPageMaintenanceAffectedComponentV2:
    """
    Example:
        {'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}

    Attributes:
        component_id (str): The ID of the affected component. This may be found by calling the ShowStatusPageStructure
            endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG2.
        component_status (StatusPageMaintenanceAffectedComponentV2ComponentStatus): The status of the relevant component
            in a status page maintenance window Example: operational.
    """

    component_id: str
    component_status: StatusPageMaintenanceAffectedComponentV2ComponentStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_id = self.component_id

        component_status = self.component_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_id": component_id,
                "component_status": component_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        component_id = d.pop("component_id")

        component_status = StatusPageMaintenanceAffectedComponentV2ComponentStatus(
            d.pop("component_status")
        )

        status_page_maintenance_affected_component_v2 = cls(
            component_id=component_id,
            component_status=component_status,
        )

        status_page_maintenance_affected_component_v2.additional_properties = d
        return status_page_maintenance_affected_component_v2

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
