from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_override_v2 import ScheduleOverrideV2


T = TypeVar("T", bound="SchedulesCreateOverrideResultV2")


@_attrs_define
class SchedulesCreateOverrideResultV2:
    """
    Example:
        {'override': {'created_at': '2021-08-17T13:28:57.801578Z', 'end_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'schedule_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
            '2021-08-17T13:28:57.801578Z', 'updated_at': '2021-08-17T13:28:57.801578Z', 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}}}

    Attributes:
        override (ScheduleOverrideV2):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'end_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'schedule_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
            '2021-08-17T13:28:57.801578Z', 'updated_at': '2021-08-17T13:28:57.801578Z', 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}}.
    """

    override: ScheduleOverrideV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        override = self.override.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "override": override,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_override_v2 import ScheduleOverrideV2

        d = dict(src_dict)
        override = ScheduleOverrideV2.from_dict(d.pop("override"))

        schedules_create_override_result_v2 = cls(
            override=override,
        )

        schedules_create_override_result_v2.additional_properties = d
        return schedules_create_override_result_v2

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
