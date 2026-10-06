from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_form_v3 import IncidentFormV3


T = TypeVar("T", bound="IncidentFormsUpdateResultV3")


@_attrs_define(kw_only=True)
class IncidentFormsUpdateResultV3:
    """
    Example:
        {'incident_form': {'created_at': '2021-08-17T13:28:57.801578Z', 'expressions': [{'else_branch': {'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate':
            {'reference': '1235', 'reference_label': 'Teams'}, 'filter': {'condition_groups': [{'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}]}, 'navigate':
            {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}, 'returns': {'array':
            True, 'type': 'IncidentStatus'}}], 'reference': 'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'},
            'root_reference': 'incident.status'}], 'form_type': 'declare', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'lifecycle_elements': [{'can_select_no_value': False,
            'config': {'require_comment': False}, 'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'default_value':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'description': 'Shown when the incident is major or above.', 'element_type':
            'name', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'placeholder': "What's happening?", 'required_if':
            'check_engine_config', 'required_if_condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence
            Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}], 'show_if_condition_groups': [{'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}]}],
            'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        incident_form (IncidentFormV3):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'expressions':
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones',
            'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate':
            {'reference': '1235', 'reference_label': 'Teams'}, 'filter': {'condition_groups': [{'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}]}, 'navigate':
            {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}, 'returns': {'array':
            True, 'type': 'IncidentStatus'}}], 'reference': 'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'},
            'root_reference': 'incident.status'}], 'form_type': 'declare', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'lifecycle_elements': [{'can_select_no_value': False,
            'config': {'require_comment': False}, 'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'default_value':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'description': 'Shown when the incident is major or above.', 'element_type':
            'name', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'placeholder': "What's happening?", 'required_if':
            'check_engine_config', 'required_if_condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence
            Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}], 'show_if_condition_groups': [{'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}]}],
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    incident_form: IncidentFormV3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_form = self.incident_form.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_form": incident_form,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_form_v3 import IncidentFormV3

        d = dict(src_dict)
        incident_form = IncidentFormV3.from_dict(d.pop("incident_form"))

        incident_forms_update_result_v3 = cls(
            incident_form=incident_form,
        )

        incident_forms_update_result_v3.additional_properties = d
        return incident_forms_update_result_v3

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
