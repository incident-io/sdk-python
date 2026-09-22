from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pay_configs_create_payload_v2_rate_time_unit import (
    PayConfigsCreatePayloadV2RateTimeUnit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pay_config_one_off_rule_payload_v2 import PayConfigOneOffRulePayloadV2
    from ..models.pay_config_weekly_rule_payload_v2 import PayConfigWeeklyRulePayloadV2


T = TypeVar("T", bound="PayConfigsCreatePayloadV2")


@_attrs_define(kw_only=True)
class PayConfigsCreatePayloadV2:
    """
    Example:
        {'base_rate_cents': 1200, 'currency': 'GBP', 'name': 'Engineering on-call', 'one_off_rules': [{'end_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day', 'rate_cents': 4800,
            'start_at': '2021-08-17T13:28:57.801578Z'}], 'rate_time_unit': 'hour', 'timezone': 'Europe/London',
            'weekly_rules': [{'end_time': '17:00', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400, 'start_time':
            '09:00', 'weekdays': ['monday']}]}

    Attributes:
        base_rate_cents (int): Rate paid for any time no rule covers, in the lowest denomination of the currency
            Example: 1200.
        currency (str): Currency this config pays in, in ISO 4217 format Example: GBP.
        name (str): Human readable name for this pay config Example: Engineering on-call.
        rate_time_unit (PayConfigsCreatePayloadV2RateTimeUnit): The unit of time every rate on this config is quoted per
            Example: hour.
        timezone (str): IANA timezone this config's rules are interpreted in Example: Europe/London.
        one_off_rules (list[PayConfigOneOffRulePayloadV2] | Unset): Rules that apply over a single window of time
            Example: [{'end_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day',
            'rate_cents': 4800, 'start_at': '2021-08-17T13:28:57.801578Z'}].
        weekly_rules (list[PayConfigWeeklyRulePayloadV2] | Unset): Rules that apply every week, in the order they should
            be evaluated Example: [{'end_time': '17:00', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400,
            'start_time': '09:00', 'weekdays': ['monday']}].
    """

    base_rate_cents: int
    currency: str
    name: str
    rate_time_unit: PayConfigsCreatePayloadV2RateTimeUnit
    timezone: str
    one_off_rules: list[PayConfigOneOffRulePayloadV2] | Unset = UNSET
    weekly_rules: list[PayConfigWeeklyRulePayloadV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_rate_cents = self.base_rate_cents

        currency = self.currency

        name = self.name

        rate_time_unit = self.rate_time_unit.value

        timezone = self.timezone

        one_off_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.one_off_rules, Unset):
            one_off_rules = []
            for one_off_rules_item_data in self.one_off_rules:
                one_off_rules_item = one_off_rules_item_data.to_dict()
                one_off_rules.append(one_off_rules_item)

        weekly_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.weekly_rules, Unset):
            weekly_rules = []
            for weekly_rules_item_data in self.weekly_rules:
                weekly_rules_item = weekly_rules_item_data.to_dict()
                weekly_rules.append(weekly_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_rate_cents": base_rate_cents,
                "currency": currency,
                "name": name,
                "rate_time_unit": rate_time_unit,
                "timezone": timezone,
            }
        )
        if one_off_rules is not UNSET:
            field_dict["one_off_rules"] = one_off_rules
        if weekly_rules is not UNSET:
            field_dict["weekly_rules"] = weekly_rules

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pay_config_one_off_rule_payload_v2 import (
            PayConfigOneOffRulePayloadV2,
        )
        from ..models.pay_config_weekly_rule_payload_v2 import (
            PayConfigWeeklyRulePayloadV2,
        )

        d = dict(src_dict)
        base_rate_cents = d.pop("base_rate_cents")

        currency = d.pop("currency")

        name = d.pop("name")

        rate_time_unit = PayConfigsCreatePayloadV2RateTimeUnit(d.pop("rate_time_unit"))

        timezone = d.pop("timezone")

        _one_off_rules = d.pop("one_off_rules", UNSET)
        one_off_rules: list[PayConfigOneOffRulePayloadV2] | Unset = UNSET
        if _one_off_rules is not UNSET:
            one_off_rules = []
            for one_off_rules_item_data in _one_off_rules:
                one_off_rules_item = PayConfigOneOffRulePayloadV2.from_dict(
                    one_off_rules_item_data
                )

                one_off_rules.append(one_off_rules_item)

        _weekly_rules = d.pop("weekly_rules", UNSET)
        weekly_rules: list[PayConfigWeeklyRulePayloadV2] | Unset = UNSET
        if _weekly_rules is not UNSET:
            weekly_rules = []
            for weekly_rules_item_data in _weekly_rules:
                weekly_rules_item = PayConfigWeeklyRulePayloadV2.from_dict(
                    weekly_rules_item_data
                )

                weekly_rules.append(weekly_rules_item)

        pay_configs_create_payload_v2 = cls(
            base_rate_cents=base_rate_cents,
            currency=currency,
            name=name,
            rate_time_unit=rate_time_unit,
            timezone=timezone,
            one_off_rules=one_off_rules,
            weekly_rules=weekly_rules,
        )

        pay_configs_create_payload_v2.additional_properties = d
        return pay_configs_create_payload_v2

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
