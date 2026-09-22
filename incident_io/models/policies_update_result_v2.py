from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.policy_v2 import PolicyV2


T = TypeVar("T", bound="PoliciesUpdateResultV2")


@_attrs_define(kw_only=True)
class PoliciesUpdateResultV2:
    """
    Example:
        {'policy': {'assignment_rules': {'bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
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
            'requirement_type': 'contiguous'}, 'status': 'enabled', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        policy (PolicyV2):  Example: {'assignment_rules': {'bindings': [{'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'reminder_cadence_after': {'interval': 'daily'},
            'reminder_cadence_before': {'interval': 'daily'}, 'reminder_detected_date_offset_hours': [0, 48],
            'reminder_due_date_offset_hours': [-24, 0, 24]}, 'conditions': [{'conditions': [{'operation': {'label':
            'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'created_at': '2021-08-17T13:28:57.801578Z', 'debrief': {'due_date_config':
            {'applies_from': '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London', 'calculation_type':
            'weekdays', 'days': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'requirements': [{'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Incident Severity', 'reference': 'incident.severity'}}]}], 'run_on_private_incidents': False}, 'description':
            'All critical incidents must export follow-ups to an external issue tracker before 7 days has passed since
            closure.', 'expressions': [{'else_branch': {'result': {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
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
            'requirement_type': 'contiguous'}, 'status': 'enabled', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    policy: PolicyV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy = self.policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policy": policy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.policy_v2 import PolicyV2

        d = dict(src_dict)
        policy = PolicyV2.from_dict(d.pop("policy"))

        policies_update_result_v2 = cls(
            policy=policy,
        )

        policies_update_result_v2.additional_properties = d
        return policies_update_result_v2

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
