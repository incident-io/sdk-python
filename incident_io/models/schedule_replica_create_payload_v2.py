from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_replica_create_payload_v2_replica_provider import (
    ScheduleReplicaCreatePayloadV2ReplicaProvider,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_replica_source_v2 import ScheduleReplicaSourceV2


T = TypeVar("T", bound="ScheduleReplicaCreatePayloadV2")


@_attrs_define(kw_only=True)
class ScheduleReplicaCreatePayloadV2:
    """
    Example:
        {'mirror_window_days': 14, 'replica_fallback_user_id': 'PA7AXXN', 'replica_provider': 'pagerduty',
            'replica_provider_id': 'PO8107X', 'sources': [{'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH'}]}

    Attributes:
        replica_fallback_user_id (str): The ID of a user in the external provider that will be assigned whenever nobody
            is on-call in the incident.io schedule. External providers typically require someone to always be on-call, so
            this user fills gaps where incident.io has no one scheduled. Example: PA7AXXN.
        replica_provider (ScheduleReplicaCreatePayloadV2ReplicaProvider): The external provider where this schedule is
            replicated to Example: pagerduty.
        replica_provider_id (str): The ID of the schedule in the external provider that this replica syncs to. For
            PagerDuty this is the schedule ID (e.g. PO8107X), for Opsgenie the schedule ID, and for Jira Service Management
            the schedule ID. Example: PO8107X.
        sources (list[ScheduleReplicaSourceV2]): The specific rotation and layer combinations from the schedule to
            replicate. Each source identifies a single layer within a rotation to sync to the external provider. Example:
            [{'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}].
        mirror_window_days (int | Unset): How many days ahead to mirror this schedule into the external provider.
            Defaults to 14 if not set; maximum 90. Example: 14.
    """

    replica_fallback_user_id: str
    replica_provider: ScheduleReplicaCreatePayloadV2ReplicaProvider
    replica_provider_id: str
    sources: list[ScheduleReplicaSourceV2]
    mirror_window_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replica_fallback_user_id = self.replica_fallback_user_id

        replica_provider = self.replica_provider.value

        replica_provider_id = self.replica_provider_id

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        mirror_window_days = self.mirror_window_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "replica_fallback_user_id": replica_fallback_user_id,
                "replica_provider": replica_provider,
                "replica_provider_id": replica_provider_id,
                "sources": sources,
            }
        )
        if mirror_window_days is not UNSET:
            field_dict["mirror_window_days"] = mirror_window_days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_replica_source_v2 import (
            ScheduleReplicaSourceV2,
        )

        d = dict(src_dict)
        replica_fallback_user_id = d.pop("replica_fallback_user_id")

        replica_provider = ScheduleReplicaCreatePayloadV2ReplicaProvider(
            d.pop("replica_provider")
        )

        replica_provider_id = d.pop("replica_provider_id")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = ScheduleReplicaSourceV2.from_dict(sources_item_data)

            sources.append(sources_item)

        mirror_window_days = d.pop("mirror_window_days", UNSET)

        schedule_replica_create_payload_v2 = cls(
            replica_fallback_user_id=replica_fallback_user_id,
            replica_provider=replica_provider,
            replica_provider_id=replica_provider_id,
            sources=sources,
            mirror_window_days=mirror_window_days,
        )

        schedule_replica_create_payload_v2.additional_properties = d
        return schedule_replica_create_payload_v2

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
