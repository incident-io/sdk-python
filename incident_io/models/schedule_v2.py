from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_config_v2 import ScheduleConfigV2
    from ..models.schedule_entry_v2 import ScheduleEntryV2
    from ..models.schedule_holidays_public_config_v2 import (
        ScheduleHolidaysPublicConfigV2,
    )
    from ..models.schedule_v2_annotations import ScheduleV2Annotations


T = TypeVar("T", bound="ScheduleV2")


@_attrs_define
class ScheduleV2:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'config': {'rotations': [{'effective_from':
            '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1,
            'interval_type': 'hourly'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'Primary On-Call Schedule', 'scheduling_mode': 'fair', 'users': [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}], 'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}], 'working_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]},
            'created_at': '2021-08-17T13:28:57.801578Z', 'current_shifts': [{'end_at': '2021-08-17T13:28:57.801578Z',
            'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id':
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
            '2021-08-17T13:28:57.801578Z'}

    Attributes:
        annotations (ScheduleV2Annotations): Annotations that track metadata about this resource Example:
            {'incident.io/terraform/version': '3.0.0'}.
        created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        id (str): Unique internal ID of the schedule Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        name (str): Human readable name synced from external provider Example: Primary On-Call Schedule.
        permalink (str): A permanent link to this schedule in the incident.io dashboard Example:
            https://app.incident.io/acme/on-call/schedules/01G0J1EXE7AXZ2C93K61WBPYEH.
        team_ids (list[str]): IDs of teams that own this schedule Example: ['01JPQA75EPNEES4479P16P4XAB'].
        timezone (str): Timezone of the schedule, as interpreted at the point of generating the report Example:
            Europe/London.
        updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        config (ScheduleConfigV2 | Unset):  Example: {'rotations': [{'effective_from': '2021-08-17T13:28:57.801578Z',
            'handover_start_at': '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'hourly'}],
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name':
            'Primary On-Call Schedule', 'scheduling_mode': 'fair', 'users': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}],
            'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}], 'working_intervals':
            [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}.
        current_shifts (list[ScheduleEntryV2] | Unset): Shifts that are ongoing for this schedule Example: [{'end_at':
            '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
            'U02AYNF2XJM'}}].
        holidays_public_config (ScheduleHolidaysPublicConfigV2 | Unset):  Example: {'country_codes': ['GB', 'FR']}.
        next_shifts (list[ScheduleEntryV2] | Unset): The shifts after the next changeover. Note that on the list
            schedules endpoint, this will always be empty if the page size requested is greater than 25. Example:
            [{'end_at': '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
            'U02AYNF2XJM'}}].
    """

    annotations: ScheduleV2Annotations
    created_at: datetime.datetime
    id: str
    name: str
    permalink: str
    team_ids: list[str]
    timezone: str
    updated_at: datetime.datetime
    config: ScheduleConfigV2 | Unset = UNSET
    current_shifts: list[ScheduleEntryV2] | Unset = UNSET
    holidays_public_config: ScheduleHolidaysPublicConfigV2 | Unset = UNSET
    next_shifts: list[ScheduleEntryV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations = self.annotations.to_dict()

        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        permalink = self.permalink

        team_ids = self.team_ids

        timezone = self.timezone

        updated_at = self.updated_at.isoformat()

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        current_shifts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.current_shifts, Unset):
            current_shifts = []
            for current_shifts_item_data in self.current_shifts:
                current_shifts_item = current_shifts_item_data.to_dict()
                current_shifts.append(current_shifts_item)

        holidays_public_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.holidays_public_config, Unset):
            holidays_public_config = self.holidays_public_config.to_dict()

        next_shifts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.next_shifts, Unset):
            next_shifts = []
            for next_shifts_item_data in self.next_shifts:
                next_shifts_item = next_shifts_item_data.to_dict()
                next_shifts.append(next_shifts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annotations": annotations,
                "created_at": created_at,
                "id": id,
                "name": name,
                "permalink": permalink,
                "team_ids": team_ids,
                "timezone": timezone,
                "updated_at": updated_at,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if current_shifts is not UNSET:
            field_dict["current_shifts"] = current_shifts
        if holidays_public_config is not UNSET:
            field_dict["holidays_public_config"] = holidays_public_config
        if next_shifts is not UNSET:
            field_dict["next_shifts"] = next_shifts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_config_v2 import ScheduleConfigV2
        from ..models.schedule_entry_v2 import ScheduleEntryV2
        from ..models.schedule_holidays_public_config_v2 import (
            ScheduleHolidaysPublicConfigV2,
        )
        from ..models.schedule_v2_annotations import (
            ScheduleV2Annotations,
        )

        d = dict(src_dict)
        annotations = ScheduleV2Annotations.from_dict(d.pop("annotations"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        permalink = d.pop("permalink")

        team_ids = cast(list[str], d.pop("team_ids"))

        timezone = d.pop("timezone")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _config = d.pop("config", UNSET)
        config: ScheduleConfigV2 | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ScheduleConfigV2.from_dict(_config)

        _current_shifts = d.pop("current_shifts", UNSET)
        current_shifts: list[ScheduleEntryV2] | Unset = UNSET
        if _current_shifts is not UNSET:
            current_shifts = []
            for current_shifts_item_data in _current_shifts:
                current_shifts_item = ScheduleEntryV2.from_dict(
                    current_shifts_item_data
                )

                current_shifts.append(current_shifts_item)

        _holidays_public_config = d.pop("holidays_public_config", UNSET)
        holidays_public_config: ScheduleHolidaysPublicConfigV2 | Unset
        if isinstance(_holidays_public_config, Unset):
            holidays_public_config = UNSET
        else:
            holidays_public_config = ScheduleHolidaysPublicConfigV2.from_dict(
                _holidays_public_config
            )

        _next_shifts = d.pop("next_shifts", UNSET)
        next_shifts: list[ScheduleEntryV2] | Unset = UNSET
        if _next_shifts is not UNSET:
            next_shifts = []
            for next_shifts_item_data in _next_shifts:
                next_shifts_item = ScheduleEntryV2.from_dict(next_shifts_item_data)

                next_shifts.append(next_shifts_item)

        schedule_v2 = cls(
            annotations=annotations,
            created_at=created_at,
            id=id,
            name=name,
            permalink=permalink,
            team_ids=team_ids,
            timezone=timezone,
            updated_at=updated_at,
            config=config,
            current_shifts=current_shifts,
            holidays_public_config=holidays_public_config,
            next_shifts=next_shifts,
        )

        schedule_v2.additional_properties = d
        return schedule_v2

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
