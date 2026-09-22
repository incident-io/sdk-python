from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2
    from ..models.pay_config_v2 import PayConfigV2


T = TypeVar("T", bound="PayConfigsListResultV2")


@_attrs_define(kw_only=True)
class PayConfigsListResultV2:
    """
    Example:
        {'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}, 'pay_configs':
            [{'base_rate_cents': 1200, 'created_at': '2021-08-17T13:28:57.801578Z', 'currency': 'GBP', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Engineering on-call', 'one_off_rules': [{'end_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day', 'rate_cents': 4800,
            'start_at': '2021-08-17T13:28:57.801578Z'}], 'published_at': '2021-08-17T13:28:57.801578Z', 'rate_time_unit':
            'hour', 'timezone': 'Europe/London', 'updated_at': '2021-08-17T13:28:57.801578Z', 'weekly_rules': [{'end_time':
            '17:00', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400, 'start_time': '09:00', 'weekdays':
            ['monday']}]}]}

    Attributes:
        pagination_meta (PaginationMetaResultV2):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
        pay_configs (list[PayConfigV2]):  Example: [{'base_rate_cents': 1200, 'created_at':
            '2021-08-17T13:28:57.801578Z', 'currency': 'GBP', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Engineering on-
            call', 'one_off_rules': [{'end_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name':
            'Christmas day', 'rate_cents': 4800, 'start_at': '2021-08-17T13:28:57.801578Z'}], 'published_at':
            '2021-08-17T13:28:57.801578Z', 'rate_time_unit': 'hour', 'timezone': 'Europe/London', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'weekly_rules': [{'end_time': '17:00', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'rate_cents': 2400, 'start_time': '09:00', 'weekdays': ['monday']}]}].
    """

    pagination_meta: PaginationMetaResultV2
    pay_configs: list[PayConfigV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination_meta = self.pagination_meta.to_dict()

        pay_configs = []
        for pay_configs_item_data in self.pay_configs:
            pay_configs_item = pay_configs_item_data.to_dict()
            pay_configs.append(pay_configs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination_meta": pagination_meta,
                "pay_configs": pay_configs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )
        from ..models.pay_config_v2 import PayConfigV2

        d = dict(src_dict)
        pagination_meta = PaginationMetaResultV2.from_dict(d.pop("pagination_meta"))

        pay_configs = []
        _pay_configs = d.pop("pay_configs")
        for pay_configs_item_data in _pay_configs:
            pay_configs_item = PayConfigV2.from_dict(pay_configs_item_data)

            pay_configs.append(pay_configs_item)

        pay_configs_list_result_v2 = cls(
            pagination_meta=pagination_meta,
            pay_configs=pay_configs,
        )

        pay_configs_list_result_v2.additional_properties = d
        return pay_configs_list_result_v2

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
