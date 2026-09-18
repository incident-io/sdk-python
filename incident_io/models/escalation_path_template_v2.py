from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_v2 import EngineParamV2
    from ..models.escalation_path_repeat_config_v2 import EscalationPathRepeatConfigV2
    from ..models.escalation_path_template_node_v2 import EscalationPathTemplateNodeV2
    from ..models.expression_v2 import ExpressionV2
    from ..models.weekday_interval_config_v2 import WeekdayIntervalConfigV2


T = TypeVar("T", bound="EscalationPathTemplateV2")


@_attrs_define
class EscalationPathTemplateV2:
    """
    Example:
        {'description': 'abc123', 'expressions': [{'else_branch': {'result': {'array_value': [{'label': 'Lawrence
            Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches':
            {'branches': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
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
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}

    Attributes:
        expressions (list[ExpressionV2]): Expressions backing the template's binding targets. Example: [{'else_branch':
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
        has_historical_escalation_path_versions (bool): Whether a previous escalation path version uses this template.
            You cannot restore those versions after the template is archived. Example: False.
        id (str): Unique identifier for this template. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): The name of this template. Example: Team on-call.
        params (list[EngineParamV2]): The parameters declared by this template. Example: [{'allowed_value_types':
            ['literal'], 'array': True, 'default_value': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'description': 'What slack channel should we send the message to?', 'label': 'To date',
            'name': 'severity', 'optional': True, 'type': 'IncidentSeverity'}].
        path (list[EscalationPathTemplateNodeV2]): The nodes that form the levels and branches of this template.
            Example: [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident
            Severity', 'reference': 'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'ack_mode':
            'all', 'retry_config': {'attempts': 3, 'interval_seconds': 300}, 'round_robin_config': {'enabled': False,
            'rotate_after_seconds': 120}, 'targets': [{'binding': {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets':
            [{'binding': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}].
        description (str | Unset): A description of what this template is for. Example: abc123.
        repeat_config (EscalationPathRepeatConfigV2 | Unset):  Example: {'delay_repeat_on_activity': False,
            'repeat_after_seconds': 1800}.
        working_hours (list[WeekdayIntervalConfigV2] | Unset): The working hours for this template. Example: [{'id':
            'abc123', 'name': 'abc123', 'timezone': 'abc123', 'weekday_intervals': [{'end_time': '17:00', 'start_time':
            '09:00', 'weekday': 'monday'}]}].
    """

    expressions: list[ExpressionV2]
    has_historical_escalation_path_versions: bool
    id: str
    name: str
    params: list[EngineParamV2]
    path: list[EscalationPathTemplateNodeV2]
    description: str | Unset = UNSET
    repeat_config: EscalationPathRepeatConfigV2 | Unset = UNSET
    working_hours: list[WeekdayIntervalConfigV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expressions = []
        for expressions_item_data in self.expressions:
            expressions_item = expressions_item_data.to_dict()
            expressions.append(expressions_item)

        has_historical_escalation_path_versions = (
            self.has_historical_escalation_path_versions
        )

        id = self.id

        name = self.name

        params = []
        for params_item_data in self.params:
            params_item = params_item_data.to_dict()
            params.append(params_item)

        path = []
        for path_item_data in self.path:
            path_item = path_item_data.to_dict()
            path.append(path_item)

        description = self.description

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
                "expressions": expressions,
                "has_historical_escalation_path_versions": has_historical_escalation_path_versions,
                "id": id,
                "name": name,
                "params": params,
                "path": path,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
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
        from ..models.escalation_path_template_node_v2 import (
            EscalationPathTemplateNodeV2,
        )
        from ..models.expression_v2 import ExpressionV2
        from ..models.weekday_interval_config_v2 import (
            WeekdayIntervalConfigV2,
        )

        d = dict(src_dict)
        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionV2.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        has_historical_escalation_path_versions = d.pop(
            "has_historical_escalation_path_versions"
        )

        id = d.pop("id")

        name = d.pop("name")

        params = []
        _params = d.pop("params")
        for params_item_data in _params:
            params_item = EngineParamV2.from_dict(params_item_data)

            params.append(params_item)

        path = []
        _path = d.pop("path")
        for path_item_data in _path:
            path_item = EscalationPathTemplateNodeV2.from_dict(path_item_data)

            path.append(path_item)

        description = d.pop("description", UNSET)

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

        escalation_path_template_v2 = cls(
            expressions=expressions,
            has_historical_escalation_path_versions=has_historical_escalation_path_versions,
            id=id,
            name=name,
            params=params,
            path=path,
            description=description,
            repeat_config=repeat_config,
            working_hours=working_hours,
        )

        escalation_path_template_v2.additional_properties = d
        return escalation_path_template_v2

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
