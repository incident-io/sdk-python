from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.announcement_rule_v2 import AnnouncementRuleV2
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2


T = TypeVar("T", bound="AnnouncementRulesListResultV2")


@_attrs_define(kw_only=True)
class AnnouncementRulesListResultV2:
    """
    Example:
        {'announcement_rules': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'conditions_no_longer_apply_behaviour': 'leave_in_place', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'microsoft_teams_channel_ids':
            ['19:abc@thread.tacv2/19:def@thread.tacv2'], 'mode': 'live_and_closed', 'name': 'Data Breaches',
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'private_incident_scope': 'all', 'slack_channel_ids':
            ['C02AW36C1M5'], 'template_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'update_sharing_mode': 'none', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}], 'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        announcement_rules (list[AnnouncementRuleV2]):  Example: [{'condition_groups': [{'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident
            Severity', 'reference': 'incident.severity'}}]}], 'conditions_no_longer_apply_behaviour': 'leave_in_place',
            'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'microsoft_teams_channel_ids':
            ['19:abc@thread.tacv2/19:def@thread.tacv2'], 'mode': 'live_and_closed', 'name': 'Data Breaches',
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'private_incident_scope': 'all', 'slack_channel_ids':
            ['C02AW36C1M5'], 'template_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'update_sharing_mode': 'none', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}].
        pagination_meta (PaginationMetaResultV2):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
    """

    announcement_rules: list[AnnouncementRuleV2]
    pagination_meta: PaginationMetaResultV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        announcement_rules = []
        for announcement_rules_item_data in self.announcement_rules:
            announcement_rules_item = announcement_rules_item_data.to_dict()
            announcement_rules.append(announcement_rules_item)

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "announcement_rules": announcement_rules,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.announcement_rule_v2 import AnnouncementRuleV2
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )

        d = dict(src_dict)
        announcement_rules = []
        _announcement_rules = d.pop("announcement_rules")
        for announcement_rules_item_data in _announcement_rules:
            announcement_rules_item = AnnouncementRuleV2.from_dict(
                announcement_rules_item_data
            )

            announcement_rules.append(announcement_rules_item)

        pagination_meta = PaginationMetaResultV2.from_dict(d.pop("pagination_meta"))

        announcement_rules_list_result_v2 = cls(
            announcement_rules=announcement_rules,
            pagination_meta=pagination_meta,
        )

        announcement_rules_list_result_v2.additional_properties = d
        return announcement_rules_list_result_v2

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
