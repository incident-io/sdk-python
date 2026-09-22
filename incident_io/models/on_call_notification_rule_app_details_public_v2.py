from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.on_call_notification_rule_app_details_public_v2_push_notification_criticality import (
    OnCallNotificationRuleAppDetailsPublicV2PushNotificationCriticality,
)

T = TypeVar("T", bound="OnCallNotificationRuleAppDetailsPublicV2")


@_attrs_define(kw_only=True)
class OnCallNotificationRuleAppDetailsPublicV2:
    """
    Example:
        {'push_notification_criticality': 'critical'}

    Attributes:
        push_notification_criticality (OnCallNotificationRuleAppDetailsPublicV2PushNotificationCriticality): Controls
            the interruption level of push notifications. 'critical' bypasses Do Not Disturb, 'active' respects it. Example:
            critical.
    """

    push_notification_criticality: (
        OnCallNotificationRuleAppDetailsPublicV2PushNotificationCriticality
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        push_notification_criticality = self.push_notification_criticality.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "push_notification_criticality": push_notification_criticality,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        push_notification_criticality = (
            OnCallNotificationRuleAppDetailsPublicV2PushNotificationCriticality(
                d.pop("push_notification_criticality")
            )
        )

        on_call_notification_rule_app_details_public_v2 = cls(
            push_notification_criticality=push_notification_criticality,
        )

        on_call_notification_rule_app_details_public_v2.additional_properties = d
        return on_call_notification_rule_app_details_public_v2

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
