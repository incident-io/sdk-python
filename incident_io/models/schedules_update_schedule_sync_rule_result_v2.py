from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_sync_rule_v2 import ScheduleSyncRuleV2


T = TypeVar("T", bound="SchedulesUpdateScheduleSyncRuleResultV2")


@_attrs_define(kw_only=True)
class SchedulesUpdateScheduleSyncRuleResultV2:
    """
    Example:
        {'schedule_sync_rule': {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01JXYZ000000000000000000CD',
            'permanent_member_user_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rotation_id': '01JXYZ000000000000000000RT',
            'schedule_id': '01JXYZ000000000000000000EF', 'schedule_sync_target': {'add_bot_to_group': True, 'created_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01JXYZ000000000000000000AB', 'linked_schedules': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB']}],
            'slack_team_id': 'T02A1AZHG3J', 'slack_user_group_id': 'S06MNNU5BMK', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'schedule_sync_target_id': '01JXYZ000000000000000000AB', 'sync_type': 'on_call',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        schedule_sync_rule (ScheduleSyncRuleV2): A sync rule links a schedule to a sync target, telling us which of the
            schedule's members should flow into the target's Slack user group.

            sync_type decides who is synced: on_call syncs only the people currently on
            call, next_on_call syncs the people on the next upcoming shift, and all_users
            syncs everyone on the schedule. By default every rotation on the schedule is
            included; set rotation_id to scope the rule to a single rotation. As the
            schedule's shifts change hands, we keep the target's Slack user group
            membership in step with the rule.

            A user group's members are the union of every rule feeding it, so one schedule
            can have several rules for the same target as long as they differ on
            rotation_id or sync_type. Point an on_call and a next_on_call rule at one group
            and it holds both the current and the next on-call.

            permanent_member_user_ids names users who stay in the group whichever way the
            shifts fall, on top of whoever sync_type selects. Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01JXYZ000000000000000000CD', 'permanent_member_user_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rotation_id':
            '01JXYZ000000000000000000RT', 'schedule_id': '01JXYZ000000000000000000EF', 'schedule_sync_target':
            {'add_bot_to_group': True, 'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01JXYZ000000000000000000AB',
            'linked_schedules': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule', 'team_ids':
            ['01JPQA75EPNEES4479P16P4XAB']}], 'slack_team_id': 'T02A1AZHG3J', 'slack_user_group_id': 'S06MNNU5BMK',
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'schedule_sync_target_id': '01JXYZ000000000000000000AB',
            'sync_type': 'on_call', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    schedule_sync_rule: ScheduleSyncRuleV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_sync_rule = self.schedule_sync_rule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_sync_rule": schedule_sync_rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_sync_rule_v2 import ScheduleSyncRuleV2

        d = dict(src_dict)
        schedule_sync_rule = ScheduleSyncRuleV2.from_dict(d.pop("schedule_sync_rule"))

        schedules_update_schedule_sync_rule_result_v2 = cls(
            schedule_sync_rule=schedule_sync_rule,
        )

        schedules_update_schedule_sync_rule_result_v2.additional_properties = d
        return schedules_update_schedule_sync_rule_result_v2

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
