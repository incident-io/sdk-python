from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2


T = TypeVar("T", bound="IncidentTimelineItemV2")


@_attrs_define
class IncidentTimelineItemV2:
    """An item on an incident's curated timeline.

    The timeline is the narrative of an incident, as opposed to the activity log, which records
    everything that happened. Some of that activity - a pinned message, an escalation, an event a
    workflow added - is promoted onto the timeline, and those items carry the ID of the activity
    log entry they came from. The rest are custom, written by hand in the dashboard or through
    the API, and have no activity_log_id.

        Example:
            {'activity_log_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'created_at': '2026-09-01T15:31:04Z', 'creator': {'alert':
                {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key':
                {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'description': 'Rolled back
                **payments-api** to v411 after error rate hit 12%.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'timestamp': '2026-09-01T15:30:00Z', 'title': 'Rolled back payments-api',
                'updated_at': '2026-09-01T16:45:00Z'}

        Attributes:
            created_at (datetime.datetime): When this item was added to the timeline Example: 2026-09-01T15:31:04Z.
            creator (ActorV2):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
                PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
                'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
                'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}.
            id (str): Unique identifier of the timeline item Example: 01FCNDV6P870EA6S7TK1DSYDG0.
            incident_id (str): ID of the incident this item belongs to. When the incident has streams, listing the parent
                also returns items belonging to its streams, and this is the stream's ID for those. Example:
                01G0J1EXE7AXZ2C93K61WBPYEH.
            timestamp (datetime.datetime): When the thing this item describes happened. This is what the timeline is ordered
                by, and is not the same as created_at. Example: 2026-09-01T15:30:00Z.
            title (str): Title of the timeline item Example: Rolled back payments-api.
            updated_at (datetime.datetime): When this item was last edited Example: 2026-09-01T16:45:00Z.
            activity_log_id (str | Unset): ID of the activity log entry this item was promoted from. Null for items written
                by hand, which are the items whose timestamp can be changed. Example: 01FCNDV6P870EA6S7TK1DSYDG1.
            description (str | Unset): Description of the timeline item, in markdown. Absent when the item has no
                description. Example: Rolled back **payments-api** to v411 after error rate hit 12%..
    """

    created_at: datetime.datetime
    creator: ActorV2
    id: str
    incident_id: str
    timestamp: datetime.datetime
    title: str
    updated_at: datetime.datetime
    activity_log_id: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        creator = self.creator.to_dict()

        id = self.id

        incident_id = self.incident_id

        timestamp = self.timestamp.isoformat()

        title = self.title

        updated_at = self.updated_at.isoformat()

        activity_log_id = self.activity_log_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "creator": creator,
                "id": id,
                "incident_id": incident_id,
                "timestamp": timestamp,
                "title": title,
                "updated_at": updated_at,
            }
        )
        if activity_log_id is not UNSET:
            field_dict["activity_log_id"] = activity_log_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        creator = ActorV2.from_dict(d.pop("creator"))

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        title = d.pop("title")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        activity_log_id = d.pop("activity_log_id", UNSET)

        description = d.pop("description", UNSET)

        incident_timeline_item_v2 = cls(
            created_at=created_at,
            creator=creator,
            id=id,
            incident_id=incident_id,
            timestamp=timestamp,
            title=title,
            updated_at=updated_at,
            activity_log_id=activity_log_id,
            description=description,
        )

        incident_timeline_item_v2.additional_properties = d
        return incident_timeline_item_v2

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
