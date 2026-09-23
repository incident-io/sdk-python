from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.announcement_template_action_v2_action_type import (
    AnnouncementTemplateActionV2ActionType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnouncementTemplateActionV2")


@_attrs_define(kw_only=True)
class AnnouncementTemplateActionV2:
    """
    Example:
        {'action_type': 'announcement_post_actions_homepage', 'emoji': 'slack', 'rank': 1, 'title': 'Join channel'}

    Attributes:
        action_type (AnnouncementTemplateActionV2ActionType): Type of this action Example:
            announcement_post_actions_homepage.
        rank (int): Position of this action on the post, lowest first Example: 1.
        title (str): Label shown on this action's button, derived from its type Example: Join channel.
        emoji (str | Unset): Emoji shown on this action's button Example: slack.
    """

    action_type: AnnouncementTemplateActionV2ActionType
    rank: int
    title: str
    emoji: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type.value

        rank = self.rank

        title = self.title

        emoji = self.emoji

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "rank": rank,
                "title": title,
            }
        )
        if emoji is not UNSET:
            field_dict["emoji"] = emoji

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        action_type = AnnouncementTemplateActionV2ActionType(d.pop("action_type"))

        rank = d.pop("rank")

        title = d.pop("title")

        emoji = d.pop("emoji", UNSET)

        announcement_template_action_v2 = cls(
            action_type=action_type,
            rank=rank,
            title=title,
            emoji=emoji,
        )

        announcement_template_action_v2.additional_properties = d
        return announcement_template_action_v2

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
