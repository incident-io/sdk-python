from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_pages_create_status_page_incident_update_payload_v2_incident_status import (
    StatusPagesCreateStatusPageIncidentUpdatePayloadV2IncidentStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_incident_affected_component_v2 import (
        StatusPageIncidentAffectedComponentV2,
    )


T = TypeVar("T", bound="StatusPagesCreateStatusPageIncidentUpdatePayloadV2")


@_attrs_define
class StatusPagesCreateStatusPageIncidentUpdatePayloadV2:
    """
    Example:
        {'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'incident_status': 'investigating', 'message': 'The fix has been deployed and we are monitoring the situation.
            Some users may still experience intermittent issues.', 'notify_subscribers': True, 'status_page_incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG1'}

    Attributes:
        message (str): Markdown update on what's changed about this status page incident Example: The fix has been
            deployed and we are monitoring the situation. Some users may still experience intermittent issues..
        notify_subscribers (bool): Whether to notify subscribers about this incident update. This will not work if your
            status page has more than 1000 subscribers. Example: True.
        status_page_incident_id (str): ID of the status page incident Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        component_statuses (list[StatusPageIncidentAffectedComponentV2] | Unset): An array of mappings from component ID
            to component status. This must not be set if the status page incident status is being set to "resolved", as all
            components statuses will update to "operational". Example: [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2',
            'component_status': 'operational'}].
        incident_status (StatusPagesCreateStatusPageIncidentUpdatePayloadV2IncidentStatus | Unset): Optional new status
            for this status page incident. If not provided, the status will remain unchanged. Setting to "resolved" will end
            the incident and all component statuses will update to "operational". Example: investigating.
    """

    message: str
    notify_subscribers: bool
    status_page_incident_id: str
    component_statuses: list[StatusPageIncidentAffectedComponentV2] | Unset = UNSET
    incident_status: (
        StatusPagesCreateStatusPageIncidentUpdatePayloadV2IncidentStatus | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        notify_subscribers = self.notify_subscribers

        status_page_incident_id = self.status_page_incident_id

        component_statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.component_statuses, Unset):
            component_statuses = []
            for component_statuses_item_data in self.component_statuses:
                component_statuses_item = component_statuses_item_data.to_dict()
                component_statuses.append(component_statuses_item)

        incident_status: str | Unset = UNSET
        if not isinstance(self.incident_status, Unset):
            incident_status = self.incident_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "notify_subscribers": notify_subscribers,
                "status_page_incident_id": status_page_incident_id,
            }
        )
        if component_statuses is not UNSET:
            field_dict["component_statuses"] = component_statuses
        if incident_status is not UNSET:
            field_dict["incident_status"] = incident_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_incident_affected_component_v2 import (
            StatusPageIncidentAffectedComponentV2,
        )

        d = dict(src_dict)
        message = d.pop("message")

        notify_subscribers = d.pop("notify_subscribers")

        status_page_incident_id = d.pop("status_page_incident_id")

        _component_statuses = d.pop("component_statuses", UNSET)
        component_statuses: list[StatusPageIncidentAffectedComponentV2] | Unset = UNSET
        if _component_statuses is not UNSET:
            component_statuses = []
            for component_statuses_item_data in _component_statuses:
                component_statuses_item = (
                    StatusPageIncidentAffectedComponentV2.from_dict(
                        component_statuses_item_data
                    )
                )

                component_statuses.append(component_statuses_item)

        _incident_status = d.pop("incident_status", UNSET)
        incident_status: (
            StatusPagesCreateStatusPageIncidentUpdatePayloadV2IncidentStatus | Unset
        )
        if isinstance(_incident_status, Unset):
            incident_status = UNSET
        else:
            incident_status = (
                StatusPagesCreateStatusPageIncidentUpdatePayloadV2IncidentStatus(
                    _incident_status
                )
            )

        status_pages_create_status_page_incident_update_payload_v2 = cls(
            message=message,
            notify_subscribers=notify_subscribers,
            status_page_incident_id=status_page_incident_id,
            component_statuses=component_statuses,
            incident_status=incident_status,
        )

        status_pages_create_status_page_incident_update_payload_v2.additional_properties = d
        return status_pages_create_status_page_incident_update_payload_v2

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
