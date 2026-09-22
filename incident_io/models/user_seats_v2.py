from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_seats_v2_on_call import UserSeatsV2OnCall
from ..models.user_seats_v2_response import UserSeatsV2Response

T = TypeVar("T", bound="UserSeatsV2")


@_attrs_define(kw_only=True)
class UserSeatsV2:
    """
    Example:
        {'on_call': 'full_access', 'response': 'viewer_only'}

    Attributes:
        on_call (UserSeatsV2OnCall): On-call seat access level Example: full_access.
        response (UserSeatsV2Response): Response seat access level Example: viewer_only.
    """

    on_call: UserSeatsV2OnCall
    response: UserSeatsV2Response
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        on_call = self.on_call.value

        response = self.response.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "on_call": on_call,
                "response": response,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        on_call = UserSeatsV2OnCall(d.pop("on_call"))

        response = UserSeatsV2Response(d.pop("response"))

        user_seats_v2 = cls(
            on_call=on_call,
            response=response,
        )

        user_seats_v2.additional_properties = d
        return user_seats_v2

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
