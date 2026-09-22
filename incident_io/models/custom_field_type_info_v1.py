from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_type_info_v1_field_type import CustomFieldTypeInfoV1FieldType

if TYPE_CHECKING:
    from ..models.custom_field_option_v1 import CustomFieldOptionV1


T = TypeVar("T", bound="CustomFieldTypeInfoV1")


@_attrs_define(kw_only=True)
class CustomFieldTypeInfoV1:
    """
    Example:
        {'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]}

    Attributes:
        description (str): Description of the custom field Example: Which team is impacted by this issue.
        field_type (CustomFieldTypeInfoV1FieldType): Type of custom field Example: single_select.
        id (str): Unique identifier for the custom field Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Human readable name for the custom field Example: Affected Team.
        options (list[CustomFieldOptionV1]): What options are available for this custom field, if this field has options
            Example: [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10,
            'value': 'Product'}].
    """

    description: str
    field_type: CustomFieldTypeInfoV1FieldType
    id: str
    name: str
    options: list[CustomFieldOptionV1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        field_type = self.field_type.value

        id = self.id

        name = self.name

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "field_type": field_type,
                "id": id,
                "name": name,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_field_option_v1 import CustomFieldOptionV1

        d = dict(src_dict)
        description = d.pop("description")

        field_type = CustomFieldTypeInfoV1FieldType(d.pop("field_type"))

        id = d.pop("id")

        name = d.pop("name")

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = CustomFieldOptionV1.from_dict(options_item_data)

            options.append(options_item)

        custom_field_type_info_v1 = cls(
            description=description,
            field_type=field_type,
            id=id,
            name=name,
            options=options,
        )

        custom_field_type_info_v1.additional_properties = d
        return custom_field_type_info_v1

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
