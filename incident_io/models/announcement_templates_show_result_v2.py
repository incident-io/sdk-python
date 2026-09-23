from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.announcement_template_v2 import AnnouncementTemplateV2


T = TypeVar("T", bound="AnnouncementTemplatesShowResultV2")


@_attrs_define(kw_only=True)
class AnnouncementTemplatesShowResultV2:
    """
    Example:
        {'announcement_template': {'actions': [{'action_type': 'announcement_post_actions_homepage', 'emoji': 'slack',
            'rank': 1, 'title': 'Join channel'}], 'fields': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji':
            'fire', 'field_type': 'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text': {'contents': 'If you work on
            **payments**, please join {{incident.reference}}', 'type': 'markdown'}, 'title': 'Severity'}], 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Major incidents', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH']}}

    Attributes:
        announcement_template (AnnouncementTemplateV2): An announcement template controls which fields and actions
            appear on an announcement post. Example: {'actions': [{'action_type': 'announcement_post_actions_homepage',
            'emoji': 'slack', 'rank': 1, 'title': 'Join channel'}], 'fields': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type': 'announcement_post_fields_status',
            'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'rank':
            1, 'rich_text': {'contents': 'If you work on **payments**, please join {{incident.reference}}', 'type':
            'markdown'}, 'title': 'Severity'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Major
            incidents', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH']}.
    """

    announcement_template: AnnouncementTemplateV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        announcement_template = self.announcement_template.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "announcement_template": announcement_template,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.announcement_template_v2 import (
            AnnouncementTemplateV2,
        )

        d = dict(src_dict)
        announcement_template = AnnouncementTemplateV2.from_dict(
            d.pop("announcement_template")
        )

        announcement_templates_show_result_v2 = cls(
            announcement_template=announcement_template,
        )

        announcement_templates_show_result_v2.additional_properties = d
        return announcement_templates_show_result_v2

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
