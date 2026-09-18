from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OnCallNotificationRuleMethodTargetSpecificPublicV2")


@_attrs_define
class OnCallNotificationRuleMethodTargetSpecificPublicV2:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        id (str): The ID of the notification method. References a method from the notification methods list. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
    """

    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        on_call_notification_rule_method_target_specific_public_v2 = cls(
            id=id,
        )

        on_call_notification_rule_method_target_specific_public_v2.additional_properties = d
        return on_call_notification_rule_method_target_specific_public_v2

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
