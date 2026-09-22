from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2
    from ..models.user_with_roles_v2 import UserWithRolesV2


T = TypeVar("T", bound="UsersListResultV2")


@_attrs_define(kw_only=True)
class UsersListResultV2:
    """
    Example:
        {'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}, 'users': [{'base_role':
            {'description': 'Elevated permissions for the customer success team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Customer Success', 'slug': 'customer-success'}, 'custom_roles': [{'description': 'Elevated permissions
            for the customer success team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug':
            'customer-success'}], 'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_active': True,
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'seats': {'on_call': 'full_access', 'response': 'viewer_only'},
            'slack_user_id': 'U02AYNF2XJM'}]}

    Attributes:
        pagination_meta (PaginationMetaResultV2):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
        users (list[UserWithRolesV2]):  Example: [{'base_role': {'description': 'Elevated permissions for the customer
            success team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'},
            'custom_roles': [{'description': 'Elevated permissions for the customer success team.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'}], 'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_active': True, 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'seats': {'on_call': 'full_access', 'response': 'viewer_only'}, 'slack_user_id': 'U02AYNF2XJM'}].
    """

    pagination_meta: PaginationMetaResultV2
    users: list[UserWithRolesV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination_meta = self.pagination_meta.to_dict()

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination_meta": pagination_meta,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )
        from ..models.user_with_roles_v2 import UserWithRolesV2

        d = dict(src_dict)
        pagination_meta = PaginationMetaResultV2.from_dict(d.pop("pagination_meta"))

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = UserWithRolesV2.from_dict(users_item_data)

            users.append(users_item)

        users_list_result_v2 = cls(
            pagination_meta=pagination_meta,
            users=users,
        )

        users_list_result_v2.additional_properties = d
        return users_list_result_v2

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
