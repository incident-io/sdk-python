from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.condition_v2 import ConditionV2
    from ..models.escalation_path_node_v2 import EscalationPathNodeV2


T = TypeVar("T", bound="EscalationPathNodeIfElseV2")


@_attrs_define
class EscalationPathNodeIfElseV2:
    """
    Example:
        {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}],
            'else_path': [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident
            Severity', 'reference': 'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'ack_mode':
            'all', 'retry_config': {'attempts': 3, 'interval_seconds': 300}, 'round_robin_config': {'enabled': False,
            'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type':
            'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'then_path': [{'delay':
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
            'repeat': {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}]}

    Attributes:
        conditions (list[ConditionV2]): The condition that defines which branch to take Example: [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident
            Severity', 'reference': 'incident.severity'}}].
        else_path (list[EscalationPathNodeV2]): The nodes that form the levels if our condition is not met Example:
            [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300, 'delay_weekday_interval_config_id':
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
            'repeat': {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}].
        then_path (list[EscalationPathNodeV2]): The nodes that form the levels if our condition is met Example:
            [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300, 'delay_weekday_interval_config_id':
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
            'repeat': {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}].
    """

    conditions: list[ConditionV2]
    else_path: list[EscalationPathNodeV2]
    then_path: list[EscalationPathNodeV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item = conditions_item_data.to_dict()
            conditions.append(conditions_item)

        else_path = []
        for else_path_item_data in self.else_path:
            else_path_item = else_path_item_data.to_dict()
            else_path.append(else_path_item)

        then_path = []
        for then_path_item_data in self.then_path:
            then_path_item = then_path_item_data.to_dict()
            then_path.append(then_path_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditions": conditions,
                "else_path": else_path,
                "then_path": then_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_v2 import ConditionV2
        from ..models.escalation_path_node_v2 import (
            EscalationPathNodeV2,
        )

        d = dict(src_dict)
        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:
            conditions_item = ConditionV2.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        else_path = []
        _else_path = d.pop("else_path")
        for else_path_item_data in _else_path:
            else_path_item = EscalationPathNodeV2.from_dict(else_path_item_data)

            else_path.append(else_path_item)

        then_path = []
        _then_path = d.pop("then_path")
        for then_path_item_data in _then_path:
            then_path_item = EscalationPathNodeV2.from_dict(then_path_item_data)

            then_path.append(then_path_item)

        escalation_path_node_if_else_v2 = cls(
            conditions=conditions,
            else_path=else_path,
            then_path=then_path,
        )

        escalation_path_node_if_else_v2.additional_properties = d
        return escalation_path_node_if_else_v2

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
