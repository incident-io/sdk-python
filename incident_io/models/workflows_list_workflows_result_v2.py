from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_slim_v2 import WorkflowSlimV2


T = TypeVar("T", bound="WorkflowsListWorkflowsResultV2")


@_attrs_define(kw_only=True)
class WorkflowsListWorkflowsResultV2:
    """
    Example:
        {'workflows': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'continue_on_step_error': True, 'delay': {'conditions_apply_over_delay': False,
            'for_seconds': 60}, 'expressions': [{'else_branch': {'result': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
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
            'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}], 'folder':
            'My folder 01', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'include_private_escalations': True,
            'include_private_incidents': True, 'name': 'My little workflow', 'once_for': [{'array': False, 'key':
            'incident.custom_field["01FCNDV6P870EA6S7TK1DSYDG0"]', 'label': 'Incident -> Affected Team', 'type':
            'IncidentSeverity'}], 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'private_incident_scope':
            'owning_teams', 'runs_from': '2021-08-17T13:28:57.801578Z', 'runs_on_incident_modes': ['standard', 'test',
            'retrospective'], 'runs_on_incidents': 'newly_created', 'shortform': 'page-the-ceo', 'state': 'active', 'steps':
            [{'label': 'PagerDuty Escalate', 'name': 'pagerduty.escalate'}], 'trigger': {'label': 'Incident Updated',
            'name': 'incident.updated'}, 'version': 3}]}

    Attributes:
        workflows (list[WorkflowSlimV2]):  Example: [{'condition_groups': [{'conditions': [{'operation': {'label':
            'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'continue_on_step_error': True, 'delay': {'conditions_apply_over_delay': False,
            'for_seconds': 60}, 'expressions': [{'else_branch': {'result': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
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
            'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}], 'folder':
            'My folder 01', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'include_private_escalations': True,
            'include_private_incidents': True, 'name': 'My little workflow', 'once_for': [{'array': False, 'key':
            'incident.custom_field["01FCNDV6P870EA6S7TK1DSYDG0"]', 'label': 'Incident -> Affected Team', 'type':
            'IncidentSeverity'}], 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'private_incident_scope':
            'owning_teams', 'runs_from': '2021-08-17T13:28:57.801578Z', 'runs_on_incident_modes': ['standard', 'test',
            'retrospective'], 'runs_on_incidents': 'newly_created', 'shortform': 'page-the-ceo', 'state': 'active', 'steps':
            [{'label': 'PagerDuty Escalate', 'name': 'pagerduty.escalate'}], 'trigger': {'label': 'Incident Updated',
            'name': 'incident.updated'}, 'version': 3}].
    """

    workflows: list[WorkflowSlimV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflows = []
        for workflows_item_data in self.workflows:
            workflows_item = workflows_item_data.to_dict()
            workflows.append(workflows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflows": workflows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_slim_v2 import WorkflowSlimV2

        d = dict(src_dict)
        workflows = []
        _workflows = d.pop("workflows")
        for workflows_item_data in _workflows:
            workflows_item = WorkflowSlimV2.from_dict(workflows_item_data)

            workflows.append(workflows_item)

        workflows_list_workflows_result_v2 = cls(
            workflows=workflows,
        )

        workflows_list_workflows_result_v2.additional_properties = d
        return workflows_list_workflows_result_v2

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
