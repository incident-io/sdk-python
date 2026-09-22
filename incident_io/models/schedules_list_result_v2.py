from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_meta_result_with_total_v2 import (
        PaginationMetaResultWithTotalV2,
    )
    from ..models.schedule_v2 import ScheduleV2


T = TypeVar("T", bound="SchedulesListResultV2")


@_attrs_define(kw_only=True)
class SchedulesListResultV2:
    """
    Example:
        {'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25, 'total_record_count': 238},
            'schedules': [{'annotations': {'incident.io/terraform/version': '3.0.0'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z',
            'handovers': [{'interval': 1, 'interval_type': 'hourly'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'Primary On-Call Schedule', 'scheduling_mode':
            'fair', 'users': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}], 'working_interval': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'monday'}], 'working_intervals': [{'end_time': '17:00', 'start_time': '09:00',
            'weekday': 'monday'}]}]}, 'created_at': '2021-08-17T13:28:57.801578Z', 'current_shifts': [{'end_at':
            '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
            'U02AYNF2XJM'}}], 'holidays_public_config': {'country_codes': ['GB', 'FR']}, 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Primary On-Call Schedule', 'next_shifts': [{'end_at': '2021-08-17T13:28:57.801578Z', 'entry_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id':
            '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
            '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}}], 'permalink':
            'https://app.incident.io/acme/on-call/schedules/01G0J1EXE7AXZ2C93K61WBPYEH', 'team_ids':
            ['01JPQA75EPNEES4479P16P4XAB'], 'timezone': 'Europe/London', 'updated_at': '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        schedules (list[ScheduleV2]):  Example: [{'annotations': {'incident.io/terraform/version': '3.0.0'}, 'config':
            {'rotations': [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'hourly'}], 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name':
            'Primary On-Call Schedule', 'scheduling_mode': 'fair', 'users': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}],
            'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}], 'working_intervals':
            [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}, 'created_at':
            '2021-08-17T13:28:57.801578Z', 'current_shifts': [{'end_at': '2021-08-17T13:28:57.801578Z', 'entry_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id':
            '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
            '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}}], 'holidays_public_config':
            {'country_codes': ['GB', 'FR']}, 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule',
            'next_shifts': [{'end_at': '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'fingerprint': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
            'U02AYNF2XJM'}}], 'permalink': 'https://app.incident.io/acme/on-call/schedules/01G0J1EXE7AXZ2C93K61WBPYEH',
            'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'timezone': 'Europe/London', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}].
        pagination_meta (PaginationMetaResultWithTotalV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0',
            'page_size': 25, 'total_record_count': 238}.
    """

    schedules: list[ScheduleV2]
    pagination_meta: PaginationMetaResultWithTotalV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedules = []
        for schedules_item_data in self.schedules:
            schedules_item = schedules_item_data.to_dict()
            schedules.append(schedules_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedules": schedules,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_meta_result_with_total_v2 import (
            PaginationMetaResultWithTotalV2,
        )
        from ..models.schedule_v2 import ScheduleV2

        d = dict(src_dict)
        schedules = []
        _schedules = d.pop("schedules")
        for schedules_item_data in _schedules:
            schedules_item = ScheduleV2.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultWithTotalV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultWithTotalV2.from_dict(
                _pagination_meta
            )

        schedules_list_result_v2 = cls(
            schedules=schedules,
            pagination_meta=pagination_meta,
        )

        schedules_list_result_v2.additional_properties = d
        return schedules_list_result_v2

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
