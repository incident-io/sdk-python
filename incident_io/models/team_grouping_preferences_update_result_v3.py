from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.team_grouping_preference_v3 import TeamGroupingPreferenceV3


T = TypeVar("T", bound="TeamGroupingPreferencesUpdateResultV3")


@_attrs_define(kw_only=True)
class TeamGroupingPreferencesUpdateResultV3:
    """
    Example:
        {'team_grouping_preference': {'created_at': '2021-08-17T13:28:57.801578Z', 'default': {'settings':
            {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe the same outage, so
            group them together.', 'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800,
            'window_type': 'rolling'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'team_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'updated_at': '2021-08-17T13:28:57.801578Z', 'version': 3}}

    Attributes:
        team_grouping_preference (TeamGroupingPreferenceV3): A team's alert grouping preference, which takes priority
            over the default grouping of every alert route its alerts match Example: {'created_at':
            '2021-08-17T13:28:57.801578Z', 'default': {'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the
            old and new clusters describe the same outage, so group them together.', 'enabled': True, 'grouping_keys':
            [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'team_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'version': 3}.
    """

    team_grouping_preference: TeamGroupingPreferenceV3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_grouping_preference = self.team_grouping_preference.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_grouping_preference": team_grouping_preference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.team_grouping_preference_v3 import (
            TeamGroupingPreferenceV3,
        )

        d = dict(src_dict)
        team_grouping_preference = TeamGroupingPreferenceV3.from_dict(
            d.pop("team_grouping_preference")
        )

        team_grouping_preferences_update_result_v3 = cls(
            team_grouping_preference=team_grouping_preference,
        )

        team_grouping_preferences_update_result_v3.additional_properties = d
        return team_grouping_preferences_update_result_v3

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
