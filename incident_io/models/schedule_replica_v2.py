from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_replica_v2_replica_provider import (
    ScheduleReplicaV2ReplicaProvider,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_replica_source_v2 import ScheduleReplicaSourceV2
    from ..models.schedule_replica_user_status_v2 import ScheduleReplicaUserStatusV2


T = TypeVar("T", bound="ScheduleReplicaV2")


@_attrs_define(kw_only=True)
class ScheduleReplicaV2:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'last_sync_error': 'Failed to
            find external user for Milly', 'last_synced_at': '2023-11-07T13:33:30Z', 'mirror_window_days': 14,
            'replica_fallback_user_id': 'PA7AXXN', 'replica_provider': 'pagerduty', 'replica_provider_id': 'PO8107X',
            'schedule_id': '01FDAG4SAP5TYPT98WGR2N7W91', 'sources': [{'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH',
            'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}], 'updated_at': '2021-08-17T13:28:57.801578Z', 'user_statuses':
            [{'external_user_id': 'PJYTRGS', 'user_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}]}

    Attributes:
        created_at (datetime.datetime): When this schedule replica was first created Example:
            2021-08-17T13:28:57.801578Z.
        id (str): Unique identifier of the schedule replica Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        replica_fallback_user_id (str): The ID of a user in the external provider that will be assigned whenever nobody
            is on-call in the incident.io schedule. External providers typically require someone to always be on-call, so
            this user fills gaps where incident.io has no one scheduled. Example: PA7AXXN.
        replica_provider (ScheduleReplicaV2ReplicaProvider): The external provider where this schedule is replicated to
            Example: pagerduty.
        replica_provider_id (str): The ID of the schedule in the external provider that this replica syncs to. For
            PagerDuty this is the schedule ID (e.g. PO8107X), for Opsgenie the schedule ID, and for Jira Service Management
            the schedule ID. Example: PO8107X.
        schedule_id (str): The ID of the incident.io schedule that this replica is syncing from Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        sources (list[ScheduleReplicaSourceV2]): The specific rotation and layer combinations from the schedule that are
            being replicated. Each source identifies a single layer within a rotation to sync to the external provider.
            Example: [{'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}].
        updated_at (datetime.datetime): When this schedule replica was last updated Example:
            2021-08-17T13:28:57.801578Z.
        user_statuses (list[ScheduleReplicaUserStatusV2]): The mapping status of each incident.io user in the schedule
            to their corresponding user in the external provider. Users must be mapped for the replica to sync their on-call
            shifts correctly. Example: [{'external_user_id': 'PJYTRGS', 'user_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}].
        last_sync_error (str | Unset): The most recent error encountered while syncing this replica to the external
            provider, if any. Common errors include unmapped users or connectivity issues with the external provider. Null
            if the last sync was successful. Example: Failed to find external user for Milly.
        last_synced_at (datetime.datetime | Unset): When the replica was last successfully synced to the external
            provider. Null if the replica has never been successfully synced. Example: 2023-11-07T13:33:30Z.
        mirror_window_days (int | Unset): How many days ahead to mirror this schedule into the external provider.
            Defaults to 14 if not set; maximum 90. Example: 14.
    """

    created_at: datetime.datetime
    id: str
    replica_fallback_user_id: str
    replica_provider: ScheduleReplicaV2ReplicaProvider
    replica_provider_id: str
    schedule_id: str
    sources: list[ScheduleReplicaSourceV2]
    updated_at: datetime.datetime
    user_statuses: list[ScheduleReplicaUserStatusV2]
    last_sync_error: str | Unset = UNSET
    last_synced_at: datetime.datetime | Unset = UNSET
    mirror_window_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        replica_fallback_user_id = self.replica_fallback_user_id

        replica_provider = self.replica_provider.value

        replica_provider_id = self.replica_provider_id

        schedule_id = self.schedule_id

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        updated_at = self.updated_at.isoformat()

        user_statuses = []
        for user_statuses_item_data in self.user_statuses:
            user_statuses_item = user_statuses_item_data.to_dict()
            user_statuses.append(user_statuses_item)

        last_sync_error = self.last_sync_error

        last_synced_at: str | Unset = UNSET
        if not isinstance(self.last_synced_at, Unset):
            last_synced_at = self.last_synced_at.isoformat()

        mirror_window_days = self.mirror_window_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "replica_fallback_user_id": replica_fallback_user_id,
                "replica_provider": replica_provider,
                "replica_provider_id": replica_provider_id,
                "schedule_id": schedule_id,
                "sources": sources,
                "updated_at": updated_at,
                "user_statuses": user_statuses,
            }
        )
        if last_sync_error is not UNSET:
            field_dict["last_sync_error"] = last_sync_error
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at
        if mirror_window_days is not UNSET:
            field_dict["mirror_window_days"] = mirror_window_days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_replica_source_v2 import (
            ScheduleReplicaSourceV2,
        )
        from ..models.schedule_replica_user_status_v2 import (
            ScheduleReplicaUserStatusV2,
        )

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        replica_fallback_user_id = d.pop("replica_fallback_user_id")

        replica_provider = ScheduleReplicaV2ReplicaProvider(d.pop("replica_provider"))

        replica_provider_id = d.pop("replica_provider_id")

        schedule_id = d.pop("schedule_id")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = ScheduleReplicaSourceV2.from_dict(sources_item_data)

            sources.append(sources_item)

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        user_statuses = []
        _user_statuses = d.pop("user_statuses")
        for user_statuses_item_data in _user_statuses:
            user_statuses_item = ScheduleReplicaUserStatusV2.from_dict(
                user_statuses_item_data
            )

            user_statuses.append(user_statuses_item)

        last_sync_error = d.pop("last_sync_error", UNSET)

        _last_synced_at = d.pop("last_synced_at", UNSET)
        last_synced_at: datetime.datetime | Unset
        if isinstance(_last_synced_at, Unset):
            last_synced_at = UNSET
        else:
            last_synced_at = datetime.datetime.fromisoformat(_last_synced_at)

        mirror_window_days = d.pop("mirror_window_days", UNSET)

        schedule_replica_v2 = cls(
            created_at=created_at,
            id=id,
            replica_fallback_user_id=replica_fallback_user_id,
            replica_provider=replica_provider,
            replica_provider_id=replica_provider_id,
            schedule_id=schedule_id,
            sources=sources,
            updated_at=updated_at,
            user_statuses=user_statuses,
            last_sync_error=last_sync_error,
            last_synced_at=last_synced_at,
            mirror_window_days=mirror_window_days,
        )

        schedule_replica_v2.additional_properties = d
        return schedule_replica_v2

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
