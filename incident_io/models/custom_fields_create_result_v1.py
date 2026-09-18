from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_field_v1 import CustomFieldV1


T = TypeVar("T", bound="CustomFieldsCreateResultV1")


@_attrs_define
class CustomFieldsCreateResultV1:
    """
    Example:
        {'custom_field': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}],
            'required': 'never', 'required_v2': 'never', 'show_before_closure': True, 'show_before_creation': True,
            'show_before_update': True, 'show_in_announcement_post': True, 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        custom_field (CustomFieldV1):  Example: {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Which team is impacted by this issue', 'field_type':
            'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}],
            'required': 'never', 'required_v2': 'never', 'show_before_closure': True, 'show_before_creation': True,
            'show_before_update': True, 'show_in_announcement_post': True, 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    custom_field: CustomFieldV1
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
        from ..models.custom_field_v1 import CustomFieldV1

        d = dict(src_dict)
        custom_field = CustomFieldV1.from_dict(d.pop("custom_field"))

        custom_fields_create_result_v1 = cls(
            custom_field=custom_field,
        )

        custom_fields_create_result_v1.additional_properties = d
        return custom_fields_create_result_v1

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
