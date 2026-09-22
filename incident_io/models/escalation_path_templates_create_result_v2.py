from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.escalation_path_template_v2 import EscalationPathTemplateV2


T = TypeVar("T", bound="EscalationPathTemplatesCreateResultV2")


@_attrs_define(kw_only=True)
class EscalationPathTemplatesCreateResultV2:
    """
    Example:
        {'escalation_path_template': {'description': 'abc123', 'expressions': [{'else_branch': {'result':
            {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack
            channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation':
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
            'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}],
            'has_historical_escalation_path_versions': False, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Team on-call',
            'params': [{'allowed_value_types': ['literal'], 'array': True, 'default_value': {'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}}, 'description': 'What slack channel should we send the
            message to?', 'label': 'To date', 'name': 'severity', 'optional': True, 'type': 'IncidentSeverity'}], 'path':
            [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300, 'delay_weekday_interval_config_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config':
            {'attempts': 3, 'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120},
            'targets': [{'binding': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets':
            [{'binding': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'repeat_config': {'delay_repeat_on_activity':
            False, 'repeat_after_seconds': 1800}, 'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}}

    Attributes:
        escalation_path_template (EscalationPathTemplateV2):  Example: {'description': 'abc123', 'expressions':
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
            'has_historical_escalation_path_versions': False, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Team on-call',
            'params': [{'allowed_value_types': ['literal'], 'array': True, 'default_value': {'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}}, 'description': 'What slack channel should we send the
            message to?', 'label': 'To date', 'name': 'severity', 'optional': True, 'type': 'IncidentSeverity'}], 'path':
            [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300, 'delay_weekday_interval_config_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config':
            {'attempts': 3, 'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120},
            'targets': [{'binding': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets':
            [{'binding': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'repeat_config': {'delay_repeat_on_activity':
            False, 'repeat_after_seconds': 1800}, 'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}.
    """

    escalation_path_template: EscalationPathTemplateV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        escalation_path_template = self.escalation_path_template.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "escalation_path_template": escalation_path_template,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.escalation_path_template_v2 import (
            EscalationPathTemplateV2,
        )

        d = dict(src_dict)
        escalation_path_template = EscalationPathTemplateV2.from_dict(
            d.pop("escalation_path_template")
        )

        escalation_path_templates_create_result_v2 = cls(
            escalation_path_template=escalation_path_template,
        )

        escalation_path_templates_create_result_v2.additional_properties = d
        return escalation_path_templates_create_result_v2

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
