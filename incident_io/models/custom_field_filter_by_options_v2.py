from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomFieldFilterByOptionsV2")


@_attrs_define
class CustomFieldFilterByOptionsV2:
    """
    Example:
        {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0', 'custom_field_id': '01H2FW182TAH0NHEVBY34SCAK0'}

    Attributes:
        catalog_attribute_id (str): This must be an attribute of the catalog type of this custom field. It must be an
            attribute that points to another catalog type (so not a plain string, number, or boolean attribute). Example:
            01H2FW182TAH0NHEVBY34SCAK0.
        custom_field_id (str): This must be the ID of a custom field, which must have values of the same type as the
            attribute you are filtering by.

            When this filtering field is set on an incident, the options for this custom field will be filtered to only
            those with the attribute value that matches the value of the filtering field. Example:
            01H2FW182TAH0NHEVBY34SCAK0.
    """

    catalog_attribute_id: str
    custom_field_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_attribute_id = self.catalog_attribute_id

        custom_field_id = self.custom_field_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_attribute_id": catalog_attribute_id,
                "custom_field_id": custom_field_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        catalog_attribute_id = d.pop("catalog_attribute_id")

        custom_field_id = d.pop("custom_field_id")

        custom_field_filter_by_options_v2 = cls(
            catalog_attribute_id=catalog_attribute_id,
            custom_field_id=custom_field_id,
        )

        custom_field_filter_by_options_v2.additional_properties = d
        return custom_field_filter_by_options_v2

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
