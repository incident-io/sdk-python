from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_incident_v2 import StatusPageIncidentV2


T = TypeVar("T", bound="StatusPagesCreateStatusPageRetrospectiveIncidentResultV2")


@_attrs_define
class StatusPagesCreateStatusPageRetrospectiveIncidentResultV2:
    """
    Example:
        {'status_page_incident': {'component_impacts': [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN',
            'component_status': 'degraded_performance', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at':
            '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'name':
            'Elevated API latency', 'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'updates': [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2',
            'component_status': 'operational'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating',
            'message': 'abc123', 'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG1'}]}}

    Attributes:
        status_page_incident (StatusPageIncidentV2 | Unset):  Example: {'component_impacts': [{'component_id':
            '01GW7P4ES31Q6V1ZQH321T0GJN', 'component_status': 'degraded_performance', 'end_at':
            '2021-08-17T13:28:57.801578Z', 'start_at': '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_status': 'investigating', 'name': 'Elevated API latency', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'message': 'abc123', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_incident_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}.
    """

    status_page_incident: StatusPageIncidentV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_page_incident: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_page_incident, Unset):
            status_page_incident = self.status_page_incident.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_page_incident is not UNSET:
            field_dict["status_page_incident"] = status_page_incident

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_incident_v2 import (
            StatusPageIncidentV2,
        )

        d = dict(src_dict)
        _status_page_incident = d.pop("status_page_incident", UNSET)
        status_page_incident: StatusPageIncidentV2 | Unset
        if isinstance(_status_page_incident, Unset):
            status_page_incident = UNSET
        else:
            status_page_incident = StatusPageIncidentV2.from_dict(_status_page_incident)

        status_pages_create_status_page_retrospective_incident_result_v2 = cls(
            status_page_incident=status_page_incident,
        )

        status_pages_create_status_page_retrospective_incident_result_v2.additional_properties = d
        return status_pages_create_status_page_retrospective_incident_result_v2

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
