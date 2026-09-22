from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_resource_v3 import CatalogResourceV3


T = TypeVar("T", bound="CatalogListResourcesResultV3")


@_attrs_define(kw_only=True)
class CatalogListResourcesResultV3:
    """
    Example:
        {'resources': [{'category': 'custom', 'description': 'Boolean true or false value', 'engine_resource_type':
            'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]', 'label': 'GitHub Repository', 'type': 'Custom["Team"]',
            'value_docstring': 'Either the GraphQL node ID of the repository or a string of <owner>/<repo>, e.g. incident-
            io/website'}]}

    Attributes:
        resources (list[CatalogResourceV3]):  Example: [{'category': 'custom', 'description': 'Boolean true or false
            value', 'engine_resource_type': 'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]', 'label': 'GitHub Repository',
            'type': 'Custom["Team"]', 'value_docstring': 'Either the GraphQL node ID of the repository or a string of
            <owner>/<repo>, e.g. incident-io/website'}].
    """

    resources: list[CatalogResourceV3]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resources": resources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_resource_v3 import CatalogResourceV3

        d = dict(src_dict)
        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = CatalogResourceV3.from_dict(resources_item_data)

            resources.append(resources_item)

        catalog_list_resources_result_v3 = cls(
            resources=resources,
        )

        catalog_list_resources_result_v3.additional_properties = d
        return catalog_list_resources_result_v3

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
