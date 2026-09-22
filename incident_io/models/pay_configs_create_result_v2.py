from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pay_config_v2 import PayConfigV2


T = TypeVar("T", bound="PayConfigsCreateResultV2")


@_attrs_define(kw_only=True)
class PayConfigsCreateResultV2:
    """
    Example:
        {'pay_config': {'base_rate_cents': 1200, 'created_at': '2021-08-17T13:28:57.801578Z', 'currency': 'GBP', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Engineering on-call', 'one_off_rules': [{'end_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day', 'rate_cents': 4800,
            'start_at': '2021-08-17T13:28:57.801578Z'}], 'published_at': '2021-08-17T13:28:57.801578Z', 'rate_time_unit':
            'hour', 'timezone': 'Europe/London', 'updated_at': '2021-08-17T13:28:57.801578Z', 'weekly_rules': [{'end_time':
            '17:00', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400, 'start_time': '09:00', 'weekdays':
            ['monday']}]}}

    Attributes:
        pay_config (PayConfigV2): A pay config sets what someone is paid for being on call: a base rate,
            plus rules that override it at particular times. An on-call pay report prices
            each person's shifts against one.

            Rules are evaluated in the order they are returned, and the first one that
            covers a shift wins. Any time no rule covers is paid at the base rate. Example: {'base_rate_cents': 1200,
            'created_at': '2021-08-17T13:28:57.801578Z', 'currency': 'GBP', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name':
            'Engineering on-call', 'one_off_rules': [{'end_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day', 'rate_cents': 4800, 'start_at':
            '2021-08-17T13:28:57.801578Z'}], 'published_at': '2021-08-17T13:28:57.801578Z', 'rate_time_unit': 'hour',
            'timezone': 'Europe/London', 'updated_at': '2021-08-17T13:28:57.801578Z', 'weekly_rules': [{'end_time': '17:00',
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400, 'start_time': '09:00', 'weekdays': ['monday']}]}.
    """

    pay_config: PayConfigV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pay_config = self.pay_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pay_config": pay_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pay_config_v2 import PayConfigV2

        d = dict(src_dict)
        pay_config = PayConfigV2.from_dict(d.pop("pay_config"))

        pay_configs_create_result_v2 = cls(
            pay_config=pay_config,
        )

        pay_configs_create_result_v2.additional_properties = d
        return pay_configs_create_result_v2

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
