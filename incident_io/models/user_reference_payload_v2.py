from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserReferencePayloadV2")


@_attrs_define
class UserReferencePayloadV2:
    """
    Example:
        {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}

    Attributes:
        email (str | Unset): The user's email address, matching the email on their Slack account Example:
            bob@example.com.
        id (str | Unset): The incident.io ID of a user Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        slack_user_id (str | Unset): The ID of the user's Slack account. Example: USER123.
    """

    email: str | Unset = UNSET
    id: str | Unset = UNSET
    slack_user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        id = self.id

        slack_user_id = self.slack_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if slack_user_id is not UNSET:
            field_dict["slack_user_id"] = slack_user_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        slack_user_id = d.pop("slack_user_id", UNSET)

        user_reference_payload_v2 = cls(
            email=email,
            id=id,
            slack_user_id=slack_user_id,
        )

        user_reference_payload_v2.additional_properties = d
        return user_reference_payload_v2

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
