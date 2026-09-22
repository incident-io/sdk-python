from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewSlackUserGroupPayloadV2")


@_attrs_define(kw_only=True)
class NewSlackUserGroupPayloadV2:
    """
    Example:
        {'description': 'The team responsible for Project A', 'handle': 'project-team-a', 'name': 'Project Team A',
            'slack_team_id': 'T01234567'}

    Attributes:
        description (str): Description of the user group Example: The team responsible for Project A.
        handle (str): Handle of the user group Example: project-team-a.
        name (str): Name of the user group Example: Project Team A.
        slack_team_id (str | Unset): Slack workspace ID where the user group should be created. Required for Enterprise
            Grid organizations with multiple workspaces. Example: T01234567.
    """

    description: str
    handle: str
    name: str
    slack_team_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        handle = self.handle

        name = self.name

        slack_team_id = self.slack_team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "handle": handle,
                "name": name,
            }
        )
        if slack_team_id is not UNSET:
            field_dict["slack_team_id"] = slack_team_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description")

        handle = d.pop("handle")

        name = d.pop("name")

        slack_team_id = d.pop("slack_team_id", UNSET)

        new_slack_user_group_payload_v2 = cls(
            description=description,
            handle=handle,
            name=name,
            slack_team_id=slack_team_id,
        )

        new_slack_user_group_payload_v2.additional_properties = d
        return new_slack_user_group_payload_v2

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
