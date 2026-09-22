from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_membership_v1 import IncidentMembershipV1


T = TypeVar("T", bound="IncidentMembershipsCreateResultV1")


@_attrs_define(kw_only=True)
class IncidentMembershipsCreateResultV1:
    """
    Example:
        {'incident_membership': {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'updated_at': '2021-08-17T13:28:57.801578Z', 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}}}

    Attributes:
        incident_membership (IncidentMembershipV1):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}}.
    """

    incident_membership: IncidentMembershipV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_membership = self.incident_membership.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_membership": incident_membership,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_membership_v1 import (
            IncidentMembershipV1,
        )

        d = dict(src_dict)
        incident_membership = IncidentMembershipV1.from_dict(
            d.pop("incident_membership")
        )

        incident_memberships_create_result_v1 = cls(
            incident_membership=incident_membership,
        )

        incident_memberships_create_result_v1.additional_properties = d
        return incident_memberships_create_result_v1

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
