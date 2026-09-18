from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogEntryEngineParamBindingValueV3")


@_attrs_define
class CatalogEntryEngineParamBindingValueV3:
    """
    Example:
        {'label': 'Lawrence Jones', 'literal': 'SEV123'}

    Attributes:
        label (str): A label for this attribute value. If the attribute refers to another Catalog entry, this will be
            the name of that entry. Example: Lawrence Jones.
        literal (str | Unset): The underlying value of the attribute, serialized as a string.

            For String, Text, Number, and Bool typed attributes, this will be empty. For attributes that refer to another
            catalog entry, this can be the ID, external ID, or one of the aliases of that catalog entry. Example: SEV123.
    """

    label: str
    literal: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        literal = self.literal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if literal is not UNSET:
            field_dict["literal"] = literal

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        label = d.pop("label")

        literal = d.pop("literal", UNSET)

        catalog_entry_engine_param_binding_value_v3 = cls(
            label=label,
            literal=literal,
        )

        catalog_entry_engine_param_binding_value_v3.additional_properties = d
        return catalog_entry_engine_param_binding_value_v3

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
