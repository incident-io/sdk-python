from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_update_v2 import IncidentUpdateV2
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2


T = TypeVar("T", bound="IncidentUpdatesListResultV2")


@_attrs_define(kw_only=True)
class IncidentUpdatesListResultV2:
    """
    Example:
        {'incident_updates': [{'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'merged_into_incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'message':
            "We're working on a fix, hoping to ship in the next 30 minutes", 'new_incident_status': {'category': 'triage',
            'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're
            ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4,
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'new_severity': {'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1,
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}}], 'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        incident_updates (list[IncidentUpdateV2]):  Example: [{'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'merged_into_incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'message': "We're working on a fix, hoping to ship in the next 30 minutes",
            'new_incident_status': {'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            "Impact has been **fully mitigated**, and we're ready to learn from this incident.", 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'new_severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to
            connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}}].
        pagination_meta (PaginationMetaResultV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size':
            25}.
    """

    incident_updates: list[IncidentUpdateV2]
    pagination_meta: PaginationMetaResultV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_updates = []
        for incident_updates_item_data in self.incident_updates:
            incident_updates_item = incident_updates_item_data.to_dict()
            incident_updates.append(incident_updates_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_updates": incident_updates,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_update_v2 import IncidentUpdateV2
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )

        d = dict(src_dict)
        incident_updates = []
        _incident_updates = d.pop("incident_updates")
        for incident_updates_item_data in _incident_updates:
            incident_updates_item = IncidentUpdateV2.from_dict(
                incident_updates_item_data
            )

            incident_updates.append(incident_updates_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultV2.from_dict(_pagination_meta)

        incident_updates_list_result_v2 = cls(
            incident_updates=incident_updates,
            pagination_meta=pagination_meta,
        )

        incident_updates_list_result_v2.additional_properties = d
        return incident_updates_list_result_v2

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
