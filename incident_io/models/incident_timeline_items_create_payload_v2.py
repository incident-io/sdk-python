from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentTimelineItemsCreatePayloadV2")


@_attrs_define
class IncidentTimelineItemsCreatePayloadV2:
    """
    Example:
        {'description': 'Rolled back **payments-api** to v411 after error rate hit 12%.', 'idempotency_key':
            'deploy-4f2c1b90', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'timestamp': '2026-09-01T15:30:00Z', 'title':
            'Rolled back payments-api'}

    Attributes:
        idempotency_key (str): Unique string used to de-duplicate timeline item requests. Retrying with the same key
            returns the item the first request created, rather than adding a second one. Example: deploy-4f2c1b90.
        incident_id (str): Incident to add this item to Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        timestamp (datetime.datetime): When the thing this item describes happened. This is where the item sits on the
            timeline, and can be in the past. Example: 2026-09-01T15:30:00Z.
        title (str): Title of the timeline item Example: Rolled back payments-api.
        description (str | Unset): Description of the timeline item, in markdown Example: Rolled back **payments-api**
            to v411 after error rate hit 12%..
    """

    idempotency_key: str
    incident_id: str
    timestamp: datetime.datetime
    title: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idempotency_key = self.idempotency_key

        incident_id = self.incident_id

        timestamp = self.timestamp.isoformat()

        title = self.title

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idempotency_key": idempotency_key,
                "incident_id": incident_id,
                "timestamp": timestamp,
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        idempotency_key = d.pop("idempotency_key")

        incident_id = d.pop("incident_id")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        title = d.pop("title")

        description = d.pop("description", UNSET)

        incident_timeline_items_create_payload_v2 = cls(
            idempotency_key=idempotency_key,
            incident_id=incident_id,
            timestamp=timestamp,
            title=title,
            description=description,
        )

        incident_timeline_items_create_payload_v2.additional_properties = d
        return incident_timeline_items_create_payload_v2

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
