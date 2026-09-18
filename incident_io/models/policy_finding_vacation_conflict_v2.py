from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyFindingVacationConflictV2")


@_attrs_define
class PolicyFindingVacationConflictV2:
    """Set when policy_type is vacation_conflict. Someone is on call while on holiday.

    Example:
        {'end_at': '2021-08-17T13:28:57.801578Z', 'holiday_name': 'Joe Bloggs - Holiday', 'rotation_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'start_at':
            '2021-08-17T13:28:57.801578Z', 'user_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        end_at (datetime.datetime): When the conflict ends Example: 2021-08-17T13:28:57.801578Z.
        schedule_id (str): The schedule the holiday conflicts with Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        start_at (datetime.datetime): When the conflict starts Example: 2021-08-17T13:28:57.801578Z.
        user_id (str): The user on holiday Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        holiday_name (str | Unset): What the holiday is called in the external system Example: Joe Bloggs - Holiday.
        rotation_id (str | Unset): The rotation the holiday conflicts with Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    end_at: datetime.datetime
    schedule_id: str
    start_at: datetime.datetime
    user_id: str
    holiday_name: str | Unset = UNSET
    rotation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_at = self.end_at.isoformat()

        schedule_id = self.schedule_id

        start_at = self.start_at.isoformat()

        user_id = self.user_id

        holiday_name = self.holiday_name

        rotation_id = self.rotation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_at": end_at,
                "schedule_id": schedule_id,
                "start_at": start_at,
                "user_id": user_id,
            }
        )
        if holiday_name is not UNSET:
            field_dict["holiday_name"] = holiday_name
        if rotation_id is not UNSET:
            field_dict["rotation_id"] = rotation_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        schedule_id = d.pop("schedule_id")

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        user_id = d.pop("user_id")

        holiday_name = d.pop("holiday_name", UNSET)

        rotation_id = d.pop("rotation_id", UNSET)

        policy_finding_vacation_conflict_v2 = cls(
            end_at=end_at,
            schedule_id=schedule_id,
            start_at=start_at,
            user_id=user_id,
            holiday_name=holiday_name,
            rotation_id=rotation_id,
        )

        policy_finding_vacation_conflict_v2.additional_properties = d
        return policy_finding_vacation_conflict_v2

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
