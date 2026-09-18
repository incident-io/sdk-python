from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_maintenance_update_v2_maintenance_status import (
    StatusPageMaintenanceUpdateV2MaintenanceStatus,
)

if TYPE_CHECKING:
    from ..models.status_page_maintenance_affected_component_v2 import (
        StatusPageMaintenanceAffectedComponentV2,
    )


T = TypeVar("T", bound="StatusPageMaintenanceUpdateV2")


@_attrs_define
class StatusPageMaintenanceUpdateV2:
    """
    Example:
        {'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status': 'maintenance_scheduled', 'message': 'abc123',
            'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_maintenance_id': '01FCNDV6P870EA6S7TK1DSYDG1'}

    Attributes:
        component_statuses (list[StatusPageMaintenanceAffectedComponentV2]): The updated statuses of affected components
            Example: [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}].
        id (str): A unique ID for this status page maintenance update Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        maintenance_status (StatusPageMaintenanceUpdateV2MaintenanceStatus): Current status for this maintenance window
            Example: maintenance_scheduled.
        message (str): Markdown update on what's changed about this status page maintenance window Example: abc123.
        published_at (datetime.datetime): When this status page maintenance update was published to the status page
            Example: 2021-08-17T13:28:57.801578Z.
        status_page_maintenance_id (str): The ID of the corresponding status page maintenance window Example:
            01FCNDV6P870EA6S7TK1DSYDG1.
    """

    component_statuses: list[StatusPageMaintenanceAffectedComponentV2]
    id: str
    maintenance_status: StatusPageMaintenanceUpdateV2MaintenanceStatus
    message: str
    published_at: datetime.datetime
    status_page_maintenance_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_statuses = []
        for component_statuses_item_data in self.component_statuses:
            component_statuses_item = component_statuses_item_data.to_dict()
            component_statuses.append(component_statuses_item)

        id = self.id

        maintenance_status = self.maintenance_status.value

        message = self.message

        published_at = self.published_at.isoformat()

        status_page_maintenance_id = self.status_page_maintenance_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_statuses": component_statuses,
                "id": id,
                "maintenance_status": maintenance_status,
                "message": message,
                "published_at": published_at,
                "status_page_maintenance_id": status_page_maintenance_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_maintenance_affected_component_v2 import (
            StatusPageMaintenanceAffectedComponentV2,
        )

        d = dict(src_dict)
        component_statuses = []
        _component_statuses = d.pop("component_statuses")
        for component_statuses_item_data in _component_statuses:
            component_statuses_item = (
                StatusPageMaintenanceAffectedComponentV2.from_dict(
                    component_statuses_item_data
                )
            )

            component_statuses.append(component_statuses_item)

        id = d.pop("id")

        maintenance_status = StatusPageMaintenanceUpdateV2MaintenanceStatus(
            d.pop("maintenance_status")
        )

        message = d.pop("message")

        published_at = datetime.datetime.fromisoformat(d.pop("published_at"))

        status_page_maintenance_id = d.pop("status_page_maintenance_id")

        status_page_maintenance_update_v2 = cls(
            component_statuses=component_statuses,
            id=id,
            maintenance_status=maintenance_status,
            message=message,
            published_at=published_at,
            status_page_maintenance_id=status_page_maintenance_id,
        )

        status_page_maintenance_update_v2.additional_properties = d
        return status_page_maintenance_update_v2

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
