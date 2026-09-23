from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.announcement_template_action_payload_v2 import (
        AnnouncementTemplateActionPayloadV2,
    )
    from ..models.announcement_template_field_payload_v2 import (
        AnnouncementTemplateFieldPayloadV2,
    )


T = TypeVar("T", bound="AnnouncementTemplatesUpdatePayloadV2")


@_attrs_define(kw_only=True)
class AnnouncementTemplatesUpdatePayloadV2:
    """
    Example:
        {'actions': [{'action_type': 'announcement_post_actions_homepage', 'emoji': 'slack', 'rank': 1}], 'fields':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type':
            'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text': {'contents': 'If you work on **payments**, please join
            {{incident.reference}}', 'type': 'markdown'}}], 'name': 'Major incidents', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH']}

    Attributes:
        actions (list[AnnouncementTemplateActionPayloadV2]): Actions shown on the announcement post. Send an empty array
            to remove them all. Example: [{'action_type': 'announcement_post_actions_homepage', 'emoji': 'slack', 'rank':
            1}].
        fields (list[AnnouncementTemplateFieldPayloadV2]): Fields shown on the announcement post. Send an empty array to
            remove them all. Example: [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type':
            'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text': {'contents': 'If you work on **payments**, please join
            {{incident.reference}}', 'type': 'markdown'}}].
        name (str): Name of this announcement template, unique within the organisation Example: Major incidents.
        owning_team_ids (list[str] | Unset): IDs of the teams that own this template. The existing owning teams are kept
            when omitted. Example: ['01G0J1EXE7AXZ2C93K61WBPYEH'].
    """

    actions: list[AnnouncementTemplateActionPayloadV2]
    fields: list[AnnouncementTemplateFieldPayloadV2]
    name: str
    owning_team_ids: list[str] | Unset = UNSET
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

        name = self.name

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
                "fields": fields,
                "name": name,
            }
        )
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.announcement_template_action_payload_v2 import (
            AnnouncementTemplateActionPayloadV2,
        )
        from ..models.announcement_template_field_payload_v2 import (
            AnnouncementTemplateFieldPayloadV2,
        )

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = AnnouncementTemplateActionPayloadV2.from_dict(
                actions_item_data
            )

            actions.append(actions_item)

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = AnnouncementTemplateFieldPayloadV2.from_dict(fields_item_data)

            fields.append(fields_item)

        name = d.pop("name")

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        announcement_templates_update_payload_v2 = cls(
            actions=actions,
            fields=fields,
            name=name,
            owning_team_ids=owning_team_ids,
        )

        announcement_templates_update_payload_v2.additional_properties = d
        return announcement_templates_update_payload_v2

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
