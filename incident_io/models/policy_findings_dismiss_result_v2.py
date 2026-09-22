from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.policy_finding_v2 import PolicyFindingV2


T = TypeVar("T", bound="PolicyFindingsDismissResultV2")


@_attrs_define(kw_only=True)
class PolicyFindingsDismissResultV2:
    """
    Example:
        {'policy_finding': {'created_at': '2021-08-17T13:28:57.801578Z', 'days': 3, 'debrief': {'incident_id':
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
            '01FCNDV6P870EA6S7TK1DSYDG0'}}}

    Attributes:
        policy_finding (PolicyFindingV2):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'days': 3, 'debrief':
            {'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'dismissal': {'dismissed_at': '2021-08-17T13:28:57.801578Z',
            'dismissed_by': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed
            to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
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
            '01FCNDV6P870EA6S7TK1DSYDG0'}}.
    """

    policy_finding: PolicyFindingV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy_finding = self.policy_finding.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policy_finding": policy_finding,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.policy_finding_v2 import PolicyFindingV2

        d = dict(src_dict)
        policy_finding = PolicyFindingV2.from_dict(d.pop("policy_finding"))

        policy_findings_dismiss_result_v2 = cls(
            policy_finding=policy_finding,
        )

        policy_findings_dismiss_result_v2.additional_properties = d
        return policy_findings_dismiss_result_v2

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
