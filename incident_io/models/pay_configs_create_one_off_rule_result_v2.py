from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pay_config_one_off_rule_v2 import PayConfigOneOffRuleV2


T = TypeVar("T", bound="PayConfigsCreateOneOffRuleResultV2")


@_attrs_define
class PayConfigsCreateOneOffRuleResultV2:
    """
    Example:
        {'one_off_rule': {'end_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name':
            'Christmas day', 'rate_cents': 4800, 'start_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        one_off_rule (PayConfigOneOffRuleV2): A rule that applies over a single window of time, such as a public
            holiday. One-off rules take precedence over weekly rules, and may not overlap each other. Example: {'end_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day', 'rate_cents': 4800,
            'start_at': '2021-08-17T13:28:57.801578Z'}.
    """

    one_off_rule: PayConfigOneOffRuleV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        one_off_rule = self.one_off_rule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "one_off_rule": one_off_rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pay_config_one_off_rule_v2 import (
            PayConfigOneOffRuleV2,
        )

        d = dict(src_dict)
        one_off_rule = PayConfigOneOffRuleV2.from_dict(d.pop("one_off_rule"))

        pay_configs_create_one_off_rule_result_v2 = cls(
            one_off_rule=one_off_rule,
        )

        pay_configs_create_one_off_rule_result_v2.additional_properties = d
        return pay_configs_create_one_off_rule_result_v2

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
