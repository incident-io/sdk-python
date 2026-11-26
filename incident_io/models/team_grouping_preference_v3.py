from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_grouping_default_branch_v3 import AlertGroupingDefaultBranchV3


T = TypeVar("T", bound="TeamGroupingPreferenceV3")


@_attrs_define(kw_only=True)
class TeamGroupingPreferenceV3:
    """A team's alert grouping preference, which takes priority over the default grouping of every alert route its alerts
    match

        Example:
            {'created_at': '2021-08-17T13:28:57.801578Z', 'default': {'settings': {'ai_enabled': False, 'ai_instructions':
                'Alerts from the old and new clusters describe the same outage, so group them together.', 'enabled': True,
                'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}, 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'team_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'updated_at':
                '2021-08-17T13:28:57.801578Z', 'version': 3}

        Attributes:
            created_at (datetime.datetime): When this preference was created Example: 2021-08-17T13:28:57.801578Z.
            default (AlertGroupingDefaultBranchV3): The fallback branch: how to group the alerts that no conditional branch
                matches Example: {'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters
                describe the same outage, so group them together.', 'enabled': True, 'grouping_keys': [{'reference':
                'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}.
            id (str): Unique identifier for this preference Example: 01FCNDV6P870EA6S7TK1DSYDG0.
            team_id (str): The catalog entry ID of the team this preference belongs to Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
            updated_at (datetime.datetime): When this preference was last updated Example: 2021-08-17T13:28:57.801578Z.
            version (int): The current version number, incremented on each update Example: 3.
    """

    created_at: datetime.datetime
    default: AlertGroupingDefaultBranchV3
    id: str
    team_id: str
    updated_at: datetime.datetime
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        default = self.default.to_dict()

        id = self.id

        team_id = self.team_id

        updated_at = self.updated_at.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "default": default,
                "id": id,
                "team_id": team_id,
                "updated_at": updated_at,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_grouping_default_branch_v3 import (
            AlertGroupingDefaultBranchV3,
        )

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        default = AlertGroupingDefaultBranchV3.from_dict(d.pop("default"))

        id = d.pop("id")

        team_id = d.pop("team_id")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        team_grouping_preference_v3 = cls(
            created_at=created_at,
            default=default,
            id=id,
            team_id=team_id,
            updated_at=updated_at,
            version=version,
        )

        team_grouping_preference_v3.additional_properties = d
        return team_grouping_preference_v3

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
