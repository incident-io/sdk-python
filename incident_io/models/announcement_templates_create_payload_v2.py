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


T = TypeVar("T", bound="AnnouncementTemplatesCreatePayloadV2")


@_attrs_define(kw_only=True)
class AnnouncementTemplatesCreatePayloadV2:
    """
    Example:
        {'actions': [{'action_type': 'announcement_post_actions_homepage', 'emoji': 'slack', 'rank': 1}], 'fields':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type':
            'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text': {'contents': 'If you work on **payments**, please join
            {{incident.reference}}', 'type': 'markdown'}}], 'name': 'Major incidents', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH']}

    Attributes:
        name (str): Name of this announcement template, unique within the organisation Example: Major incidents.
        actions (list[AnnouncementTemplateActionPayloadV2] | Unset): Actions shown on the announcement post Example:
            [{'action_type': 'announcement_post_actions_homepage', 'emoji': 'slack', 'rank': 1}].
        fields (list[AnnouncementTemplateFieldPayloadV2] | Unset): Fields shown on the announcement post Example:
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type':
            'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text': {'contents': 'If you work on **payments**, please join
            {{incident.reference}}', 'type': 'markdown'}}].
        owning_team_ids (list[str] | Unset): IDs of the teams that own this template Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
    """

    name: str
    actions: list[AnnouncementTemplateActionPayloadV2] | Unset = UNSET
    fields: list[AnnouncementTemplateFieldPayloadV2] | Unset = UNSET
    owning_team_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if actions is not UNSET:
            field_dict["actions"] = actions
        if fields is not UNSET:
            field_dict["fields"] = fields
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
        name = d.pop("name")

        _actions = d.pop("actions", UNSET)
        actions: list[AnnouncementTemplateActionPayloadV2] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = AnnouncementTemplateActionPayloadV2.from_dict(
                    actions_item_data
                )

                actions.append(actions_item)

        _fields = d.pop("fields", UNSET)
        fields: list[AnnouncementTemplateFieldPayloadV2] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = AnnouncementTemplateFieldPayloadV2.from_dict(
                    fields_item_data
                )

                fields.append(fields_item)

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        announcement_templates_create_payload_v2 = cls(
            name=name,
            actions=actions,
            fields=fields,
            owning_team_ids=owning_team_ids,
        )

        announcement_templates_create_payload_v2.additional_properties = d
        return announcement_templates_create_payload_v2

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
