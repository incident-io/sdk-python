from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleSlimV2")


@_attrs_define(kw_only=True)
class ScheduleSlimV2:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call
            Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'timezone': 'Europe/London', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        id (str): Unique internal ID of the schedule Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        name (str): Human readable name synced from external provider Example: Primary On-Call Schedule.
        timezone (str): Timezone of the schedule, as interpreted at the point of generating the report Example:
            Europe/London.
        updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        team_ids (list[str] | Unset): IDs of teams that own this schedule Example: ['01JPQA75EPNEES4479P16P4XAB'].
    """

    created_at: datetime.datetime
    id: str
    name: str
    timezone: str
    updated_at: datetime.datetime
    team_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        timezone = self.timezone

        updated_at = self.updated_at.isoformat()

        team_ids: list[str] | Unset = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "name": name,
                "timezone": timezone,
                "updated_at": updated_at,
            }
        )
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        timezone = d.pop("timezone")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        team_ids = cast(list[str], d.pop("team_ids", UNSET))

        schedule_slim_v2 = cls(
            created_at=created_at,
            id=id,
            name=name,
            timezone=timezone,
            updated_at=updated_at,
            team_ids=team_ids,
        )

        schedule_slim_v2.additional_properties = d
        return schedule_slim_v2

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
