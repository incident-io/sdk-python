from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_status_page_incident_update_shared_v1_response_body_event_type import (
    WebhooksStatusPageIncidentUpdateSharedV1ResponseBodyEventType,
)

if TYPE_CHECKING:
    from ..models.status_page_incident_with_update_v2 import (
        StatusPageIncidentWithUpdateV2,
    )


T = TypeVar("T", bound="WebhooksStatusPageIncidentUpdateSharedV1ResponseBody")


@_attrs_define(kw_only=True)
class WebhooksStatusPageIncidentUpdateSharedV1ResponseBody:
    """
    Example:
        {'event_type': 'status_page_incident.update_shared_v1', 'status_page_incident.update_shared_v1':
            {'status_page_incident': {'component_impacts': [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN',
            'component_status': 'degraded_performance', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at':
            '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'name':
            'Elevated API latency', 'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'updates': [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2',
            'component_status': 'operational'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating',
            'message': 'abc123', 'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG1'}]}, 'update': {'component_statuses': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_status': 'investigating', 'message': 'abc123', 'published_at': '2021-08-17T13:28:57.801578Z',
            'status_page_incident_id': '01FCNDV6P870EA6S7TK1DSYDG1'}}}

    Attributes:
        event_type (WebhooksStatusPageIncidentUpdateSharedV1ResponseBodyEventType): What type of event is this webhook
            for? Example: status_page_incident.update_shared_v1.
        status_page_incident_update_shared_v1 (StatusPageIncidentWithUpdateV2):  Example: {'status_page_incident':
            {'component_impacts': [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN', 'component_status':
            'degraded_performance', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at': '2021-08-17T13:28:57.801578Z'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'name': 'Elevated API latency',
            'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'message': 'abc123', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_incident_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}, 'update':
            {'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'message': 'abc123', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_incident_id': '01FCNDV6P870EA6S7TK1DSYDG1'}}.
    """

    event_type: WebhooksStatusPageIncidentUpdateSharedV1ResponseBodyEventType
    status_page_incident_update_shared_v1: StatusPageIncidentWithUpdateV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        status_page_incident_update_shared_v1 = (
            self.status_page_incident_update_shared_v1.to_dict()
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "status_page_incident.update_shared_v1": status_page_incident_update_shared_v1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_incident_with_update_v2 import (
            StatusPageIncidentWithUpdateV2,
        )

        d = dict(src_dict)
        event_type = WebhooksStatusPageIncidentUpdateSharedV1ResponseBodyEventType(
            d.pop("event_type")
        )

        status_page_incident_update_shared_v1 = (
            StatusPageIncidentWithUpdateV2.from_dict(
                d.pop("status_page_incident.update_shared_v1")
            )
        )

        webhooks_status_page_incident_update_shared_v1_response_body = cls(
            event_type=event_type,
            status_page_incident_update_shared_v1=status_page_incident_update_shared_v1,
        )

        webhooks_status_page_incident_update_shared_v1_response_body.additional_properties = d
        return webhooks_status_page_incident_update_shared_v1_response_body

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
