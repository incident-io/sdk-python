from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_with_roles_v2_role import UserWithRolesV2Role
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rbac_role_v2 import RBACRoleV2
    from ..models.user_seats_v2 import UserSeatsV2


T = TypeVar("T", bound="UserWithRolesV2")


@_attrs_define(kw_only=True)
class UserWithRolesV2:
    """
    Example:
        {'base_role': {'description': 'Elevated permissions for the customer success team.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'}, 'custom_roles':
            [{'description': 'Elevated permissions for the customer success team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Customer Success', 'slug': 'customer-success'}], 'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_active': True, 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'seats':
            {'on_call': 'full_access', 'response': 'viewer_only'}, 'slack_user_id': 'U02AYNF2XJM'}

    Attributes:
        base_role (RBACRoleV2):  Example: {'description': 'Elevated permissions for the customer success team.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'}.
        custom_roles (list[RBACRoleV2]):  Example: [{'description': 'Elevated permissions for the customer success
            team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'}].
        id (str): Unique identifier of the user Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        is_active (bool): Whether the user is active. False if the user has been deactivated (e.g. offboarded) or is not
            yet active. Example: True.
        name (str): Name of the user Example: Lisa Karlin Curtis.
        role (UserWithRolesV2Role): DEPRECATED: Role of the user as of March 9th 2023, this value is no longer updated.
            Example: owner.
        seats (UserSeatsV2):  Example: {'on_call': 'full_access', 'response': 'viewer_only'}.
        email (str | Unset): Email address of the user. Example: lisa@incident.io.
        slack_user_id (str | Unset): Slack ID of the user Example: U02AYNF2XJM.
    """

    base_role: RBACRoleV2
    custom_roles: list[RBACRoleV2]
    id: str
    is_active: bool
    name: str
    role: UserWithRolesV2Role
    seats: UserSeatsV2
    email: str | Unset = UNSET
    slack_user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_role = self.base_role.to_dict()

        custom_roles = []
        for custom_roles_item_data in self.custom_roles:
            custom_roles_item = custom_roles_item_data.to_dict()
            custom_roles.append(custom_roles_item)

        id = self.id

        is_active = self.is_active

        name = self.name

        role = self.role.value

        seats = self.seats.to_dict()

        email = self.email

        slack_user_id = self.slack_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_role": base_role,
                "custom_roles": custom_roles,
                "id": id,
                "is_active": is_active,
                "name": name,
                "role": role,
                "seats": seats,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if slack_user_id is not UNSET:
            field_dict["slack_user_id"] = slack_user_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rbac_role_v2 import RBACRoleV2
        from ..models.user_seats_v2 import UserSeatsV2

        d = dict(src_dict)
        base_role = RBACRoleV2.from_dict(d.pop("base_role"))

        custom_roles = []
        _custom_roles = d.pop("custom_roles")
        for custom_roles_item_data in _custom_roles:
            custom_roles_item = RBACRoleV2.from_dict(custom_roles_item_data)

            custom_roles.append(custom_roles_item)

        id = d.pop("id")

        is_active = d.pop("is_active")

        name = d.pop("name")

        role = UserWithRolesV2Role(d.pop("role"))

        seats = UserSeatsV2.from_dict(d.pop("seats"))

        email = d.pop("email", UNSET)

        slack_user_id = d.pop("slack_user_id", UNSET)

        user_with_roles_v2 = cls(
            base_role=base_role,
            custom_roles=custom_roles,
            id=id,
            is_active=is_active,
            name=name,
            role=role,
            seats=seats,
            email=email,
            slack_user_id=slack_user_id,
        )

        user_with_roles_v2.additional_properties = d
        return user_with_roles_v2

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
