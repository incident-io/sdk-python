from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_participant_workload_hour_v2 import (
        IncidentParticipantWorkloadHourV2,
    )
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2
    from ..models.workload_metadata_v2 import WorkloadMetadataV2


T = TypeVar("T", bound="IncidentParticipantWorkloadsListHoursResultV2")


@_attrs_define(kw_only=True)
class IncidentParticipantWorkloadsListHoursResultV2:
    """
    Example:
        {'incident_participant_workload_hours': [{'activity_hour': '2021-08-17T13:00:00Z', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workload':
            {'minutes_spent_on_incident': 125.5, 'minutes_spent_on_incident_in_late_hours': 20.5,
            'minutes_spent_on_incident_in_sleeping_hours': 15, 'minutes_spent_on_incident_in_working_hours': 90}}],
            'metadata': {'data_synced_at': '2021-08-17T13:00:00Z'}, 'pagination_meta': {'after':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        incident_participant_workload_hours (list[IncidentParticipantWorkloadHourV2]):  Example: [{'activity_hour':
            '2021-08-17T13:00:00Z', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workload': {'minutes_spent_on_incident': 125.5, 'minutes_spent_on_incident_in_late_hours': 20.5,
            'minutes_spent_on_incident_in_sleeping_hours': 15, 'minutes_spent_on_incident_in_working_hours': 90}}].
        metadata (WorkloadMetadataV2):  Example: {'data_synced_at': '2021-08-17T13:00:00Z'}.
        pagination_meta (PaginationMetaResultV2):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
    """

    incident_participant_workload_hours: list[IncidentParticipantWorkloadHourV2]
    metadata: WorkloadMetadataV2
    pagination_meta: PaginationMetaResultV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_participant_workload_hours = []
        for (
            incident_participant_workload_hours_item_data
        ) in self.incident_participant_workload_hours:
            incident_participant_workload_hours_item = (
                incident_participant_workload_hours_item_data.to_dict()
            )
            incident_participant_workload_hours.append(
                incident_participant_workload_hours_item
            )

        metadata = self.metadata.to_dict()

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_participant_workload_hours": incident_participant_workload_hours,
                "metadata": metadata,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_participant_workload_hour_v2 import (
            IncidentParticipantWorkloadHourV2,
        )
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )
        from ..models.workload_metadata_v2 import WorkloadMetadataV2

        d = dict(src_dict)
        incident_participant_workload_hours = []
        _incident_participant_workload_hours = d.pop(
            "incident_participant_workload_hours"
        )
        for (
            incident_participant_workload_hours_item_data
        ) in _incident_participant_workload_hours:
            incident_participant_workload_hours_item = (
                IncidentParticipantWorkloadHourV2.from_dict(
                    incident_participant_workload_hours_item_data
                )
            )

            incident_participant_workload_hours.append(
                incident_participant_workload_hours_item
            )

        metadata = WorkloadMetadataV2.from_dict(d.pop("metadata"))

        pagination_meta = PaginationMetaResultV2.from_dict(d.pop("pagination_meta"))

        incident_participant_workloads_list_hours_result_v2 = cls(
            incident_participant_workload_hours=incident_participant_workload_hours,
            metadata=metadata,
            pagination_meta=pagination_meta,
        )

        incident_participant_workloads_list_hours_result_v2.additional_properties = d
        return incident_participant_workloads_list_hours_result_v2

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
