from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_rotation_v2 import ScheduleRotationV2


T = TypeVar("T", bound="ScheduleConfigV2")


@_attrs_define
class ScheduleConfigV2:
    """
    Example:
        {'rotations': [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'hourly'}], 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name':
            'Primary On-Call Schedule', 'scheduling_mode': 'fair', 'users': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}],
            'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}], 'working_intervals':
            [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}

    Attributes:
        rotations (list[ScheduleRotationV2]): Rotas in this schedule Example: [{'effective_from':
            '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1,
            'interval_type': 'hourly'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'Primary On-Call Schedule', 'scheduling_mode': 'fair', 'users': [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}], 'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}], 'working_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}].
    """

    rotations: list[ScheduleRotationV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rotations = []
        for rotations_item_data in self.rotations:
            rotations_item = rotations_item_data.to_dict()
            rotations.append(rotations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rotations": rotations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_rotation_v2 import ScheduleRotationV2

        d = dict(src_dict)
        rotations = []
        _rotations = d.pop("rotations")
        for rotations_item_data in _rotations:
            rotations_item = ScheduleRotationV2.from_dict(rotations_item_data)

            rotations.append(rotations_item)

        schedule_config_v2 = cls(
            rotations=rotations,
        )

        schedule_config_v2.additional_properties = d
        return schedule_config_v2

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
