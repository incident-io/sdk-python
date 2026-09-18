from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomFieldFixedFilterOptionsV2")


@_attrs_define
class CustomFieldFixedFilterOptionsV2:
    """
    Example:
        {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0', 'values': ['01H2FW182TAH0NHEVBY34SCAK0',
            '01H2FW182TAH0NHEVBY34SCAK1']}

    Attributes:
        catalog_attribute_id (str): This must be an attribute of the catalog type of this custom field. It must be an
            attribute that points to another catalog type (so not a plain string, number, or boolean attribute). Example:
            01H2FW182TAH0NHEVBY34SCAK0.
        values (list[str]): The catalog entry IDs (of the type the attribute points at) that the attribute must
            reference. The options for this custom field are restricted to entries matching one of these values. Example:
            ['01H2FW182TAH0NHEVBY34SCAK0', '01H2FW182TAH0NHEVBY34SCAK1'].
    """

    catalog_attribute_id: str
    values: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_attribute_id = self.catalog_attribute_id

        values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_attribute_id": catalog_attribute_id,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        catalog_attribute_id = d.pop("catalog_attribute_id")

        values = cast(list[str], d.pop("values"))

        custom_field_fixed_filter_options_v2 = cls(
            catalog_attribute_id=catalog_attribute_id,
            values=values,
        )

        custom_field_fixed_filter_options_v2.additional_properties = d
        return custom_field_fixed_filter_options_v2

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
