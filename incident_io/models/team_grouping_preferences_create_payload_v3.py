from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_grouping_default_branch_v3 import AlertGroupingDefaultBranchV3


T = TypeVar("T", bound="TeamGroupingPreferencesCreatePayloadV3")


@_attrs_define(kw_only=True)
class TeamGroupingPreferencesCreatePayloadV3:
    """
    Example:
        {'default': {'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe
            the same outage, so group them together.', 'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}],
            'window_seconds': 1800, 'window_type': 'rolling'}}, 'team_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}

    Attributes:
        default (AlertGroupingDefaultBranchV3): The fallback branch: how to group the alerts that no conditional branch
            matches Example: {'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters
            describe the same outage, so group them together.', 'enabled': True, 'grouping_keys': [{'reference':
            'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}.
        team_id (str): The catalog entry ID of the team this preference belongs to Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
    """

    default: AlertGroupingDefaultBranchV3
    team_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default.to_dict()

        team_id = self.team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
                "team_id": team_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_grouping_default_branch_v3 import (
            AlertGroupingDefaultBranchV3,
        )

        d = dict(src_dict)
        default = AlertGroupingDefaultBranchV3.from_dict(d.pop("default"))

        team_id = d.pop("team_id")

        team_grouping_preferences_create_payload_v3 = cls(
            default=default,
            team_id=team_id,
        )

        team_grouping_preferences_create_payload_v3.additional_properties = d
        return team_grouping_preferences_create_payload_v3

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
