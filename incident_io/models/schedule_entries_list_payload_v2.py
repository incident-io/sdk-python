from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_entry_v2 import ScheduleEntryV2


T = TypeVar("T", bound="ScheduleEntriesListPayloadV2")


@_attrs_define(kw_only=True)
class ScheduleEntriesListPayloadV2:
    """The schedule entries for a window of time, grouped by where they come from.

    `scheduled` are the entries produced by the schedule's rotation rules before
    any overrides are taken into account. `overrides` are the one-off changes that
    apply within the window. `final` is the effective schedule after overrides
    have been merged in — this is normally the list to use when working out who
    is on-call.

        Example:
            {'final': [{'end_at': '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
                'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
                'U02AYNF2XJM'}}], 'overrides': [{'end_at': '2021-08-17T13:28:57.801578Z', 'entry_id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id':
                '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
                '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
                'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}}], 'scheduled': [{'end_at':
                '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
                'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
                'U02AYNF2XJM'}}]}

        Attributes:
            final (list[ScheduleEntryV2]): The effective schedule after overrides have been merged in Example: [{'end_at':
                '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
                'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
                'U02AYNF2XJM'}}].
            overrides (list[ScheduleEntryV2]): Overrides that apply within the requested window Example: [{'end_at':
                '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
                'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
                'U02AYNF2XJM'}}].
            scheduled (list[ScheduleEntryV2]): Entries from the schedule's rotation rules, before overrides are applied
                Example: [{'end_at': '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
                'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
                'U02AYNF2XJM'}}].
    """

    final: list[ScheduleEntryV2]
    overrides: list[ScheduleEntryV2]
    scheduled: list[ScheduleEntryV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        final = []
        for final_item_data in self.final:
            final_item = final_item_data.to_dict()
            final.append(final_item)

        overrides = []
        for overrides_item_data in self.overrides:
            overrides_item = overrides_item_data.to_dict()
            overrides.append(overrides_item)

        scheduled = []
        for scheduled_item_data in self.scheduled:
            scheduled_item = scheduled_item_data.to_dict()
            scheduled.append(scheduled_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "final": final,
                "overrides": overrides,
                "scheduled": scheduled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_entry_v2 import ScheduleEntryV2

        d = dict(src_dict)
        final = []
        _final = d.pop("final")
        for final_item_data in _final:
            final_item = ScheduleEntryV2.from_dict(final_item_data)

            final.append(final_item)

        overrides = []
        _overrides = d.pop("overrides")
        for overrides_item_data in _overrides:
            overrides_item = ScheduleEntryV2.from_dict(overrides_item_data)

            overrides.append(overrides_item)

        scheduled = []
        _scheduled = d.pop("scheduled")
        for scheduled_item_data in _scheduled:
            scheduled_item = ScheduleEntryV2.from_dict(scheduled_item_data)

            scheduled.append(scheduled_item)

        schedule_entries_list_payload_v2 = cls(
            final=final,
            overrides=overrides,
            scheduled=scheduled,
        )

        schedule_entries_list_payload_v2.additional_properties = d
        return schedule_entries_list_payload_v2

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
