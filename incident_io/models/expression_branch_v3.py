from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.condition_group_v3 import ConditionGroupV3
    from ..models.engine_param_binding_v3 import EngineParamBindingV3


T = TypeVar("T", bound="ExpressionBranchV3")


@_attrs_define(kw_only=True)
class ExpressionBranchV3:
    """
    Example:
        {'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}

    Attributes:
        condition_groups (list[ConditionGroupV3]): When one of these condition groups are satisfied, this branch will be
            evaluated Example: [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}].
        result (EngineParamBindingV3):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    condition_groups: list[ConditionGroupV3]
    result: EngineParamBindingV3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_groups": condition_groups,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_group_v3 import ConditionGroupV3
        from ..models.engine_param_binding_v3 import (
            EngineParamBindingV3,
        )

        d = dict(src_dict)
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupV3.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        result = EngineParamBindingV3.from_dict(d.pop("result"))

        expression_branch_v3 = cls(
            condition_groups=condition_groups,
            result=result,
        )

        expression_branch_v3.additional_properties = d
        return expression_branch_v3

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
