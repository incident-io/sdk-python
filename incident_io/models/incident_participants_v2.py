from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_participant_v2 import IncidentParticipantV2


T = TypeVar("T", bound="IncidentParticipantsV2")


@_attrs_define(kw_only=True)
class IncidentParticipantsV2:
    """
    Example:
        {'active': [{'participant_type': 'observer', 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}}],
            'passive': [{'participant_type': 'observer', 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}}]}

    Attributes:
        active (list[IncidentParticipantV2]): Participants who are actively helping with the incident Example:
            [{'participant_type': 'observer', 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}}].
        passive (list[IncidentParticipantV2]): Participants who are just observing the incident Example:
            [{'participant_type': 'observer', 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}}].
    """

    active: list[IncidentParticipantV2]
    passive: list[IncidentParticipantV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = []
        for active_item_data in self.active:
            active_item = active_item_data.to_dict()
            active.append(active_item)

        passive = []
        for passive_item_data in self.passive:
            passive_item = passive_item_data.to_dict()
            passive.append(passive_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "passive": passive,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_participant_v2 import (
            IncidentParticipantV2,
        )

        d = dict(src_dict)
        active = []
        _active = d.pop("active")
        for active_item_data in _active:
            active_item = IncidentParticipantV2.from_dict(active_item_data)

            active.append(active_item)

        passive = []
        _passive = d.pop("passive")
        for passive_item_data in _passive:
            passive_item = IncidentParticipantV2.from_dict(passive_item_data)

            passive.append(passive_item)

        incident_participants_v2 = cls(
            active=active,
            passive=passive,
        )

        incident_participants_v2.additional_properties = d
        return incident_participants_v2

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
