from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_engine_param_binding_payload_v3 import (
        CatalogEngineParamBindingPayloadV3,
    )


T = TypeVar("T", bound="PartialEntryPayloadV3AttributeValues")


@_attrs_define
class PartialEntryPayloadV3AttributeValues:
    """The attribute values to apply to this entry

    Example:
        {'abc123': {'array_value': [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}

    """

    additional_properties: dict[str, CatalogEngineParamBindingPayloadV3] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_engine_param_binding_payload_v3 import (
            CatalogEngineParamBindingPayloadV3,
        )

        d = dict(src_dict)
        partial_entry_payload_v3_attribute_values = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CatalogEngineParamBindingPayloadV3.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        partial_entry_payload_v3_attribute_values.additional_properties = (
            additional_properties
        )
        return partial_entry_payload_v3_attribute_values

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CatalogEngineParamBindingPayloadV3:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: CatalogEngineParamBindingPayloadV3) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
