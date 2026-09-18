from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_v2_status import ActionV2Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ActionV2")


@_attrs_define
class ActionV2:
    """
    Example:
        {'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'completed_at': '2021-08-17T13:28:57.801578Z', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}, 'description': 'Call the fire brigade', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'status': 'outstanding', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the action was created Example: 2021-08-17T13:28:57.801578Z.
        creator (ActorV2):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
            PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}.
        description (str): Description of the action Example: Call the fire brigade.
        id (str): Unique identifier for the action Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str): Unique identifier of the incident the action belongs to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        status (ActionV2Status): Status of the action Example: outstanding.
        updated_at (datetime.datetime): When the action was last updated Example: 2021-08-17T13:28:57.801578Z.
        assignee (UserV2 | Unset):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        completed_at (datetime.datetime | Unset): When the action was completed Example: 2021-08-17T13:28:57.801578Z.
    """

    created_at: datetime.datetime
    creator: ActorV2
    description: str
    id: str
    incident_id: str
    status: ActionV2Status
    updated_at: datetime.datetime
    assignee: UserV2 | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        creator = self.creator.to_dict()

        description = self.description

        id = self.id

        incident_id = self.incident_id

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "creator": creator,
                "description": description,
                "id": id,
                "incident_id": incident_id,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        creator = ActorV2.from_dict(d.pop("creator"))

        description = d.pop("description")

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        status = ActionV2Status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _assignee = d.pop("assignee", UNSET)
        assignee: UserV2 | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = UserV2.from_dict(_assignee)

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = datetime.datetime.fromisoformat(_completed_at)

        action_v2 = cls(
            created_at=created_at,
            creator=creator,
            description=description,
            id=id,
            incident_id=incident_id,
            status=status,
            updated_at=updated_at,
            assignee=assignee,
            completed_at=completed_at,
        )

        action_v2.additional_properties = d
        return action_v2

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
