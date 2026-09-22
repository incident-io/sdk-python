from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.engine_param_binding_v2 import EngineParamBindingV2


T = TypeVar("T", bound="EscalationPathV2ParamBindings")


@_attrs_define(kw_only=True)
class EscalationPathV2ParamBindings:
    """For a templated path, the values bound to the template's declared parameters, keyed by parameter name.

    Example:
        {'abc123': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}

    """

    additional_properties: dict[str, EngineParamBindingV2] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_v2 import (
            EngineParamBindingV2,
        )

        d = dict(src_dict)
        escalation_path_v2_param_bindings = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = EngineParamBindingV2.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        escalation_path_v2_param_bindings.additional_properties = additional_properties
        return escalation_path_v2_param_bindings

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> EngineParamBindingV2:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: EngineParamBindingV2) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
