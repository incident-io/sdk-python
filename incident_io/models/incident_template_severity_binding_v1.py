from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_template_severity_binding_v1_merge_strategy import (
    IncidentTemplateSeverityBindingV1MergeStrategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_v3 import EngineParamBindingV3


T = TypeVar("T", bound="IncidentTemplateSeverityBindingV1")


@_attrs_define
class IncidentTemplateSeverityBindingV1:
    """
    Example:
        {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'merge_strategy': 'first-wins'}

    Attributes:
        merge_strategy (IncidentTemplateSeverityBindingV1MergeStrategy): Strategy for merging severity when multiple
            alerts create/update the same incident Example: first-wins.
        binding (EngineParamBindingV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    merge_strategy: IncidentTemplateSeverityBindingV1MergeStrategy
    binding: EngineParamBindingV3 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merge_strategy = self.merge_strategy.value

        binding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.binding, Unset):
            binding = self.binding.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "merge_strategy": merge_strategy,
            }
        )
        if binding is not UNSET:
            field_dict["binding"] = binding

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_v3 import (
            EngineParamBindingV3,
        )

        d = dict(src_dict)
        merge_strategy = IncidentTemplateSeverityBindingV1MergeStrategy(
            d.pop("merge_strategy")
        )

        _binding = d.pop("binding", UNSET)
        binding: EngineParamBindingV3 | Unset
        if isinstance(_binding, Unset):
            binding = UNSET
        else:
            binding = EngineParamBindingV3.from_dict(_binding)

        incident_template_severity_binding_v1 = cls(
            merge_strategy=merge_strategy,
            binding=binding,
        )

        incident_template_severity_binding_v1.additional_properties = d
        return incident_template_severity_binding_v1

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
