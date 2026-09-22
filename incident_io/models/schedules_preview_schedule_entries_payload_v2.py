from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_update_payload_v2 import ScheduleUpdatePayloadV2


T = TypeVar("T", bound="SchedulesPreviewScheduleEntriesPayloadV2")


@_attrs_define(kw_only=True)
class SchedulesPreviewScheduleEntriesPayloadV2:
    """
    Example:
        {'entry_window_end': '2021-01-08T00:00:00Z', 'entry_window_start': '2021-01-01T00:00:00Z', 'schedule':
            {'annotations': {'incident.io/terraform/version': 'version-of-terraform'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z',
            'handovers': [{'interval': 1, 'interval_type': 'hourly'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'My Rotation', 'scheduling_mode': 'fair', 'users':
            [{'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}],
            'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}], 'working_intervals':
            [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}, 'holidays_public_config':
            {'country_codes': ['abc123']}, 'name': 'Primary On-call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'],
            'timezone': 'America/Los_Angeles'}}

    Attributes:
        schedule (ScheduleUpdatePayloadV2):  Example: {'annotations': {'incident.io/terraform/version': 'version-of-
            terraform'}, 'config': {'rotations': [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'hourly'}], 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'My
            Rotation', 'scheduling_mode': 'fair', 'users': [{'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}], 'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}], 'working_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]},
            'holidays_public_config': {'country_codes': ['abc123']}, 'name': 'Primary On-call Schedule', 'team_ids':
            ['01JPQA75EPNEES4479P16P4XAB'], 'timezone': 'America/Los_Angeles'}.
        entry_window_end (datetime.datetime | Unset): The end of the window to preview entries for. Defaults to four
            weeks after entry_window_start. Example: 2021-01-08T00:00:00Z.
        entry_window_start (datetime.datetime | Unset): The start of the window to preview entries for. Defaults to now.
            Example: 2021-01-01T00:00:00Z.
    """

    schedule: ScheduleUpdatePayloadV2
    entry_window_end: datetime.datetime | Unset = UNSET
    entry_window_start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule = self.schedule.to_dict()

        entry_window_end: str | Unset = UNSET
        if not isinstance(self.entry_window_end, Unset):
            entry_window_end = self.entry_window_end.isoformat()

        entry_window_start: str | Unset = UNSET
        if not isinstance(self.entry_window_start, Unset):
            entry_window_start = self.entry_window_start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule": schedule,
            }
        )
        if entry_window_end is not UNSET:
            field_dict["entry_window_end"] = entry_window_end
        if entry_window_start is not UNSET:
            field_dict["entry_window_start"] = entry_window_start

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_update_payload_v2 import (
            ScheduleUpdatePayloadV2,
        )

        d = dict(src_dict)
        schedule = ScheduleUpdatePayloadV2.from_dict(d.pop("schedule"))

        _entry_window_end = d.pop("entry_window_end", UNSET)
        entry_window_end: datetime.datetime | Unset
        if isinstance(_entry_window_end, Unset):
            entry_window_end = UNSET
        else:
            entry_window_end = datetime.datetime.fromisoformat(_entry_window_end)

        _entry_window_start = d.pop("entry_window_start", UNSET)
        entry_window_start: datetime.datetime | Unset
        if isinstance(_entry_window_start, Unset):
            entry_window_start = UNSET
        else:
            entry_window_start = datetime.datetime.fromisoformat(_entry_window_start)

        schedules_preview_schedule_entries_payload_v2 = cls(
            schedule=schedule,
            entry_window_end=entry_window_end,
            entry_window_start=entry_window_start,
        )

        schedules_preview_schedule_entries_payload_v2.additional_properties = d
        return schedules_preview_schedule_entries_payload_v2

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
