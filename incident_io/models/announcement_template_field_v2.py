from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.announcement_template_field_v2_field_type import (
    AnnouncementTemplateFieldV2FieldType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.announcement_template_rich_text_v2 import (
        AnnouncementTemplateRichTextV2,
    )


T = TypeVar("T", bound="AnnouncementTemplateFieldV2")


@_attrs_define(kw_only=True)
class AnnouncementTemplateFieldV2:
    """
    Example:
        {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type':
            'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text': {'contents': 'If you work on **payments**, please join
            {{incident.reference}}', 'type': 'markdown'}, 'title': 'Severity'}

    Attributes:
        field_type (AnnouncementTemplateFieldV2FieldType): Type of this field Example: announcement_post_fields_status.
        rank (int): Position of this field on the post, lowest first Example: 1.
        title (str): Title shown next to this field, derived from its type Example: Severity.
        custom_field_id (str | Unset): ID of the custom field to show, for custom field fields Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        emoji (str | Unset): Emoji shown next to this field Example: fire.
        incident_role_id (str | Unset): ID of the incident role to show, for incident role fields Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        incident_timestamp_id (str | Unset): ID of the incident timestamp to show, for incident timestamp fields
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        rich_text (AnnouncementTemplateRichTextV2 | Unset): Content of a rich text field. The type says how contents is
            written. Example: {'contents': 'If you work on **payments**, please join {{incident.reference}}', 'type':
            'markdown'}.
    """

    field_type: AnnouncementTemplateFieldV2FieldType
    rank: int
    title: str
    custom_field_id: str | Unset = UNSET
    emoji: str | Unset = UNSET
    incident_role_id: str | Unset = UNSET
    incident_timestamp_id: str | Unset = UNSET
    rich_text: AnnouncementTemplateRichTextV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_type = self.field_type.value

        rank = self.rank

        title = self.title

        custom_field_id = self.custom_field_id

        emoji = self.emoji

        incident_role_id = self.incident_role_id

        incident_timestamp_id = self.incident_timestamp_id

        rich_text: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rich_text, Unset):
            rich_text = self.rich_text.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_type": field_type,
                "rank": rank,
                "title": title,
            }
        )
        if custom_field_id is not UNSET:
            field_dict["custom_field_id"] = custom_field_id
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if incident_role_id is not UNSET:
            field_dict["incident_role_id"] = incident_role_id
        if incident_timestamp_id is not UNSET:
            field_dict["incident_timestamp_id"] = incident_timestamp_id
        if rich_text is not UNSET:
            field_dict["rich_text"] = rich_text

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.announcement_template_rich_text_v2 import (
            AnnouncementTemplateRichTextV2,
        )

        d = dict(src_dict)
        field_type = AnnouncementTemplateFieldV2FieldType(d.pop("field_type"))

        rank = d.pop("rank")

        title = d.pop("title")

        custom_field_id = d.pop("custom_field_id", UNSET)

        emoji = d.pop("emoji", UNSET)

        incident_role_id = d.pop("incident_role_id", UNSET)

        incident_timestamp_id = d.pop("incident_timestamp_id", UNSET)

        _rich_text = d.pop("rich_text", UNSET)
        rich_text: AnnouncementTemplateRichTextV2 | Unset
        if isinstance(_rich_text, Unset):
            rich_text = UNSET
        else:
            rich_text = AnnouncementTemplateRichTextV2.from_dict(_rich_text)

        announcement_template_field_v2 = cls(
            field_type=field_type,
            rank=rank,
            title=title,
            custom_field_id=custom_field_id,
            emoji=emoji,
            incident_role_id=incident_role_id,
            incident_timestamp_id=incident_timestamp_id,
            rich_text=rich_text,
        )

        announcement_template_field_v2.additional_properties = d
        return announcement_template_field_v2

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
