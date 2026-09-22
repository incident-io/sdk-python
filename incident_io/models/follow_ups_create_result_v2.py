from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.follow_up_v2 import FollowUpV2


T = TypeVar("T", bound="FollowUpsCreateResultV2")


@_attrs_define(kw_only=True)
class FollowUpsCreateResultV2:
    """
    Example:
        {'follow_up': {'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'assignee_team': {'id': 'abc123', 'name':
            'abc123'}, 'completed_at': '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z',
            'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to
            connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'description': 'Call the fire brigade', 'external_issue_reference': {'issue_name': 'INC-123',
            'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up', 'provider':
            'asana'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'labels': ['bug',
            'urgent'], 'priority': {'description': 'A follow-up that requires immediate attention.', 'id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name': 'Urgent', 'rank': 10}, 'status': 'outstanding', 'title': 'Cat is stuck in
            the tree', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        follow_up (FollowUpV2):  Example: {'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'assignee_team': {'id':
            'abc123', 'name': 'abc123'}, 'completed_at': '2021-08-17T13:28:57.801578Z', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}, 'description': 'Call the fire brigade', 'external_issue_reference':
            {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-
            write-up', 'provider': 'asana'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'labels': ['bug', 'urgent'], 'priority': {'description': 'A follow-up that
            requires immediate attention.', 'id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name': 'Urgent', 'rank': 10}, 'status':
            'outstanding', 'title': 'Cat is stuck in the tree', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    follow_up: FollowUpV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        follow_up = self.follow_up.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "follow_up": follow_up,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.follow_up_v2 import FollowUpV2

        d = dict(src_dict)
        follow_up = FollowUpV2.from_dict(d.pop("follow_up"))

        follow_ups_create_result_v2 = cls(
            follow_up=follow_up,
        )

        follow_ups_create_result_v2.additional_properties = d
        return follow_ups_create_result_v2

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
