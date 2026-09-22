from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.incident_role_v2 import IncidentRoleV2
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ActivityRoleUpdateV2")


@_attrs_define(kw_only=True)
class ActivityRoleUpdateV2:
    """
    Example:
        {'new_assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'previous_assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the
            incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are
            clear on responsibilities', 'name': 'Incident Lead', 'role_type': 'lead', 'shortform': 'lead', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}}

    Attributes:
        new_assignee (UserV2 | Unset):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        previous_assignee (UserV2 | Unset):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        role (IncidentRoleV2 | Unset):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The
            person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on
            the incident; Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'role_type': 'lead',
            'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
        updater (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
    """

    new_assignee: UserV2 | Unset = UNSET
    previous_assignee: UserV2 | Unset = UNSET
    role: IncidentRoleV2 | Unset = UNSET
    updater: ActorV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_assignee, Unset):
            new_assignee = self.new_assignee.to_dict()

        previous_assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_assignee, Unset):
            previous_assignee = self.previous_assignee.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        updater: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updater, Unset):
            updater = self.updater.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_assignee is not UNSET:
            field_dict["new_assignee"] = new_assignee
        if previous_assignee is not UNSET:
            field_dict["previous_assignee"] = previous_assignee
        if role is not UNSET:
            field_dict["role"] = role
        if updater is not UNSET:
            field_dict["updater"] = updater

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.incident_role_v2 import IncidentRoleV2
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        _new_assignee = d.pop("new_assignee", UNSET)
        new_assignee: UserV2 | Unset
        if isinstance(_new_assignee, Unset):
            new_assignee = UNSET
        else:
            new_assignee = UserV2.from_dict(_new_assignee)

        _previous_assignee = d.pop("previous_assignee", UNSET)
        previous_assignee: UserV2 | Unset
        if isinstance(_previous_assignee, Unset):
            previous_assignee = UNSET
        else:
            previous_assignee = UserV2.from_dict(_previous_assignee)

        _role = d.pop("role", UNSET)
        role: IncidentRoleV2 | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = IncidentRoleV2.from_dict(_role)

        _updater = d.pop("updater", UNSET)
        updater: ActorV2 | Unset
        if isinstance(_updater, Unset):
            updater = UNSET
        else:
            updater = ActorV2.from_dict(_updater)

        activity_role_update_v2 = cls(
            new_assignee=new_assignee,
            previous_assignee=previous_assignee,
            role=role,
            updater=updater,
        )

        activity_role_update_v2.additional_properties = d
        return activity_role_update_v2

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
