from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.announcement_template_action_v2 import AnnouncementTemplateActionV2
    from ..models.announcement_template_field_v2 import AnnouncementTemplateFieldV2


T = TypeVar("T", bound="AnnouncementTemplateV2")


@_attrs_define(kw_only=True)
class AnnouncementTemplateV2:
    """An announcement template controls which fields and actions appear on an announcement post.

    Example:
        {'actions': [{'action_type': 'announcement_post_actions_homepage', 'emoji': 'slack', 'rank': 1, 'title': 'Join
            channel'}], 'fields': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type':
            'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text': {'contents': 'If you work on **payments**, please join
            {{incident.reference}}', 'type': 'markdown'}, 'title': 'Severity'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'is_default': False, 'name': 'Major incidents', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH']}

    Attributes:
        actions (list[AnnouncementTemplateActionV2]): Actions shown on the announcement post, in rank order Example:
            [{'action_type': 'announcement_post_actions_homepage', 'emoji': 'slack', 'rank': 1, 'title': 'Join channel'}].
        fields (list[AnnouncementTemplateFieldV2]): Fields shown on the announcement post, in rank order Example:
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type':
            'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text': {'contents': 'If you work on **payments**, please join
            {{incident.reference}}', 'type': 'markdown'}, 'title': 'Severity'}].
        id (str): Unique identifier for this announcement template Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        is_default (bool): Whether this is the organisation's default template, used by rules that don't choose one
            Example: False.
        name (str): Name of this announcement template Example: Major incidents.
        owning_team_ids (list[str]): IDs of the teams that own this template Example: ['01G0J1EXE7AXZ2C93K61WBPYEH'].
    """

    actions: list[AnnouncementTemplateActionV2]
    fields: list[AnnouncementTemplateFieldV2]
    id: str
    is_default: bool
    name: str
    owning_team_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        id = self.id

        is_default = self.is_default

        name = self.name

        owning_team_ids = self.owning_team_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
                "fields": fields,
                "id": id,
                "is_default": is_default,
                "name": name,
                "owning_team_ids": owning_team_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.announcement_template_action_v2 import (
            AnnouncementTemplateActionV2,
        )
        from ..models.announcement_template_field_v2 import (
            AnnouncementTemplateFieldV2,
        )

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = AnnouncementTemplateActionV2.from_dict(actions_item_data)

            actions.append(actions_item)

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = AnnouncementTemplateFieldV2.from_dict(fields_item_data)

            fields.append(fields_item)

        id = d.pop("id")

        is_default = d.pop("is_default")

        name = d.pop("name")

        owning_team_ids = cast(list[str], d.pop("owning_team_ids"))

        announcement_template_v2 = cls(
            actions=actions,
            fields=fields,
            id=id,
            is_default=is_default,
            name=name,
            owning_team_ids=owning_team_ids,
        )

        announcement_template_v2.additional_properties = d
        return announcement_template_v2

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
