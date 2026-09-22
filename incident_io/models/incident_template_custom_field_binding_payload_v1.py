from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_template_custom_field_binding_payload_v1_merge_strategy import (
    IncidentTemplateCustomFieldBindingPayloadV1MergeStrategy,
)

if TYPE_CHECKING:
    from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3


T = TypeVar("T", bound="IncidentTemplateCustomFieldBindingPayloadV1")


@_attrs_define(kw_only=True)
class IncidentTemplateCustomFieldBindingPayloadV1:
    """
    Example:
        {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'merge_strategy':
            'first-wins'}

    Attributes:
        binding (EngineParamBindingPayloadV3):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        custom_field_id (str): ID of the custom field Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        merge_strategy (IncidentTemplateCustomFieldBindingPayloadV1MergeStrategy): The strategy to use when multiple
            alerts match this route Example: first-wins.
    """

    binding: EngineParamBindingPayloadV3
    custom_field_id: str
    merge_strategy: IncidentTemplateCustomFieldBindingPayloadV1MergeStrategy
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        binding = self.binding.to_dict()

        custom_field_id = self.custom_field_id

        merge_strategy = self.merge_strategy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "binding": binding,
                "custom_field_id": custom_field_id,
                "merge_strategy": merge_strategy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_payload_v3 import (
            EngineParamBindingPayloadV3,
        )

        d = dict(src_dict)
        binding = EngineParamBindingPayloadV3.from_dict(d.pop("binding"))

        custom_field_id = d.pop("custom_field_id")

        merge_strategy = IncidentTemplateCustomFieldBindingPayloadV1MergeStrategy(
            d.pop("merge_strategy")
        )

        incident_template_custom_field_binding_payload_v1 = cls(
            binding=binding,
            custom_field_id=custom_field_id,
            merge_strategy=merge_strategy,
        )

        incident_template_custom_field_binding_payload_v1.additional_properties = d
        return incident_template_custom_field_binding_payload_v1

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
