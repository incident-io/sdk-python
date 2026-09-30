from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IncidentTeamMembershipsRevokePayloadV1")


@_attrs_define(kw_only=True)
class IncidentTeamMembershipsRevokePayloadV1:
    """
    Example:
        {'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'team_id': '01FCQSP07Z74QMMYPDDGQB9FTG'}

    Attributes:
        incident_id (str): Revoke team access to this incident Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        team_id (str):  Example: 01FCQSP07Z74QMMYPDDGQB9FTG.
    """

    incident_id: str
    team_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        team_id = self.team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
                "team_id": team_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        incident_id = d.pop("incident_id")

        team_id = d.pop("team_id")

        incident_team_memberships_revoke_payload_v1 = cls(
            incident_id=incident_id,
            team_id=team_id,
        )

        incident_team_memberships_revoke_payload_v1.additional_properties = d
        return incident_team_memberships_revoke_payload_v1

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
