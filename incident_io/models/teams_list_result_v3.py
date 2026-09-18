from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination_meta_result_v3 import PaginationMetaResultV3
    from ..models.team_v3 import TeamV3


T = TypeVar("T", bound="TeamsListResultV3")


@_attrs_define
class TeamsListResultV3:
    """
    Example:
        {'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}, 'teams': [{'catalog_entry':
            {'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-
            call'}, 'id': 'abc123', 'members': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'slack_user_id': 'U02AYNF2XJM'}], 'name': 'abc123'}]}

    Attributes:
        pagination_meta (PaginationMetaResultV3):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
        teams (list[TeamV3]):  Example: [{'catalog_entry': {'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'id': 'abc123', 'members': [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'slack_user_id':
            'U02AYNF2XJM'}], 'name': 'abc123'}].
    """

    pagination_meta: PaginationMetaResultV3
    teams: list[TeamV3]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination_meta = self.pagination_meta.to_dict()

        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination_meta": pagination_meta,
                "teams": teams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_meta_result_v3 import (
            PaginationMetaResultV3,
        )
        from ..models.team_v3 import TeamV3

        d = dict(src_dict)
        pagination_meta = PaginationMetaResultV3.from_dict(d.pop("pagination_meta"))

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = TeamV3.from_dict(teams_item_data)

            teams.append(teams_item)

        teams_list_result_v3 = cls(
            pagination_meta=pagination_meta,
            teams=teams,
        )

        teams_list_result_v3.additional_properties = d
        return teams_list_result_v3

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
