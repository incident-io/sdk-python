from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_participant_v2_participant_type import (
    IncidentParticipantV2ParticipantType,
)

if TYPE_CHECKING:
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="IncidentParticipantV2")


@_attrs_define(kw_only=True)
class IncidentParticipantV2:
    """
    Example:
        {'participant_type': 'observer', 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}}

    Attributes:
        participant_type (IncidentParticipantV2ParticipantType): The role they took in the incident Example: observer.
        user (UserV2):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
    """

    participant_type: IncidentParticipantV2ParticipantType
    user: UserV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        participant_type = self.participant_type.value

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "participant_type": participant_type,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        participant_type = IncidentParticipantV2ParticipantType(
            d.pop("participant_type")
        )

        user = UserV2.from_dict(d.pop("user"))

        incident_participant_v2 = cls(
            participant_type=participant_type,
            user=user,
        )

        incident_participant_v2.additional_properties = d
        return incident_participant_v2

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
