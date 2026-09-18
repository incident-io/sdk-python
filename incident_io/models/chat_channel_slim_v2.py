from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatChannelSlimV2")


@_attrs_define
class ChatChannelSlimV2:
    """
    Example:
        {'microsoft_teams_channel_id': 'abc123', 'microsoft_teams_team_id': 'abc123', 'slack_channel_id': 'abc123',
            'slack_team_id': 'abc123'}

    Attributes:
        microsoft_teams_channel_id (str | Unset): ID of the Microsoft Teams channel, if there is one Example: abc123.
        microsoft_teams_team_id (str | Unset): ID of the Microsoft Teams team, if there is one Example: abc123.
        slack_channel_id (str | Unset): ID of the Slack channel, if there is one Example: abc123.
        slack_team_id (str | Unset): ID of the Slack team, if there is one Example: abc123.
    """

    microsoft_teams_channel_id: str | Unset = UNSET
    microsoft_teams_team_id: str | Unset = UNSET
    slack_channel_id: str | Unset = UNSET
    slack_team_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        microsoft_teams_channel_id = self.microsoft_teams_channel_id

        microsoft_teams_team_id = self.microsoft_teams_team_id

        slack_channel_id = self.slack_channel_id

        slack_team_id = self.slack_team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if microsoft_teams_channel_id is not UNSET:
            field_dict["microsoft_teams_channel_id"] = microsoft_teams_channel_id
        if microsoft_teams_team_id is not UNSET:
            field_dict["microsoft_teams_team_id"] = microsoft_teams_team_id
        if slack_channel_id is not UNSET:
            field_dict["slack_channel_id"] = slack_channel_id
        if slack_team_id is not UNSET:
            field_dict["slack_team_id"] = slack_team_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        microsoft_teams_channel_id = d.pop("microsoft_teams_channel_id", UNSET)

        microsoft_teams_team_id = d.pop("microsoft_teams_team_id", UNSET)

        slack_channel_id = d.pop("slack_channel_id", UNSET)

        slack_team_id = d.pop("slack_team_id", UNSET)

        chat_channel_slim_v2 = cls(
            microsoft_teams_channel_id=microsoft_teams_channel_id,
            microsoft_teams_team_id=microsoft_teams_team_id,
            slack_channel_id=slack_channel_id,
            slack_team_id=slack_team_id,
        )

        chat_channel_slim_v2.additional_properties = d
        return chat_channel_slim_v2

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
