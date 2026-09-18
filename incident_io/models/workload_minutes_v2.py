from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkloadMinutesV2")


@_attrs_define
class WorkloadMinutesV2:
    """
    Example:
        {'minutes_spent_on_incident': 125.5, 'minutes_spent_on_incident_in_late_hours': 20.5,
            'minutes_spent_on_incident_in_sleeping_hours': 15, 'minutes_spent_on_incident_in_working_hours': 90}

    Attributes:
        minutes_spent_on_incident (float): Total minutes the user spent on the incident Example: 125.5.
        minutes_spent_on_incident_in_late_hours (float): Minutes spent during the user's late hours Example: 20.5.
        minutes_spent_on_incident_in_sleeping_hours (float): Minutes spent during the user's sleeping hours Example: 15.
        minutes_spent_on_incident_in_working_hours (float): Minutes spent during the user's working hours Example: 90.
    """

    minutes_spent_on_incident: float
    minutes_spent_on_incident_in_late_hours: float
    minutes_spent_on_incident_in_sleeping_hours: float
    minutes_spent_on_incident_in_working_hours: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minutes_spent_on_incident = self.minutes_spent_on_incident

        minutes_spent_on_incident_in_late_hours = (
            self.minutes_spent_on_incident_in_late_hours
        )

        minutes_spent_on_incident_in_sleeping_hours = (
            self.minutes_spent_on_incident_in_sleeping_hours
        )

        minutes_spent_on_incident_in_working_hours = (
            self.minutes_spent_on_incident_in_working_hours
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "minutes_spent_on_incident": minutes_spent_on_incident,
                "minutes_spent_on_incident_in_late_hours": minutes_spent_on_incident_in_late_hours,
                "minutes_spent_on_incident_in_sleeping_hours": minutes_spent_on_incident_in_sleeping_hours,
                "minutes_spent_on_incident_in_working_hours": minutes_spent_on_incident_in_working_hours,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        minutes_spent_on_incident = d.pop("minutes_spent_on_incident")

        minutes_spent_on_incident_in_late_hours = d.pop(
            "minutes_spent_on_incident_in_late_hours"
        )

        minutes_spent_on_incident_in_sleeping_hours = d.pop(
            "minutes_spent_on_incident_in_sleeping_hours"
        )

        minutes_spent_on_incident_in_working_hours = d.pop(
            "minutes_spent_on_incident_in_working_hours"
        )

        workload_minutes_v2 = cls(
            minutes_spent_on_incident=minutes_spent_on_incident,
            minutes_spent_on_incident_in_late_hours=minutes_spent_on_incident_in_late_hours,
            minutes_spent_on_incident_in_sleeping_hours=minutes_spent_on_incident_in_sleeping_hours,
            minutes_spent_on_incident_in_working_hours=minutes_spent_on_incident_in_working_hours,
        )

        workload_minutes_v2.additional_properties = d
        return workload_minutes_v2

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
