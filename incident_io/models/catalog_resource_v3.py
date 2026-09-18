from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_resource_v3_category import CatalogResourceV3Category

T = TypeVar("T", bound="CatalogResourceV3")


@_attrs_define
class CatalogResourceV3:
    """
    Example:
        {'category': 'custom', 'description': 'Boolean true or false value', 'engine_resource_type':
            'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]', 'label': 'GitHub Repository', 'type': 'Custom["Team"]',
            'value_docstring': 'Either the GraphQL node ID of the repository or a string of <owner>/<repo>, e.g. incident-
            io/website'}

    Attributes:
        category (CatalogResourceV3Category): Which category of resource Example: custom.
        description (str): Human readable description for this resource Example: Boolean true or false value.
        engine_resource_type (str): The way this resource type is referenced in the engine, as used when setting the
            type of an alert attribute Example: CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"].
        label (str): Label for this catalog resource type Example: GitHub Repository.
        type_ (str): Catalog type name for this resource, as used when setting the type of a catalog type attribute
            Example: Custom["Team"].
        value_docstring (str): Documentation for the literal string value of this resource Example: Either the GraphQL
            node ID of the repository or a string of <owner>/<repo>, e.g. incident-io/website.
    """

    category: CatalogResourceV3Category
    description: str
    engine_resource_type: str
    label: str
    type_: str
    value_docstring: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        description = self.description

        engine_resource_type = self.engine_resource_type

        label = self.label

        type_ = self.type_

        value_docstring = self.value_docstring

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "description": description,
                "engine_resource_type": engine_resource_type,
                "label": label,
                "type": type_,
                "value_docstring": value_docstring,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        category = CatalogResourceV3Category(d.pop("category"))

        description = d.pop("description")

        engine_resource_type = d.pop("engine_resource_type")

        label = d.pop("label")

        type_ = d.pop("type")

        value_docstring = d.pop("value_docstring")

        catalog_resource_v3 = cls(
            category=category,
            description=description,
            engine_resource_type=engine_resource_type,
            label=label,
            type_=type_,
            value_docstring=value_docstring,
        )

        catalog_resource_v3.additional_properties = d
        return catalog_resource_v3

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
