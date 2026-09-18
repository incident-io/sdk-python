from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_role_v1 import IncidentRoleV1
    from ..models.user_v1 import UserV1


T = TypeVar("T", bound="IncidentRoleAssignmentV1")


@_attrs_define
class IncidentRoleAssignmentV1:
    """
    Example:
        {'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'The person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'instructions': 'Take point on the incident; Make sure people are clear on responsibilities', 'name': 'Incident
            Lead', 'required': False, 'role_type': 'lead', 'shortform': 'lead', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        role (IncidentRoleV1):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person
            currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the
            incident; Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': False,
            'role_type': 'lead', 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
        assignee (UserV1 | Unset):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}.
    """

    role: IncidentRoleV1
    assignee: UserV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role.to_dict()

        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )
        if assignee is not UNSET:
            field_dict["assignee"] = assignee

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_role_v1 import IncidentRoleV1
        from ..models.user_v1 import UserV1

        d = dict(src_dict)
        role = IncidentRoleV1.from_dict(d.pop("role"))

        _assignee = d.pop("assignee", UNSET)
        assignee: UserV1 | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = UserV1.from_dict(_assignee)

        incident_role_assignment_v1 = cls(
            role=role,
            assignee=assignee,
        )

        incident_role_assignment_v1.additional_properties = d
        return incident_role_assignment_v1

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
