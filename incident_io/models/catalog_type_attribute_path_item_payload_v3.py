from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CatalogTypeAttributePathItemPayloadV3")


@_attrs_define
class CatalogTypeAttributePathItemPayloadV3:
    """
    Example:
        {'attribute_id': 'abc123'}

    Attributes:
        attribute_id (str): the ID of the attribute to use Example: abc123.
    """

    attribute_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_id = self.attribute_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_id": attribute_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attribute_id = d.pop("attribute_id")

        catalog_type_attribute_path_item_payload_v3 = cls(
            attribute_id=attribute_id,
        )

        catalog_type_attribute_path_item_payload_v3.additional_properties = d
        return catalog_type_attribute_path_item_payload_v3

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
