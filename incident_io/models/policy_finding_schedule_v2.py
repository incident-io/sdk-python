from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_finding_schedule_v2_cause import PolicyFindingScheduleV2Cause
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_finding_schedule_impacted_user_v2 import (
        PolicyFindingScheduleImpactedUserV2,
    )


T = TypeVar("T", bound="PolicyFindingScheduleV2")


@_attrs_define(kw_only=True)
class PolicyFindingScheduleV2:
    """Set when policy_type is schedule. Describes a gap in on-call cover.

    Example:
        {'cause': 'nobody_scheduled', 'end_at': '2021-08-17T13:28:57.801578Z', 'has_unscheduled_time': True,
            'impacted_users': [{'cause': 'no_on_call_seat', 'name': 'Alice Green', 'user_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}], 'rotation_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'start_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        end_at (datetime.datetime): When the gap ends Example: 2021-08-17T13:28:57.801578Z.
        schedule_id (str): The schedule with the gap Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        start_at (datetime.datetime): When the gap starts Example: 2021-08-17T13:28:57.801578Z.
        cause (PolicyFindingScheduleV2Cause | Unset): Why the gap exists Example: nobody_scheduled.
        has_unscheduled_time (bool | Unset): Whether part of the gap has nobody scheduled at all, so impacted_users
            doesn't fully explain it Example: True.
        impacted_users (list[PolicyFindingScheduleImpactedUserV2] | Unset): Users scheduled across the gap whose entries
            don't count as cover Example: [{'cause': 'no_on_call_seat', 'name': 'Alice Green', 'user_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}].
        rotation_id (str | Unset): The rotation with the gap, when the policy evaluates per rotation Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
    """

    end_at: datetime.datetime
    schedule_id: str
    start_at: datetime.datetime
    cause: PolicyFindingScheduleV2Cause | Unset = UNSET
    has_unscheduled_time: bool | Unset = UNSET
    impacted_users: list[PolicyFindingScheduleImpactedUserV2] | Unset = UNSET
    rotation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_at = self.end_at.isoformat()

        schedule_id = self.schedule_id

        start_at = self.start_at.isoformat()

        cause: str | Unset = UNSET
        if not isinstance(self.cause, Unset):
            cause = self.cause.value

        has_unscheduled_time = self.has_unscheduled_time

        impacted_users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.impacted_users, Unset):
            impacted_users = []
            for impacted_users_item_data in self.impacted_users:
                impacted_users_item = impacted_users_item_data.to_dict()
                impacted_users.append(impacted_users_item)

        rotation_id = self.rotation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_at": end_at,
                "schedule_id": schedule_id,
                "start_at": start_at,
            }
        )
        if cause is not UNSET:
            field_dict["cause"] = cause
        if has_unscheduled_time is not UNSET:
            field_dict["has_unscheduled_time"] = has_unscheduled_time
        if impacted_users is not UNSET:
            field_dict["impacted_users"] = impacted_users
        if rotation_id is not UNSET:
            field_dict["rotation_id"] = rotation_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.policy_finding_schedule_impacted_user_v2 import (
            PolicyFindingScheduleImpactedUserV2,
        )

        d = dict(src_dict)
        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        schedule_id = d.pop("schedule_id")

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        _cause = d.pop("cause", UNSET)
        cause: PolicyFindingScheduleV2Cause | Unset
        if isinstance(_cause, Unset):
            cause = UNSET
        else:
            cause = PolicyFindingScheduleV2Cause(_cause)

        has_unscheduled_time = d.pop("has_unscheduled_time", UNSET)

        _impacted_users = d.pop("impacted_users", UNSET)
        impacted_users: list[PolicyFindingScheduleImpactedUserV2] | Unset = UNSET
        if _impacted_users is not UNSET:
            impacted_users = []
            for impacted_users_item_data in _impacted_users:
                impacted_users_item = PolicyFindingScheduleImpactedUserV2.from_dict(
                    impacted_users_item_data
                )

                impacted_users.append(impacted_users_item)

        rotation_id = d.pop("rotation_id", UNSET)

        policy_finding_schedule_v2 = cls(
            end_at=end_at,
            schedule_id=schedule_id,
            start_at=start_at,
            cause=cause,
            has_unscheduled_time=has_unscheduled_time,
            impacted_users=impacted_users,
            rotation_id=rotation_id,
        )

        policy_finding_schedule_v2.additional_properties = d
        return policy_finding_schedule_v2

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
