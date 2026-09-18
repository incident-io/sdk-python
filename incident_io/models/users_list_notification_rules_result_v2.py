from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.on_call_notification_rule_public_v2 import (
        OnCallNotificationRulePublicV2,
    )


T = TypeVar("T", bound="UsersListNotificationRulesResultV2")


@_attrs_define
class UsersListNotificationRulesResultV2:
    """
    Example:
        {'notification_rules': [{'app': {'push_notification_criticality': 'critical'}, 'delay_seconds': 0, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'method_target': {'all': {}, 'specific': {'id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'type': 'specific'}, 'method_type': 'app', 'phone': {'channel': 'voice'}, 'rule_type': 'low_urgency'}]}

    Attributes:
        notification_rules (list[OnCallNotificationRulePublicV2]):  Example: [{'app': {'push_notification_criticality':
            'critical'}, 'delay_seconds': 0, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'method_target': {'all': {}, 'specific':
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'specific'}, 'method_type': 'app', 'phone': {'channel': 'voice'},
            'rule_type': 'low_urgency'}].
    """

    notification_rules: list[OnCallNotificationRulePublicV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_rules = []
        for notification_rules_item_data in self.notification_rules:
            notification_rules_item = notification_rules_item_data.to_dict()
            notification_rules.append(notification_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notification_rules": notification_rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.on_call_notification_rule_public_v2 import (
            OnCallNotificationRulePublicV2,
        )

        d = dict(src_dict)
        notification_rules = []
        _notification_rules = d.pop("notification_rules")
        for notification_rules_item_data in _notification_rules:
            notification_rules_item = OnCallNotificationRulePublicV2.from_dict(
                notification_rules_item_data
            )

            notification_rules.append(notification_rules_item)

        users_list_notification_rules_result_v2 = cls(
            notification_rules=notification_rules,
        )

        users_list_notification_rules_result_v2.additional_properties = d
        return users_list_notification_rules_result_v2

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
