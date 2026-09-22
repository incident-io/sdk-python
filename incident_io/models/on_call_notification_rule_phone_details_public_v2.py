from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.on_call_notification_rule_phone_details_public_v2_channel import (
    OnCallNotificationRulePhoneDetailsPublicV2Channel,
)

T = TypeVar("T", bound="OnCallNotificationRulePhoneDetailsPublicV2")


@_attrs_define(kw_only=True)
class OnCallNotificationRulePhoneDetailsPublicV2:
    """
    Example:
        {'channel': 'voice'}

    Attributes:
        channel (OnCallNotificationRulePhoneDetailsPublicV2Channel): Which channel of a phone notification method this
            rule uses. Example: voice.
    """

    channel: OnCallNotificationRulePhoneDetailsPublicV2Channel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel = OnCallNotificationRulePhoneDetailsPublicV2Channel(d.pop("channel"))

        on_call_notification_rule_phone_details_public_v2 = cls(
            channel=channel,
        )

        on_call_notification_rule_phone_details_public_v2.additional_properties = d
        return on_call_notification_rule_phone_details_public_v2

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
