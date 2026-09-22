from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_value_v2 import EngineParamBindingValueV2


T = TypeVar("T", bound="EngineParamBindingV2")


@_attrs_define(kw_only=True)
class EngineParamBindingV2:
    """
    Example:
        {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}

    Attributes:
        array_value (list[EngineParamBindingValueV2] | Unset): If array_value is set, this helps render the values
            Example: [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}].
        value (EngineParamBindingValueV2 | Unset):  Example: {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}.
    """

    array_value: list[EngineParamBindingValueV2] | Unset = UNSET
    value: EngineParamBindingValueV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        array_value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.array_value, Unset):
            array_value = []
            for array_value_item_data in self.array_value:
                array_value_item = array_value_item_data.to_dict()
                array_value.append(array_value_item)

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if array_value is not UNSET:
            field_dict["array_value"] = array_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_value_v2 import (
            EngineParamBindingValueV2,
        )

        d = dict(src_dict)
        _array_value = d.pop("array_value", UNSET)
        array_value: list[EngineParamBindingValueV2] | Unset = UNSET
        if _array_value is not UNSET:
            array_value = []
            for array_value_item_data in _array_value:
                array_value_item = EngineParamBindingValueV2.from_dict(
                    array_value_item_data
                )

                array_value.append(array_value_item)

        _value = d.pop("value", UNSET)
        value: EngineParamBindingValueV2 | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = EngineParamBindingValueV2.from_dict(_value)

        engine_param_binding_v2 = cls(
            array_value=array_value,
            value=value,
        )

        engine_param_binding_v2.additional_properties = d
        return engine_param_binding_v2

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
