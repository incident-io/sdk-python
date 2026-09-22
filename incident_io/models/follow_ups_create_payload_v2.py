from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FollowUpsCreatePayloadV2")


@_attrs_define(kw_only=True)
class FollowUpsCreatePayloadV2:
    """
    Example:
        {'assignee_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'assignee_team_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'description':
            'Call the fire brigade', 'external_issue_reference_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'follow_up_category_id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'follow_up_priority_option_id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'labels': ['bug', 'urgent'], 'title': 'Add alerting on replica lag'}

    Attributes:
        incident_id (str): Unique identifier of the incident the follow-up belongs to Example:
            01FCNDV6P870EA6S7TK1DSYD5H.
        title (str): Title of the follow-up Example: Add alerting on replica lag.
        assignee_id (str | Unset): ID of the user this follow-up is assigned to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        assignee_team_id (str | Unset): ID of the team this follow-up is assigned to Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        description (str | Unset): Description of the follow-up. Supports Markdown. Example: Call the fire brigade.
        external_issue_reference_id (str | Unset): If this follow-up is related to an external issue, the ID of that
            issue Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        follow_up_category_id (str | Unset): ID of the category for this follow-up Example: 01GNW4BAQ7XRMFF6FHKNXDFPRW.
        follow_up_priority_option_id (str | Unset): ID of the priority for this follow-up Example:
            01GNW4BAQ7XRMFF6FHKNXDFPRW.
        labels (list[str] | Unset): Labels associated with this follow-up Example: ['bug', 'urgent'].
    """

    incident_id: str
    title: str
    assignee_id: str | Unset = UNSET
    assignee_team_id: str | Unset = UNSET
    description: str | Unset = UNSET
    external_issue_reference_id: str | Unset = UNSET
    follow_up_category_id: str | Unset = UNSET
    follow_up_priority_option_id: str | Unset = UNSET
    labels: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        title = self.title

        assignee_id = self.assignee_id

        assignee_team_id = self.assignee_team_id

        description = self.description

        external_issue_reference_id = self.external_issue_reference_id

        follow_up_category_id = self.follow_up_category_id

        follow_up_priority_option_id = self.follow_up_priority_option_id

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
                "title": title,
            }
        )
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id
        if assignee_team_id is not UNSET:
            field_dict["assignee_team_id"] = assignee_team_id
        if description is not UNSET:
            field_dict["description"] = description
        if external_issue_reference_id is not UNSET:
            field_dict["external_issue_reference_id"] = external_issue_reference_id
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
        incident_id = d.pop("incident_id")

        title = d.pop("title")

        assignee_id = d.pop("assignee_id", UNSET)

        assignee_team_id = d.pop("assignee_team_id", UNSET)

        description = d.pop("description", UNSET)

        external_issue_reference_id = d.pop("external_issue_reference_id", UNSET)

        follow_up_category_id = d.pop("follow_up_category_id", UNSET)

        follow_up_priority_option_id = d.pop("follow_up_priority_option_id", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        follow_ups_create_payload_v2 = cls(
            incident_id=incident_id,
            title=title,
            assignee_id=assignee_id,
            assignee_team_id=assignee_team_id,
            description=description,
            external_issue_reference_id=external_issue_reference_id,
            follow_up_category_id=follow_up_category_id,
            follow_up_priority_option_id=follow_up_priority_option_id,
            labels=labels,
        )

        follow_ups_create_payload_v2.additional_properties = d
        return follow_ups_create_payload_v2

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
