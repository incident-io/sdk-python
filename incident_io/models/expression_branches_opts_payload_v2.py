from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.expression_branch_payload_v2 import ExpressionBranchPayloadV2
    from ..models.returns_meta_v2 import ReturnsMetaV2


T = TypeVar("T", bound="ExpressionBranchesOptsPayloadV2")


@_attrs_define(kw_only=True)
class ExpressionBranchesOptsPayloadV2:
    """
    Example:
        {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}

    Attributes:
        branches (list[ExpressionBranchPayloadV2]): The branches to apply for this operation Example:
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}].
        returns (ReturnsMetaV2):  Example: {'array': True, 'type': 'IncidentStatus'}.
    """

    branches: list[ExpressionBranchPayloadV2]
    returns: ReturnsMetaV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branches = []
        for branches_item_data in self.branches:
            branches_item = branches_item_data.to_dict()
            branches.append(branches_item)

        returns = self.returns.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branches": branches,
                "returns": returns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.expression_branch_payload_v2 import (
            ExpressionBranchPayloadV2,
        )
        from ..models.returns_meta_v2 import ReturnsMetaV2

        d = dict(src_dict)
        branches = []
        _branches = d.pop("branches")
        for branches_item_data in _branches:
            branches_item = ExpressionBranchPayloadV2.from_dict(branches_item_data)

            branches.append(branches_item)

        returns = ReturnsMetaV2.from_dict(d.pop("returns"))

        expression_branches_opts_payload_v2 = cls(
            branches=branches,
            returns=returns,
        )

        expression_branches_opts_payload_v2.additional_properties = d
        return expression_branches_opts_payload_v2

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
