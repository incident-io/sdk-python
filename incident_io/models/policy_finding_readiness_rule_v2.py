from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_finding_readiness_rule_v2_method_types_item import (
    PolicyFindingReadinessRuleV2MethodTypesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyFindingReadinessRuleV2")


@_attrs_define
class PolicyFindingReadinessRuleV2:
    """
    Example:
        {'max_delay_seconds': 300, 'met': False, 'method_types': ['slack']}

    Attributes:
        met (bool): Whether the user's notification rules satisfy this one Example: False.
        method_types (list[PolicyFindingReadinessRuleV2MethodTypesItem]):  Example: ['slack'].
        max_delay_seconds (int | Unset): How quickly the method must fire to count Example: 300.
    """

    met: bool
    method_types: list[PolicyFindingReadinessRuleV2MethodTypesItem]
    max_delay_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        met = self.met

        method_types = []
        for method_types_item_data in self.method_types:
            method_types_item = method_types_item_data.value
            method_types.append(method_types_item)

        max_delay_seconds = self.max_delay_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "met": met,
                "method_types": method_types,
            }
        )
        if max_delay_seconds is not UNSET:
            field_dict["max_delay_seconds"] = max_delay_seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        met = d.pop("met")

        method_types = []
        _method_types = d.pop("method_types")
        for method_types_item_data in _method_types:
            method_types_item = PolicyFindingReadinessRuleV2MethodTypesItem(
                method_types_item_data
            )

            method_types.append(method_types_item)

        max_delay_seconds = d.pop("max_delay_seconds", UNSET)

        policy_finding_readiness_rule_v2 = cls(
            met=met,
            method_types=method_types,
            max_delay_seconds=max_delay_seconds,
        )

        policy_finding_readiness_rule_v2.additional_properties = d
        return policy_finding_readiness_rule_v2

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
