from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_template_attribute_payload_v2 import (
        AlertTemplateAttributePayloadV2,
    )
    from ..models.engine_param_binding_payload_v2 import EngineParamBindingPayloadV2
    from ..models.engine_param_binding_value_payload_v2 import (
        EngineParamBindingValuePayloadV2,
    )
    from ..models.expression_payload_v2 import ExpressionPayloadV2


T = TypeVar("T", bound="AlertTemplatePayloadV2")


@_attrs_define
class AlertTemplatePayloadV2:
    """
    Example:
        {'attributes': [{'alert_attribute_id': 'abc123', 'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'merge_strategy': 'first_wins', 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'description': {'literal': 'SEV123', 'reference': 'incident.severity'}, 'expressions':
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
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}],
            'is_private': False, 'title': {'literal': 'SEV123', 'reference': 'incident.severity'}, 'visible_to_teams':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}

    Attributes:
        attributes (list[AlertTemplateAttributePayloadV2]): Attributes to set on alerts coming from this source, with a
            binding describing how to set them. Example: [{'alert_attribute_id': 'abc123', 'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'merge_strategy': 'first_wins', 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}].
        description (EngineParamBindingValuePayloadV2):  Example: {'literal': 'SEV123', 'reference':
            'incident.severity'}.
        expressions (list[ExpressionPayloadV2]): Expressions available for use in bindings within this template Example:
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
        title (EngineParamBindingValuePayloadV2):  Example: {'literal': 'SEV123', 'reference': 'incident.severity'}.
        is_private (bool | Unset): Whether or not alerts produced by this source should be private Example: False.
        visible_to_teams (EngineParamBindingPayloadV2 | Unset):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    attributes: list[AlertTemplateAttributePayloadV2]
    description: EngineParamBindingValuePayloadV2
    expressions: list[ExpressionPayloadV2]
    title: EngineParamBindingValuePayloadV2
    is_private: bool | Unset = UNSET
    visible_to_teams: EngineParamBindingPayloadV2 | Unset = UNSET
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

        title = self.title.to_dict()

        is_private = self.is_private

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
                "title": title,
            }
        )
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if visible_to_teams is not UNSET:
            field_dict["visible_to_teams"] = visible_to_teams

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_template_attribute_payload_v2 import (
            AlertTemplateAttributePayloadV2,
        )
        from ..models.engine_param_binding_payload_v2 import (
            EngineParamBindingPayloadV2,
        )
        from ..models.engine_param_binding_value_payload_v2 import (
            EngineParamBindingValuePayloadV2,
        )
        from ..models.expression_payload_v2 import ExpressionPayloadV2

        d = dict(src_dict)
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = AlertTemplateAttributePayloadV2.from_dict(
                attributes_item_data
            )

            attributes.append(attributes_item)

        description = EngineParamBindingValuePayloadV2.from_dict(d.pop("description"))

        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionPayloadV2.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        title = EngineParamBindingValuePayloadV2.from_dict(d.pop("title"))

        is_private = d.pop("is_private", UNSET)

        _visible_to_teams = d.pop("visible_to_teams", UNSET)
        visible_to_teams: EngineParamBindingPayloadV2 | Unset
        if isinstance(_visible_to_teams, Unset):
            visible_to_teams = UNSET
        else:
            visible_to_teams = EngineParamBindingPayloadV2.from_dict(_visible_to_teams)

        alert_template_payload_v2 = cls(
            attributes=attributes,
            description=description,
            expressions=expressions,
            title=title,
            is_private=is_private,
            visible_to_teams=visible_to_teams,
        )

        alert_template_payload_v2.additional_properties = d
        return alert_template_payload_v2

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
