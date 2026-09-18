from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_pages_create_status_page_incident_payload_v2_incident_status import (
    StatusPagesCreateStatusPageIncidentPayloadV2IncidentStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_incident_affected_component_v2 import (
        StatusPageIncidentAffectedComponentV2,
    )


T = TypeVar("T", bound="StatusPagesCreateStatusPageIncidentPayloadV2")


@_attrs_define
class StatusPagesCreateStatusPageIncidentPayloadV2:
    """
    Example:
        {'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'idempotency_key': 'alert-12345-abcde', 'incident_status': 'investigating', 'message': 'We are currently
            investigating reports of elevated error rates affecting our API.', 'name': 'Elevated API latency',
            'notify_subscribers': True, 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        idempotency_key (str): A unique key to de-duplicate requests. If you send a request with an idempotency_key that
            was already used, the original response will be returned. Example: alert-12345-abcde.
        incident_status (StatusPagesCreateStatusPageIncidentPayloadV2IncidentStatus): Current status for this status
            page incident Example: investigating.
        message (str): Markdown initial update on this status page incident Example: We are currently investigating
            reports of elevated error rates affecting our API..
        name (str): A title for the incident Example: Elevated API latency.
        notify_subscribers (bool): Whether to notify subscribers about this status page incident. This will not work if
            your status page has more than 1000 subscribers. Example: True.
        status_page_id (str): ID of the status page. You can find this by calling the ListStatusPages endpoint. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        component_statuses (list[StatusPageIncidentAffectedComponentV2] | Unset): An array of mappings from component ID
            to current component status Example: [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status':
            'operational'}].
    """

    idempotency_key: str
    incident_status: StatusPagesCreateStatusPageIncidentPayloadV2IncidentStatus
    message: str
    name: str
    notify_subscribers: bool
    status_page_id: str
    component_statuses: list[StatusPageIncidentAffectedComponentV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idempotency_key = self.idempotency_key

        incident_status = self.incident_status.value

        message = self.message

        name = self.name

        notify_subscribers = self.notify_subscribers

        status_page_id = self.status_page_id

        component_statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.component_statuses, Unset):
            component_statuses = []
            for component_statuses_item_data in self.component_statuses:
                component_statuses_item = component_statuses_item_data.to_dict()
                component_statuses.append(component_statuses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idempotency_key": idempotency_key,
                "incident_status": incident_status,
                "message": message,
                "name": name,
                "notify_subscribers": notify_subscribers,
                "status_page_id": status_page_id,
            }
        )
        if component_statuses is not UNSET:
            field_dict["component_statuses"] = component_statuses

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_incident_affected_component_v2 import (
            StatusPageIncidentAffectedComponentV2,
        )

        d = dict(src_dict)
        idempotency_key = d.pop("idempotency_key")

        incident_status = StatusPagesCreateStatusPageIncidentPayloadV2IncidentStatus(
            d.pop("incident_status")
        )

        message = d.pop("message")

        name = d.pop("name")

        notify_subscribers = d.pop("notify_subscribers")

        status_page_id = d.pop("status_page_id")

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

        status_pages_create_status_page_incident_payload_v2 = cls(
            idempotency_key=idempotency_key,
            incident_status=incident_status,
            message=message,
            name=name,
            notify_subscribers=notify_subscribers,
            status_page_id=status_page_id,
            component_statuses=component_statuses,
        )

        status_pages_create_status_page_incident_payload_v2.additional_properties = d
        return status_pages_create_status_page_incident_payload_v2

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
