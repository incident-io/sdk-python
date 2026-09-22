from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_slim_v2_private_incident_scope import (
    WorkflowSlimV2PrivateIncidentScope,
)
from ..models.workflow_slim_v2_runs_on_incident_modes_item import (
    WorkflowSlimV2RunsOnIncidentModesItem,
)
from ..models.workflow_slim_v2_runs_on_incidents import WorkflowSlimV2RunsOnIncidents
from ..models.workflow_slim_v2_state import WorkflowSlimV2State
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_group_v2 import ConditionGroupV2
    from ..models.engine_reference_v2 import EngineReferenceV2
    from ..models.expression_v2 import ExpressionV2
    from ..models.step_config_slim_v2 import StepConfigSlimV2
    from ..models.trigger_slim_v2 import TriggerSlimV2
    from ..models.workflow_delay_v2 import WorkflowDelayV2


T = TypeVar("T", bound="WorkflowSlimV2")


@_attrs_define(kw_only=True)
class WorkflowSlimV2:
    """
    Example:
        {'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
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
            'name': 'incident.updated'}, 'version': 3}

    Attributes:
        condition_groups (list[ConditionGroupV2]): Conditions that apply to the workflow trigger Example:
            [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}]}].
        continue_on_step_error (bool): Whether to continue executing the workflow if a step fails Example: True.
        expressions (list[ExpressionV2]): Expressions that make variables available in the scope Example:
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
            'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}].
        id (str): Unique identifier for the workflow Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        include_private_escalations (bool): Whether to include private escalations Example: True.
        include_private_incidents (bool): DEPRECATED: use `private_incident_scope` instead. `true` when the workflow
            runs on private incidents (a `private_incident_scope` of `all` or `owning_teams`), `false` when the scope is
            `none`. Example: True.
        name (str): Name provided by the user when creating the workflow Example: My little workflow.
        once_for (list[EngineReferenceV2]): This workflow will run 'once for' a list of references Example: [{'array':
            False, 'key': 'incident.custom_field["01FCNDV6P870EA6S7TK1DSYDG0"]', 'label': 'Incident -> Affected Team',
            'type': 'IncidentSeverity'}].
        private_incident_scope (WorkflowSlimV2PrivateIncidentScope): Which private incidents this workflow acts on:
            every private incident (all), those an owning team can see (owning_teams), or none Example: owning_teams.
        runs_on_incident_modes (list[WorkflowSlimV2RunsOnIncidentModesItem]): Which incident modes should this workflow
            run on? By default, workflows only run on standard incidents, but can also be configured to run on test and
            retrospective incidents. Example: ['standard', 'test', 'retrospective'].
        runs_on_incidents (WorkflowSlimV2RunsOnIncidents): Which incidents should the workflow be applied to? Example:
            newly_created.
        state (WorkflowSlimV2State): What state this workflow is in Example: active.
        steps (list[StepConfigSlimV2]): Steps that are executed as part of the workflow Example: [{'label': 'PagerDuty
            Escalate', 'name': 'pagerduty.escalate'}].
        trigger (TriggerSlimV2):  Example: {'label': 'Incident Updated', 'name': 'incident.updated'}.
        version (int): Revision of the workflow, uniquely identifying it's version Example: 3.
        delay (WorkflowDelayV2 | Unset):  Example: {'conditions_apply_over_delay': False, 'for_seconds': 60}.
        folder (str | Unset): Folder to display the workflow in Example: My folder 01.
        owning_team_ids (list[str] | Unset): IDs of the teams that own this workflow Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
        runs_from (datetime.datetime | Unset): The time from which this workflow will run on incidents Example:
            2021-08-17T13:28:57.801578Z.
        shortform (str | Unset): The shortform used to trigger this workflow (only applicable for manual triggers)
            Example: page-the-ceo.
    """

    condition_groups: list[ConditionGroupV2]
    continue_on_step_error: bool
    expressions: list[ExpressionV2]
    id: str
    include_private_escalations: bool
    include_private_incidents: bool
    name: str
    once_for: list[EngineReferenceV2]
    private_incident_scope: WorkflowSlimV2PrivateIncidentScope
    runs_on_incident_modes: list[WorkflowSlimV2RunsOnIncidentModesItem]
    runs_on_incidents: WorkflowSlimV2RunsOnIncidents
    state: WorkflowSlimV2State
    steps: list[StepConfigSlimV2]
    trigger: TriggerSlimV2
    version: int
    delay: WorkflowDelayV2 | Unset = UNSET
    folder: str | Unset = UNSET
    owning_team_ids: list[str] | Unset = UNSET
    runs_from: datetime.datetime | Unset = UNSET
    shortform: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        continue_on_step_error = self.continue_on_step_error

        expressions = []
        for expressions_item_data in self.expressions:
            expressions_item = expressions_item_data.to_dict()
            expressions.append(expressions_item)

        id = self.id

        include_private_escalations = self.include_private_escalations

        include_private_incidents = self.include_private_incidents

        name = self.name

        once_for = []
        for once_for_item_data in self.once_for:
            once_for_item = once_for_item_data.to_dict()
            once_for.append(once_for_item)

        private_incident_scope = self.private_incident_scope.value

        runs_on_incident_modes = []
        for runs_on_incident_modes_item_data in self.runs_on_incident_modes:
            runs_on_incident_modes_item = runs_on_incident_modes_item_data.value
            runs_on_incident_modes.append(runs_on_incident_modes_item)

        runs_on_incidents = self.runs_on_incidents.value

        state = self.state.value

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        trigger = self.trigger.to_dict()

        version = self.version

        delay: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delay, Unset):
            delay = self.delay.to_dict()

        folder = self.folder

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        runs_from: str | Unset = UNSET
        if not isinstance(self.runs_from, Unset):
            runs_from = self.runs_from.isoformat()

        shortform = self.shortform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_groups": condition_groups,
                "continue_on_step_error": continue_on_step_error,
                "expressions": expressions,
                "id": id,
                "include_private_escalations": include_private_escalations,
                "include_private_incidents": include_private_incidents,
                "name": name,
                "once_for": once_for,
                "private_incident_scope": private_incident_scope,
                "runs_on_incident_modes": runs_on_incident_modes,
                "runs_on_incidents": runs_on_incidents,
                "state": state,
                "steps": steps,
                "trigger": trigger,
                "version": version,
            }
        )
        if delay is not UNSET:
            field_dict["delay"] = delay
        if folder is not UNSET:
            field_dict["folder"] = folder
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids
        if runs_from is not UNSET:
            field_dict["runs_from"] = runs_from
        if shortform is not UNSET:
            field_dict["shortform"] = shortform

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_group_v2 import ConditionGroupV2
        from ..models.engine_reference_v2 import EngineReferenceV2
        from ..models.expression_v2 import ExpressionV2
        from ..models.step_config_slim_v2 import StepConfigSlimV2
        from ..models.trigger_slim_v2 import TriggerSlimV2
        from ..models.workflow_delay_v2 import WorkflowDelayV2

        d = dict(src_dict)
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupV2.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        continue_on_step_error = d.pop("continue_on_step_error")

        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionV2.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        id = d.pop("id")

        include_private_escalations = d.pop("include_private_escalations")

        include_private_incidents = d.pop("include_private_incidents")

        name = d.pop("name")

        once_for = []
        _once_for = d.pop("once_for")
        for once_for_item_data in _once_for:
            once_for_item = EngineReferenceV2.from_dict(once_for_item_data)

            once_for.append(once_for_item)

        private_incident_scope = WorkflowSlimV2PrivateIncidentScope(
            d.pop("private_incident_scope")
        )

        runs_on_incident_modes = []
        _runs_on_incident_modes = d.pop("runs_on_incident_modes")
        for runs_on_incident_modes_item_data in _runs_on_incident_modes:
            runs_on_incident_modes_item = WorkflowSlimV2RunsOnIncidentModesItem(
                runs_on_incident_modes_item_data
            )

            runs_on_incident_modes.append(runs_on_incident_modes_item)

        runs_on_incidents = WorkflowSlimV2RunsOnIncidents(d.pop("runs_on_incidents"))

        state = WorkflowSlimV2State(d.pop("state"))

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = StepConfigSlimV2.from_dict(steps_item_data)

            steps.append(steps_item)

        trigger = TriggerSlimV2.from_dict(d.pop("trigger"))

        version = d.pop("version")

        _delay = d.pop("delay", UNSET)
        delay: WorkflowDelayV2 | Unset
        if isinstance(_delay, Unset):
            delay = UNSET
        else:
            delay = WorkflowDelayV2.from_dict(_delay)

        folder = d.pop("folder", UNSET)

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        _runs_from = d.pop("runs_from", UNSET)
        runs_from: datetime.datetime | Unset
        if isinstance(_runs_from, Unset):
            runs_from = UNSET
        else:
            runs_from = datetime.datetime.fromisoformat(_runs_from)

        shortform = d.pop("shortform", UNSET)

        workflow_slim_v2 = cls(
            condition_groups=condition_groups,
            continue_on_step_error=continue_on_step_error,
            expressions=expressions,
            id=id,
            include_private_escalations=include_private_escalations,
            include_private_incidents=include_private_incidents,
            name=name,
            once_for=once_for,
            private_incident_scope=private_incident_scope,
            runs_on_incident_modes=runs_on_incident_modes,
            runs_on_incidents=runs_on_incidents,
            state=state,
            steps=steps,
            trigger=trigger,
            version=version,
            delay=delay,
            folder=folder,
            owning_team_ids=owning_team_ids,
            runs_from=runs_from,
            shortform=shortform,
        )

        workflow_slim_v2.additional_properties = d
        return workflow_slim_v2

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
