from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_timeline_item_v2 import IncidentTimelineItemV2


T = TypeVar("T", bound="IncidentTimelineItemsUpdateResultV2")


@_attrs_define
class IncidentTimelineItemsUpdateResultV2:
    """
    Example:
        {'incident_timeline_item': {'activity_log_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'created_at':
            '2026-09-01T15:31:04Z', 'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
            PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'description': 'Rolled back **payments-api** to v411 after error rate hit 12%.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'timestamp': '2026-09-01T15:30:00Z',
            'title': 'Rolled back payments-api', 'updated_at': '2026-09-01T16:45:00Z'}}

    Attributes:
        incident_timeline_item (IncidentTimelineItemV2): An item on an incident's curated timeline.

            The timeline is the narrative of an incident, as opposed to the activity log, which records
            everything that happened. Some of that activity - a pinned message, an escalation, an event a
            workflow added - is promoted onto the timeline, and those items carry the ID of the activity
            log entry they came from. The rest are custom, written by hand in the dashboard or through
            the API, and have no activity_log_id. Example: {'activity_log_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'created_at':
            '2026-09-01T15:31:04Z', 'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
            PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'description': 'Rolled back **payments-api** to v411 after error rate hit 12%.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'timestamp': '2026-09-01T15:30:00Z',
            'title': 'Rolled back payments-api', 'updated_at': '2026-09-01T16:45:00Z'}.
    """

    incident_timeline_item: IncidentTimelineItemV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_timeline_item = self.incident_timeline_item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_timeline_item": incident_timeline_item,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_timeline_item_v2 import (
            IncidentTimelineItemV2,
        )

        d = dict(src_dict)
        incident_timeline_item = IncidentTimelineItemV2.from_dict(
            d.pop("incident_timeline_item")
        )

        incident_timeline_items_update_result_v2 = cls(
            incident_timeline_item=incident_timeline_item,
        )

        incident_timeline_items_update_result_v2.additional_properties = d
        return incident_timeline_items_update_result_v2

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
