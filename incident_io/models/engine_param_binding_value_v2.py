from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EngineParamBindingValueV2")


@_attrs_define(kw_only=True)
class EngineParamBindingValueV2:
    """
    Example:
        {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}

    Attributes:
        label (str): Human readable label to be displayed for user to select Example: Lawrence Jones.
        literal (str | Unset): If set, this is the literal value of the step parameter Example: SEV123.
        reference (str | Unset): If set, this is the reference into the trigger scope that is the value of this
            parameter Example: incident.severity.
    """

    label: str
    literal: str | Unset = UNSET
    reference: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        literal = self.literal

        reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if literal is not UNSET:
            field_dict["literal"] = literal
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        label = d.pop("label")

        literal = d.pop("literal", UNSET)

        reference = d.pop("reference", UNSET)

        engine_param_binding_value_v2 = cls(
            label=label,
            literal=literal,
            reference=reference,
        )

        engine_param_binding_value_v2.additional_properties = d
        return engine_param_binding_value_v2

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
