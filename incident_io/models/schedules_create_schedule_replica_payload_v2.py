from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_replica_create_payload_v2 import (
        ScheduleReplicaCreatePayloadV2,
    )


T = TypeVar("T", bound="SchedulesCreateScheduleReplicaPayloadV2")


@_attrs_define(kw_only=True)
class SchedulesCreateScheduleReplicaPayloadV2:
    """
    Example:
        {'schedule_replica': {'mirror_window_days': 14, 'replica_fallback_user_id': 'PA7AXXN', 'replica_provider':
            'pagerduty', 'replica_provider_id': 'PO8107X', 'sources': [{'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH',
            'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}]}}

    Attributes:
        schedule_replica (ScheduleReplicaCreatePayloadV2):  Example: {'mirror_window_days': 14,
            'replica_fallback_user_id': 'PA7AXXN', 'replica_provider': 'pagerduty', 'replica_provider_id': 'PO8107X',
            'sources': [{'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}]}.
    """

    schedule_replica: ScheduleReplicaCreatePayloadV2
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
        from ..models.schedule_replica_create_payload_v2 import (
            ScheduleReplicaCreatePayloadV2,
        )

        d = dict(src_dict)
        schedule_replica = ScheduleReplicaCreatePayloadV2.from_dict(
            d.pop("schedule_replica")
        )

        schedules_create_schedule_replica_payload_v2 = cls(
            schedule_replica=schedule_replica,
        )

        schedules_create_schedule_replica_payload_v2.additional_properties = d
        return schedules_create_schedule_replica_payload_v2

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
