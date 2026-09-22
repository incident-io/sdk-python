from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_type_attribute_v2_mode import CatalogTypeAttributeV2Mode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_type_attribute_path_item_v2 import (
        CatalogTypeAttributePathItemV2,
    )


T = TypeVar("T", bound="CatalogTypeAttributeV2")


@_attrs_define(kw_only=True)
class CatalogTypeAttributeV2:
    """
    Example:
        {'array': False, 'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': '', 'name': 'tier',
            'path': [{'attribute_id': 'abc123', 'attribute_name': 'abc123'}], 'type': 'Custom["Service"]'}

    Attributes:
        array (bool): Whether this attribute is an array Example: False.
        id (str): The ID of this attribute Example: 01GW2G3V0S59R238FAHPDS1R66.
        mode (CatalogTypeAttributeV2Mode): Controls how this attribute is modified
        name (str): Unique name of this attribute Example: tier.
        type_ (str): Catalog type name for this attribute Example: Custom["Service"].
        backlink_attribute (str | Unset): The attribute to use (if this is a backlink) Example: abc123.
        path (list[CatalogTypeAttributePathItemV2] | Unset): The path to use (if this is a path attribute) Example:
            [{'attribute_id': 'abc123', 'attribute_name': 'abc123'}].
    """

    array: bool
    id: str
    mode: CatalogTypeAttributeV2Mode
    name: str
    type_: str
    backlink_attribute: str | Unset = UNSET
    path: list[CatalogTypeAttributePathItemV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        array = self.array

        id = self.id

        mode = self.mode.value

        name = self.name

        type_ = self.type_

        backlink_attribute = self.backlink_attribute

        path: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = []
            for path_item_data in self.path:
                path_item = path_item_data.to_dict()
                path.append(path_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "id": id,
                "mode": mode,
                "name": name,
                "type": type_,
            }
        )
        if backlink_attribute is not UNSET:
            field_dict["backlink_attribute"] = backlink_attribute
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_type_attribute_path_item_v2 import (
            CatalogTypeAttributePathItemV2,
        )

        d = dict(src_dict)
        array = d.pop("array")

        id = d.pop("id")

        mode = CatalogTypeAttributeV2Mode(d.pop("mode"))

        name = d.pop("name")

        type_ = d.pop("type")

        backlink_attribute = d.pop("backlink_attribute", UNSET)

        _path = d.pop("path", UNSET)
        path: list[CatalogTypeAttributePathItemV2] | Unset = UNSET
        if _path is not UNSET:
            path = []
            for path_item_data in _path:
                path_item = CatalogTypeAttributePathItemV2.from_dict(path_item_data)

                path.append(path_item)

        catalog_type_attribute_v2 = cls(
            array=array,
            id=id,
            mode=mode,
            name=name,
            type_=type_,
            backlink_attribute=backlink_attribute,
            path=path,
        )

        catalog_type_attribute_v2.additional_properties = d
        return catalog_type_attribute_v2

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
