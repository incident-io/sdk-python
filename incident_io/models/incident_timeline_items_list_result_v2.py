from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_timeline_item_v2 import IncidentTimelineItemV2
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2


T = TypeVar("T", bound="IncidentTimelineItemsListResultV2")


@_attrs_define
class IncidentTimelineItemsListResultV2:
    """
    Example:
        {'incident_timeline_items': [{'activity_log_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'created_at':
            '2026-09-01T15:31:04Z', 'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
            PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'description': 'Rolled back **payments-api** to v411 after error rate hit 12%.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'timestamp': '2026-09-01T15:30:00Z',
            'title': 'Rolled back payments-api', 'updated_at': '2026-09-01T16:45:00Z'}], 'pagination_meta': {'after':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        incident_timeline_items (list[IncidentTimelineItemV2]):  Example: [{'activity_log_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'created_at': '2026-09-01T15:31:04Z', 'creator': {'alert': {'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'description': 'Rolled back
            **payments-api** to v411 after error rate hit 12%.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'timestamp': '2026-09-01T15:30:00Z', 'title': 'Rolled back payments-api',
            'updated_at': '2026-09-01T16:45:00Z'}].
        pagination_meta (PaginationMetaResultV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size':
            25}.
    """

    incident_timeline_items: list[IncidentTimelineItemV2]
    pagination_meta: PaginationMetaResultV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_timeline_items = []
        for incident_timeline_items_item_data in self.incident_timeline_items:
            incident_timeline_items_item = incident_timeline_items_item_data.to_dict()
            incident_timeline_items.append(incident_timeline_items_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_timeline_items": incident_timeline_items,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_timeline_item_v2 import (
            IncidentTimelineItemV2,
        )
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )

        d = dict(src_dict)
        incident_timeline_items = []
        _incident_timeline_items = d.pop("incident_timeline_items")
        for incident_timeline_items_item_data in _incident_timeline_items:
            incident_timeline_items_item = IncidentTimelineItemV2.from_dict(
                incident_timeline_items_item_data
            )

            incident_timeline_items.append(incident_timeline_items_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultV2.from_dict(_pagination_meta)

        incident_timeline_items_list_result_v2 = cls(
            incident_timeline_items=incident_timeline_items,
            pagination_meta=pagination_meta,
        )

        incident_timeline_items_list_result_v2.additional_properties = d
        return incident_timeline_items_list_result_v2

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
