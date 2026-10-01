from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.policy_finding_shift_conflict_shift_v2 import (
        PolicyFindingShiftConflictShiftV2,
    )


T = TypeVar("T", bound="PolicyFindingShiftConflictV2")


@_attrs_define(kw_only=True)
class PolicyFindingShiftConflictV2:
    """Set when policy_type is shift_conflict. Someone is on call in two or more places at once.

    Example:
        {'end_at': '2021-08-17T13:28:57.801578Z', 'shifts': [{'end_at': '2021-08-17T13:28:57.801578Z', 'layer_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'rotation_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'start_at': '2021-08-17T13:28:57.801578Z'}], 'start_at':
            '2021-08-17T13:28:57.801578Z', 'user_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        end_at (datetime.datetime): When the conflict ends Example: 2021-08-17T13:28:57.801578Z.
        shifts (list[PolicyFindingShiftConflictShiftV2]): Every shift that overlaps the conflict Example: [{'end_at':
            '2021-08-17T13:28:57.801578Z', 'layer_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'rotation_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'start_at':
            '2021-08-17T13:28:57.801578Z'}].
        start_at (datetime.datetime): When the conflict starts Example: 2021-08-17T13:28:57.801578Z.
        user_id (str): The user with overlapping shifts Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    end_at: datetime.datetime
    shifts: list[PolicyFindingShiftConflictShiftV2]
    start_at: datetime.datetime
    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_at = self.end_at.isoformat()

        shifts = []
        for shifts_item_data in self.shifts:
            shifts_item = shifts_item_data.to_dict()
            shifts.append(shifts_item)

        start_at = self.start_at.isoformat()

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_at": end_at,
                "shifts": shifts,
                "start_at": start_at,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.policy_finding_shift_conflict_shift_v2 import (
            PolicyFindingShiftConflictShiftV2,
        )

        d = dict(src_dict)
        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        shifts = []
        _shifts = d.pop("shifts")
        for shifts_item_data in _shifts:
            shifts_item = PolicyFindingShiftConflictShiftV2.from_dict(shifts_item_data)

            shifts.append(shifts_item)

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        user_id = d.pop("user_id")

        policy_finding_shift_conflict_v2 = cls(
            end_at=end_at,
            shifts=shifts,
            start_at=start_at,
            user_id=user_id,
        )

        policy_finding_shift_conflict_v2.additional_properties = d
        return policy_finding_shift_conflict_v2

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
