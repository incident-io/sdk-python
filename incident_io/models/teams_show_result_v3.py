from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.team_v3 import TeamV3


T = TypeVar("T", bound="TeamsShowResultV3")


@_attrs_define(kw_only=True)
class TeamsShowResultV3:
    """
    Example:
        {'team': {'catalog_entry': {'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'id': 'abc123', 'members': [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'slack_user_id':
            'U02AYNF2XJM'}], 'name': 'abc123'}}

    Attributes:
        team (TeamV3):  Example: {'catalog_entry': {'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'id': 'abc123', 'members': [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'slack_user_id':
            'U02AYNF2XJM'}], 'name': 'abc123'}.
    """

    team: TeamV3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team = self.team.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.team_v3 import TeamV3

        d = dict(src_dict)
        team = TeamV3.from_dict(d.pop("team"))

        teams_show_result_v3 = cls(
            team=team,
        )

        teams_show_result_v3.additional_properties = d
        return teams_show_result_v3

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
