from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pay_configs_update_payload_v2_rate_time_unit import (
    PayConfigsUpdatePayloadV2RateTimeUnit,
)

T = TypeVar("T", bound="PayConfigsUpdatePayloadV2")


@_attrs_define
class PayConfigsUpdatePayloadV2:
    """
    Example:
        {'base_rate_cents': 1200, 'currency': 'GBP', 'name': 'Engineering on-call', 'rate_time_unit': 'hour',
            'timezone': 'Europe/London'}

    Attributes:
        base_rate_cents (int): Rate paid for any time no rule covers, in the lowest denomination of the currency
            Example: 1200.
        currency (str): Currency this config pays in, in ISO 4217 format Example: GBP.
        name (str): Human readable name for this pay config Example: Engineering on-call.
        rate_time_unit (PayConfigsUpdatePayloadV2RateTimeUnit): The unit of time every rate on this config is quoted
            per. Pay is pro-rated by the second either way. Example: hour.
        timezone (str): IANA timezone this config's rules are interpreted in Example: Europe/London.
    """

    base_rate_cents: int
    currency: str
    name: str
    rate_time_unit: PayConfigsUpdatePayloadV2RateTimeUnit
    timezone: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_rate_cents = self.base_rate_cents

        currency = self.currency

        name = self.name

        rate_time_unit = self.rate_time_unit.value

        timezone = self.timezone

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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        base_rate_cents = d.pop("base_rate_cents")

        currency = d.pop("currency")

        name = d.pop("name")

        rate_time_unit = PayConfigsUpdatePayloadV2RateTimeUnit(d.pop("rate_time_unit"))

        timezone = d.pop("timezone")

        pay_configs_update_payload_v2 = cls(
            base_rate_cents=base_rate_cents,
            currency=currency,
            name=name,
            rate_time_unit=rate_time_unit,
            timezone=timezone,
        )

        pay_configs_update_payload_v2.additional_properties = d
        return pay_configs_update_payload_v2

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
