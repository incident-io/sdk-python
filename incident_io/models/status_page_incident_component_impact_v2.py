from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_incident_component_impact_v2_component_status import (
    StatusPageIncidentComponentImpactV2ComponentStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageIncidentComponentImpactV2")


@_attrs_define
class StatusPageIncidentComponentImpactV2:
    """
    Example:
        {'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN', 'component_status': 'degraded_performance', 'end_at':
            '2021-08-17T13:28:57.801578Z', 'start_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        component_id (str): The ID of the affected component. This may be found by calling the ShowStatusPageStructure
            endpoint. Example: 01GW7P4ES31Q6V1ZQH321T0GJN.
        component_status (StatusPageIncidentComponentImpactV2ComponentStatus): The status of the relevant component
            impact in a status page incident - this excludes the operational status. Example: degraded_performance.
        start_at (datetime.datetime): When the component entered this status Example: 2021-08-17T13:28:57.801578Z.
        end_at (datetime.datetime | Unset): When the component left this status. If this is null, the impact is ongoing.
            Example: 2021-08-17T13:28:57.801578Z.
    """

    component_id: str
    component_status: StatusPageIncidentComponentImpactV2ComponentStatus
    start_at: datetime.datetime
    end_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_id = self.component_id

        component_status = self.component_status.value

        start_at = self.start_at.isoformat()

        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_id": component_id,
                "component_status": component_status,
                "start_at": start_at,
            }
        )
        if end_at is not UNSET:
            field_dict["end_at"] = end_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        component_id = d.pop("component_id")

        component_status = StatusPageIncidentComponentImpactV2ComponentStatus(
            d.pop("component_status")
        )

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        _end_at = d.pop("end_at", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at, Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)

        status_page_incident_component_impact_v2 = cls(
            component_id=component_id,
            component_status=component_status,
            start_at=start_at,
            end_at=end_at,
        )

        status_page_incident_component_impact_v2.additional_properties = d
        return status_page_incident_component_impact_v2

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
