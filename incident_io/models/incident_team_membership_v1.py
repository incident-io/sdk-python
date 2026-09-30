from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_team_v1 import IncidentTeamV1


T = TypeVar("T", bound="IncidentTeamMembershipV1")


@_attrs_define(kw_only=True)
class IncidentTeamMembershipV1:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'team': {'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Platform'}, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the team membership was created Example: 2021-08-17T13:28:57.801578Z.
        id (str): Unique identifier of this incident team membership Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_id (str): Unique identifier of the incident Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        team (IncidentTeamV1):  Example: {'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Platform'}.
        updated_at (datetime.datetime): When the team membership was last updated Example: 2021-08-17T13:28:57.801578Z.
    """

    created_at: datetime.datetime
    id: str
    incident_id: str
    team: IncidentTeamV1
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        incident_id = self.incident_id

        team = self.team.to_dict()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "incident_id": incident_id,
                "team": team,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_team_v1 import IncidentTeamV1

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        team = IncidentTeamV1.from_dict(d.pop("team"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        incident_team_membership_v1 = cls(
            created_at=created_at,
            id=id,
            incident_id=incident_id,
            team=team,
            updated_at=updated_at,
        )

        incident_team_membership_v1.additional_properties = d
        return incident_team_membership_v1

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
