from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_v1_roles_item import IdentityV1RolesItem
from ..models.identity_v1_team_roles_item import IdentityV1TeamRolesItem

if TYPE_CHECKING:
    from ..models.identity_team_v1 import IdentityTeamV1


T = TypeVar("T", bound="IdentityV1")


@_attrs_define(kw_only=True)
class IdentityV1:
    """
    Example:
        {'dashboard_url': 'https://app.incident.io/my-org', 'name': 'Alertmanager token', 'roles': ['viewer'],
            'team_roles': ['catalog_editor'], 'teams': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Platform'}]}

    Attributes:
        dashboard_url (str): The dashboard URL for this organisation Example: https://app.incident.io/my-org.
        name (str): The name assigned to the current API Key Example: Alertmanager token.
        roles (list[IdentityV1RolesItem]): Which roles have been enabled for this key Example: ['viewer'].
        team_roles (list[IdentityV1TeamRolesItem]): If set, these roles apply to requests that operate on resources
            owned by any of the teams in the 'teams' array. These are in addition to any 'roles' which are applied on all
            requests. Example: ['catalog_editor'].
        teams (list[IdentityTeamV1]): Teams that this API key is scoped to. If this is not empty, the current API key
            has additional roles within these teams (see team_roles). Example: [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name':
            'Platform'}].
    """

    dashboard_url: str
    name: str
    roles: list[IdentityV1RolesItem]
    team_roles: list[IdentityV1TeamRolesItem]
    teams: list[IdentityTeamV1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dashboard_url = self.dashboard_url

        name = self.name

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.value
            roles.append(roles_item)

        team_roles = []
        for team_roles_item_data in self.team_roles:
            team_roles_item = team_roles_item_data.value
            team_roles.append(team_roles_item)

        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dashboard_url": dashboard_url,
                "name": name,
                "roles": roles,
                "team_roles": team_roles,
                "teams": teams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.identity_team_v1 import IdentityTeamV1

        d = dict(src_dict)
        dashboard_url = d.pop("dashboard_url")

        name = d.pop("name")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = IdentityV1RolesItem(roles_item_data)

            roles.append(roles_item)

        team_roles = []
        _team_roles = d.pop("team_roles")
        for team_roles_item_data in _team_roles:
            team_roles_item = IdentityV1TeamRolesItem(team_roles_item_data)

            team_roles.append(team_roles_item)

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = IdentityTeamV1.from_dict(teams_item_data)

            teams.append(teams_item)

        identity_v1 = cls(
            dashboard_url=dashboard_url,
            name=name,
            roles=roles,
            team_roles=team_roles,
            teams=teams,
        )

        identity_v1.additional_properties = d
        return identity_v1

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
