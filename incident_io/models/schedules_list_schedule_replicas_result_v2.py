from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_replica_v2 import ScheduleReplicaV2


T = TypeVar("T", bound="SchedulesListScheduleReplicasResultV2")


@_attrs_define
class SchedulesListScheduleReplicasResultV2:
    """
    Example:
        {'schedule_replicas': [{'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'last_sync_error': 'Failed to find external user for Milly', 'last_synced_at': '2023-11-07T13:33:30Z',
            'mirror_window_days': 14, 'replica_fallback_user_id': 'PA7AXXN', 'replica_provider': 'pagerduty',
            'replica_provider_id': 'PO8107X', 'schedule_id': '01FDAG4SAP5TYPT98WGR2N7W91', 'sources': [{'layer_id':
            '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}], 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'user_statuses': [{'external_user_id': 'PJYTRGS', 'user_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH'}]}]}

    Attributes:
        schedule_replicas (list[ScheduleReplicaV2]):  Example: [{'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'last_sync_error': 'Failed to find external user for Milly', 'last_synced_at':
            '2023-11-07T13:33:30Z', 'mirror_window_days': 14, 'replica_fallback_user_id': 'PA7AXXN', 'replica_provider':
            'pagerduty', 'replica_provider_id': 'PO8107X', 'schedule_id': '01FDAG4SAP5TYPT98WGR2N7W91', 'sources':
            [{'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}], 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'user_statuses': [{'external_user_id': 'PJYTRGS', 'user_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH'}]}].
    """

    schedule_replicas: list[ScheduleReplicaV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_replicas = []
        for schedule_replicas_item_data in self.schedule_replicas:
            schedule_replicas_item = schedule_replicas_item_data.to_dict()
            schedule_replicas.append(schedule_replicas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_replicas": schedule_replicas,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_replica_v2 import ScheduleReplicaV2

        d = dict(src_dict)
        schedule_replicas = []
        _schedule_replicas = d.pop("schedule_replicas")
        for schedule_replicas_item_data in _schedule_replicas:
            schedule_replicas_item = ScheduleReplicaV2.from_dict(
                schedule_replicas_item_data
            )

            schedule_replicas.append(schedule_replicas_item)

        schedules_list_schedule_replicas_result_v2 = cls(
            schedule_replicas=schedule_replicas,
        )

        schedules_list_schedule_replicas_result_v2.additional_properties = d
        return schedules_list_schedule_replicas_result_v2

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
