from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentTimelineItemsUpdatePayloadV2")


@_attrs_define(kw_only=True)
class IncidentTimelineItemsUpdatePayloadV2:
    """
    Example:
        {'description': 'Rolled back **payments-api** to v411 after error rate hit 12%.', 'timestamp':
            '2026-09-01T15:30:00Z', 'title': 'Rolled back payments-api'}

    Attributes:
        description (str | Unset): Description of the timeline item, in markdown. Send an empty string to remove it.
            Example: Rolled back **payments-api** to v411 after error rate hit 12%..
        timestamp (datetime.datetime | Unset): When the thing this item describes happened. Only editable on a custom
            item. Example: 2026-09-01T15:30:00Z.
        title (str | Unset): Title of the timeline item Example: Rolled back payments-api.
    """

    description: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        title = d.pop("title", UNSET)

        incident_timeline_items_update_payload_v2 = cls(
            description=description,
            timestamp=timestamp,
            title=title,
        )

        incident_timeline_items_update_payload_v2.additional_properties = d
        return incident_timeline_items_update_payload_v2

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
