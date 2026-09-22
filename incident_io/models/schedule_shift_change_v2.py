from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_slim_v2 import ScheduleSlimV2
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ScheduleShiftChangeV2")


@_attrs_define(kw_only=True)
class ScheduleShiftChangeV2:
    """
    Example:
        {'current_users': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}], 'previous_users': [{'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
            'U02AYNF2XJM'}], 'schedule': {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Primary On-Call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'timezone': 'Europe/London',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        current_users (list[UserV2]): Users who are now on-call (empty array if shift ending) Example: [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}].
        previous_users (list[UserV2]): Users who were previously on-call (empty array if shift starting) Example:
            [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}].
        schedule (ScheduleSlimV2):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'],
            'timezone': 'Europe/London', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    current_users: list[UserV2]
    previous_users: list[UserV2]
    schedule: ScheduleSlimV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_users = []
        for current_users_item_data in self.current_users:
            current_users_item = current_users_item_data.to_dict()
            current_users.append(current_users_item)

        previous_users = []
        for previous_users_item_data in self.previous_users:
            previous_users_item = previous_users_item_data.to_dict()
            previous_users.append(previous_users_item)

        schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_users": current_users,
                "previous_users": previous_users,
                "schedule": schedule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_slim_v2 import ScheduleSlimV2
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        current_users = []
        _current_users = d.pop("current_users")
        for current_users_item_data in _current_users:
            current_users_item = UserV2.from_dict(current_users_item_data)

            current_users.append(current_users_item)

        previous_users = []
        _previous_users = d.pop("previous_users")
        for previous_users_item_data in _previous_users:
            previous_users_item = UserV2.from_dict(previous_users_item_data)

            previous_users.append(previous_users_item)

        schedule = ScheduleSlimV2.from_dict(d.pop("schedule"))

        schedule_shift_change_v2 = cls(
            current_users=current_users,
            previous_users=previous_users,
            schedule=schedule,
        )

        schedule_shift_change_v2.additional_properties = d
        return schedule_shift_change_v2

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
