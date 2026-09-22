from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_participants_v2 import IncidentParticipantsV2


T = TypeVar("T", bound="IncidentParticipantsListResultV2")


@_attrs_define(kw_only=True)
class IncidentParticipantsListResultV2:
    """
    Example:
        {'incident_participants': {'active': [{'participant_type': 'observer', 'user': {'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
            'U02AYNF2XJM'}}], 'passive': [{'participant_type': 'observer', 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}}]}}

    Attributes:
        incident_participants (IncidentParticipantsV2):  Example: {'active': [{'participant_type': 'observer', 'user':
            {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}}], 'passive': [{'participant_type': 'observer', 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}}]}.
    """

    incident_participants: IncidentParticipantsV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_participants = self.incident_participants.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_participants": incident_participants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_participants_v2 import (
            IncidentParticipantsV2,
        )

        d = dict(src_dict)
        incident_participants = IncidentParticipantsV2.from_dict(
            d.pop("incident_participants")
        )

        incident_participants_list_result_v2 = cls(
            incident_participants=incident_participants,
        )

        incident_participants_list_result_v2.additional_properties = d
        return incident_participants_list_result_v2

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
