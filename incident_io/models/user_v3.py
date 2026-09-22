from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserV3")


@_attrs_define(kw_only=True)
class UserV3:
    """
    Example:
        {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'slack_user_id':
            'U02AYNF2XJM'}

    Attributes:
        id (str): Unique identifier of the user Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name of the user Example: Lisa Karlin Curtis.
        email (str | Unset): Email address of the user. Example: lisa@incident.io.
        slack_user_id (str | Unset): Slack ID of the user Example: U02AYNF2XJM.
    """

    id: str
    name: str
    email: str | Unset = UNSET
    slack_user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        email = self.email

        slack_user_id = self.slack_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if slack_user_id is not UNSET:
            field_dict["slack_user_id"] = slack_user_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        email = d.pop("email", UNSET)

        slack_user_id = d.pop("slack_user_id", UNSET)

        user_v3 = cls(
            id=id,
            name=name,
            email=email,
            slack_user_id=slack_user_id,
        )

        user_v3.additional_properties = d
        return user_v3

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
