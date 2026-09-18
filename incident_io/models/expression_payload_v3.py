from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expression_else_branch_payload_v3 import ExpressionElseBranchPayloadV3
    from ..models.expression_operation_payload_v3 import ExpressionOperationPayloadV3


T = TypeVar("T", bound="ExpressionPayloadV3")


@_attrs_define
class ExpressionPayloadV3:
    """
    Example:
        {'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}

    Attributes:
        label (str): The human readable label of the expression Example: Team Slack channel.
        operations (list[ExpressionOperationPayloadV3]):  Example: [{'branches': {'branches': [{'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}].
        reference (str): A short ID that can be used to reference the expression Example: abc123.
        root_reference (str): The root reference for this expression (i.e. where the expression starts) Example:
            incident.status.
        else_branch (ExpressionElseBranchPayloadV3 | Unset):  Example: {'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}.
    """

    label: str
    operations: list[ExpressionOperationPayloadV3]
    reference: str
    root_reference: str
    else_branch: ExpressionElseBranchPayloadV3 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()
            operations.append(operations_item)

        reference = self.reference

        root_reference = self.root_reference

        else_branch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.else_branch, Unset):
            else_branch = self.else_branch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "operations": operations,
                "reference": reference,
                "root_reference": root_reference,
            }
        )
        if else_branch is not UNSET:
            field_dict["else_branch"] = else_branch

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.expression_else_branch_payload_v3 import (
            ExpressionElseBranchPayloadV3,
        )
        from ..models.expression_operation_payload_v3 import (
            ExpressionOperationPayloadV3,
        )

        d = dict(src_dict)
        label = d.pop("label")

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = ExpressionOperationPayloadV3.from_dict(
                operations_item_data
            )

            operations.append(operations_item)

        reference = d.pop("reference")

        root_reference = d.pop("root_reference")

        _else_branch = d.pop("else_branch", UNSET)
        else_branch: ExpressionElseBranchPayloadV3 | Unset
        if isinstance(_else_branch, Unset):
            else_branch = UNSET
        else:
            else_branch = ExpressionElseBranchPayloadV3.from_dict(_else_branch)

        expression_payload_v3 = cls(
            label=label,
            operations=operations,
            reference=reference,
            root_reference=root_reference,
            else_branch=else_branch,
        )

        expression_payload_v3.additional_properties = d
        return expression_payload_v3

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
