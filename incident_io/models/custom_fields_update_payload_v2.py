from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_filter_by_options_v2 import CustomFieldFilterByOptionsV2
    from ..models.custom_field_fixed_filter_options_v2 import (
        CustomFieldFixedFilterOptionsV2,
    )


T = TypeVar("T", bound="CustomFieldsUpdatePayloadV2")


@_attrs_define
class CustomFieldsUpdatePayloadV2:
    """
    Example:
        {'description': 'Which team is impacted by this issue', 'filter_by': {'catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'custom_field_id': '01H2FW182TAH0NHEVBY34SCAK0'}, 'fixed_filter':
            {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0', 'values': ['01H2FW182TAH0NHEVBY34SCAK0',
            '01H2FW182TAH0NHEVBY34SCAK1']}, 'group_by_catalog_attribute_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'helptext_catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0', 'name': 'Affected Team'}

    Attributes:
        description (str): Description of the custom field Example: Which team is impacted by this issue.
        name (str): Human readable name for the custom field Example: Affected Team.
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
    name: str
    filter_by: CustomFieldFilterByOptionsV2 | Unset = UNSET
    fixed_filter: CustomFieldFixedFilterOptionsV2 | Unset = UNSET
    group_by_catalog_attribute_id: str | Unset = UNSET
    helptext_catalog_attribute_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

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
                "name": name,
            }
        )
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

        name = d.pop("name")

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

        custom_fields_update_payload_v2 = cls(
            description=description,
            name=name,
            filter_by=filter_by,
            fixed_filter=fixed_filter,
            group_by_catalog_attribute_id=group_by_catalog_attribute_id,
            helptext_catalog_attribute_id=helptext_catalog_attribute_id,
        )

        custom_fields_update_payload_v2.additional_properties = d
        return custom_fields_update_payload_v2

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
