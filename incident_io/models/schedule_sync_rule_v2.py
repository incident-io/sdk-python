from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_sync_rule_v2_sync_type import ScheduleSyncRuleV2SyncType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_sync_target_resource_v2 import ScheduleSyncTargetResourceV2


T = TypeVar("T", bound="ScheduleSyncRuleV2")


@_attrs_define
class ScheduleSyncRuleV2:
    """A sync rule links a schedule to a sync target, telling us which of the
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
    shifts fall, on top of whoever sync_type selects.

        Example:
            {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01JXYZ000000000000000000CD', 'permanent_member_user_ids':
                ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rotation_id': '01JXYZ000000000000000000RT', 'schedule_id':
                '01JXYZ000000000000000000EF', 'schedule_sync_target': {'add_bot_to_group': True, 'created_at':
                '2021-08-17T13:28:57.801578Z', 'id': '01JXYZ000000000000000000AB', 'linked_schedules': [{'id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB']}],
                'slack_team_id': 'T02A1AZHG3J', 'slack_user_group_id': 'S06MNNU5BMK', 'updated_at':
                '2021-08-17T13:28:57.801578Z'}, 'schedule_sync_target_id': '01JXYZ000000000000000000AB', 'sync_type': 'on_call',
                'updated_at': '2021-08-17T13:28:57.801578Z'}

        Attributes:
            created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            id (str): Unique identifier of the sync rule Example: 01JXYZ000000000000000000CD.
            permanent_member_user_ids (list[str]): IDs of users always kept in the Slack user group, regardless of who is on
                call. Useful for keeping e.g. a manager in the group so they see mentions without being paged. Scoped to this
                rule: when several rules feed the same group, we sync the union of their permanent members. Example:
                ['01G0J1EXE7AXZ2C93K61WBPYEH'].
            schedule_id (str): The schedule this rule belongs to Example: 01JXYZ000000000000000000EF.
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
            schedule_sync_target_id (str): The sync target ID this rule links to Example: 01JXYZ000000000000000000AB.
            sync_type (ScheduleSyncRuleV2SyncType): Which schedule members sync to the user group Example: on_call.
            updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            rotation_id (str | Unset): If set, only members of this rotation sync to the user group. When unset, all
                rotations on the schedule are synced. Example: 01JXYZ000000000000000000RT.
    """

    created_at: datetime.datetime
    id: str
    permanent_member_user_ids: list[str]
    schedule_id: str
    schedule_sync_target: ScheduleSyncTargetResourceV2
    schedule_sync_target_id: str
    sync_type: ScheduleSyncRuleV2SyncType
    updated_at: datetime.datetime
    rotation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        permanent_member_user_ids = self.permanent_member_user_ids

        schedule_id = self.schedule_id

        schedule_sync_target = self.schedule_sync_target.to_dict()

        schedule_sync_target_id = self.schedule_sync_target_id

        sync_type = self.sync_type.value

        updated_at = self.updated_at.isoformat()

        rotation_id = self.rotation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "permanent_member_user_ids": permanent_member_user_ids,
                "schedule_id": schedule_id,
                "schedule_sync_target": schedule_sync_target,
                "schedule_sync_target_id": schedule_sync_target_id,
                "sync_type": sync_type,
                "updated_at": updated_at,
            }
        )
        if rotation_id is not UNSET:
            field_dict["rotation_id"] = rotation_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_sync_target_resource_v2 import (
            ScheduleSyncTargetResourceV2,
        )

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        permanent_member_user_ids = cast(list[str], d.pop("permanent_member_user_ids"))

        schedule_id = d.pop("schedule_id")

        schedule_sync_target = ScheduleSyncTargetResourceV2.from_dict(
            d.pop("schedule_sync_target")
        )

        schedule_sync_target_id = d.pop("schedule_sync_target_id")

        sync_type = ScheduleSyncRuleV2SyncType(d.pop("sync_type"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        rotation_id = d.pop("rotation_id", UNSET)

        schedule_sync_rule_v2 = cls(
            created_at=created_at,
            id=id,
            permanent_member_user_ids=permanent_member_user_ids,
            schedule_id=schedule_id,
            schedule_sync_target=schedule_sync_target,
            schedule_sync_target_id=schedule_sync_target_id,
            sync_type=sync_type,
            updated_at=updated_at,
            rotation_id=rotation_id,
        )

        schedule_sync_rule_v2.additional_properties = d
        return schedule_sync_rule_v2

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
