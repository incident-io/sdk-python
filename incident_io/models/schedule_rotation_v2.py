from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_rotation_v2_scheduling_mode import (
    ScheduleRotationV2SchedulingMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_layer_v2 import ScheduleLayerV2
    from ..models.schedule_rotation_handover_v2 import ScheduleRotationHandoverV2
    from ..models.schedule_rotation_working_interval_v2 import (
        ScheduleRotationWorkingIntervalV2,
    )
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ScheduleRotationV2")


@_attrs_define
class ScheduleRotationV2:
    """
    Example:
        {'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z',
            'handovers': [{'interval': 1, 'interval_type': 'hourly'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'Primary On-Call Schedule', 'scheduling_mode':
            'fair', 'users': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}], 'working_interval': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'monday'}], 'working_intervals': [{'end_time': '17:00', 'start_time': '09:00',
            'weekday': 'monday'}]}

    Attributes:
        handover_start_at (datetime.datetime): Determines when shifts change hands and who takes them: the first user in
            `users` comes on shift at this time, handing over to the next user after each `handovers` interval, cycling
            through the list — for example, weekly handovers from a Monday 09:00 give week-long shifts that change hands on
            Mondays at 09:00. Example: 2021-08-17T13:28:57.801578Z.
        handovers (list[ScheduleRotationHandoverV2]): The cadence shifts hand over on. With more than one entry, the
            intervals apply in turn — for example, one day then three days produces alternating one-day and three-day
            shifts. Example: [{'interval': 1, 'interval_type': 'hourly'}].
        id (str): Unique internal ID of the rotation Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        layers (list[ScheduleLayerV2]): Controls how many people are on-call concurrently Example: [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}].
        name (str): Human readable name synced from external provider Example: Primary On-Call Schedule.
        users (list[UserV2]): The people in the rotation, in the order they take shifts. Example: [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}].
        working_intervals (list[ScheduleRotationWorkingIntervalV2]): Optional restrictions that define when to schedule
            people for this rota Example: [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}].
        effective_from (datetime.datetime | Unset): When this version of the rotation takes effect. A rotation can
            appear multiple times in `rotations` with the same `id`, scheduling changes ahead of time: each version applies
            from its `effective_from` until the next version's. A rotation's first version has no `effective_from`. Example:
            2021-08-17T13:28:57.801578Z.
        scheduling_mode (ScheduleRotationV2SchedulingMode | Unset): Scheduling algorithm to use for this rotation.
            'fair' balances workload by considering handover duration, while 'sequential' uses simple round-robin rotation
            through users. Only applies when you have asymmetric handovers (e.g., 2 days then 5 days). Example: fair.
        working_interval (list[ScheduleRotationWorkingIntervalV2] | Unset): DEPRECATED: Use working_intervals instead.
            Example: [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}].
    """

    handover_start_at: datetime.datetime
    handovers: list[ScheduleRotationHandoverV2]
    id: str
    layers: list[ScheduleLayerV2]
    name: str
    users: list[UserV2]
    working_intervals: list[ScheduleRotationWorkingIntervalV2]
    effective_from: datetime.datetime | Unset = UNSET
    scheduling_mode: ScheduleRotationV2SchedulingMode | Unset = UNSET
    working_interval: list[ScheduleRotationWorkingIntervalV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        handover_start_at = self.handover_start_at.isoformat()

        handovers = []
        for handovers_item_data in self.handovers:
            handovers_item = handovers_item_data.to_dict()
            handovers.append(handovers_item)

        id = self.id

        layers = []
        for layers_item_data in self.layers:
            layers_item = layers_item_data.to_dict()
            layers.append(layers_item)

        name = self.name

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        working_intervals = []
        for working_intervals_item_data in self.working_intervals:
            working_intervals_item = working_intervals_item_data.to_dict()
            working_intervals.append(working_intervals_item)

        effective_from: str | Unset = UNSET
        if not isinstance(self.effective_from, Unset):
            effective_from = self.effective_from.isoformat()

        scheduling_mode: str | Unset = UNSET
        if not isinstance(self.scheduling_mode, Unset):
            scheduling_mode = self.scheduling_mode.value

        working_interval: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.working_interval, Unset):
            working_interval = []
            for working_interval_item_data in self.working_interval:
                working_interval_item = working_interval_item_data.to_dict()
                working_interval.append(working_interval_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "handover_start_at": handover_start_at,
                "handovers": handovers,
                "id": id,
                "layers": layers,
                "name": name,
                "users": users,
                "working_intervals": working_intervals,
            }
        )
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from
        if scheduling_mode is not UNSET:
            field_dict["scheduling_mode"] = scheduling_mode
        if working_interval is not UNSET:
            field_dict["working_interval"] = working_interval

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_layer_v2 import ScheduleLayerV2
        from ..models.schedule_rotation_handover_v2 import (
            ScheduleRotationHandoverV2,
        )
        from ..models.schedule_rotation_working_interval_v2 import (
            ScheduleRotationWorkingIntervalV2,
        )
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        handover_start_at = datetime.datetime.fromisoformat(d.pop("handover_start_at"))

        handovers = []
        _handovers = d.pop("handovers")
        for handovers_item_data in _handovers:
            handovers_item = ScheduleRotationHandoverV2.from_dict(handovers_item_data)

            handovers.append(handovers_item)

        id = d.pop("id")

        layers = []
        _layers = d.pop("layers")
        for layers_item_data in _layers:
            layers_item = ScheduleLayerV2.from_dict(layers_item_data)

            layers.append(layers_item)

        name = d.pop("name")

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = UserV2.from_dict(users_item_data)

            users.append(users_item)

        working_intervals = []
        _working_intervals = d.pop("working_intervals")
        for working_intervals_item_data in _working_intervals:
            working_intervals_item = ScheduleRotationWorkingIntervalV2.from_dict(
                working_intervals_item_data
            )

            working_intervals.append(working_intervals_item)

        _effective_from = d.pop("effective_from", UNSET)
        effective_from: datetime.datetime | Unset
        if isinstance(_effective_from, Unset):
            effective_from = UNSET
        else:
            effective_from = datetime.datetime.fromisoformat(_effective_from)

        _scheduling_mode = d.pop("scheduling_mode", UNSET)
        scheduling_mode: ScheduleRotationV2SchedulingMode | Unset
        if isinstance(_scheduling_mode, Unset):
            scheduling_mode = UNSET
        else:
            scheduling_mode = ScheduleRotationV2SchedulingMode(_scheduling_mode)

        _working_interval = d.pop("working_interval", UNSET)
        working_interval: list[ScheduleRotationWorkingIntervalV2] | Unset = UNSET
        if _working_interval is not UNSET:
            working_interval = []
            for working_interval_item_data in _working_interval:
                working_interval_item = ScheduleRotationWorkingIntervalV2.from_dict(
                    working_interval_item_data
                )

                working_interval.append(working_interval_item)

        schedule_rotation_v2 = cls(
            handover_start_at=handover_start_at,
            handovers=handovers,
            id=id,
            layers=layers,
            name=name,
            users=users,
            working_intervals=working_intervals,
            effective_from=effective_from,
            scheduling_mode=scheduling_mode,
            working_interval=working_interval,
        )

        schedule_rotation_v2.additional_properties = d
        return schedule_rotation_v2

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
