from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_create_type_payload_v2_categories_item import (
    CatalogCreateTypePayloadV2CategoriesItem,
)
from ..models.catalog_create_type_payload_v2_color import (
    CatalogCreateTypePayloadV2Color,
)
from ..models.catalog_create_type_payload_v2_icon import CatalogCreateTypePayloadV2Icon
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_create_type_payload_v2_annotations import (
        CatalogCreateTypePayloadV2Annotations,
    )


T = TypeVar("T", bound="CatalogCreateTypePayloadV2")


@_attrs_define
class CatalogCreateTypePayloadV2:
    """
    Example:
        {'annotations': {'incident.io/catalog-importer/id': 'id-of-config'}, 'categories': ['customer'], 'color':
            'yellow', 'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'alert', 'name':
            'Kubernetes Cluster', 'ranked': True, 'source_repo_url': 'https://github.com/my-company/incident-io-catalog',
            'type_name': 'Custom["BackstageGroup"]'}

    Attributes:
        description (str): Human readble description of this type Example: Represents Kubernetes clusters that we run
            inside of GKE..
        name (str): Name is the human readable name of this type Example: Kubernetes Cluster.
        annotations (CatalogCreateTypePayloadV2Annotations | Unset): Annotations that can track metadata about this type
            Example: {'incident.io/catalog-importer/id': 'id-of-config'}.
        categories (list[CatalogCreateTypePayloadV2CategoriesItem] | Unset): What categories is this type considered
            part of Example: ['customer'].
        color (CatalogCreateTypePayloadV2Color | Unset): Sets the display color of this type in the dashboard Example:
            yellow.
        icon (CatalogCreateTypePayloadV2Icon | Unset): Sets the display icon of this type in the dashboard Example:
            alert.
        ranked (bool | Unset): If this type should be ranked Example: True.
        source_repo_url (str | Unset): The url of the external repository where this type is managed Example:
            https://github.com/my-company/incident-io-catalog.
        type_name (str | Unset): The type name of this catalog type, to be used when defining attributes. This is
            immutable once a CatalogType has been created. For non-externally sync types, it must follow the pattern
            Custom["SomeName"] Example: Custom["BackstageGroup"].
    """

    description: str
    name: str
    annotations: CatalogCreateTypePayloadV2Annotations | Unset = UNSET
    categories: list[CatalogCreateTypePayloadV2CategoriesItem] | Unset = UNSET
    color: CatalogCreateTypePayloadV2Color | Unset = UNSET
    icon: CatalogCreateTypePayloadV2Icon | Unset = UNSET
    ranked: bool | Unset = UNSET
    source_repo_url: str | Unset = UNSET
    type_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        annotations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.value
                categories.append(categories_item)

        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        icon: str | Unset = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.value

        ranked = self.ranked

        source_repo_url = self.source_repo_url

        type_name = self.type_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if categories is not UNSET:
            field_dict["categories"] = categories
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if ranked is not UNSET:
            field_dict["ranked"] = ranked
        if source_repo_url is not UNSET:
            field_dict["source_repo_url"] = source_repo_url
        if type_name is not UNSET:
            field_dict["type_name"] = type_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_create_type_payload_v2_annotations import (
            CatalogCreateTypePayloadV2Annotations,
        )

        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        _annotations = d.pop("annotations", UNSET)
        annotations: CatalogCreateTypePayloadV2Annotations | Unset
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = CatalogCreateTypePayloadV2Annotations.from_dict(_annotations)

        _categories = d.pop("categories", UNSET)
        categories: list[CatalogCreateTypePayloadV2CategoriesItem] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = CatalogCreateTypePayloadV2CategoriesItem(
                    categories_item_data
                )

                categories.append(categories_item)

        _color = d.pop("color", UNSET)
        color: CatalogCreateTypePayloadV2Color | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CatalogCreateTypePayloadV2Color(_color)

        _icon = d.pop("icon", UNSET)
        icon: CatalogCreateTypePayloadV2Icon | Unset
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = CatalogCreateTypePayloadV2Icon(_icon)

        ranked = d.pop("ranked", UNSET)

        source_repo_url = d.pop("source_repo_url", UNSET)

        type_name = d.pop("type_name", UNSET)

        catalog_create_type_payload_v2 = cls(
            description=description,
            name=name,
            annotations=annotations,
            categories=categories,
            color=color,
            icon=icon,
            ranked=ranked,
            source_repo_url=source_repo_url,
            type_name=type_name,
        )

        catalog_create_type_payload_v2.additional_properties = d
        return catalog_create_type_payload_v2

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
