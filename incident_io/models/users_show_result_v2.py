from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_with_roles_v2 import UserWithRolesV2


T = TypeVar("T", bound="UsersShowResultV2")


@_attrs_define
class UsersShowResultV2:
    """
    Example:
        {'user': {'base_role': {'description': 'Elevated permissions for the customer success team.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'}, 'custom_roles':
            [{'description': 'Elevated permissions for the customer success team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Customer Success', 'slug': 'customer-success'}], 'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_active': True, 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'seats':
            {'on_call': 'full_access', 'response': 'viewer_only'}, 'slack_user_id': 'U02AYNF2XJM'}}

    Attributes:
        user (UserWithRolesV2):  Example: {'base_role': {'description': 'Elevated permissions for the customer success
            team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'},
            'custom_roles': [{'description': 'Elevated permissions for the customer success team.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'}], 'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_active': True, 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'seats': {'on_call': 'full_access', 'response': 'viewer_only'}, 'slack_user_id': 'U02AYNF2XJM'}.
    """

    user: UserWithRolesV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_with_roles_v2 import UserWithRolesV2

        d = dict(src_dict)
        user = UserWithRolesV2.from_dict(d.pop("user"))

        users_show_result_v2 = cls(
            user=user,
        )

        users_show_result_v2.additional_properties = d
        return users_show_result_v2

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
