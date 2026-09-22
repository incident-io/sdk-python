from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.on_call_notification_method_public_v2 import (
        OnCallNotificationMethodPublicV2,
    )


T = TypeVar("T", bound="UsersListNotificationMethodsResultV2")


@_attrs_define(kw_only=True)
class UsersListNotificationMethodsResultV2:
    """
    Example:
        {'notification_methods': [{'address': '•••••••6789', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_usable': True,
            'method_type': 'app', 'phone_details': {'supports_sms': True, 'supports_voice': True}}]}

    Attributes:
        notification_methods (list[OnCallNotificationMethodPublicV2]):  Example: [{'address': '•••••••6789', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_usable': True, 'method_type': 'app', 'phone_details': {'supports_sms': True,
            'supports_voice': True}}].
    """

    notification_methods: list[OnCallNotificationMethodPublicV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_methods = []
        for notification_methods_item_data in self.notification_methods:
            notification_methods_item = notification_methods_item_data.to_dict()
            notification_methods.append(notification_methods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notification_methods": notification_methods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.on_call_notification_method_public_v2 import (
            OnCallNotificationMethodPublicV2,
        )

        d = dict(src_dict)
        notification_methods = []
        _notification_methods = d.pop("notification_methods")
        for notification_methods_item_data in _notification_methods:
            notification_methods_item = OnCallNotificationMethodPublicV2.from_dict(
                notification_methods_item_data
            )

            notification_methods.append(notification_methods_item)

        users_list_notification_methods_result_v2 = cls(
            notification_methods=notification_methods,
        )

        users_list_notification_methods_result_v2.additional_properties = d
        return users_list_notification_methods_result_v2

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
