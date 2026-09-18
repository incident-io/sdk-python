from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_finding_v2_policy_type import PolicyFindingV2PolicyType
from ..models.policy_finding_v2_state import PolicyFindingV2State
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_finding_debrief_v2 import PolicyFindingDebriefV2
    from ..models.policy_finding_dismissal_v2 import PolicyFindingDismissalV2
    from ..models.policy_finding_follow_up_v2 import PolicyFindingFollowUpV2
    from ..models.policy_finding_on_call_readiness_v2 import (
        PolicyFindingOnCallReadinessV2,
    )
    from ..models.policy_finding_post_mortem_v2 import PolicyFindingPostMortemV2
    from ..models.policy_finding_schedule_v2 import PolicyFindingScheduleV2
    from ..models.policy_finding_vacation_conflict_v2 import (
        PolicyFindingVacationConflictV2,
    )
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="PolicyFindingV2")


@_attrs_define
class PolicyFindingV2:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'days': 3, 'debrief': {'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'dismissal': {'dismissed_at': '2021-08-17T13:28:57.801578Z', 'dismissed_by':
            {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
            'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'reason': 'This incident is special.'}, 'due_at': '2025-10-14T00:00:00.000000Z', 'follow_up':
            {'follow_up_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'last_checked_at': '2021-08-17T13:28:57.801578Z', 'on_call_readiness':
            {'high_urgency': [{'max_delay_seconds': 300, 'met': False, 'method_types': ['slack']}], 'low_urgency':
            [{'max_delay_seconds': 300, 'met': False, 'method_types': ['slack']}], 'user_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'policy_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'policy_type': 'follow_up', 'post_mortem': {'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'responsible_users': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}],
            'schedule': {'cause': 'nobody_scheduled', 'end_at': '2021-08-17T13:28:57.801578Z', 'has_unscheduled_time': True,
            'impacted_users': [{'cause': 'no_on_call_seat', 'name': 'Alice Green', 'user_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}], 'rotation_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'start_at': '2021-08-17T13:28:57.801578Z'}, 'state': 'active', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'vacation_conflict': {'end_at': '2021-08-17T13:28:57.801578Z', 'holiday_name':
            'Joe Bloggs - Holiday', 'rotation_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'start_at': '2021-08-17T13:28:57.801578Z', 'user_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}}

    Attributes:
        created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        id (str): Unique ID of the finding Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        last_checked_at (datetime.datetime): When this finding was last re-evaluated Example:
            2021-08-17T13:28:57.801578Z.
        policy_id (str): The policy this finding was raised against Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        policy_type (PolicyFindingV2PolicyType): Type of the policy this finding was raised against Example: follow_up.
        responsible_users (list[UserV2]): Who is expected to resolve this finding Example: [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}].
        state (PolicyFindingV2State): Where this finding is in its lifecycle Example: active.
        updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        days (int | Unset): Days outside the policy's due date Example: 3.
        debrief (PolicyFindingDebriefV2 | Unset): Set when policy_type is debrief. Example: {'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}.
        dismissal (PolicyFindingDismissalV2 | Unset):  Example: {'dismissed_at': '2021-08-17T13:28:57.801578Z',
            'dismissed_by': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed
            to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'reason': 'This incident is special.'}.
        due_at (datetime.datetime | Unset): When this finding becomes overdue Example: 2025-10-14T00:00:00.000000Z.
        follow_up (PolicyFindingFollowUpV2 | Unset): Set when policy_type is follow_up. Example: {'follow_up_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
        on_call_readiness (PolicyFindingOnCallReadinessV2 | Unset): Set when policy_type is on_call_readiness. The user
            is always the one the finding is about. Example: {'high_urgency': [{'max_delay_seconds': 300, 'met': False,
            'method_types': ['slack']}], 'low_urgency': [{'max_delay_seconds': 300, 'met': False, 'method_types':
            ['slack']}], 'user_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
        post_mortem (PolicyFindingPostMortemV2 | Unset): Set when policy_type is post_mortem. Example: {'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}.
        schedule (PolicyFindingScheduleV2 | Unset): Set when policy_type is schedule. Describes a gap in on-call cover.
            Example: {'cause': 'nobody_scheduled', 'end_at': '2021-08-17T13:28:57.801578Z', 'has_unscheduled_time': True,
            'impacted_users': [{'cause': 'no_on_call_seat', 'name': 'Alice Green', 'user_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}], 'rotation_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'start_at': '2021-08-17T13:28:57.801578Z'}.
        vacation_conflict (PolicyFindingVacationConflictV2 | Unset): Set when policy_type is vacation_conflict. Someone
            is on call while on holiday. Example: {'end_at': '2021-08-17T13:28:57.801578Z', 'holiday_name': 'Joe Bloggs -
            Holiday', 'rotation_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'start_at':
            '2021-08-17T13:28:57.801578Z', 'user_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
    """

    created_at: datetime.datetime
    id: str
    last_checked_at: datetime.datetime
    policy_id: str
    policy_type: PolicyFindingV2PolicyType
    responsible_users: list[UserV2]
    state: PolicyFindingV2State
    updated_at: datetime.datetime
    days: int | Unset = UNSET
    debrief: PolicyFindingDebriefV2 | Unset = UNSET
    dismissal: PolicyFindingDismissalV2 | Unset = UNSET
    due_at: datetime.datetime | Unset = UNSET
    follow_up: PolicyFindingFollowUpV2 | Unset = UNSET
    on_call_readiness: PolicyFindingOnCallReadinessV2 | Unset = UNSET
    post_mortem: PolicyFindingPostMortemV2 | Unset = UNSET
    schedule: PolicyFindingScheduleV2 | Unset = UNSET
    vacation_conflict: PolicyFindingVacationConflictV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        last_checked_at = self.last_checked_at.isoformat()

        policy_id = self.policy_id

        policy_type = self.policy_type.value

        responsible_users = []
        for responsible_users_item_data in self.responsible_users:
            responsible_users_item = responsible_users_item_data.to_dict()
            responsible_users.append(responsible_users_item)

        state = self.state.value

        updated_at = self.updated_at.isoformat()

        days = self.days

        debrief: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debrief, Unset):
            debrief = self.debrief.to_dict()

        dismissal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dismissal, Unset):
            dismissal = self.dismissal.to_dict()

        due_at: str | Unset = UNSET
        if not isinstance(self.due_at, Unset):
            due_at = self.due_at.isoformat()

        follow_up: dict[str, Any] | Unset = UNSET
        if not isinstance(self.follow_up, Unset):
            follow_up = self.follow_up.to_dict()

        on_call_readiness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.on_call_readiness, Unset):
            on_call_readiness = self.on_call_readiness.to_dict()

        post_mortem: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post_mortem, Unset):
            post_mortem = self.post_mortem.to_dict()

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        vacation_conflict: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vacation_conflict, Unset):
            vacation_conflict = self.vacation_conflict.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "last_checked_at": last_checked_at,
                "policy_id": policy_id,
                "policy_type": policy_type,
                "responsible_users": responsible_users,
                "state": state,
                "updated_at": updated_at,
            }
        )
        if days is not UNSET:
            field_dict["days"] = days
        if debrief is not UNSET:
            field_dict["debrief"] = debrief
        if dismissal is not UNSET:
            field_dict["dismissal"] = dismissal
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if follow_up is not UNSET:
            field_dict["follow_up"] = follow_up
        if on_call_readiness is not UNSET:
            field_dict["on_call_readiness"] = on_call_readiness
        if post_mortem is not UNSET:
            field_dict["post_mortem"] = post_mortem
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if vacation_conflict is not UNSET:
            field_dict["vacation_conflict"] = vacation_conflict

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.policy_finding_debrief_v2 import (
            PolicyFindingDebriefV2,
        )
        from ..models.policy_finding_dismissal_v2 import (
            PolicyFindingDismissalV2,
        )
        from ..models.policy_finding_follow_up_v2 import (
            PolicyFindingFollowUpV2,
        )
        from ..models.policy_finding_on_call_readiness_v2 import (
            PolicyFindingOnCallReadinessV2,
        )
        from ..models.policy_finding_post_mortem_v2 import (
            PolicyFindingPostMortemV2,
        )
        from ..models.policy_finding_schedule_v2 import (
            PolicyFindingScheduleV2,
        )
        from ..models.policy_finding_vacation_conflict_v2 import (
            PolicyFindingVacationConflictV2,
        )
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        last_checked_at = datetime.datetime.fromisoformat(d.pop("last_checked_at"))

        policy_id = d.pop("policy_id")

        policy_type = PolicyFindingV2PolicyType(d.pop("policy_type"))

        responsible_users = []
        _responsible_users = d.pop("responsible_users")
        for responsible_users_item_data in _responsible_users:
            responsible_users_item = UserV2.from_dict(responsible_users_item_data)

            responsible_users.append(responsible_users_item)

        state = PolicyFindingV2State(d.pop("state"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        days = d.pop("days", UNSET)

        _debrief = d.pop("debrief", UNSET)
        debrief: PolicyFindingDebriefV2 | Unset
        if isinstance(_debrief, Unset):
            debrief = UNSET
        else:
            debrief = PolicyFindingDebriefV2.from_dict(_debrief)

        _dismissal = d.pop("dismissal", UNSET)
        dismissal: PolicyFindingDismissalV2 | Unset
        if isinstance(_dismissal, Unset):
            dismissal = UNSET
        else:
            dismissal = PolicyFindingDismissalV2.from_dict(_dismissal)

        _due_at = d.pop("due_at", UNSET)
        due_at: datetime.datetime | Unset
        if isinstance(_due_at, Unset):
            due_at = UNSET
        else:
            due_at = datetime.datetime.fromisoformat(_due_at)

        _follow_up = d.pop("follow_up", UNSET)
        follow_up: PolicyFindingFollowUpV2 | Unset
        if isinstance(_follow_up, Unset):
            follow_up = UNSET
        else:
            follow_up = PolicyFindingFollowUpV2.from_dict(_follow_up)

        _on_call_readiness = d.pop("on_call_readiness", UNSET)
        on_call_readiness: PolicyFindingOnCallReadinessV2 | Unset
        if isinstance(_on_call_readiness, Unset):
            on_call_readiness = UNSET
        else:
            on_call_readiness = PolicyFindingOnCallReadinessV2.from_dict(
                _on_call_readiness
            )

        _post_mortem = d.pop("post_mortem", UNSET)
        post_mortem: PolicyFindingPostMortemV2 | Unset
        if isinstance(_post_mortem, Unset):
            post_mortem = UNSET
        else:
            post_mortem = PolicyFindingPostMortemV2.from_dict(_post_mortem)

        _schedule = d.pop("schedule", UNSET)
        schedule: PolicyFindingScheduleV2 | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = PolicyFindingScheduleV2.from_dict(_schedule)

        _vacation_conflict = d.pop("vacation_conflict", UNSET)
        vacation_conflict: PolicyFindingVacationConflictV2 | Unset
        if isinstance(_vacation_conflict, Unset):
            vacation_conflict = UNSET
        else:
            vacation_conflict = PolicyFindingVacationConflictV2.from_dict(
                _vacation_conflict
            )

        policy_finding_v2 = cls(
            created_at=created_at,
            id=id,
            last_checked_at=last_checked_at,
            policy_id=policy_id,
            policy_type=policy_type,
            responsible_users=responsible_users,
            state=state,
            updated_at=updated_at,
            days=days,
            debrief=debrief,
            dismissal=dismissal,
            due_at=due_at,
            follow_up=follow_up,
            on_call_readiness=on_call_readiness,
            post_mortem=post_mortem,
            schedule=schedule,
            vacation_conflict=vacation_conflict,
        )

        policy_finding_v2.additional_properties = d
        return policy_finding_v2

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
