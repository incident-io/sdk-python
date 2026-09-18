from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pay_config_one_off_rule_v2 import PayConfigOneOffRuleV2


T = TypeVar("T", bound="PayConfigsListOneOffRulesResultV2")


@_attrs_define
class PayConfigsListOneOffRulesResultV2:
    """
    Example:
        {'one_off_rules': [{'end_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name':
            'Christmas day', 'rate_cents': 4800, 'start_at': '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        one_off_rules (list[PayConfigOneOffRuleV2]):  Example: [{'end_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day', 'rate_cents': 4800, 'start_at':
            '2021-08-17T13:28:57.801578Z'}].
    """

    one_off_rules: list[PayConfigOneOffRuleV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        one_off_rules = []
        for one_off_rules_item_data in self.one_off_rules:
            one_off_rules_item = one_off_rules_item_data.to_dict()
            one_off_rules.append(one_off_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "one_off_rules": one_off_rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pay_config_one_off_rule_v2 import (
            PayConfigOneOffRuleV2,
        )

        d = dict(src_dict)
        one_off_rules = []
        _one_off_rules = d.pop("one_off_rules")
        for one_off_rules_item_data in _one_off_rules:
            one_off_rules_item = PayConfigOneOffRuleV2.from_dict(
                one_off_rules_item_data
            )

            one_off_rules.append(one_off_rules_item)

        pay_configs_list_one_off_rules_result_v2 = cls(
            one_off_rules=one_off_rules,
        )

        pay_configs_list_one_off_rules_result_v2.additional_properties = d
        return pay_configs_list_one_off_rules_result_v2

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
