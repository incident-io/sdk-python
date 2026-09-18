from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_create_type_payload_v3_categories_item import (
    CatalogCreateTypePayloadV3CategoriesItem,
)
from ..models.catalog_create_type_payload_v3_color import (
    CatalogCreateTypePayloadV3Color,
)
from ..models.catalog_create_type_payload_v3_icon import CatalogCreateTypePayloadV3Icon
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_create_type_payload_v3_annotations import (
        CatalogCreateTypePayloadV3Annotations,
    )


T = TypeVar("T", bound="CatalogCreateTypePayloadV3")


@_attrs_define
class CatalogCreateTypePayloadV3:
    """
    Example:
        {'annotations': {'incident.io/catalog-importer/id': 'id-of-config'}, 'categories': ['customer'], 'color':
            'yellow', 'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'alert', 'name':
            'Kubernetes Cluster', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog', 'type_name': 'Custom["BackstageGroup"]',
            'use_name_as_identifier': True}

    Attributes:
        description (str): Human readble description of this type Example: Represents Kubernetes clusters that we run
            inside of GKE..
        name (str): Name is the human readable name of this type Example: Kubernetes Cluster.
        annotations (CatalogCreateTypePayloadV3Annotations | Unset): Annotations that can track metadata about this type
            Example: {'incident.io/catalog-importer/id': 'id-of-config'}.
        categories (list[CatalogCreateTypePayloadV3CategoriesItem] | Unset): What categories is this type considered
            part of Example: ['customer'].
        color (CatalogCreateTypePayloadV3Color | Unset): Sets the display color of this type in the dashboard Example:
            yellow.
        icon (CatalogCreateTypePayloadV3Icon | Unset): Sets the display icon of this type in the dashboard Example:
            alert.
        owning_team_ids (list[str] | Unset): IDs of the teams that own this catalog type Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
        ranked (bool | Unset): If this type should be ranked Example: True.
        source_repo_url (str | Unset): The url of the external repository where this type is managed Example:
            https://github.com/my-company/incident-io-catalog.
        type_name (str | Unset): The type name of this catalog type, to be used when defining attributes. This is
            immutable once a CatalogType has been created. For non-externally sync types, it must follow the pattern
            Custom["SomeName"] Example: Custom["BackstageGroup"].
        use_name_as_identifier (bool | Unset): If enabled, you can refer to entries of this type by their name, as well
            as their external ID and any aliases. Example: True.
    """

    description: str
    name: str
    annotations: CatalogCreateTypePayloadV3Annotations | Unset = UNSET
    categories: list[CatalogCreateTypePayloadV3CategoriesItem] | Unset = UNSET
    color: CatalogCreateTypePayloadV3Color | Unset = UNSET
    icon: CatalogCreateTypePayloadV3Icon | Unset = UNSET
    owning_team_ids: list[str] | Unset = UNSET
    ranked: bool | Unset = UNSET
    source_repo_url: str | Unset = UNSET
    type_name: str | Unset = UNSET
    use_name_as_identifier: bool | Unset = UNSET
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

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        ranked = self.ranked

        source_repo_url = self.source_repo_url

        type_name = self.type_name

        use_name_as_identifier = self.use_name_as_identifier

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
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids
        if ranked is not UNSET:
            field_dict["ranked"] = ranked
        if source_repo_url is not UNSET:
            field_dict["source_repo_url"] = source_repo_url
        if type_name is not UNSET:
            field_dict["type_name"] = type_name
        if use_name_as_identifier is not UNSET:
            field_dict["use_name_as_identifier"] = use_name_as_identifier

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_create_type_payload_v3_annotations import (
            CatalogCreateTypePayloadV3Annotations,
        )

        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        _annotations = d.pop("annotations", UNSET)
        annotations: CatalogCreateTypePayloadV3Annotations | Unset
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = CatalogCreateTypePayloadV3Annotations.from_dict(_annotations)

        _categories = d.pop("categories", UNSET)
        categories: list[CatalogCreateTypePayloadV3CategoriesItem] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = CatalogCreateTypePayloadV3CategoriesItem(
                    categories_item_data
                )

                categories.append(categories_item)

        _color = d.pop("color", UNSET)
        color: CatalogCreateTypePayloadV3Color | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CatalogCreateTypePayloadV3Color(_color)

        _icon = d.pop("icon", UNSET)
        icon: CatalogCreateTypePayloadV3Icon | Unset
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = CatalogCreateTypePayloadV3Icon(_icon)

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        ranked = d.pop("ranked", UNSET)

        source_repo_url = d.pop("source_repo_url", UNSET)

        type_name = d.pop("type_name", UNSET)

        use_name_as_identifier = d.pop("use_name_as_identifier", UNSET)

        catalog_create_type_payload_v3 = cls(
            description=description,
            name=name,
            annotations=annotations,
            categories=categories,
            color=color,
            icon=icon,
            owning_team_ids=owning_team_ids,
            ranked=ranked,
            source_repo_url=source_repo_url,
            type_name=type_name,
            use_name_as_identifier=use_name_as_identifier,
        )

        catalog_create_type_payload_v3.additional_properties = d
        return catalog_create_type_payload_v3

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
