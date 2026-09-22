from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2
    from ..models.schedule_sync_rule_v2 import ScheduleSyncRuleV2


T = TypeVar("T", bound="SchedulesListScheduleSyncRulesResultV2")


@_attrs_define(kw_only=True)
class SchedulesListScheduleSyncRulesResultV2:
    """
    Example:
        {'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}, 'schedule_sync_rules':
            [{'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01JXYZ000000000000000000CD', 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rotation_id': '01JXYZ000000000000000000RT', 'schedule_id':
            '01JXYZ000000000000000000EF', 'schedule_sync_target': {'add_bot_to_group': True, 'created_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01JXYZ000000000000000000AB', 'linked_schedules': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB']}],
            'slack_team_id': 'T02A1AZHG3J', 'slack_user_group_id': 'S06MNNU5BMK', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'schedule_sync_target_id': '01JXYZ000000000000000000AB', 'sync_type': 'on_call',
            'updated_at': '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        schedule_sync_rules (list[ScheduleSyncRuleV2]):  Example: [{'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01JXYZ000000000000000000CD', 'permanent_member_user_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rotation_id':
            '01JXYZ000000000000000000RT', 'schedule_id': '01JXYZ000000000000000000EF', 'schedule_sync_target':
            {'add_bot_to_group': True, 'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01JXYZ000000000000000000AB',
            'linked_schedules': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule', 'team_ids':
            ['01JPQA75EPNEES4479P16P4XAB']}], 'slack_team_id': 'T02A1AZHG3J', 'slack_user_group_id': 'S06MNNU5BMK',
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'schedule_sync_target_id': '01JXYZ000000000000000000AB',
            'sync_type': 'on_call', 'updated_at': '2021-08-17T13:28:57.801578Z'}].
        pagination_meta (PaginationMetaResultV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size':
            25}.
    """

    schedule_sync_rules: list[ScheduleSyncRuleV2]
    pagination_meta: PaginationMetaResultV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_sync_rules = []
        for schedule_sync_rules_item_data in self.schedule_sync_rules:
            schedule_sync_rules_item = schedule_sync_rules_item_data.to_dict()
            schedule_sync_rules.append(schedule_sync_rules_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_sync_rules": schedule_sync_rules,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )
        from ..models.schedule_sync_rule_v2 import ScheduleSyncRuleV2

        d = dict(src_dict)
        schedule_sync_rules = []
        _schedule_sync_rules = d.pop("schedule_sync_rules")
        for schedule_sync_rules_item_data in _schedule_sync_rules:
            schedule_sync_rules_item = ScheduleSyncRuleV2.from_dict(
                schedule_sync_rules_item_data
            )

            schedule_sync_rules.append(schedule_sync_rules_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultV2.from_dict(_pagination_meta)

        schedules_list_schedule_sync_rules_result_v2 = cls(
            schedule_sync_rules=schedule_sync_rules,
            pagination_meta=pagination_meta,
        )

        schedules_list_schedule_sync_rules_result_v2.additional_properties = d
        return schedules_list_schedule_sync_rules_result_v2

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
