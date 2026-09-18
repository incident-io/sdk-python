from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PayReportV2TotalPayByCurrency")


@_attrs_define
class PayReportV2TotalPayByCurrency:
    """Total owed for this report, keyed by ISO 4217 currency code, in the lowest denomination of that currency. Reports
    spanning pay configs with different currencies have an entry per currency, and those totals must not be summed.
    Unset until the report is complete, and for a legacy report, which we do not summarise.

        Example:
            {'GBP': 2400}

    """

    additional_properties: dict[str, int] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pay_report_v2_total_pay_by_currency = cls()

        pay_report_v2_total_pay_by_currency.additional_properties = d
        return pay_report_v2_total_pay_by_currency

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
