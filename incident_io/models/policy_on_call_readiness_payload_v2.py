from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_on_call_readiness_payload_v2_enforcement import (
    PolicyOnCallReadinessPayloadV2Enforcement,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_readiness_rule_v2 import PolicyReadinessRuleV2


T = TypeVar("T", bound="PolicyOnCallReadinessPayloadV2")


@_attrs_define(kw_only=True)
class PolicyOnCallReadinessPayloadV2:
    """Set when policy_type is on_call_readiness. The assignee is always the user the finding is about and cannot be
    configured.

        Example:
            {'enforcement': 'advisory', 'high_interruption_level': [{'max_delay_seconds': 300, 'method_types': ['slack']}],
                'high_urgency': [{'max_delay_seconds': 300, 'method_types': ['slack']}], 'low_interruption_level':
                [{'max_delay_seconds': 300, 'method_types': ['slack']}], 'low_urgency': [{'max_delay_seconds': 300,
                'method_types': ['slack']}]}

        Attributes:
            enforcement (PolicyOnCallReadinessPayloadV2Enforcement | Unset): advisory reports only; blocking also prevents
                users saving non-compliant notification rules. Defaults to advisory. Example: advisory.
            high_interruption_level (list[PolicyReadinessRuleV2] | Unset): The high interruption level rules the policy
                requires. Example: [{'max_delay_seconds': 300, 'method_types': ['slack']}].
            high_urgency (list[PolicyReadinessRuleV2] | Unset): Deprecated: use high_interruption_level, which always has
                the same value. Example: [{'max_delay_seconds': 300, 'method_types': ['slack']}].
            low_interruption_level (list[PolicyReadinessRuleV2] | Unset): The low interruption level rules the policy
                requires. Example: [{'max_delay_seconds': 300, 'method_types': ['slack']}].
            low_urgency (list[PolicyReadinessRuleV2] | Unset): Deprecated: use low_interruption_level, which always has the
                same value. Example: [{'max_delay_seconds': 300, 'method_types': ['slack']}].
    """

    enforcement: PolicyOnCallReadinessPayloadV2Enforcement | Unset = UNSET
    high_interruption_level: list[PolicyReadinessRuleV2] | Unset = UNSET
    high_urgency: list[PolicyReadinessRuleV2] | Unset = UNSET
    low_interruption_level: list[PolicyReadinessRuleV2] | Unset = UNSET
    low_urgency: list[PolicyReadinessRuleV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enforcement: str | Unset = UNSET
        if not isinstance(self.enforcement, Unset):
            enforcement = self.enforcement.value

        high_interruption_level: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.high_interruption_level, Unset):
            high_interruption_level = []
            for high_interruption_level_item_data in self.high_interruption_level:
                high_interruption_level_item = (
                    high_interruption_level_item_data.to_dict()
                )
                high_interruption_level.append(high_interruption_level_item)

        high_urgency: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.high_urgency, Unset):
            high_urgency = []
            for high_urgency_item_data in self.high_urgency:
                high_urgency_item = high_urgency_item_data.to_dict()
                high_urgency.append(high_urgency_item)

        low_interruption_level: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.low_interruption_level, Unset):
            low_interruption_level = []
            for low_interruption_level_item_data in self.low_interruption_level:
                low_interruption_level_item = low_interruption_level_item_data.to_dict()
                low_interruption_level.append(low_interruption_level_item)

        low_urgency: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.low_urgency, Unset):
            low_urgency = []
            for low_urgency_item_data in self.low_urgency:
                low_urgency_item = low_urgency_item_data.to_dict()
                low_urgency.append(low_urgency_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enforcement is not UNSET:
            field_dict["enforcement"] = enforcement
        if high_interruption_level is not UNSET:
            field_dict["high_interruption_level"] = high_interruption_level
        if high_urgency is not UNSET:
            field_dict["high_urgency"] = high_urgency
        if low_interruption_level is not UNSET:
            field_dict["low_interruption_level"] = low_interruption_level
        if low_urgency is not UNSET:
            field_dict["low_urgency"] = low_urgency

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.policy_readiness_rule_v2 import (
            PolicyReadinessRuleV2,
        )

        d = dict(src_dict)
        _enforcement = d.pop("enforcement", UNSET)
        enforcement: PolicyOnCallReadinessPayloadV2Enforcement | Unset
        if isinstance(_enforcement, Unset):
            enforcement = UNSET
        else:
            enforcement = PolicyOnCallReadinessPayloadV2Enforcement(_enforcement)

        _high_interruption_level = d.pop("high_interruption_level", UNSET)
        high_interruption_level: list[PolicyReadinessRuleV2] | Unset = UNSET
        if _high_interruption_level is not UNSET:
            high_interruption_level = []
            for high_interruption_level_item_data in _high_interruption_level:
                high_interruption_level_item = PolicyReadinessRuleV2.from_dict(
                    high_interruption_level_item_data
                )

                high_interruption_level.append(high_interruption_level_item)

        _high_urgency = d.pop("high_urgency", UNSET)
        high_urgency: list[PolicyReadinessRuleV2] | Unset = UNSET
        if _high_urgency is not UNSET:
            high_urgency = []
            for high_urgency_item_data in _high_urgency:
                high_urgency_item = PolicyReadinessRuleV2.from_dict(
                    high_urgency_item_data
                )

                high_urgency.append(high_urgency_item)

        _low_interruption_level = d.pop("low_interruption_level", UNSET)
        low_interruption_level: list[PolicyReadinessRuleV2] | Unset = UNSET
        if _low_interruption_level is not UNSET:
            low_interruption_level = []
            for low_interruption_level_item_data in _low_interruption_level:
                low_interruption_level_item = PolicyReadinessRuleV2.from_dict(
                    low_interruption_level_item_data
                )

                low_interruption_level.append(low_interruption_level_item)

        _low_urgency = d.pop("low_urgency", UNSET)
        low_urgency: list[PolicyReadinessRuleV2] | Unset = UNSET
        if _low_urgency is not UNSET:
            low_urgency = []
            for low_urgency_item_data in _low_urgency:
                low_urgency_item = PolicyReadinessRuleV2.from_dict(
                    low_urgency_item_data
                )

                low_urgency.append(low_urgency_item)

        policy_on_call_readiness_payload_v2 = cls(
            enforcement=enforcement,
            high_interruption_level=high_interruption_level,
            high_urgency=high_urgency,
            low_interruption_level=low_interruption_level,
            low_urgency=low_urgency,
        )

        policy_on_call_readiness_payload_v2.additional_properties = d
        return policy_on_call_readiness_payload_v2

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
