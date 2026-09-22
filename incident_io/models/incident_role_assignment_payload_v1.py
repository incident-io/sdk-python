from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_reference_payload_v1 import UserReferencePayloadV1


T = TypeVar("T", bound="IncidentRoleAssignmentPayloadV1")


@_attrs_define(kw_only=True)
class IncidentRoleAssignmentPayloadV1:
    """
    Example:
        {'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}

    Attributes:
        assignee (UserReferencePayloadV1):  Example: {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}.
        incident_role_id (str): Unique ID of an incident role. Note that the 'reporter' role can only be assigned when
            creating an incident. Example: 01FH5TZRWMNAFB0DZ23FD1TV96.
    """

    assignee: UserReferencePayloadV1
    incident_role_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignee = self.assignee.to_dict()

        incident_role_id = self.incident_role_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignee": assignee,
                "incident_role_id": incident_role_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_reference_payload_v1 import (
            UserReferencePayloadV1,
        )

        d = dict(src_dict)
        assignee = UserReferencePayloadV1.from_dict(d.pop("assignee"))

        incident_role_id = d.pop("incident_role_id")

        incident_role_assignment_payload_v1 = cls(
            assignee=assignee,
            incident_role_id=incident_role_id,
        )

        incident_role_assignment_payload_v1.additional_properties = d
        return incident_role_assignment_payload_v1

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
