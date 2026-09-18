from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_incident_v2_incident_status import (
    StatusPageIncidentV2IncidentStatus,
)

if TYPE_CHECKING:
    from ..models.status_page_incident_component_impact_v2 import (
        StatusPageIncidentComponentImpactV2,
    )
    from ..models.status_page_incident_update_v2 import StatusPageIncidentUpdateV2


T = TypeVar("T", bound="StatusPageIncidentV2")


@_attrs_define
class StatusPageIncidentV2:
    """
    Example:
        {'component_impacts': [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN', 'component_status':
            'degraded_performance', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at': '2021-08-17T13:28:57.801578Z'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'name': 'Elevated API latency',
            'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'message': 'abc123', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_incident_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}

    Attributes:
        component_impacts (list[StatusPageIncidentComponentImpactV2]): A list of time periods that this status page
            incident had an impact on a component Example: [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN',
            'component_status': 'degraded_performance', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at':
            '2021-08-17T13:28:57.801578Z'}].
        id (str): A unique ID for this status page incident Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_status (StatusPageIncidentV2IncidentStatus): Current status for this incident Example: investigating.
        name (str): A title for the incident Example: Elevated API latency.
        published_at (datetime.datetime): When this status page incident was published to the status page Example:
            2021-08-17T13:28:57.801578Z.
        status_page_id (str): The ID of the corresponding status page Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        updates (list[StatusPageIncidentUpdateV2]): A list of updates posted to this status page incident Example:
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'message': 'abc123', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_incident_id': '01FCNDV6P870EA6S7TK1DSYDG1'}].
    """

    component_impacts: list[StatusPageIncidentComponentImpactV2]
    id: str
    incident_status: StatusPageIncidentV2IncidentStatus
    name: str
    published_at: datetime.datetime
    status_page_id: str
    updates: list[StatusPageIncidentUpdateV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_impacts = []
        for component_impacts_item_data in self.component_impacts:
            component_impacts_item = component_impacts_item_data.to_dict()
            component_impacts.append(component_impacts_item)

        id = self.id

        incident_status = self.incident_status.value

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
                "component_impacts": component_impacts,
                "id": id,
                "incident_status": incident_status,
                "name": name,
                "published_at": published_at,
                "status_page_id": status_page_id,
                "updates": updates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_incident_component_impact_v2 import (
            StatusPageIncidentComponentImpactV2,
        )
        from ..models.status_page_incident_update_v2 import (
            StatusPageIncidentUpdateV2,
        )

        d = dict(src_dict)
        component_impacts = []
        _component_impacts = d.pop("component_impacts")
        for component_impacts_item_data in _component_impacts:
            component_impacts_item = StatusPageIncidentComponentImpactV2.from_dict(
                component_impacts_item_data
            )

            component_impacts.append(component_impacts_item)

        id = d.pop("id")

        incident_status = StatusPageIncidentV2IncidentStatus(d.pop("incident_status"))

        name = d.pop("name")

        published_at = datetime.datetime.fromisoformat(d.pop("published_at"))

        status_page_id = d.pop("status_page_id")

        updates = []
        _updates = d.pop("updates")
        for updates_item_data in _updates:
            updates_item = StatusPageIncidentUpdateV2.from_dict(updates_item_data)

            updates.append(updates_item)

        status_page_incident_v2 = cls(
            component_impacts=component_impacts,
            id=id,
            incident_status=incident_status,
            name=name,
            published_at=published_at,
            status_page_id=status_page_id,
            updates=updates,
        )

        status_page_incident_v2.additional_properties = d
        return status_page_incident_v2

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
