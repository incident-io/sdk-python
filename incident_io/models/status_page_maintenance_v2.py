from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_maintenance_v2_maintenance_status import (
    StatusPageMaintenanceV2MaintenanceStatus,
)

if TYPE_CHECKING:
    from ..models.status_page_maintenance_component_maintenance_period_v2 import (
        StatusPageMaintenanceComponentMaintenancePeriodV2,
    )
    from ..models.status_page_maintenance_update_v2 import StatusPageMaintenanceUpdateV2


T = TypeVar("T", bound="StatusPageMaintenanceV2")


@_attrs_define
class StatusPageMaintenanceV2:
    """
    Example:
        {'automate_maintenance_status': True, 'component_maintenance_periods': [{'component_id':
            '01GW7P4ES31Q6V1ZQH321T0GJN', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at':
            '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status':
            'maintenance_scheduled', 'name': 'Routine infrastructure upgrade', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status': 'maintenance_scheduled', 'message': 'abc123',
            'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_maintenance_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}

    Attributes:
        automate_maintenance_status (bool): Whether updates are published automatically, moving this maintenance window
            to in progress at its start time and to complete at its end time Example: True.
        component_maintenance_periods (list[StatusPageMaintenanceComponentMaintenancePeriodV2]): A list of time periods
            where components were under maintenance during this status page maintenance window Example: [{'component_id':
            '01GW7P4ES31Q6V1ZQH321T0GJN', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at':
            '2021-08-17T13:28:57.801578Z'}].
        id (str): A unique ID for this status page maintenance window Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        maintenance_status (StatusPageMaintenanceV2MaintenanceStatus): Current status for this maintenance window
            Example: maintenance_scheduled.
        name (str): A title for the maintenance window Example: Routine infrastructure upgrade.
        published_at (datetime.datetime): When this status page maintenance window was published to the status page
            Example: 2021-08-17T13:28:57.801578Z.
        status_page_id (str): The ID of the corresponding status page Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        updates (list[StatusPageMaintenanceUpdateV2]): A list of updates posted to this status page maintenance window
            Example: [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status':
            'operational'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status': 'maintenance_scheduled', 'message':
            'abc123', 'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_maintenance_id':
            '01FCNDV6P870EA6S7TK1DSYDG1'}].
    """

    automate_maintenance_status: bool
    component_maintenance_periods: list[
        StatusPageMaintenanceComponentMaintenancePeriodV2
    ]
    id: str
    maintenance_status: StatusPageMaintenanceV2MaintenanceStatus
    name: str
    published_at: datetime.datetime
    status_page_id: str
    updates: list[StatusPageMaintenanceUpdateV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automate_maintenance_status = self.automate_maintenance_status

        component_maintenance_periods = []
        for (
            component_maintenance_periods_item_data
        ) in self.component_maintenance_periods:
            component_maintenance_periods_item = (
                component_maintenance_periods_item_data.to_dict()
            )
            component_maintenance_periods.append(component_maintenance_periods_item)

        id = self.id

        maintenance_status = self.maintenance_status.value

        name = self.name

        published_at = self.published_at.isoformat()

        status_page_id = self.status_page_id

        updates = []
        for updates_item_data in self.updates:
            updates_item = updates_item_data.to_dict()
            updates.append(updates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "automate_maintenance_status": automate_maintenance_status,
                "component_maintenance_periods": component_maintenance_periods,
                "id": id,
                "maintenance_status": maintenance_status,
                "name": name,
                "published_at": published_at,
                "status_page_id": status_page_id,
                "updates": updates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_maintenance_component_maintenance_period_v2 import (
            StatusPageMaintenanceComponentMaintenancePeriodV2,
        )
        from ..models.status_page_maintenance_update_v2 import (
            StatusPageMaintenanceUpdateV2,
        )

        d = dict(src_dict)
        automate_maintenance_status = d.pop("automate_maintenance_status")

        component_maintenance_periods = []
        _component_maintenance_periods = d.pop("component_maintenance_periods")
        for component_maintenance_periods_item_data in _component_maintenance_periods:
            component_maintenance_periods_item = (
                StatusPageMaintenanceComponentMaintenancePeriodV2.from_dict(
                    component_maintenance_periods_item_data
                )
            )

            component_maintenance_periods.append(component_maintenance_periods_item)

        id = d.pop("id")

        maintenance_status = StatusPageMaintenanceV2MaintenanceStatus(
            d.pop("maintenance_status")
        )

        name = d.pop("name")

        published_at = datetime.datetime.fromisoformat(d.pop("published_at"))

        status_page_id = d.pop("status_page_id")

        updates = []
        _updates = d.pop("updates")
        for updates_item_data in _updates:
            updates_item = StatusPageMaintenanceUpdateV2.from_dict(updates_item_data)

            updates.append(updates_item)

        status_page_maintenance_v2 = cls(
            automate_maintenance_status=automate_maintenance_status,
            component_maintenance_periods=component_maintenance_periods,
            id=id,
            maintenance_status=maintenance_status,
            name=name,
            published_at=published_at,
            status_page_id=status_page_id,
            updates=updates,
        )

        status_page_maintenance_v2.additional_properties = d
        return status_page_maintenance_v2

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
