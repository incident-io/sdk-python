from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.follow_up_v3 import FollowUpV3
    from ..models.pagination_meta_result_v3 import PaginationMetaResultV3


T = TypeVar("T", bound="FollowUpsListResultV3")


@_attrs_define
class FollowUpsListResultV3:
    """
    Example:
        {'follow_ups': [{'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'assignee_team': {'id': 'abc123', 'name':
            'abc123'}, 'category': {'description': 'Follow-ups related to infrastructure changes.', 'id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name': 'Infrastructure', 'rank': 10}, 'completed_at':
            '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z', 'creator': {'alert': {'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'description': 'Call the fire
            brigade', 'external_issue_reference': {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-
            io/issue/INC-1609/find-copywriter-to-write-up', 'provider': 'asana'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'labels': ['bug', 'urgent'], 'priority': {'description': 'A follow-
            up that requires immediate attention.', 'id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name': 'Urgent', 'rank': 10},
            'status': 'outstanding', 'title': 'Cat is stuck in the tree', 'updated_at': '2021-08-17T13:28:57.801578Z'}],
            'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        follow_ups (list[FollowUpV3]):  Example: [{'assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'assignee_team': {'id': 'abc123', 'name': 'abc123'}, 'category': {'description': 'Follow-ups related to
            infrastructure changes.', 'id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name': 'Infrastructure', 'rank': 10},
            'completed_at': '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z', 'creator': {'alert':
            {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key':
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'description': 'Call the fire
            brigade', 'external_issue_reference': {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-
            io/issue/INC-1609/find-copywriter-to-write-up', 'provider': 'asana'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'labels': ['bug', 'urgent'], 'priority': {'description': 'A follow-
            up that requires immediate attention.', 'id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name': 'Urgent', 'rank': 10},
            'status': 'outstanding', 'title': 'Cat is stuck in the tree', 'updated_at': '2021-08-17T13:28:57.801578Z'}].
        pagination_meta (PaginationMetaResultV3):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
    """

    follow_ups: list[FollowUpV3]
    pagination_meta: PaginationMetaResultV3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        follow_ups = []
        for follow_ups_item_data in self.follow_ups:
            follow_ups_item = follow_ups_item_data.to_dict()
            follow_ups.append(follow_ups_item)

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "follow_ups": follow_ups,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.follow_up_v3 import FollowUpV3
        from ..models.pagination_meta_result_v3 import (
            PaginationMetaResultV3,
        )

        d = dict(src_dict)
        follow_ups = []
        _follow_ups = d.pop("follow_ups")
        for follow_ups_item_data in _follow_ups:
            follow_ups_item = FollowUpV3.from_dict(follow_ups_item_data)

            follow_ups.append(follow_ups_item)

        pagination_meta = PaginationMetaResultV3.from_dict(d.pop("pagination_meta"))

        follow_ups_list_result_v3 = cls(
            follow_ups=follow_ups,
            pagination_meta=pagination_meta,
        )

        follow_ups_list_result_v3.additional_properties = d
        return follow_ups_list_result_v3

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
