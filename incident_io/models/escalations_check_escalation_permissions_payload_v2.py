from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EscalationsCheckEscalationPermissionsPayloadV2")


@_attrs_define
class EscalationsCheckEscalationPermissionsPayloadV2:
    """
    Example:
        {'user_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH']}

    Attributes:
        user_ids (list[str]): The IDs of the users to check response options for Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
    """

    user_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_ids": user_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user_ids = cast(list[str], d.pop("user_ids"))

        escalations_check_escalation_permissions_payload_v2 = cls(
            user_ids=user_ids,
        )

        escalations_check_escalation_permissions_payload_v2.additional_properties = d
        return escalations_check_escalation_permissions_payload_v2

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
