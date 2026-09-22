from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.policy_finding_readiness_rule_v2 import PolicyFindingReadinessRuleV2


T = TypeVar("T", bound="PolicyFindingOnCallReadinessV2")


@_attrs_define(kw_only=True)
class PolicyFindingOnCallReadinessV2:
    """Set when policy_type is on_call_readiness. The user is always the one the finding is about.

    Example:
        {'high_urgency': [{'max_delay_seconds': 300, 'met': False, 'method_types': ['slack']}], 'low_urgency':
            [{'max_delay_seconds': 300, 'met': False, 'method_types': ['slack']}], 'user_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        high_urgency (list[PolicyFindingReadinessRuleV2]): The high urgency rules the policy requires, and whether each
            was met Example: [{'max_delay_seconds': 300, 'met': False, 'method_types': ['slack']}].
        low_urgency (list[PolicyFindingReadinessRuleV2]): The low urgency rules the policy requires, and whether each
            was met Example: [{'max_delay_seconds': 300, 'met': False, 'method_types': ['slack']}].
        user_id (str): The user whose notification rules fell short Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    high_urgency: list[PolicyFindingReadinessRuleV2]
    low_urgency: list[PolicyFindingReadinessRuleV2]
    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        high_urgency = []
        for high_urgency_item_data in self.high_urgency:
            high_urgency_item = high_urgency_item_data.to_dict()
            high_urgency.append(high_urgency_item)

        low_urgency = []
        for low_urgency_item_data in self.low_urgency:
            low_urgency_item = low_urgency_item_data.to_dict()
            low_urgency.append(low_urgency_item)

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "high_urgency": high_urgency,
                "low_urgency": low_urgency,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.policy_finding_readiness_rule_v2 import (
            PolicyFindingReadinessRuleV2,
        )

        d = dict(src_dict)
        high_urgency = []
        _high_urgency = d.pop("high_urgency")
        for high_urgency_item_data in _high_urgency:
            high_urgency_item = PolicyFindingReadinessRuleV2.from_dict(
                high_urgency_item_data
            )

            high_urgency.append(high_urgency_item)

        low_urgency = []
        _low_urgency = d.pop("low_urgency")
        for low_urgency_item_data in _low_urgency:
            low_urgency_item = PolicyFindingReadinessRuleV2.from_dict(
                low_urgency_item_data
            )

            low_urgency.append(low_urgency_item)

        user_id = d.pop("user_id")

        policy_finding_on_call_readiness_v2 = cls(
            high_urgency=high_urgency,
            low_urgency=low_urgency,
            user_id=user_id,
        )

        policy_finding_on_call_readiness_v2.additional_properties = d
        return policy_finding_on_call_readiness_v2

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
