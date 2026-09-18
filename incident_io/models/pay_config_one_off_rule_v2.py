from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PayConfigOneOffRuleV2")


@_attrs_define
class PayConfigOneOffRuleV2:
    """A rule that applies over a single window of time, such as a public holiday. One-off rules take precedence over
    weekly rules, and may not overlap each other.

        Example:
            {'end_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day',
                'rate_cents': 4800, 'start_at': '2021-08-17T13:28:57.801578Z'}

        Attributes:
            end_at (datetime.datetime): When this rule stops applying Example: 2021-08-17T13:28:57.801578Z.
            id (str): Unique identifier for this rule, stable across edits to the config Example:
                01G0J1EXE7AXZ2C93K61WBPYEH.
            name (str): Human readable name for this rule Example: Christmas day.
            rate_cents (int): Rate paid while this rule applies, in the lowest denomination of the config's currency
                Example: 4800.
            start_at (datetime.datetime): When this rule starts applying Example: 2021-08-17T13:28:57.801578Z.
    """

    end_at: datetime.datetime
    id: str
    name: str
    rate_cents: int
    start_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_at = self.end_at.isoformat()

        id = self.id

        name = self.name

        rate_cents = self.rate_cents

        start_at = self.start_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_at": end_at,
                "id": id,
                "name": name,
                "rate_cents": rate_cents,
                "start_at": start_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        id = d.pop("id")

        name = d.pop("name")

        rate_cents = d.pop("rate_cents")

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        pay_config_one_off_rule_v2 = cls(
            end_at=end_at,
            id=id,
            name=name,
            rate_cents=rate_cents,
            start_at=start_at,
        )

        pay_config_one_off_rule_v2.additional_properties = d
        return pay_config_one_off_rule_v2

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
