from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.linked_schedule_v2 import LinkedScheduleV2


T = TypeVar("T", bound="ScheduleSyncTargetResourceV2")


@_attrs_define(kw_only=True)
class ScheduleSyncTargetResourceV2:
    """A sync target is the link between incident.io and a single Slack user group,
    used to keep that group's membership in step with who is currently on call.

    A target identifies the group by its Slack user group ID and Slack team ID,
    and remembers whether the incident.io bot should be added to the group so it
    can manage membership. On its own a target does nothing: you link it to a
    schedule by creating a schedule sync rule (see the Schedules service), and
    that rule decides which schedule members flow into the group. As the
    schedule's shifts change hands, we update the Slack user group to match.

    A single target can be referenced by sync rules on several schedules at once;
    linked_schedules lists every schedule with an active rule pointing at it.

        Example:
            {'add_bot_to_group': True, 'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01JXYZ000000000000000000AB',
                'linked_schedules': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule', 'team_ids':
                ['01JPQA75EPNEES4479P16P4XAB']}], 'slack_team_id': 'T02A1AZHG3J', 'slack_user_group_id': 'S06MNNU5BMK',
                'updated_at': '2021-08-17T13:28:57.801578Z'}

        Attributes:
            add_bot_to_group (bool): Whether the incident.io bot should be added to the group as a member. This is needed
                for some Slack configurations to let us manage the group's membership. Example: True.
            created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            id (str): Unique identifier of the sync target Example: 01JXYZ000000000000000000AB.
            linked_schedules (list[LinkedScheduleV2]): Schedules with an active sync rule pointing at this target Example:
                [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule', 'team_ids':
                ['01JPQA75EPNEES4479P16P4XAB']}].
            slack_team_id (str): Slack team (workspace) ID the user group lives in. On Enterprise Grid this identifies which
                workspace within the org the group belongs to. Example: T02A1AZHG3J.
            slack_user_group_id (str): Slack ID of the user group whose membership is kept in sync. This is the Slack-
                assigned group ID (starting with 'S'), not the @-handle. Example: S06MNNU5BMK.
            updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
    """

    add_bot_to_group: bool
    created_at: datetime.datetime
    id: str
    linked_schedules: list[LinkedScheduleV2]
    slack_team_id: str
    slack_user_group_id: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_bot_to_group = self.add_bot_to_group

        created_at = self.created_at.isoformat()

        id = self.id

        linked_schedules = []
        for linked_schedules_item_data in self.linked_schedules:
            linked_schedules_item = linked_schedules_item_data.to_dict()
            linked_schedules.append(linked_schedules_item)

        slack_team_id = self.slack_team_id

        slack_user_group_id = self.slack_user_group_id

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "add_bot_to_group": add_bot_to_group,
                "created_at": created_at,
                "id": id,
                "linked_schedules": linked_schedules,
                "slack_team_id": slack_team_id,
                "slack_user_group_id": slack_user_group_id,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.linked_schedule_v2 import LinkedScheduleV2

        d = dict(src_dict)
        add_bot_to_group = d.pop("add_bot_to_group")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        linked_schedules = []
        _linked_schedules = d.pop("linked_schedules")
        for linked_schedules_item_data in _linked_schedules:
            linked_schedules_item = LinkedScheduleV2.from_dict(
                linked_schedules_item_data
            )

            linked_schedules.append(linked_schedules_item)

        slack_team_id = d.pop("slack_team_id")

        slack_user_group_id = d.pop("slack_user_group_id")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        schedule_sync_target_resource_v2 = cls(
            add_bot_to_group=add_bot_to_group,
            created_at=created_at,
            id=id,
            linked_schedules=linked_schedules,
            slack_team_id=slack_team_id,
            slack_user_group_id=slack_user_group_id,
            updated_at=updated_at,
        )

        schedule_sync_target_resource_v2.additional_properties = d
        return schedule_sync_target_resource_v2

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
