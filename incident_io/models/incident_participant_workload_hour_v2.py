from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_v2 import UserV2
    from ..models.workload_minutes_v2 import WorkloadMinutesV2


T = TypeVar("T", bound="IncidentParticipantWorkloadHourV2")


@_attrs_define(kw_only=True)
class IncidentParticipantWorkloadHourV2:
    """
    Example:
        {'activity_hour': '2021-08-17T13:00:00Z', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workload': {'minutes_spent_on_incident': 125.5,
            'minutes_spent_on_incident_in_late_hours': 20.5, 'minutes_spent_on_incident_in_sleeping_hours': 15,
            'minutes_spent_on_incident_in_working_hours': 90}}

    Attributes:
        activity_hour (datetime.datetime): The start of the hour this workload is for Example: 2021-08-17T13:00:00Z.
        incident_id (str): The incident the user worked on Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        user (UserV2):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        workload (WorkloadMinutesV2):  Example: {'minutes_spent_on_incident': 125.5,
            'minutes_spent_on_incident_in_late_hours': 20.5, 'minutes_spent_on_incident_in_sleeping_hours': 15,
            'minutes_spent_on_incident_in_working_hours': 90}.
    """

    activity_hour: datetime.datetime
    incident_id: str
    user: UserV2
    workload: WorkloadMinutesV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_hour = self.activity_hour.isoformat()

        incident_id = self.incident_id

        user = self.user.to_dict()

        workload = self.workload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activity_hour": activity_hour,
                "incident_id": incident_id,
                "user": user,
                "workload": workload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_v2 import UserV2
        from ..models.workload_minutes_v2 import WorkloadMinutesV2

        d = dict(src_dict)
        activity_hour = datetime.datetime.fromisoformat(d.pop("activity_hour"))

        incident_id = d.pop("incident_id")

        user = UserV2.from_dict(d.pop("user"))

        workload = WorkloadMinutesV2.from_dict(d.pop("workload"))

        incident_participant_workload_hour_v2 = cls(
            activity_hour=activity_hour,
            incident_id=incident_id,
            user=user,
            workload=workload,
        )

        incident_participant_workload_hour_v2.additional_properties = d
        return incident_participant_workload_hour_v2

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
