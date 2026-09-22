from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_participant_workload_v2_participant_type import (
    IncidentParticipantWorkloadV2ParticipantType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_v2 import UserV2
    from ..models.workload_minutes_v2 import WorkloadMinutesV2


T = TypeVar("T", bound="IncidentParticipantWorkloadV2")


@_attrs_define(kw_only=True)
class IncidentParticipantWorkloadV2:
    """
    Example:
        {'archived_at': '2021-08-17T13:28:57.801578Z', 'participant_type': 'observer', 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workload': {'minutes_spent_on_incident': 125.5,
            'minutes_spent_on_incident_in_late_hours': 20.5, 'minutes_spent_on_incident_in_sleeping_hours': 15,
            'minutes_spent_on_incident_in_working_hours': 90}}

    Attributes:
        user (UserV2):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        workload (WorkloadMinutesV2):  Example: {'minutes_spent_on_incident': 125.5,
            'minutes_spent_on_incident_in_late_hours': 20.5, 'minutes_spent_on_incident_in_sleeping_hours': 15,
            'minutes_spent_on_incident_in_working_hours': 90}.
        archived_at (datetime.datetime | Unset): When the user left the incident, if they are no longer an active
            participant Example: 2021-08-17T13:28:57.801578Z.
        participant_type (IncidentParticipantWorkloadV2ParticipantType | Unset): The role they had in the incident
            Example: observer.
    """

    user: UserV2
    workload: WorkloadMinutesV2
    archived_at: datetime.datetime | Unset = UNSET
    participant_type: IncidentParticipantWorkloadV2ParticipantType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        workload = self.workload.to_dict()

        archived_at: str | Unset = UNSET
        if not isinstance(self.archived_at, Unset):
            archived_at = self.archived_at.isoformat()

        participant_type: str | Unset = UNSET
        if not isinstance(self.participant_type, Unset):
            participant_type = self.participant_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "workload": workload,
            }
        )
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if participant_type is not UNSET:
            field_dict["participant_type"] = participant_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_v2 import UserV2
        from ..models.workload_minutes_v2 import WorkloadMinutesV2

        d = dict(src_dict)
        user = UserV2.from_dict(d.pop("user"))

        workload = WorkloadMinutesV2.from_dict(d.pop("workload"))

        _archived_at = d.pop("archived_at", UNSET)
        archived_at: datetime.datetime | Unset
        if isinstance(_archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = datetime.datetime.fromisoformat(_archived_at)

        _participant_type = d.pop("participant_type", UNSET)
        participant_type: IncidentParticipantWorkloadV2ParticipantType | Unset
        if isinstance(_participant_type, Unset):
            participant_type = UNSET
        else:
            participant_type = IncidentParticipantWorkloadV2ParticipantType(
                _participant_type
            )

        incident_participant_workload_v2 = cls(
            user=user,
            workload=workload,
            archived_at=archived_at,
            participant_type=participant_type,
        )

        incident_participant_workload_v2.additional_properties = d
        return incident_participant_workload_v2

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
