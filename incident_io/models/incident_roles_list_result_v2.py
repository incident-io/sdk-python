from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_role_v2 import IncidentRoleV2


T = TypeVar("T", bound="IncidentRolesListResultV2")


@_attrs_define(kw_only=True)
class IncidentRolesListResultV2:
    """
    Example:
        {'incident_roles': [{'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently
            coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident;
            Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'role_type': 'lead', 'shortform':
            'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        incident_roles (list[IncidentRoleV2]):  Example: [{'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'The person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take
            point on the incident; Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'role_type':
            'lead', 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}].
    """

    incident_roles: list[IncidentRoleV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_roles = []
        for incident_roles_item_data in self.incident_roles:
            incident_roles_item = incident_roles_item_data.to_dict()
            incident_roles.append(incident_roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_roles": incident_roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_role_v2 import IncidentRoleV2

        d = dict(src_dict)
        incident_roles = []
        _incident_roles = d.pop("incident_roles")
        for incident_roles_item_data in _incident_roles:
            incident_roles_item = IncidentRoleV2.from_dict(incident_roles_item_data)

            incident_roles.append(incident_roles_item)

        incident_roles_list_result_v2 = cls(
            incident_roles=incident_roles,
        )

        incident_roles_list_result_v2.additional_properties = d
        return incident_roles_list_result_v2

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
