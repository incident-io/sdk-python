from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_v2 import EngineParamBindingV2


T = TypeVar("T", bound="StepConfigV2")


@_attrs_define(kw_only=True)
class StepConfigV2:
    """
    Example:
        {'for_each': 'abc123', 'id': 'abc123', 'label': 'PagerDuty Escalate', 'name': 'pagerduty.escalate',
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}]}

    Attributes:
        id (str): Unique ID of this step in a workflow Example: abc123.
        label (str): Human readable identifier for this step Example: PagerDuty Escalate.
        name (str): Unique name of the step in the engine Example: pagerduty.escalate.
        param_bindings (list[EngineParamBindingV2]): Bindings for the step parameters Example: [{'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}].
        for_each (str | Unset): Reference to an expression that returns resources to run this step over Example: abc123.
    """

    id: str
    label: str
    name: str
    param_bindings: list[EngineParamBindingV2]
    for_each: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        name = self.name

        param_bindings = []
        for param_bindings_item_data in self.param_bindings:
            param_bindings_item = param_bindings_item_data.to_dict()
            param_bindings.append(param_bindings_item)

        for_each = self.for_each

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "name": name,
                "param_bindings": param_bindings,
            }
        )
        if for_each is not UNSET:
            field_dict["for_each"] = for_each

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_v2 import (
            EngineParamBindingV2,
        )

        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        name = d.pop("name")

        param_bindings = []
        _param_bindings = d.pop("param_bindings")
        for param_bindings_item_data in _param_bindings:
            param_bindings_item = EngineParamBindingV2.from_dict(
                param_bindings_item_data
            )

            param_bindings.append(param_bindings_item)

        for_each = d.pop("for_each", UNSET)

        step_config_v2 = cls(
            id=id,
            label=label,
            name=name,
            param_bindings=param_bindings,
            for_each=for_each,
        )

        step_config_v2.additional_properties = d
        return step_config_v2

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
