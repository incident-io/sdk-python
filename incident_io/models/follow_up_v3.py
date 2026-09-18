from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.follow_up_v3_status import FollowUpV3Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.external_issue_reference_v2 import ExternalIssueReferenceV2
    from ..models.follow_up_category_v3 import FollowUpCategoryV3
    from ..models.follow_up_priority_v2 import FollowUpPriorityV2
    from ..models.team_slim_v2 import TeamSlimV2
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="FollowUpV3")


@_attrs_define
class FollowUpV3:
    """
    Example:
        {'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'assignee_team': {'id': 'abc123', 'name': 'abc123'},
            'category': {'description': 'Follow-ups related to infrastructure changes.', 'id': '01GNW4BAQ7XRMFF6FHKNXDFPRW',
            'name': 'Infrastructure', 'rank': 10}, 'completed_at': '2021-08-17T13:28:57.801578Z', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}, 'description': 'Call the fire brigade', 'external_issue_reference':
            {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-
            write-up', 'provider': 'asana'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'labels': ['bug', 'urgent'], 'priority': {'description': 'A follow-up that
            requires immediate attention.', 'id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name': 'Urgent', 'rank': 10}, 'status':
            'outstanding', 'title': 'Cat is stuck in the tree', 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the follow-up was created Example: 2021-08-17T13:28:57.801578Z.
        creator (ActorV2):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
            PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}.
        id (str): Unique identifier for the follow-up Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str): Unique identifier of the incident the follow-up belongs to Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        labels (list[str]): Labels associated with this follow-up Example: ['bug', 'urgent'].
        status (FollowUpV3Status): Status of the follow-up Example: outstanding.
        title (str): Title of the follow-up Example: Cat is stuck in the tree.
        updated_at (datetime.datetime): When the follow-up was last updated Example: 2021-08-17T13:28:57.801578Z.
        assignee (UserV2 | Unset):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        assignee_team (TeamSlimV2 | Unset):  Example: {'id': 'abc123', 'name': 'abc123'}.
        category (FollowUpCategoryV3 | Unset):  Example: {'description': 'Follow-ups related to infrastructure
            changes.', 'id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name': 'Infrastructure', 'rank': 10}.
        completed_at (datetime.datetime | Unset): When the follow-up was completed Example: 2021-08-17T13:28:57.801578Z.
        description (str | Unset): Description of the follow-up Example: Call the fire brigade.
        external_issue_reference (ExternalIssueReferenceV2 | Unset):  Example: {'issue_name': 'INC-123',
            'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up', 'provider':
            'asana'}.
        priority (FollowUpPriorityV2 | Unset):  Example: {'description': 'A follow-up that requires immediate
            attention.', 'id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name': 'Urgent', 'rank': 10}.
    """

    created_at: datetime.datetime
    creator: ActorV2
    id: str
    incident_id: str
    labels: list[str]
    status: FollowUpV3Status
    title: str
    updated_at: datetime.datetime
    assignee: UserV2 | Unset = UNSET
    assignee_team: TeamSlimV2 | Unset = UNSET
    category: FollowUpCategoryV3 | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    external_issue_reference: ExternalIssueReferenceV2 | Unset = UNSET
    priority: FollowUpPriorityV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        creator = self.creator.to_dict()

        id = self.id

        incident_id = self.incident_id

        labels = self.labels

        status = self.status.value

        title = self.title

        updated_at = self.updated_at.isoformat()

        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        assignee_team: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee_team, Unset):
            assignee_team = self.assignee_team.to_dict()

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        description = self.description

        external_issue_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_issue_reference, Unset):
            external_issue_reference = self.external_issue_reference.to_dict()

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "creator": creator,
                "id": id,
                "incident_id": incident_id,
                "labels": labels,
                "status": status,
                "title": title,
                "updated_at": updated_at,
            }
        )
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if assignee_team is not UNSET:
            field_dict["assignee_team"] = assignee_team
        if category is not UNSET:
            field_dict["category"] = category
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if description is not UNSET:
            field_dict["description"] = description
        if external_issue_reference is not UNSET:
            field_dict["external_issue_reference"] = external_issue_reference
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.external_issue_reference_v2 import (
            ExternalIssueReferenceV2,
        )
        from ..models.follow_up_category_v3 import FollowUpCategoryV3
        from ..models.follow_up_priority_v2 import FollowUpPriorityV2
        from ..models.team_slim_v2 import TeamSlimV2
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        creator = ActorV2.from_dict(d.pop("creator"))

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        labels = cast(list[str], d.pop("labels"))

        status = FollowUpV3Status(d.pop("status"))

        title = d.pop("title")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _assignee = d.pop("assignee", UNSET)
        assignee: UserV2 | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = UserV2.from_dict(_assignee)

        _assignee_team = d.pop("assignee_team", UNSET)
        assignee_team: TeamSlimV2 | Unset
        if isinstance(_assignee_team, Unset):
            assignee_team = UNSET
        else:
            assignee_team = TeamSlimV2.from_dict(_assignee_team)

        _category = d.pop("category", UNSET)
        category: FollowUpCategoryV3 | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = FollowUpCategoryV3.from_dict(_category)

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = datetime.datetime.fromisoformat(_completed_at)

        description = d.pop("description", UNSET)

        _external_issue_reference = d.pop("external_issue_reference", UNSET)
        external_issue_reference: ExternalIssueReferenceV2 | Unset
        if isinstance(_external_issue_reference, Unset):
            external_issue_reference = UNSET
        else:
            external_issue_reference = ExternalIssueReferenceV2.from_dict(
                _external_issue_reference
            )

        _priority = d.pop("priority", UNSET)
        priority: FollowUpPriorityV2 | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = FollowUpPriorityV2.from_dict(_priority)

        follow_up_v3 = cls(
            created_at=created_at,
            creator=creator,
            id=id,
            incident_id=incident_id,
            labels=labels,
            status=status,
            title=title,
            updated_at=updated_at,
            assignee=assignee,
            assignee_team=assignee_team,
            category=category,
            completed_at=completed_at,
            description=description,
            external_issue_reference=external_issue_reference,
            priority=priority,
        )

        follow_up_v3.additional_properties = d
        return follow_up_v3

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
