from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_keys_update_payload_v1_role_names_item import (
    APIKeysUpdatePayloadV1RoleNamesItem,
)
from ..models.api_keys_update_payload_v1_team_role_names_item import (
    APIKeysUpdatePayloadV1TeamRoleNamesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="APIKeysUpdatePayloadV1")


@_attrs_define
class APIKeysUpdatePayloadV1:
    """
    Example:
        {'comments': 'Requested in https://example.slack.com/archives/C123/p456', 'name': 'My test API key',
            'role_names': ['viewer', 'incident_creator'], 'team_ids': ['01FCNDV6P870EA6S7TK1DSYDG0'], 'team_role_names':
            ['schedules_editor']}

    Attributes:
        name (str): Human-readable name for the API key Example: My test API key.
        role_names (list[APIKeysUpdatePayloadV1RoleNamesItem]): Account-level roles for the API key. These roles apply
            across the entire account, not scoped to specific teams. Pass an empty array if no account-level roles are
            needed. Example: ['viewer', 'incident_creator'].
        team_ids (list[str]): IDs of teams to scope the `team_role_names` to. If provided, `team_role_names` must also
            be a non-empty array, and vice versa. Pass an empty array if the key should not be scoped to any teams. Example:
            ['01FCNDV6P870EA6S7TK1DSYDG0'].
        team_role_names (list[APIKeysUpdatePayloadV1TeamRoleNamesItem]): Roles to grant for the teams specified in
            `team_ids`. If provided, `team_ids` must also be a non-empty array, and vice versa. Pass an empty array if no
            team-level roles are needed. Example: ['schedules_editor'].
        comments (str | Unset): Freeform notes about the API key Example: Requested in
            https://example.slack.com/archives/C123/p456.
    """

    name: str
    role_names: list[APIKeysUpdatePayloadV1RoleNamesItem]
    team_ids: list[str]
    team_role_names: list[APIKeysUpdatePayloadV1TeamRoleNamesItem]
    comments: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        role_names = []
        for role_names_item_data in self.role_names:
            role_names_item = role_names_item_data.value
            role_names.append(role_names_item)

        team_ids = self.team_ids

        team_role_names = []
        for team_role_names_item_data in self.team_role_names:
            team_role_names_item = team_role_names_item_data.value
            team_role_names.append(team_role_names_item)

        comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "role_names": role_names,
                "team_ids": team_ids,
                "team_role_names": team_role_names,
            }
        )
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        role_names = []
        _role_names = d.pop("role_names")
        for role_names_item_data in _role_names:
            role_names_item = APIKeysUpdatePayloadV1RoleNamesItem(role_names_item_data)

            role_names.append(role_names_item)

        team_ids = cast(list[str], d.pop("team_ids"))

        team_role_names = []
        _team_role_names = d.pop("team_role_names")
        for team_role_names_item_data in _team_role_names:
            team_role_names_item = APIKeysUpdatePayloadV1TeamRoleNamesItem(
                team_role_names_item_data
            )

            team_role_names.append(team_role_names_item)

        comments = d.pop("comments", UNSET)

        api_keys_update_payload_v1 = cls(
            name=name,
            role_names=role_names,
            team_ids=team_ids,
            team_role_names=team_role_names,
            comments=comments,
        )

        api_keys_update_payload_v1.additional_properties = d
        return api_keys_update_payload_v1

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
