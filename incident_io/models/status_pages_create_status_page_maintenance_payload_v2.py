from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_pages_create_status_page_maintenance_payload_v2_maintenance_status import (
    StatusPagesCreateStatusPageMaintenancePayloadV2MaintenanceStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPagesCreateStatusPageMaintenancePayloadV2")


@_attrs_define
class StatusPagesCreateStatusPageMaintenancePayloadV2:
    """
    Example:
        {'affected_component_ids': ['01FCNDV6P870EA6S7TK1DSYDG2'], 'automate_maintenance_status': True, 'end_at':
            '2025-01-28T12:00:00Z', 'idempotency_key': 'maintenance-12345-abcde', 'maintenance_status':
            'maintenance_scheduled', 'message': 'Planned maintenance has been scheduled to upgrade our infrastructure. We
            expect minimal disruption, but some features may be briefly unavailable.', 'name': 'Routine infrastructure
            upgrade', 'notify_subscribers': True, 'start_at': '2025-01-28T10:00:00Z', 'status_page_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        affected_component_ids (list[str]): An array of IDs of component affected by the maintenance window Example:
            ['01FCNDV6P870EA6S7TK1DSYDG2'].
        end_at (datetime.datetime): The time the maintenance window ends Example: 2025-01-28T12:00:00Z.
        idempotency_key (str): A unique key to de-duplicate requests. If you send a request with an idempotency_key that
            was already used, the original response will be returned. Example: maintenance-12345-abcde.
        maintenance_status (StatusPagesCreateStatusPageMaintenancePayloadV2MaintenanceStatus): Current status for this
            status page maintenance window Example: maintenance_scheduled.
        message (str): Markdown initial update on this status page maintenance window Example: Planned maintenance has
            been scheduled to upgrade our infrastructure. We expect minimal disruption, but some features may be briefly
            unavailable..
        name (str): A title for the maintenance window Example: Routine infrastructure upgrade.
        notify_subscribers (bool): Whether to notify subscribers about this status page maintenance. This will not work
            if your status page has more than 1000 subscribers. Example: True.
        start_at (datetime.datetime): The time the maintenance window starts Example: 2025-01-28T10:00:00Z.
        status_page_id (str): ID of the status page. You can find this by calling the ListStatusPages endpoint. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        automate_maintenance_status (bool | Unset): Whether to publish updates automatically, moving this maintenance
            window to in progress at start_at and to complete at end_at. Defaults to false, which means you publish those
            updates yourself. When notify_subscribers is true, the automated updates notify subscribers too. Publishing your
            own update that sets maintenance_status turns automation off. Example: True.
    """

    affected_component_ids: list[str]
    end_at: datetime.datetime
    idempotency_key: str
    maintenance_status: StatusPagesCreateStatusPageMaintenancePayloadV2MaintenanceStatus
    message: str
    name: str
    notify_subscribers: bool
    start_at: datetime.datetime
    status_page_id: str
    automate_maintenance_status: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_component_ids = self.affected_component_ids

        end_at = self.end_at.isoformat()

        idempotency_key = self.idempotency_key

        maintenance_status = self.maintenance_status.value

        message = self.message

        name = self.name

        notify_subscribers = self.notify_subscribers

        start_at = self.start_at.isoformat()

        status_page_id = self.status_page_id

        automate_maintenance_status = self.automate_maintenance_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "affected_component_ids": affected_component_ids,
                "end_at": end_at,
                "idempotency_key": idempotency_key,
                "maintenance_status": maintenance_status,
                "message": message,
                "name": name,
                "notify_subscribers": notify_subscribers,
                "start_at": start_at,
                "status_page_id": status_page_id,
            }
        )
        if automate_maintenance_status is not UNSET:
            field_dict["automate_maintenance_status"] = automate_maintenance_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        affected_component_ids = cast(list[str], d.pop("affected_component_ids"))

        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        idempotency_key = d.pop("idempotency_key")

        maintenance_status = (
            StatusPagesCreateStatusPageMaintenancePayloadV2MaintenanceStatus(
                d.pop("maintenance_status")
            )
        )

        message = d.pop("message")

        name = d.pop("name")

        notify_subscribers = d.pop("notify_subscribers")

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        status_page_id = d.pop("status_page_id")

        automate_maintenance_status = d.pop("automate_maintenance_status", UNSET)

        status_pages_create_status_page_maintenance_payload_v2 = cls(
            affected_component_ids=affected_component_ids,
            end_at=end_at,
            idempotency_key=idempotency_key,
            maintenance_status=maintenance_status,
            message=message,
            name=name,
            notify_subscribers=notify_subscribers,
            start_at=start_at,
            status_page_id=status_page_id,
            automate_maintenance_status=automate_maintenance_status,
        )

        status_pages_create_status_page_maintenance_payload_v2.additional_properties = d
        return status_pages_create_status_page_maintenance_payload_v2

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
