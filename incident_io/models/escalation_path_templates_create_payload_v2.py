from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_v2 import EngineParamV2
    from ..models.escalation_path_repeat_config_v2 import EscalationPathRepeatConfigV2
    from ..models.escalation_path_template_node_payload_v2 import (
        EscalationPathTemplateNodePayloadV2,
    )
    from ..models.expression_payload_v2 import ExpressionPayloadV2
    from ..models.weekday_interval_config_v2 import WeekdayIntervalConfigV2


T = TypeVar("T", bound="EscalationPathTemplatesCreatePayloadV2")


@_attrs_define
class EscalationPathTemplatesCreatePayloadV2:
    """
    Example:
        {'description': 'Pages the team on-call, then a fallback user', 'expressions': [{'else_branch': {'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123',
            'root_reference': 'incident.status'}], 'name': 'Team on-call', 'params': [{'allowed_value_types': ['literal'],
            'array': True, 'default_value': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'description': 'What slack channel should we send the message to?', 'label': 'To date',
            'name': 'severity', 'optional': True, 'type': 'IncidentSeverity'}], 'path': [{'delay':
            {'delay_interval_condition': 'active', 'delay_seconds': 300, 'delay_weekday_interval_config_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}], 'then_path': [{}]},
            'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3, 'interval_seconds': 300}, 'round_robin_config':
            {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'binding': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'notify_channel': {'targets': [{'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'repeat': {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'repeat_config':
            {'delay_repeat_on_activity': False, 'repeat_after_seconds': 1800}, 'working_hours': [{'id': 'abc123', 'name':
            'abc123', 'timezone': 'abc123', 'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}]}]}

    Attributes:
        name (str): The name of this template, for the user's reference. Example: Team on-call.
        path (list[EscalationPathTemplateNodePayloadV2]): The nodes that form the levels and branches of this template.
            Example: [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}],
            'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3, 'interval_seconds': 300},
            'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets':
            [{'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode':
            'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}].
        description (str | Unset): A description of what this template is for. Example: Pages the team on-call, then a
            fallback user.
        expressions (list[ExpressionPayloadV2] | Unset): Expressions backing the template's binding targets. Example:
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}].
        params (list[EngineParamV2] | Unset): The parameters declared by this template, bound per templated path.
            Example: [{'allowed_value_types': ['literal'], 'array': True, 'default_value': {'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}}, 'description': 'What slack channel should we send the
            message to?', 'label': 'To date', 'name': 'severity', 'optional': True, 'type': 'IncidentSeverity'}].
        repeat_config (EscalationPathRepeatConfigV2 | Unset):  Example: {'delay_repeat_on_activity': False,
            'repeat_after_seconds': 1800}.
        working_hours (list[WeekdayIntervalConfigV2] | Unset): The working hours for this template. Example: [{'id':
            'abc123', 'name': 'abc123', 'timezone': 'abc123', 'weekday_intervals': [{'end_time': '17:00', 'start_time':
            '09:00', 'weekday': 'monday'}]}].
    """

    name: str
    path: list[EscalationPathTemplateNodePayloadV2]
    description: str | Unset = UNSET
    expressions: list[ExpressionPayloadV2] | Unset = UNSET
    params: list[EngineParamV2] | Unset = UNSET
    repeat_config: EscalationPathRepeatConfigV2 | Unset = UNSET
    working_hours: list[WeekdayIntervalConfigV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = []
        for path_item_data in self.path:
            path_item = path_item_data.to_dict()
            path.append(path_item)

        description = self.description

        expressions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expressions, Unset):
            expressions = []
            for expressions_item_data in self.expressions:
                expressions_item = expressions_item_data.to_dict()
                expressions.append(expressions_item)

        params: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = []
            for params_item_data in self.params:
                params_item = params_item_data.to_dict()
                params.append(params_item)

        repeat_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repeat_config, Unset):
            repeat_config = self.repeat_config.to_dict()

        working_hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.working_hours, Unset):
            working_hours = []
            for working_hours_item_data in self.working_hours:
                working_hours_item = working_hours_item_data.to_dict()
                working_hours.append(working_hours_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "path": path,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if expressions is not UNSET:
            field_dict["expressions"] = expressions
        if params is not UNSET:
            field_dict["params"] = params
        if repeat_config is not UNSET:
            field_dict["repeat_config"] = repeat_config
        if working_hours is not UNSET:
            field_dict["working_hours"] = working_hours

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_v2 import EngineParamV2
        from ..models.escalation_path_repeat_config_v2 import (
            EscalationPathRepeatConfigV2,
        )
        from ..models.escalation_path_template_node_payload_v2 import (
            EscalationPathTemplateNodePayloadV2,
        )
        from ..models.expression_payload_v2 import ExpressionPayloadV2
        from ..models.weekday_interval_config_v2 import (
            WeekdayIntervalConfigV2,
        )

        d = dict(src_dict)
        name = d.pop("name")

        path = []
        _path = d.pop("path")
        for path_item_data in _path:
            path_item = EscalationPathTemplateNodePayloadV2.from_dict(path_item_data)

            path.append(path_item)

        description = d.pop("description", UNSET)

        _expressions = d.pop("expressions", UNSET)
        expressions: list[ExpressionPayloadV2] | Unset = UNSET
        if _expressions is not UNSET:
            expressions = []
            for expressions_item_data in _expressions:
                expressions_item = ExpressionPayloadV2.from_dict(expressions_item_data)

                expressions.append(expressions_item)

        _params = d.pop("params", UNSET)
        params: list[EngineParamV2] | Unset = UNSET
        if _params is not UNSET:
            params = []
            for params_item_data in _params:
                params_item = EngineParamV2.from_dict(params_item_data)

                params.append(params_item)

        _repeat_config = d.pop("repeat_config", UNSET)
        repeat_config: EscalationPathRepeatConfigV2 | Unset
        if isinstance(_repeat_config, Unset):
            repeat_config = UNSET
        else:
            repeat_config = EscalationPathRepeatConfigV2.from_dict(_repeat_config)

        _working_hours = d.pop("working_hours", UNSET)
        working_hours: list[WeekdayIntervalConfigV2] | Unset = UNSET
        if _working_hours is not UNSET:
            working_hours = []
            for working_hours_item_data in _working_hours:
                working_hours_item = WeekdayIntervalConfigV2.from_dict(
                    working_hours_item_data
                )

                working_hours.append(working_hours_item)

        escalation_path_templates_create_payload_v2 = cls(
            name=name,
            path=path,
            description=description,
            expressions=expressions,
            params=params,
            repeat_config=repeat_config,
            working_hours=working_hours,
        )

        escalation_path_templates_create_payload_v2.additional_properties = d
        return escalation_path_templates_create_payload_v2

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
