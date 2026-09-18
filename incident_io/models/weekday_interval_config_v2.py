from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.weekday_interval_v2 import WeekdayIntervalV2


T = TypeVar("T", bound="WeekdayIntervalConfigV2")


@_attrs_define
class WeekdayIntervalConfigV2:
    """
    Example:
        {'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123', 'weekday_intervals': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'monday'}]}

    Attributes:
        id (str): The unique identifier for this set of working intervals Example: abc123.
        name (str): A human readable label for this set of working intervals Example: abc123.
        timezone (str): How to interpret all the intervals Example: abc123.
        weekday_intervals (list[WeekdayIntervalV2]):  Example: [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}].
    """

    id: str
    name: str
    timezone: str
    weekday_intervals: list[WeekdayIntervalV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        timezone = self.timezone

        weekday_intervals = []
        for weekday_intervals_item_data in self.weekday_intervals:
            weekday_intervals_item = weekday_intervals_item_data.to_dict()
            weekday_intervals.append(weekday_intervals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "timezone": timezone,
                "weekday_intervals": weekday_intervals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.weekday_interval_v2 import WeekdayIntervalV2

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        timezone = d.pop("timezone")

        weekday_intervals = []
        _weekday_intervals = d.pop("weekday_intervals")
        for weekday_intervals_item_data in _weekday_intervals:
            weekday_intervals_item = WeekdayIntervalV2.from_dict(
                weekday_intervals_item_data
            )

            weekday_intervals.append(weekday_intervals_item)

        weekday_interval_config_v2 = cls(
            id=id,
            name=name,
            timezone=timezone,
            weekday_intervals=weekday_intervals,
        )

        weekday_interval_config_v2.additional_properties = d
        return weekday_interval_config_v2

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
