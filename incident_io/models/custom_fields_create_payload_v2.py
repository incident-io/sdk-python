from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_fields_create_payload_v2_field_type import (
    CustomFieldsCreatePayloadV2FieldType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_filter_by_options_v2 import CustomFieldFilterByOptionsV2
    from ..models.custom_field_fixed_filter_options_v2 import (
        CustomFieldFixedFilterOptionsV2,
    )


T = TypeVar("T", bound="CustomFieldsCreatePayloadV2")


@_attrs_define(kw_only=True)
class CustomFieldsCreatePayloadV2:
    """
    Example:
        {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'description': 'Which team is impacted by this issue',
            'field_type': 'single_select', 'filter_by': {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0',
            'custom_field_id': '01H2FW182TAH0NHEVBY34SCAK0'}, 'fixed_filter': {'catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'values': ['01H2FW182TAH0NHEVBY34SCAK0', '01H2FW182TAH0NHEVBY34SCAK1']},
            'group_by_catalog_attribute_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'helptext_catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'name': 'Affected Team'}

    Attributes:
        description (str): Description of the custom field Example: Which team is impacted by this issue.
        field_type (CustomFieldsCreatePayloadV2FieldType): Type of custom field Example: single_select.
        name (str): Human readable name for the custom field Example: Affected Team.
        catalog_type_id (str | Unset): For catalog fields, the ID of the associated catalog type Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        filter_by (CustomFieldFilterByOptionsV2 | Unset):  Example: {'catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'custom_field_id': '01H2FW182TAH0NHEVBY34SCAK0'}.
        fixed_filter (CustomFieldFixedFilterOptionsV2 | Unset):  Example: {'catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'values': ['01H2FW182TAH0NHEVBY34SCAK0', '01H2FW182TAH0NHEVBY34SCAK1']}.
        group_by_catalog_attribute_id (str | Unset): For catalog fields, the ID of the attribute used to group catalog
            entries (if applicable) Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        helptext_catalog_attribute_id (str | Unset): Which catalog attribute provides helptext for the options Example:
            01H2FW182TAH0NHEVBY34SCAK0.
    """

    description: str
    field_type: CustomFieldsCreatePayloadV2FieldType
    name: str
    catalog_type_id: str | Unset = UNSET
    filter_by: CustomFieldFilterByOptionsV2 | Unset = UNSET
    fixed_filter: CustomFieldFixedFilterOptionsV2 | Unset = UNSET
    group_by_catalog_attribute_id: str | Unset = UNSET
    helptext_catalog_attribute_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        field_type = self.field_type.value

        name = self.name

        catalog_type_id = self.catalog_type_id

        filter_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_by, Unset):
            filter_by = self.filter_by.to_dict()

        fixed_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fixed_filter, Unset):
            fixed_filter = self.fixed_filter.to_dict()

        group_by_catalog_attribute_id = self.group_by_catalog_attribute_id

        helptext_catalog_attribute_id = self.helptext_catalog_attribute_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "field_type": field_type,
                "name": name,
            }
        )
        if catalog_type_id is not UNSET:
            field_dict["catalog_type_id"] = catalog_type_id
        if filter_by is not UNSET:
            field_dict["filter_by"] = filter_by
        if fixed_filter is not UNSET:
            field_dict["fixed_filter"] = fixed_filter
        if group_by_catalog_attribute_id is not UNSET:
            field_dict["group_by_catalog_attribute_id"] = group_by_catalog_attribute_id
        if helptext_catalog_attribute_id is not UNSET:
            field_dict["helptext_catalog_attribute_id"] = helptext_catalog_attribute_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_field_filter_by_options_v2 import (
            CustomFieldFilterByOptionsV2,
        )
        from ..models.custom_field_fixed_filter_options_v2 import (
            CustomFieldFixedFilterOptionsV2,
        )

        d = dict(src_dict)
        description = d.pop("description")

        field_type = CustomFieldsCreatePayloadV2FieldType(d.pop("field_type"))

        name = d.pop("name")

        catalog_type_id = d.pop("catalog_type_id", UNSET)

        _filter_by = d.pop("filter_by", UNSET)
        filter_by: CustomFieldFilterByOptionsV2 | Unset
        if isinstance(_filter_by, Unset):
            filter_by = UNSET
        else:
            filter_by = CustomFieldFilterByOptionsV2.from_dict(_filter_by)

        _fixed_filter = d.pop("fixed_filter", UNSET)
        fixed_filter: CustomFieldFixedFilterOptionsV2 | Unset
        if isinstance(_fixed_filter, Unset):
            fixed_filter = UNSET
        else:
            fixed_filter = CustomFieldFixedFilterOptionsV2.from_dict(_fixed_filter)

        group_by_catalog_attribute_id = d.pop("group_by_catalog_attribute_id", UNSET)

        helptext_catalog_attribute_id = d.pop("helptext_catalog_attribute_id", UNSET)

        custom_fields_create_payload_v2 = cls(
            description=description,
            field_type=field_type,
            name=name,
            catalog_type_id=catalog_type_id,
            filter_by=filter_by,
            fixed_filter=fixed_filter,
            group_by_catalog_attribute_id=group_by_catalog_attribute_id,
            helptext_catalog_attribute_id=helptext_catalog_attribute_id,
        )

        custom_fields_create_payload_v2.additional_properties = d
        return custom_fields_create_payload_v2

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
