from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.engine_param_v2_allowed_value_types_item import (
    EngineParamV2AllowedValueTypesItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_v2 import EngineParamBindingV2


T = TypeVar("T", bound="EngineParamV2")


@_attrs_define
class EngineParamV2:
    """
    Example:
        {'allowed_value_types': ['literal'], 'array': True, 'default_value': {'array_value': [{'label': 'Lawrence
            Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'description': 'What slack channel should we send the message
            to?', 'label': 'To date', 'name': 'severity', 'optional': True, 'type': 'IncidentSeverity'}

    Attributes:
        array (bool): Whether this parameter is an array Example: True.
        description (str): A string describing the param Example: What slack channel should we send the message to?.
        label (str): Human readable label for this parameter Example: To date.
        name (str): The unique identifier for the parameter Example: severity.
        optional (bool): Whether this parameter is optional Example: True.
        type_ (str): The type of the parameter Example: IncidentSeverity.
        allowed_value_types (list[EngineParamV2AllowedValueTypesItem] | Unset): Which kinds of binding the dashboard
            should offer for this parameter. When empty, all types are allowed. Example: ['literal'].
        default_value (EngineParamBindingV2 | Unset):  Example: {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}.
    """

    array: bool
    description: str
    label: str
    name: str
    optional: bool
    type_: str
    allowed_value_types: list[EngineParamV2AllowedValueTypesItem] | Unset = UNSET
    default_value: EngineParamBindingV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        array = self.array

        description = self.description

        label = self.label

        name = self.name

        optional = self.optional

        type_ = self.type_

        allowed_value_types: list[str] | Unset = UNSET
        if not isinstance(self.allowed_value_types, Unset):
            allowed_value_types = []
            for allowed_value_types_item_data in self.allowed_value_types:
                allowed_value_types_item = allowed_value_types_item_data.value
                allowed_value_types.append(allowed_value_types_item)

        default_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "description": description,
                "label": label,
                "name": name,
                "optional": optional,
                "type": type_,
            }
        )
        if allowed_value_types is not UNSET:
            field_dict["allowed_value_types"] = allowed_value_types
        if default_value is not UNSET:
            field_dict["default_value"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_v2 import (
            EngineParamBindingV2,
        )

        d = dict(src_dict)
        array = d.pop("array")

        description = d.pop("description")

        label = d.pop("label")

        name = d.pop("name")

        optional = d.pop("optional")

        type_ = d.pop("type")

        _allowed_value_types = d.pop("allowed_value_types", UNSET)
        allowed_value_types: list[EngineParamV2AllowedValueTypesItem] | Unset = UNSET
        if _allowed_value_types is not UNSET:
            allowed_value_types = []
            for allowed_value_types_item_data in _allowed_value_types:
                allowed_value_types_item = EngineParamV2AllowedValueTypesItem(
                    allowed_value_types_item_data
                )

                allowed_value_types.append(allowed_value_types_item)

        _default_value = d.pop("default_value", UNSET)
        default_value: EngineParamBindingV2 | Unset
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = EngineParamBindingV2.from_dict(_default_value)

        engine_param_v2 = cls(
            array=array,
            description=description,
            label=label,
            name=name,
            optional=optional,
            type_=type_,
            allowed_value_types=allowed_value_types,
            default_value=default_value,
        )

        engine_param_v2.additional_properties = d
        return engine_param_v2

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
