from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pay_config_weekly_rule_v2 import PayConfigWeeklyRuleV2


T = TypeVar("T", bound="PayConfigsListWeeklyRulesResultV2")


@_attrs_define(kw_only=True)
class PayConfigsListWeeklyRulesResultV2:
    """
    Example:
        {'weekly_rules': [{'end_time': '17:00', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400, 'start_time':
            '09:00', 'weekdays': ['monday']}]}

    Attributes:
        weekly_rules (list[PayConfigWeeklyRuleV2]):  Example: [{'end_time': '17:00', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'rate_cents': 2400, 'start_time': '09:00', 'weekdays': ['monday']}].
    """

    weekly_rules: list[PayConfigWeeklyRuleV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weekly_rules = []
        for weekly_rules_item_data in self.weekly_rules:
            weekly_rules_item = weekly_rules_item_data.to_dict()
            weekly_rules.append(weekly_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "weekly_rules": weekly_rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pay_config_weekly_rule_v2 import (
            PayConfigWeeklyRuleV2,
        )

        d = dict(src_dict)
        weekly_rules = []
        _weekly_rules = d.pop("weekly_rules")
        for weekly_rules_item_data in _weekly_rules:
            weekly_rules_item = PayConfigWeeklyRuleV2.from_dict(weekly_rules_item_data)

            weekly_rules.append(weekly_rules_item)

        pay_configs_list_weekly_rules_result_v2 = cls(
            weekly_rules=weekly_rules,
        )

        pay_configs_list_weekly_rules_result_v2.additional_properties = d
        return pay_configs_list_weekly_rules_result_v2

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
