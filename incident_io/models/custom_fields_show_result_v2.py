from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_field_v2 import CustomFieldV2


T = TypeVar("T", bound="CustomFieldsShowResultV2")


@_attrs_define(kw_only=True)
class CustomFieldsShowResultV2:
    """
    Example:
        {'custom_field': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'filter_by':
            {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0', 'custom_field_id': '01H2FW182TAH0NHEVBY34SCAK0'},
            'fixed_filter': {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0', 'values': ['01H2FW182TAH0NHEVBY34SCAK0',
            '01H2FW182TAH0NHEVBY34SCAK1']}, 'group_by_catalog_attribute_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'helptext_catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Affected Team', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        custom_field (CustomFieldV2):  Example: {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Which team is impacted by this issue', 'field_type':
            'single_select', 'filter_by': {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0', 'custom_field_id':
            '01H2FW182TAH0NHEVBY34SCAK0'}, 'fixed_filter': {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0', 'values':
            ['01H2FW182TAH0NHEVBY34SCAK0', '01H2FW182TAH0NHEVBY34SCAK1']}, 'group_by_catalog_attribute_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'helptext_catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    custom_field: CustomFieldV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_field = self.custom_field.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field": custom_field,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_field_v2 import CustomFieldV2

        d = dict(src_dict)
        custom_field = CustomFieldV2.from_dict(d.pop("custom_field"))

        custom_fields_show_result_v2 = cls(
            custom_field=custom_field,
        )

        custom_fields_show_result_v2.additional_properties = d
        return custom_fields_show_result_v2

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
