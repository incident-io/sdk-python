from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2
    from ..models.pay_report_v2 import PayReportV2


T = TypeVar("T", bound="PayReportsListResultV2")


@_attrs_define(kw_only=True)
class PayReportsListResultV2:
    """
    Example:
        {'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}, 'pay_reports': [{'created_at':
            '2026-04-01T09:00:00Z', 'creator': {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}},
            'end_date': '2026-03-31', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'March 2026', 'overlapping_shifts':
            'paid_per_schedule', 'published_at': '2026-04-01T09:00:00Z', 'schedule_ids': ['01FCNDV6P870EA6S7TK1DSYDG0'],
            'start_date': '2026-03-01', 'status': 'complete', 'total_duration_seconds': 3600, 'total_pay_by_currency':
            {'GBP': 2400}, 'unpaid_shifts': 'included', 'updated_at': '2026-04-01T09:00:00Z'}]}

    Attributes:
        pagination_meta (PaginationMetaResultV2):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
        pay_reports (list[PayReportV2]):  Example: [{'created_at': '2026-04-01T09:00:00Z', 'creator': {'api_key': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}}, 'end_date': '2026-03-31', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'March 2026', 'overlapping_shifts': 'paid_per_schedule', 'published_at':
            '2026-04-01T09:00:00Z', 'schedule_ids': ['01FCNDV6P870EA6S7TK1DSYDG0'], 'start_date': '2026-03-01', 'status':
            'complete', 'total_duration_seconds': 3600, 'total_pay_by_currency': {'GBP': 2400}, 'unpaid_shifts': 'included',
            'updated_at': '2026-04-01T09:00:00Z'}].
    """

    pagination_meta: PaginationMetaResultV2
    pay_reports: list[PayReportV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination_meta = self.pagination_meta.to_dict()

        pay_reports = []
        for pay_reports_item_data in self.pay_reports:
            pay_reports_item = pay_reports_item_data.to_dict()
            pay_reports.append(pay_reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination_meta": pagination_meta,
                "pay_reports": pay_reports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )
        from ..models.pay_report_v2 import PayReportV2

        d = dict(src_dict)
        pagination_meta = PaginationMetaResultV2.from_dict(d.pop("pagination_meta"))

        pay_reports = []
        _pay_reports = d.pop("pay_reports")
        for pay_reports_item_data in _pay_reports:
            pay_reports_item = PayReportV2.from_dict(pay_reports_item_data)

            pay_reports.append(pay_reports_item)

        pay_reports_list_result_v2 = cls(
            pagination_meta=pagination_meta,
            pay_reports=pay_reports,
        )

        pay_reports_list_result_v2.additional_properties = d
        return pay_reports_list_result_v2

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
