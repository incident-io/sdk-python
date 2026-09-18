from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ScheduleEntryV2")


@_attrs_define
class ScheduleEntryV2:
    """A single shift on a schedule, representing who is on-call between a start
    and end time. When present, `rotation_id` and `layer_id` tell you which
    rotation and which layer within that rotation the entry belongs to. A
    schedule may have multiple rotations (for example, a primary and a secondary
    rotation) and each rotation can be made up of several layers — entries are
    returned for every rotation and layer on the schedule.

    Entries come from two places: they are either generated from a schedule's
    rotation configuration (the regular pattern of who is on-call) or created by
    an override (a one-off change that replaces the normal rotation for a period
    of time). When you call the List schedule entries endpoint we return both
    kinds separately, along with the merged `final` schedule that reflects what
    will actually happen.

    `entry_id` is only populated for entries that correspond to a stored
    record. Scheduled entries are projections computed from the rotation rules
    on the fly and don't have a persisted ID, so `entry_id` will be absent for
    those. Use `fingerprint` if you need a stable identifier to deduplicate or
    diff a shift across requests.

        Example:
            {'end_at': '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
                'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
                'U02AYNF2XJM'}}

        Attributes:
            end_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            start_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            entry_id (str | Unset): Unique identifier of the schedule entry Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
            fingerprint (str | Unset): A unique identifier for this entry, used to determine a unique shift Example:
                01G0J1EXE7AXZ2C93K61WBPYEH.
            layer_id (str | Unset): If present, the layer this entry applies to on the rotation Example:
                01G0J1EXE7AXZ2C93K61WBPYNH.
            rotation_id (str | Unset): If present, the rotation this entry applies to on the schedule Example:
                01G0J1EXE7AXZ2C93K61WBPYEH.
            user (UserV2 | Unset):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
                Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
    """

    end_at: datetime.datetime
    start_at: datetime.datetime
    entry_id: str | Unset = UNSET
    fingerprint: str | Unset = UNSET
    layer_id: str | Unset = UNSET
    rotation_id: str | Unset = UNSET
    user: UserV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_at = self.end_at.isoformat()

        start_at = self.start_at.isoformat()

        entry_id = self.entry_id

        fingerprint = self.fingerprint

        layer_id = self.layer_id

        rotation_id = self.rotation_id

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_at": end_at,
                "start_at": start_at,
            }
        )
        if entry_id is not UNSET:
            field_dict["entry_id"] = entry_id
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if layer_id is not UNSET:
            field_dict["layer_id"] = layer_id
        if rotation_id is not UNSET:
            field_dict["rotation_id"] = rotation_id
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        entry_id = d.pop("entry_id", UNSET)

        fingerprint = d.pop("fingerprint", UNSET)

        layer_id = d.pop("layer_id", UNSET)

        rotation_id = d.pop("rotation_id", UNSET)

        _user = d.pop("user", UNSET)
        user: UserV2 | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserV2.from_dict(_user)

        schedule_entry_v2 = cls(
            end_at=end_at,
            start_at=start_at,
            entry_id=entry_id,
            fingerprint=fingerprint,
            layer_id=layer_id,
            rotation_id=rotation_id,
            user=user,
        )

        schedule_entry_v2.additional_properties = d
        return schedule_entry_v2

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
