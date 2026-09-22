from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.escalation_path_v2 import EscalationPathV2


T = TypeVar("T", bound="EscalationsUpdatePathResultV2")


@_attrs_define(kw_only=True)
class EscalationsUpdatePathResultV2:
    """
    Example:
        {'escalation_path': {'current_responders': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}], 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'kind': 'templated', 'name': 'Urgent Support', 'param_bindings': {'abc123':
            {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'path': [{'delay':
            {'delay_interval_condition': 'active', 'delay_seconds': 300, 'delay_weekday_interval_config_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config':
            {'attempts': 3, 'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120},
            'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'notify_channel': {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'repeat': {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'repeat_config':
            {'delay_repeat_on_activity': False, 'repeat_after_seconds': 1800}, 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'],
            'template_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone':
            'abc123', 'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}}

    Attributes:
        escalation_path (EscalationPathV2):  Example: {'current_responders': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'kind': 'templated', 'name': 'Urgent Support', 'param_bindings': {'abc123':
            {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'path': [{'delay':
            {'delay_interval_condition': 'active', 'delay_seconds': 300, 'delay_weekday_interval_config_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config':
            {'attempts': 3, 'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120},
            'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'notify_channel': {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'repeat': {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'repeat_config':
            {'delay_repeat_on_activity': False, 'repeat_after_seconds': 1800}, 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'],
            'template_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone':
            'abc123', 'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}.
    """

    escalation_path: EscalationPathV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        escalation_path = self.escalation_path.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "escalation_path": escalation_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.escalation_path_v2 import EscalationPathV2

        d = dict(src_dict)
        escalation_path = EscalationPathV2.from_dict(d.pop("escalation_path"))

        escalations_update_path_result_v2 = cls(
            escalation_path=escalation_path,
        )

        escalations_update_path_result_v2.additional_properties = d
        return escalations_update_path_result_v2

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
