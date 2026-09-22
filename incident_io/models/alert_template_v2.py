from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_template_attribute_v2 import AlertTemplateAttributeV2
    from ..models.engine_param_binding_v2 import EngineParamBindingV2
    from ..models.engine_param_binding_value_v2 import EngineParamBindingValueV2
    from ..models.expression_v2 import ExpressionV2


T = TypeVar("T", bound="AlertTemplateV2")


@_attrs_define(kw_only=True)
class AlertTemplateV2:
    """
    Example:
        {'attributes': [{'alert_attribute_id': 'abc123', 'binding': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'merge_strategy': 'first_wins', 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'description': {'label': 'Lawrence
            Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}, 'expressions': [{'else_branch': {'result':
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
            'is_private': False, 'title': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}, 'visible_to_teams': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}

    Attributes:
        attributes (list[AlertTemplateAttributeV2]): Attributes to set on alerts coming from this source, with a binding
            describing how to set them. Example: [{'alert_attribute_id': 'abc123', 'binding': {'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'merge_strategy': 'first_wins',
            'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}].
        description (EngineParamBindingValueV2):  Example: {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}.
        expressions (list[ExpressionV2]): Expressions available for use in bindings within this template Example:
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
        is_private (bool): Whether or not alerts produced by this source should be private Example: False.
        title (EngineParamBindingValueV2):  Example: {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}.
        visible_to_teams (EngineParamBindingV2 | Unset):  Example: {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}.
    """

    attributes: list[AlertTemplateAttributeV2]
    description: EngineParamBindingValueV2
    expressions: list[ExpressionV2]
    is_private: bool
    title: EngineParamBindingValueV2
    visible_to_teams: EngineParamBindingV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        description = self.description.to_dict()

        expressions = []
        for expressions_item_data in self.expressions:
            expressions_item = expressions_item_data.to_dict()
            expressions.append(expressions_item)

        is_private = self.is_private

        title = self.title.to_dict()

        visible_to_teams: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visible_to_teams, Unset):
            visible_to_teams = self.visible_to_teams.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "description": description,
                "expressions": expressions,
                "is_private": is_private,
                "title": title,
            }
        )
        if visible_to_teams is not UNSET:
            field_dict["visible_to_teams"] = visible_to_teams

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_template_attribute_v2 import (
            AlertTemplateAttributeV2,
        )
        from ..models.engine_param_binding_v2 import (
            EngineParamBindingV2,
        )
        from ..models.engine_param_binding_value_v2 import (
            EngineParamBindingValueV2,
        )
        from ..models.expression_v2 import ExpressionV2

        d = dict(src_dict)
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = AlertTemplateAttributeV2.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        description = EngineParamBindingValueV2.from_dict(d.pop("description"))

        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionV2.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        is_private = d.pop("is_private")

        title = EngineParamBindingValueV2.from_dict(d.pop("title"))

        _visible_to_teams = d.pop("visible_to_teams", UNSET)
        visible_to_teams: EngineParamBindingV2 | Unset
        if isinstance(_visible_to_teams, Unset):
            visible_to_teams = UNSET
        else:
            visible_to_teams = EngineParamBindingV2.from_dict(_visible_to_teams)

        alert_template_v2 = cls(
            attributes=attributes,
            description=description,
            expressions=expressions,
            is_private=is_private,
            title=title,
            visible_to_teams=visible_to_teams,
        )

        alert_template_v2.additional_properties = d
        return alert_template_v2

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
