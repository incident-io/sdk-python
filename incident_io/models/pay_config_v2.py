from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pay_config_v2_rate_time_unit import PayConfigV2RateTimeUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pay_config_one_off_rule_v2 import PayConfigOneOffRuleV2
    from ..models.pay_config_weekly_rule_v2 import PayConfigWeeklyRuleV2


T = TypeVar("T", bound="PayConfigV2")


@_attrs_define
class PayConfigV2:
    """A pay config sets what someone is paid for being on call: a base rate,
    plus rules that override it at particular times. An on-call pay report prices
    each person's shifts against one.

    Rules are evaluated in the order they are returned, and the first one that
    covers a shift wins. Any time no rule covers is paid at the base rate.

        Example:
            {'base_rate_cents': 1200, 'created_at': '2021-08-17T13:28:57.801578Z', 'currency': 'GBP', 'id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Engineering on-call', 'one_off_rules': [{'end_at':
                '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day', 'rate_cents': 4800,
                'start_at': '2021-08-17T13:28:57.801578Z'}], 'published_at': '2021-08-17T13:28:57.801578Z', 'rate_time_unit':
                'hour', 'timezone': 'Europe/London', 'updated_at': '2021-08-17T13:28:57.801578Z', 'weekly_rules': [{'end_time':
                '17:00', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400, 'start_time': '09:00', 'weekdays':
                ['monday']}]}

        Attributes:
            base_rate_cents (int): Rate paid for any time no rule covers, in the lowest denomination of the currency
                Example: 1200.
            created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            currency (str): Currency this config pays in, in ISO 4217 format Example: GBP.
            id (str): Unique identifier for this pay config Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
            name (str): Human readable name for this pay config Example: Engineering on-call.
            one_off_rules (list[PayConfigOneOffRuleV2]): Rules that apply over a single window of time, such as a public
                holiday Example: [{'end_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name':
                'Christmas day', 'rate_cents': 4800, 'start_at': '2021-08-17T13:28:57.801578Z'}].
            rate_time_unit (PayConfigV2RateTimeUnit): The unit of time every rate on this config is quoted per. Pay is pro-
                rated by the second either way. Example: hour.
            timezone (str): IANA timezone this config's rules are interpreted in Example: Europe/London.
            updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            weekly_rules (list[PayConfigWeeklyRuleV2]): Rules that apply every week, by day of week and time of day, in
                evaluation order Example: [{'end_time': '17:00', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400,
                'start_time': '09:00', 'weekdays': ['monday']}].
            published_at (datetime.datetime | Unset): When a published report first priced against this config. Once set,
                editing the config needs the schedule_pay_configs.update_published scope. Example: 2021-08-17T13:28:57.801578Z.
    """

    base_rate_cents: int
    created_at: datetime.datetime
    currency: str
    id: str
    name: str
    one_off_rules: list[PayConfigOneOffRuleV2]
    rate_time_unit: PayConfigV2RateTimeUnit
    timezone: str
    updated_at: datetime.datetime
    weekly_rules: list[PayConfigWeeklyRuleV2]
    published_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_rate_cents = self.base_rate_cents

        created_at = self.created_at.isoformat()

        currency = self.currency

        id = self.id

        name = self.name

        one_off_rules = []
        for one_off_rules_item_data in self.one_off_rules:
            one_off_rules_item = one_off_rules_item_data.to_dict()
            one_off_rules.append(one_off_rules_item)

        rate_time_unit = self.rate_time_unit.value

        timezone = self.timezone

        updated_at = self.updated_at.isoformat()

        weekly_rules = []
        for weekly_rules_item_data in self.weekly_rules:
            weekly_rules_item = weekly_rules_item_data.to_dict()
            weekly_rules.append(weekly_rules_item)

        published_at: str | Unset = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_rate_cents": base_rate_cents,
                "created_at": created_at,
                "currency": currency,
                "id": id,
                "name": name,
                "one_off_rules": one_off_rules,
                "rate_time_unit": rate_time_unit,
                "timezone": timezone,
                "updated_at": updated_at,
                "weekly_rules": weekly_rules,
            }
        )
        if published_at is not UNSET:
            field_dict["published_at"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pay_config_one_off_rule_v2 import (
            PayConfigOneOffRuleV2,
        )
        from ..models.pay_config_weekly_rule_v2 import (
            PayConfigWeeklyRuleV2,
        )

        d = dict(src_dict)
        base_rate_cents = d.pop("base_rate_cents")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        currency = d.pop("currency")

        id = d.pop("id")

        name = d.pop("name")

        one_off_rules = []
        _one_off_rules = d.pop("one_off_rules")
        for one_off_rules_item_data in _one_off_rules:
            one_off_rules_item = PayConfigOneOffRuleV2.from_dict(
                one_off_rules_item_data
            )

            one_off_rules.append(one_off_rules_item)

        rate_time_unit = PayConfigV2RateTimeUnit(d.pop("rate_time_unit"))

        timezone = d.pop("timezone")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        weekly_rules = []
        _weekly_rules = d.pop("weekly_rules")
        for weekly_rules_item_data in _weekly_rules:
            weekly_rules_item = PayConfigWeeklyRuleV2.from_dict(weekly_rules_item_data)

            weekly_rules.append(weekly_rules_item)

        _published_at = d.pop("published_at", UNSET)
        published_at: datetime.datetime | Unset
        if isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = datetime.datetime.fromisoformat(_published_at)

        pay_config_v2 = cls(
            base_rate_cents=base_rate_cents,
            created_at=created_at,
            currency=currency,
            id=id,
            name=name,
            one_off_rules=one_off_rules,
            rate_time_unit=rate_time_unit,
            timezone=timezone,
            updated_at=updated_at,
            weekly_rules=weekly_rules,
            published_at=published_at,
        )

        pay_config_v2.additional_properties = d
        return pay_config_v2

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
