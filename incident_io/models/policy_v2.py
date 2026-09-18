from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_v2_policy_type import PolicyV2PolicyType
from ..models.policy_v2_status import PolicyV2Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_group_v2 import ConditionGroupV2
    from ..models.expression_v2 import ExpressionV2
    from ..models.policy_assignment_rules_v2 import PolicyAssignmentRulesV2
    from ..models.policy_debrief_v2 import PolicyDebriefV2
    from ..models.policy_follow_up_v2 import PolicyFollowUpV2
    from ..models.policy_on_call_readiness_v2 import PolicyOnCallReadinessV2
    from ..models.policy_post_mortem_v2 import PolicyPostMortemV2
    from ..models.policy_schedule_v2 import PolicyScheduleV2


T = TypeVar("T", bound="PolicyV2")


@_attrs_define
class PolicyV2:
    """
    Example:
        {'assignment_rules': {'bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'reminder_cadence_after': {'interval': 'daily'}, 'reminder_cadence_before': {'interval':
            'daily'}, 'reminder_detected_date_offset_hours': [0, 48], 'reminder_due_date_offset_hours': [-24, 0, 24]},
            'conditions': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}]}],
            'created_at': '2021-08-17T13:28:57.801578Z', 'debrief': {'due_date_config': {'applies_from':
            '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London', 'calculation_type': 'weekdays', 'days':
            {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}, 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'requirements': [{'conditions': [{'operation': {'label': 'Lawrence Jones',
            'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'run_on_private_incidents': False}, 'description': 'All critical incidents must export
            follow-ups to an external issue tracker before 7 days has passed since closure.', 'expressions':
            [{'else_branch': {'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference': '1235', 'reference_label': 'Teams'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}]}, 'navigate': {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type':
            'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}, 'returns': {'array': True, 'type': 'IncidentStatus'}}], 'reference':
            'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}],
            'follow_up': {'due_date_config': {'applies_from': '2021-08-17T13:28:57.801578Z', 'calculation_timezone':
            'Europe/London', 'calculation_type': 'weekdays', 'days': {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'requirements':
            [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}]}],
            'run_on_private_incidents': False}, 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Critical incidents must export
            follow-ups', 'on_call_readiness': {'enforcement': 'advisory', 'high_urgency': [{'max_delay_seconds': 300,
            'method_types': ['slack']}], 'low_urgency': [{'max_delay_seconds': 300, 'method_types': ['slack']}]},
            'policy_type': 'follow_up', 'post_mortem': {'due_date_config': {'applies_from': '2021-08-17T13:28:57.801578Z',
            'calculation_timezone': 'Europe/London', 'calculation_type': 'weekdays', 'days': {'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'requirements': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'run_on_private_incidents': False}, 'schedule': {'evaluation_level': 'schedule',
            'requirement_type': 'contiguous'}, 'status': 'enabled', 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        conditions (list[ConditionGroupV2]): Conditions which determine which resources are in scope for this policy
            Example: [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}]}].
        created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        id (str): Unique ID of the policy Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        name (str): Human readable name of the policy Example: Critical incidents must export follow-ups.
        policy_type (PolicyV2PolicyType): Type of the policy, specifying what this applies to Example: follow_up.
        status (PolicyV2Status): Disabled policies stop evaluating but keep their config Example: enabled.
        updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        assignment_rules (PolicyAssignmentRulesV2 | Unset):  Example: {'bindings': [{'array_value': [{'label': 'Lawrence
            Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'reminder_cadence_after': {'interval': 'daily'},
            'reminder_cadence_before': {'interval': 'daily'}, 'reminder_detected_date_offset_hours': [0, 48],
            'reminder_due_date_offset_hours': [-24, 0, 24]}.
        debrief (PolicyDebriefV2 | Unset): Set when policy_type is debrief. Example: {'due_date_config':
            {'applies_from': '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London', 'calculation_type':
            'weekdays', 'days': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'requirements': [{'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Incident Severity', 'reference': 'incident.severity'}}]}], 'run_on_private_incidents': False}.
        description (str | Unset): Human readable description of the policy Example: All critical incidents must export
            follow-ups to an external issue tracker before 7 days has passed since closure..
        expressions (list[ExpressionV2] | Unset): The expressions relating to this policy Example: [{'else_branch':
            {'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team
            Slack channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident
            Severity', 'reference': 'incident.severity'}}]}], 'result': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast':
            {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference': '1235', 'reference_label':
            'Teams'}, 'filter': {'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}]}, 'navigate': {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type':
            'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}, 'returns': {'array': True, 'type': 'IncidentStatus'}}], 'reference':
            'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}].
        follow_up (PolicyFollowUpV2 | Unset): Set when policy_type is follow_up. Example: {'due_date_config':
            {'applies_from': '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London', 'calculation_type':
            'weekdays', 'days': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'requirements': [{'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Incident Severity', 'reference': 'incident.severity'}}]}], 'run_on_private_incidents': False}.
        on_call_readiness (PolicyOnCallReadinessV2 | Unset): Set when policy_type is on_call_readiness. The assignee is
            always the user the finding is about and cannot be configured. Example: {'enforcement': 'advisory',
            'high_urgency': [{'max_delay_seconds': 300, 'method_types': ['slack']}], 'low_urgency': [{'max_delay_seconds':
            300, 'method_types': ['slack']}]}.
        post_mortem (PolicyPostMortemV2 | Unset): Set when policy_type is post_mortem. Example: {'due_date_config':
            {'applies_from': '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London', 'calculation_type':
            'weekdays', 'days': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'requirements': [{'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Incident Severity', 'reference': 'incident.severity'}}]}], 'run_on_private_incidents': False}.
        schedule (PolicyScheduleV2 | Unset): Detects gaps in on-call coverage. Set when policy_type is schedule.
            Example: {'evaluation_level': 'schedule', 'requirement_type': 'contiguous'}.
    """

    conditions: list[ConditionGroupV2]
    created_at: datetime.datetime
    id: str
    name: str
    policy_type: PolicyV2PolicyType
    status: PolicyV2Status
    updated_at: datetime.datetime
    assignment_rules: PolicyAssignmentRulesV2 | Unset = UNSET
    debrief: PolicyDebriefV2 | Unset = UNSET
    description: str | Unset = UNSET
    expressions: list[ExpressionV2] | Unset = UNSET
    follow_up: PolicyFollowUpV2 | Unset = UNSET
    on_call_readiness: PolicyOnCallReadinessV2 | Unset = UNSET
    post_mortem: PolicyPostMortemV2 | Unset = UNSET
    schedule: PolicyScheduleV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item = conditions_item_data.to_dict()
            conditions.append(conditions_item)

        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        policy_type = self.policy_type.value

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        assignment_rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignment_rules, Unset):
            assignment_rules = self.assignment_rules.to_dict()

        debrief: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debrief, Unset):
            debrief = self.debrief.to_dict()

        description = self.description

        expressions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expressions, Unset):
            expressions = []
            for expressions_item_data in self.expressions:
                expressions_item = expressions_item_data.to_dict()
                expressions.append(expressions_item)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditions": conditions,
                "created_at": created_at,
                "id": id,
                "name": name,
                "policy_type": policy_type,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if assignment_rules is not UNSET:
            field_dict["assignment_rules"] = assignment_rules
        if debrief is not UNSET:
            field_dict["debrief"] = debrief
        if description is not UNSET:
            field_dict["description"] = description
        if expressions is not UNSET:
            field_dict["expressions"] = expressions
        if follow_up is not UNSET:
            field_dict["follow_up"] = follow_up
        if on_call_readiness is not UNSET:
            field_dict["on_call_readiness"] = on_call_readiness
        if post_mortem is not UNSET:
            field_dict["post_mortem"] = post_mortem
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_group_v2 import ConditionGroupV2
        from ..models.expression_v2 import ExpressionV2
        from ..models.policy_assignment_rules_v2 import (
            PolicyAssignmentRulesV2,
        )
        from ..models.policy_debrief_v2 import PolicyDebriefV2
        from ..models.policy_follow_up_v2 import PolicyFollowUpV2
        from ..models.policy_on_call_readiness_v2 import (
            PolicyOnCallReadinessV2,
        )
        from ..models.policy_post_mortem_v2 import PolicyPostMortemV2
        from ..models.policy_schedule_v2 import PolicyScheduleV2

        d = dict(src_dict)
        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:
            conditions_item = ConditionGroupV2.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        policy_type = PolicyV2PolicyType(d.pop("policy_type"))

        status = PolicyV2Status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _assignment_rules = d.pop("assignment_rules", UNSET)
        assignment_rules: PolicyAssignmentRulesV2 | Unset
        if isinstance(_assignment_rules, Unset):
            assignment_rules = UNSET
        else:
            assignment_rules = PolicyAssignmentRulesV2.from_dict(_assignment_rules)

        _debrief = d.pop("debrief", UNSET)
        debrief: PolicyDebriefV2 | Unset
        if isinstance(_debrief, Unset):
            debrief = UNSET
        else:
            debrief = PolicyDebriefV2.from_dict(_debrief)

        description = d.pop("description", UNSET)

        _expressions = d.pop("expressions", UNSET)
        expressions: list[ExpressionV2] | Unset = UNSET
        if _expressions is not UNSET:
            expressions = []
            for expressions_item_data in _expressions:
                expressions_item = ExpressionV2.from_dict(expressions_item_data)

                expressions.append(expressions_item)

        _follow_up = d.pop("follow_up", UNSET)
        follow_up: PolicyFollowUpV2 | Unset
        if isinstance(_follow_up, Unset):
            follow_up = UNSET
        else:
            follow_up = PolicyFollowUpV2.from_dict(_follow_up)

        _on_call_readiness = d.pop("on_call_readiness", UNSET)
        on_call_readiness: PolicyOnCallReadinessV2 | Unset
        if isinstance(_on_call_readiness, Unset):
            on_call_readiness = UNSET
        else:
            on_call_readiness = PolicyOnCallReadinessV2.from_dict(_on_call_readiness)

        _post_mortem = d.pop("post_mortem", UNSET)
        post_mortem: PolicyPostMortemV2 | Unset
        if isinstance(_post_mortem, Unset):
            post_mortem = UNSET
        else:
            post_mortem = PolicyPostMortemV2.from_dict(_post_mortem)

        _schedule = d.pop("schedule", UNSET)
        schedule: PolicyScheduleV2 | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = PolicyScheduleV2.from_dict(_schedule)

        policy_v2 = cls(
            conditions=conditions,
            created_at=created_at,
            id=id,
            name=name,
            policy_type=policy_type,
            status=status,
            updated_at=updated_at,
            assignment_rules=assignment_rules,
            debrief=debrief,
            description=description,
            expressions=expressions,
            follow_up=follow_up,
            on_call_readiness=on_call_readiness,
            post_mortem=post_mortem,
            schedule=schedule,
        )

        policy_v2.additional_properties = d
        return policy_v2

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
