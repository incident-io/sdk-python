from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflows_create_workflow_payload_v2_private_incident_scope import (
    WorkflowsCreateWorkflowPayloadV2PrivateIncidentScope,
)
from ..models.workflows_create_workflow_payload_v2_runs_on_incident_modes_item import (
    WorkflowsCreateWorkflowPayloadV2RunsOnIncidentModesItem,
)
from ..models.workflows_create_workflow_payload_v2_runs_on_incidents import (
    WorkflowsCreateWorkflowPayloadV2RunsOnIncidents,
)
from ..models.workflows_create_workflow_payload_v2_state import (
    WorkflowsCreateWorkflowPayloadV2State,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2
    from ..models.expression_payload_v2 import ExpressionPayloadV2
    from ..models.step_config_payload_v2 import StepConfigPayloadV2
    from ..models.workflow_delay_v2 import WorkflowDelayV2
    from ..models.workflow_form_field_payload_v2 import WorkflowFormFieldPayloadV2
    from ..models.workflows_create_workflow_payload_v2_annotations import (
        WorkflowsCreateWorkflowPayloadV2Annotations,
    )


T = TypeVar("T", bound="WorkflowsCreateWorkflowPayloadV2")


@_attrs_define
class WorkflowsCreateWorkflowPayloadV2:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}],
            'continue_on_step_error': True, 'delay': {'conditions_apply_over_delay': False, 'for_seconds': 60},
            'expressions': [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack
            channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns':
            {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}],
            'folder': 'My folder 01', 'form_fields': [{'array': True, 'description': 'The customer affected by this
            incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'key': 'affected_customer', 'required': True, 'title': 'Affected
            customer', 'type': 'User'}], 'include_private_escalations': True, 'include_private_incidents': True, 'name': 'My
            little workflow', 'once_for': ['incident.url'], 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'private_incident_scope': 'owning_teams', 'runs_on_incident_modes': ['standard', 'test', 'retrospective'],
            'runs_on_incidents': 'newly_created', 'shortform': 'page-the-ceo', 'state': 'active', 'steps': [{'for_each':
            'abc123', 'id': 'abc123', 'name': 'pagerduty.escalate', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}]}], 'trigger': 'incident.updated'}

    Attributes:
        condition_groups (list[ConditionGroupPayloadV2]): Conditions that apply to the workflow trigger Example:
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}].
        continue_on_step_error (bool): Whether to continue executing the workflow if a step fails Example: True.
        expressions (list[ExpressionPayloadV2]): The expressions to use in the workflow Example: [{'else_branch':
            {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches':
            {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123',
            'root_reference': 'incident.status'}].
        name (str): Name provided by the user when creating the workflow Example: My little workflow.
        once_for (list[str]): This workflow will run 'once for' a list of references Example: ['incident.url'].
        runs_on_incident_modes (list[WorkflowsCreateWorkflowPayloadV2RunsOnIncidentModesItem]): Which incident modes
            should this workflow run on? By default, workflows only run on standard incidents, but can also be configured to
            run on test and retrospective incidents. Example: ['standard', 'test', 'retrospective'].
        runs_on_incidents (WorkflowsCreateWorkflowPayloadV2RunsOnIncidents): Which incidents should the workflow be
            applied to? Example: newly_created.
        steps (list[StepConfigPayloadV2]): Steps that are executed as part of the workflow Example: [{'for_each':
            'abc123', 'id': 'abc123', 'name': 'pagerduty.escalate', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}]}].
        trigger (str): Trigger to set on the workflow Example: incident.updated.
        annotations (WorkflowsCreateWorkflowPayloadV2Annotations | Unset): Annotations that track metadata about this
            resource Example: {'incident.io/terraform/version': '3.0.0'}.
        delay (WorkflowDelayV2 | Unset):  Example: {'conditions_apply_over_delay': False, 'for_seconds': 60}.
        folder (str | Unset): Folder to display the workflow in Example: My folder 01.
        form_fields (list[WorkflowFormFieldPayloadV2] | Unset): User-configured form fields available in the workflow
            scope (manual triggers only) Example: [{'array': True, 'description': 'The customer affected by this incident',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'key': 'affected_customer', 'required': True, 'title': 'Affected customer',
            'type': 'User'}].
        include_private_escalations (bool | Unset): Whether to include private escalations Example: True.
        include_private_incidents (bool | Unset): DEPRECATED: use `private_incident_scope` instead. May be sent
            alongside `private_incident_scope` only if they agree; contradictory values return a validation error. Example:
            True.
        owning_team_ids (list[str] | Unset): IDs of the teams that own this workflow Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
        private_incident_scope (WorkflowsCreateWorkflowPayloadV2PrivateIncidentScope | Unset): Which private incidents
            this workflow acts on: every private incident (all), those an owning team can see (owning_teams), or none
            Example: owning_teams.
        shortform (str | Unset): The shortform used to trigger this workflow (only applicable for manual triggers)
            Example: page-the-ceo.
        state (WorkflowsCreateWorkflowPayloadV2State | Unset): What state this workflow is in Example: active.
    """

    condition_groups: list[ConditionGroupPayloadV2]
    continue_on_step_error: bool
    expressions: list[ExpressionPayloadV2]
    name: str
    once_for: list[str]
    runs_on_incident_modes: list[
        WorkflowsCreateWorkflowPayloadV2RunsOnIncidentModesItem
    ]
    runs_on_incidents: WorkflowsCreateWorkflowPayloadV2RunsOnIncidents
    steps: list[StepConfigPayloadV2]
    trigger: str
    annotations: WorkflowsCreateWorkflowPayloadV2Annotations | Unset = UNSET
    delay: WorkflowDelayV2 | Unset = UNSET
    folder: str | Unset = UNSET
    form_fields: list[WorkflowFormFieldPayloadV2] | Unset = UNSET
    include_private_escalations: bool | Unset = UNSET
    include_private_incidents: bool | Unset = UNSET
    owning_team_ids: list[str] | Unset = UNSET
    private_incident_scope: (
        WorkflowsCreateWorkflowPayloadV2PrivateIncidentScope | Unset
    ) = UNSET
    shortform: str | Unset = UNSET
    state: WorkflowsCreateWorkflowPayloadV2State | Unset = UNSET
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

        name = self.name

        once_for = self.once_for

        runs_on_incident_modes = []
        for runs_on_incident_modes_item_data in self.runs_on_incident_modes:
            runs_on_incident_modes_item = runs_on_incident_modes_item_data.value
            runs_on_incident_modes.append(runs_on_incident_modes_item)

        runs_on_incidents = self.runs_on_incidents.value

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        trigger = self.trigger

        annotations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        delay: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delay, Unset):
            delay = self.delay.to_dict()

        folder = self.folder

        form_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.form_fields, Unset):
            form_fields = []
            for form_fields_item_data in self.form_fields:
                form_fields_item = form_fields_item_data.to_dict()
                form_fields.append(form_fields_item)

        include_private_escalations = self.include_private_escalations

        include_private_incidents = self.include_private_incidents

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        private_incident_scope: str | Unset = UNSET
        if not isinstance(self.private_incident_scope, Unset):
            private_incident_scope = self.private_incident_scope.value

        shortform = self.shortform

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_groups": condition_groups,
                "continue_on_step_error": continue_on_step_error,
                "expressions": expressions,
                "name": name,
                "once_for": once_for,
                "runs_on_incident_modes": runs_on_incident_modes,
                "runs_on_incidents": runs_on_incidents,
                "steps": steps,
                "trigger": trigger,
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if delay is not UNSET:
            field_dict["delay"] = delay
        if folder is not UNSET:
            field_dict["folder"] = folder
        if form_fields is not UNSET:
            field_dict["form_fields"] = form_fields
        if include_private_escalations is not UNSET:
            field_dict["include_private_escalations"] = include_private_escalations
        if include_private_incidents is not UNSET:
            field_dict["include_private_incidents"] = include_private_incidents
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids
        if private_incident_scope is not UNSET:
            field_dict["private_incident_scope"] = private_incident_scope
        if shortform is not UNSET:
            field_dict["shortform"] = shortform
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_group_payload_v2 import (
            ConditionGroupPayloadV2,
        )
        from ..models.expression_payload_v2 import ExpressionPayloadV2
        from ..models.step_config_payload_v2 import StepConfigPayloadV2
        from ..models.workflow_delay_v2 import WorkflowDelayV2
        from ..models.workflow_form_field_payload_v2 import (
            WorkflowFormFieldPayloadV2,
        )
        from ..models.workflows_create_workflow_payload_v2_annotations import (
            WorkflowsCreateWorkflowPayloadV2Annotations,
        )

        d = dict(src_dict)
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV2.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        continue_on_step_error = d.pop("continue_on_step_error")

        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionPayloadV2.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        name = d.pop("name")

        once_for = cast(list[str], d.pop("once_for"))

        runs_on_incident_modes = []
        _runs_on_incident_modes = d.pop("runs_on_incident_modes")
        for runs_on_incident_modes_item_data in _runs_on_incident_modes:
            runs_on_incident_modes_item = (
                WorkflowsCreateWorkflowPayloadV2RunsOnIncidentModesItem(
                    runs_on_incident_modes_item_data
                )
            )

            runs_on_incident_modes.append(runs_on_incident_modes_item)

        runs_on_incidents = WorkflowsCreateWorkflowPayloadV2RunsOnIncidents(
            d.pop("runs_on_incidents")
        )

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = StepConfigPayloadV2.from_dict(steps_item_data)

            steps.append(steps_item)

        trigger = d.pop("trigger")

        _annotations = d.pop("annotations", UNSET)
        annotations: WorkflowsCreateWorkflowPayloadV2Annotations | Unset
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = WorkflowsCreateWorkflowPayloadV2Annotations.from_dict(
                _annotations
            )

        _delay = d.pop("delay", UNSET)
        delay: WorkflowDelayV2 | Unset
        if isinstance(_delay, Unset):
            delay = UNSET
        else:
            delay = WorkflowDelayV2.from_dict(_delay)

        folder = d.pop("folder", UNSET)

        _form_fields = d.pop("form_fields", UNSET)
        form_fields: list[WorkflowFormFieldPayloadV2] | Unset = UNSET
        if _form_fields is not UNSET:
            form_fields = []
            for form_fields_item_data in _form_fields:
                form_fields_item = WorkflowFormFieldPayloadV2.from_dict(
                    form_fields_item_data
                )

                form_fields.append(form_fields_item)

        include_private_escalations = d.pop("include_private_escalations", UNSET)

        include_private_incidents = d.pop("include_private_incidents", UNSET)

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        _private_incident_scope = d.pop("private_incident_scope", UNSET)
        private_incident_scope: (
            WorkflowsCreateWorkflowPayloadV2PrivateIncidentScope | Unset
        )
        if isinstance(_private_incident_scope, Unset):
            private_incident_scope = UNSET
        else:
            private_incident_scope = (
                WorkflowsCreateWorkflowPayloadV2PrivateIncidentScope(
                    _private_incident_scope
                )
            )

        shortform = d.pop("shortform", UNSET)

        _state = d.pop("state", UNSET)
        state: WorkflowsCreateWorkflowPayloadV2State | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = WorkflowsCreateWorkflowPayloadV2State(_state)

        workflows_create_workflow_payload_v2 = cls(
            condition_groups=condition_groups,
            continue_on_step_error=continue_on_step_error,
            expressions=expressions,
            name=name,
            once_for=once_for,
            runs_on_incident_modes=runs_on_incident_modes,
            runs_on_incidents=runs_on_incidents,
            steps=steps,
            trigger=trigger,
            annotations=annotations,
            delay=delay,
            folder=folder,
            form_fields=form_fields,
            include_private_escalations=include_private_escalations,
            include_private_incidents=include_private_incidents,
            owning_team_ids=owning_team_ids,
            private_incident_scope=private_incident_scope,
            shortform=shortform,
            state=state,
        )

        workflows_create_workflow_payload_v2.additional_properties = d
        return workflows_create_workflow_payload_v2

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
