from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_rotation_handover_v2_interval_type import (
    ScheduleRotationHandoverV2IntervalType,
)

T = TypeVar("T", bound="ScheduleRotationHandoverV2")


@_attrs_define(kw_only=True)
class ScheduleRotationHandoverV2:
    """
    Example:
        {'interval': 1, 'interval_type': 'hourly'}

    Attributes:
        interval (int):  Example: 1.
        interval_type (ScheduleRotationHandoverV2IntervalType): How often a handover occurs Example: hourly.
    """

    interval: int
    interval_type: ScheduleRotationHandoverV2IntervalType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval = self.interval

        interval_type = self.interval_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interval": interval,
                "interval_type": interval_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        interval = d.pop("interval")

        interval_type = ScheduleRotationHandoverV2IntervalType(d.pop("interval_type"))

        schedule_rotation_handover_v2 = cls(
            interval=interval,
            interval_type=interval_type,
        )

        schedule_rotation_handover_v2.additional_properties = d
        return schedule_rotation_handover_v2

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
