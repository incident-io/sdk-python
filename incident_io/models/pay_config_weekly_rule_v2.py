from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pay_config_weekly_rule_v2_weekdays_item import (
    PayConfigWeeklyRuleV2WeekdaysItem,
)

T = TypeVar("T", bound="PayConfigWeeklyRuleV2")


@_attrs_define
class PayConfigWeeklyRuleV2:
    """A rule that applies every week, over the same days and hours.

    Example:
        {'end_time': '17:00', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400, 'start_time': '09:00', 'weekdays':
            ['monday']}

    Attributes:
        end_time (str): Time of day this rule ends, in 24 hour format. Equal to start_time means it runs for the whole
            day. Example: 17:00.
        id (str): Unique identifier for this rule, stable across edits to the config Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        rate_cents (int): Rate paid while this rule applies, in the lowest denomination of the config's currency
            Example: 2400.
        start_time (str): Time of day this rule starts, in 24 hour format Example: 09:00.
        weekdays (list[PayConfigWeeklyRuleV2WeekdaysItem]): Days of the week this rule applies on Example: ['monday'].
    """

    end_time: str
    id: str
    rate_cents: int
    start_time: str
    weekdays: list[PayConfigWeeklyRuleV2WeekdaysItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time = self.end_time

        id = self.id

        rate_cents = self.rate_cents

        start_time = self.start_time

        weekdays = []
        for weekdays_item_data in self.weekdays:
            weekdays_item = weekdays_item_data.value
            weekdays.append(weekdays_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_time": end_time,
                "id": id,
                "rate_cents": rate_cents,
                "start_time": start_time,
                "weekdays": weekdays,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        end_time = d.pop("end_time")

        id = d.pop("id")

        rate_cents = d.pop("rate_cents")

        start_time = d.pop("start_time")

        weekdays = []
        _weekdays = d.pop("weekdays")
        for weekdays_item_data in _weekdays:
            weekdays_item = PayConfigWeeklyRuleV2WeekdaysItem(weekdays_item_data)

            weekdays.append(weekdays_item)

        pay_config_weekly_rule_v2 = cls(
            end_time=end_time,
            id=id,
            rate_cents=rate_cents,
            start_time=start_time,
            weekdays=weekdays,
        )

        pay_config_weekly_rule_v2.additional_properties = d
        return pay_config_weekly_rule_v2

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
