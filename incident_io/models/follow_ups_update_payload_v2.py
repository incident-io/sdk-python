from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.follow_ups_update_payload_v2_status import FollowUpsUpdatePayloadV2Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="FollowUpsUpdatePayloadV2")


@_attrs_define
class FollowUpsUpdatePayloadV2:
    """
    Example:
        {'assignee_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'assignee_team_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'description':
            'Call the fire brigade', 'follow_up_category_id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'follow_up_priority_option_id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'labels': ['bug', 'urgent'], 'status': 'outstanding', 'title': 'Add alerting on
            replica lag'}

    Attributes:
        status (FollowUpsUpdatePayloadV2Status): Status of the follow-up. Setting this to `deleted` is not allowed; use
            the delete endpoint instead. Example: outstanding.
        title (str): Title of the follow-up Example: Add alerting on replica lag.
        assignee_id (str | Unset): ID of the user this follow-up is assigned to. Set to null to unassign. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        assignee_team_id (str | Unset): ID of the team this follow-up is assigned to. Set to null to unassign. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        description (str | Unset): Description of the follow-up. Supports Markdown. Example: Call the fire brigade.
        follow_up_category_id (str | Unset): ID of the category for this follow-up Example: 01GNW4BAQ7XRMFF6FHKNXDFPRW.
        follow_up_priority_option_id (str | Unset): ID of the priority for this follow-up Example:
            01GNW4BAQ7XRMFF6FHKNXDFPRW.
        labels (list[str] | Unset): Labels associated with this follow-up Example: ['bug', 'urgent'].
    """

    status: FollowUpsUpdatePayloadV2Status
    title: str
    assignee_id: str | Unset = UNSET
    assignee_team_id: str | Unset = UNSET
    description: str | Unset = UNSET
    follow_up_category_id: str | Unset = UNSET
    follow_up_priority_option_id: str | Unset = UNSET
    labels: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        title = self.title

        assignee_id = self.assignee_id

        assignee_team_id = self.assignee_team_id

        description = self.description

        follow_up_category_id = self.follow_up_category_id

        follow_up_priority_option_id = self.follow_up_priority_option_id

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "title": title,
            }
        )
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id
        if assignee_team_id is not UNSET:
            field_dict["assignee_team_id"] = assignee_team_id
        if description is not UNSET:
            field_dict["description"] = description
        if follow_up_category_id is not UNSET:
            field_dict["follow_up_category_id"] = follow_up_category_id
        if follow_up_priority_option_id is not UNSET:
            field_dict["follow_up_priority_option_id"] = follow_up_priority_option_id
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = FollowUpsUpdatePayloadV2Status(d.pop("status"))

        title = d.pop("title")

        assignee_id = d.pop("assignee_id", UNSET)

        assignee_team_id = d.pop("assignee_team_id", UNSET)

        description = d.pop("description", UNSET)

        follow_up_category_id = d.pop("follow_up_category_id", UNSET)

        follow_up_priority_option_id = d.pop("follow_up_priority_option_id", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        follow_ups_update_payload_v2 = cls(
            status=status,
            title=title,
            assignee_id=assignee_id,
            assignee_team_id=assignee_team_id,
            description=description,
            follow_up_category_id=follow_up_category_id,
            follow_up_priority_option_id=follow_up_priority_option_id,
            labels=labels,
        )

        follow_ups_update_payload_v2.additional_properties = d
        return follow_ups_update_payload_v2

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
