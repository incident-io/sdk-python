from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.condition_operation_v3 import ConditionOperationV3
    from ..models.condition_subject_v3 import ConditionSubjectV3
    from ..models.engine_param_binding_v3 import EngineParamBindingV3


T = TypeVar("T", bound="ConditionV3")


@_attrs_define(kw_only=True)
class ConditionV3:
    """
    Example:
        {'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}

    Attributes:
        operation (ConditionOperationV3):  Example: {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}.
        param_bindings (list[EngineParamBindingV3]): Bindings for the operation parameters Example: [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}].
        subject (ConditionSubjectV3):  Example: {'label': 'Priority', 'reference': 'alert.priority'}.
    """

    operation: ConditionOperationV3
    param_bindings: list[EngineParamBindingV3]
    subject: ConditionSubjectV3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation.to_dict()

        param_bindings = []
        for param_bindings_item_data in self.param_bindings:
            param_bindings_item = param_bindings_item_data.to_dict()
            param_bindings.append(param_bindings_item)

        subject = self.subject.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
                "param_bindings": param_bindings,
                "subject": subject,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_operation_v3 import (
            ConditionOperationV3,
        )
        from ..models.condition_subject_v3 import ConditionSubjectV3
        from ..models.engine_param_binding_v3 import (
            EngineParamBindingV3,
        )

        d = dict(src_dict)
        operation = ConditionOperationV3.from_dict(d.pop("operation"))

        param_bindings = []
        _param_bindings = d.pop("param_bindings")
        for param_bindings_item_data in _param_bindings:
            param_bindings_item = EngineParamBindingV3.from_dict(
                param_bindings_item_data
            )

            param_bindings.append(param_bindings_item)

        subject = ConditionSubjectV3.from_dict(d.pop("subject"))

        condition_v3 = cls(
            operation=operation,
            param_bindings=param_bindings,
            subject=subject,
        )

        condition_v3.additional_properties = d
        return condition_v3

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
