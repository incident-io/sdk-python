from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_rotation_working_interval_create_payload_v2_weekday import (
    ScheduleRotationWorkingIntervalCreatePayloadV2Weekday,
)

T = TypeVar("T", bound="ScheduleRotationWorkingIntervalCreatePayloadV2")


@_attrs_define(kw_only=True)
class ScheduleRotationWorkingIntervalCreatePayloadV2:
    """
    Example:
        {'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}

    Attributes:
        end_time (str): End time of the interval, in 24hr format Example: 17:00.
        start_time (str): Start time of the interval, in 24hr format Example: 09:00.
        weekday (ScheduleRotationWorkingIntervalCreatePayloadV2Weekday): Weekdays for use with a schedule Example:
            monday.
    """

    end_time: str
    start_time: str
    weekday: ScheduleRotationWorkingIntervalCreatePayloadV2Weekday
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time = self.end_time

        start_time = self.start_time

        weekday = self.weekday.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_time": end_time,
                "start_time": start_time,
                "weekday": weekday,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        end_time = d.pop("end_time")

        start_time = d.pop("start_time")

        weekday = ScheduleRotationWorkingIntervalCreatePayloadV2Weekday(
            d.pop("weekday")
        )

        schedule_rotation_working_interval_create_payload_v2 = cls(
            end_time=end_time,
            start_time=start_time,
            weekday=weekday,
        )

        schedule_rotation_working_interval_create_payload_v2.additional_properties = d
        return schedule_rotation_working_interval_create_payload_v2

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
