from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_replica_v2 import ScheduleReplicaV2


T = TypeVar("T", bound="SchedulesShowScheduleReplicaResultV2")


@_attrs_define(kw_only=True)
class SchedulesShowScheduleReplicaResultV2:
    """
    Example:
        {'schedule_replica': {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'last_sync_error': 'Failed to find external user for Milly', 'last_synced_at': '2023-11-07T13:33:30Z',
            'mirror_window_days': 14, 'replica_fallback_user_id': 'PA7AXXN', 'replica_provider': 'pagerduty',
            'replica_provider_id': 'PO8107X', 'schedule_id': '01FDAG4SAP5TYPT98WGR2N7W91', 'sources': [{'layer_id':
            '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}], 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'user_statuses': [{'external_user_id': 'PJYTRGS', 'user_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH'}]}}

    Attributes:
        schedule_replica (ScheduleReplicaV2):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'last_sync_error': 'Failed to find external user for Milly', 'last_synced_at':
            '2023-11-07T13:33:30Z', 'mirror_window_days': 14, 'replica_fallback_user_id': 'PA7AXXN', 'replica_provider':
            'pagerduty', 'replica_provider_id': 'PO8107X', 'schedule_id': '01FDAG4SAP5TYPT98WGR2N7W91', 'sources':
            [{'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}], 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'user_statuses': [{'external_user_id': 'PJYTRGS', 'user_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH'}]}.
    """

    schedule_replica: ScheduleReplicaV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_replica = self.schedule_replica.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_replica": schedule_replica,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_replica_v2 import ScheduleReplicaV2

        d = dict(src_dict)
        schedule_replica = ScheduleReplicaV2.from_dict(d.pop("schedule_replica"))

        schedules_show_schedule_replica_result_v2 = cls(
            schedule_replica=schedule_replica,
        )

        schedules_show_schedule_replica_result_v2.additional_properties = d
        return schedules_show_schedule_replica_result_v2

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
