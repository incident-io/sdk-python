from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.on_call_notification_method_public_v2_method_type import (
    OnCallNotificationMethodPublicV2MethodType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.on_call_notification_method_phone_details_public_v2 import (
        OnCallNotificationMethodPhoneDetailsPublicV2,
    )


T = TypeVar("T", bound="OnCallNotificationMethodPublicV2")


@_attrs_define
class OnCallNotificationMethodPublicV2:
    """
    Example:
        {'address': '•••••••6789', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_usable': True, 'method_type': 'app',
            'phone_details': {'supports_sms': True, 'supports_voice': True}}

    Attributes:
        address (str): The address of this method (e.g. redacted phone number, email address, device name, Slack user
            name) Example: •••••••6789.
        id (str): Unique identifier for this notification method Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        is_usable (bool): Whether this method is ready to receive notifications. For phone, this means verified. For app
            devices, this means push notifications can be sent. For email, Slack, and Microsoft Teams this is always true.
            Example: True.
        method_type (OnCallNotificationMethodPublicV2MethodType): The high-level type of notification method. Phone
            rules include phone details that distinguish SMS from voice calls. Example: app.
        phone_details (OnCallNotificationMethodPhoneDetailsPublicV2 | Unset):  Example: {'supports_sms': True,
            'supports_voice': True}.
    """

    address: str
    id: str
    is_usable: bool
    method_type: OnCallNotificationMethodPublicV2MethodType
    phone_details: OnCallNotificationMethodPhoneDetailsPublicV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        id = self.id

        is_usable = self.is_usable

        method_type = self.method_type.value

        phone_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.phone_details, Unset):
            phone_details = self.phone_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "id": id,
                "is_usable": is_usable,
                "method_type": method_type,
            }
        )
        if phone_details is not UNSET:
            field_dict["phone_details"] = phone_details

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.on_call_notification_method_phone_details_public_v2 import (
            OnCallNotificationMethodPhoneDetailsPublicV2,
        )

        d = dict(src_dict)
        address = d.pop("address")

        id = d.pop("id")

        is_usable = d.pop("is_usable")

        method_type = OnCallNotificationMethodPublicV2MethodType(d.pop("method_type"))

        _phone_details = d.pop("phone_details", UNSET)
        phone_details: OnCallNotificationMethodPhoneDetailsPublicV2 | Unset
        if isinstance(_phone_details, Unset):
            phone_details = UNSET
        else:
            phone_details = OnCallNotificationMethodPhoneDetailsPublicV2.from_dict(
                _phone_details
            )

        on_call_notification_method_public_v2 = cls(
            address=address,
            id=id,
            is_usable=is_usable,
            method_type=method_type,
            phone_details=phone_details,
        )

        on_call_notification_method_public_v2.additional_properties = d
        return on_call_notification_method_public_v2

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
