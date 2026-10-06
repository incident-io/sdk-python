from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_forms_create_payload_v3_form_type import (
    IncidentFormsCreatePayloadV3FormType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expression_payload_v3 import ExpressionPayloadV3
    from ..models.incident_form_lifecycle_element_payload_v3 import (
        IncidentFormLifecycleElementPayloadV3,
    )


T = TypeVar("T", bound="IncidentFormsCreatePayloadV3")


@_attrs_define(kw_only=True)
class IncidentFormsCreatePayloadV3:
    """
    Example:
        {'expressions': [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack
            channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns':
            {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}],
            'form_type': 'declare', 'incident_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'lifecycle_elements':
            [{'can_select_no_value': False, 'config': {'require_comment': False}, 'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'default_value': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'description': 'Shown
            when the incident is major or above.', 'element_type': 'name', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'placeholder': "What's happening?", 'required_if': 'check_engine_config', 'required_if_condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}], 'show_if_condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}]}]}

    Attributes:
        expressions (list[ExpressionPayloadV3]): Expressions available to every element's conditions and defaults.
            Referenced by reference, not by ID. Example: [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label':
            'Team Slack channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}].
        form_type (IncidentFormsCreatePayloadV3FormType): Which form this is. Escalate forms are not part of this API.
            Example: declare.
        incident_type_id (str | Unset): The incident type this form belongs to. Leave unset for the organisation's
            default form of this type. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        lifecycle_elements (list[IncidentFormLifecycleElementPayloadV3] | Unset): Elements on this form, in display
            order. List position is the order: there is no separate rank. Example: [{'can_select_no_value': False, 'config':
            {'require_comment': False}, 'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'default_value': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'description': 'Shown when the incident is major or above.', 'element_type': 'name',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'placeholder': "What's happening?", 'required_if': 'check_engine_config',
            'required_if_condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'show_if_condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}].
    """

    expressions: list[ExpressionPayloadV3]
    form_type: IncidentFormsCreatePayloadV3FormType
    incident_type_id: str | Unset = UNSET
    lifecycle_elements: list[IncidentFormLifecycleElementPayloadV3] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expressions = []
        for expressions_item_data in self.expressions:
            expressions_item = expressions_item_data.to_dict()
            expressions.append(expressions_item)

        form_type = self.form_type.value

        incident_type_id = self.incident_type_id

        lifecycle_elements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lifecycle_elements, Unset):
            lifecycle_elements = []
            for lifecycle_elements_item_data in self.lifecycle_elements:
                lifecycle_elements_item = lifecycle_elements_item_data.to_dict()
                lifecycle_elements.append(lifecycle_elements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expressions": expressions,
                "form_type": form_type,
            }
        )
        if incident_type_id is not UNSET:
            field_dict["incident_type_id"] = incident_type_id
        if lifecycle_elements is not UNSET:
            field_dict["lifecycle_elements"] = lifecycle_elements

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.expression_payload_v3 import ExpressionPayloadV3
        from ..models.incident_form_lifecycle_element_payload_v3 import (
            IncidentFormLifecycleElementPayloadV3,
        )

        d = dict(src_dict)
        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionPayloadV3.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        form_type = IncidentFormsCreatePayloadV3FormType(d.pop("form_type"))

        incident_type_id = d.pop("incident_type_id", UNSET)

        _lifecycle_elements = d.pop("lifecycle_elements", UNSET)
        lifecycle_elements: list[IncidentFormLifecycleElementPayloadV3] | Unset = UNSET
        if _lifecycle_elements is not UNSET:
            lifecycle_elements = []
            for lifecycle_elements_item_data in _lifecycle_elements:
                lifecycle_elements_item = (
                    IncidentFormLifecycleElementPayloadV3.from_dict(
                        lifecycle_elements_item_data
                    )
                )

                lifecycle_elements.append(lifecycle_elements_item)

        incident_forms_create_payload_v3 = cls(
            expressions=expressions,
            form_type=form_type,
            incident_type_id=incident_type_id,
            lifecycle_elements=lifecycle_elements,
        )

        incident_forms_create_payload_v3.additional_properties = d
        return incident_forms_create_payload_v3

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
