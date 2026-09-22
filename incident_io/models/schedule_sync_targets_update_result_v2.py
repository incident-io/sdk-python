from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_sync_target_resource_v2 import ScheduleSyncTargetResourceV2


T = TypeVar("T", bound="ScheduleSyncTargetsUpdateResultV2")


@_attrs_define(kw_only=True)
class ScheduleSyncTargetsUpdateResultV2:
    """
    Example:
        {'schedule_sync_target': {'add_bot_to_group': True, 'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01JXYZ000000000000000000AB', 'linked_schedules': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call
            Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB']}], 'slack_team_id': 'T02A1AZHG3J', 'slack_user_group_id':
            'S06MNNU5BMK', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        schedule_sync_target (ScheduleSyncTargetResourceV2): A sync target is the link between incident.io and a single
            Slack user group,
            used to keep that group's membership in step with who is currently on call.

            A target identifies the group by its Slack user group ID and Slack team ID,
            and remembers whether the incident.io bot should be added to the group so it
            can manage membership. On its own a target does nothing: you link it to a
            schedule by creating a schedule sync rule (see the Schedules service), and
            that rule decides which schedule members flow into the group. As the
            schedule's shifts change hands, we update the Slack user group to match.

            A single target can be referenced by sync rules on several schedules at once;
            linked_schedules lists every schedule with an active rule pointing at it. Example: {'add_bot_to_group': True,
            'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01JXYZ000000000000000000AB', 'linked_schedules': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB']}],
            'slack_team_id': 'T02A1AZHG3J', 'slack_user_group_id': 'S06MNNU5BMK', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    schedule_sync_target: ScheduleSyncTargetResourceV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_sync_target = self.schedule_sync_target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_sync_target": schedule_sync_target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_sync_target_resource_v2 import (
            ScheduleSyncTargetResourceV2,
        )

        d = dict(src_dict)
        schedule_sync_target = ScheduleSyncTargetResourceV2.from_dict(
            d.pop("schedule_sync_target")
        )

        schedule_sync_targets_update_result_v2 = cls(
            schedule_sync_target=schedule_sync_target,
        )

        schedule_sync_targets_update_result_v2.additional_properties = d
        return schedule_sync_targets_update_result_v2

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
