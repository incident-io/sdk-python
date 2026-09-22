from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_page_retrospective_incident_update_v2 import (
        StatusPageRetrospectiveIncidentUpdateV2,
    )


T = TypeVar("T", bound="StatusPagesCreateStatusPageRetrospectiveIncidentPayloadV2")


@_attrs_define(kw_only=True)
class StatusPagesCreateStatusPageRetrospectiveIncidentPayloadV2:
    """
    Example:
        {'idempotency_key': 'historical-incident-2021-08-17', 'name': 'Elevated API latency', 'status_page_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'updates': [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2',
            'component_status': 'operational'}], 'incident_status': 'investigating', 'message': 'We are currently
            investigating reports of elevated error rates affecting our API.', 'published_at':
            '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        idempotency_key (str): A unique key to de-duplicate requests. If you send a request with an idempotency_key that
            was already used, the original response will be returned. Example: historical-incident-2021-08-17.
        name (str): A title for the incident Example: Elevated API latency.
        status_page_id (str): ID of the status page. You can find this by calling the ListStatusPages endpoint. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        updates (list[StatusPageRetrospectiveIncidentUpdateV2]): The reconstructed timeline of updates for this
            incident, ordered chronologically (earliest first). The final update must set incident_status to "resolved".
            Example: [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status':
            'operational'}], 'incident_status': 'investigating', 'message': 'We are currently investigating reports of
            elevated error rates affecting our API.', 'published_at': '2021-08-17T13:28:57.801578Z'}].
    """

    idempotency_key: str
    name: str
    status_page_id: str
    updates: list[StatusPageRetrospectiveIncidentUpdateV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idempotency_key = self.idempotency_key

        name = self.name

        status_page_id = self.status_page_id

        updates = []
        for updates_item_data in self.updates:
            updates_item = updates_item_data.to_dict()
            updates.append(updates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idempotency_key": idempotency_key,
                "name": name,
                "status_page_id": status_page_id,
                "updates": updates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_retrospective_incident_update_v2 import (
            StatusPageRetrospectiveIncidentUpdateV2,
        )

        d = dict(src_dict)
        idempotency_key = d.pop("idempotency_key")

        name = d.pop("name")

        status_page_id = d.pop("status_page_id")

        updates = []
        _updates = d.pop("updates")
        for updates_item_data in _updates:
            updates_item = StatusPageRetrospectiveIncidentUpdateV2.from_dict(
                updates_item_data
            )

            updates.append(updates_item)

        status_pages_create_status_page_retrospective_incident_payload_v2 = cls(
            idempotency_key=idempotency_key,
            name=name,
            status_page_id=status_page_id,
            updates=updates,
        )

        status_pages_create_status_page_retrospective_incident_payload_v2.additional_properties = d
        return status_pages_create_status_page_retrospective_incident_payload_v2

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
