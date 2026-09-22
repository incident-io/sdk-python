from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_type_attribute_payload_v2_mode import (
    CatalogTypeAttributePayloadV2Mode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_type_attribute_path_item_payload_v2 import (
        CatalogTypeAttributePathItemPayloadV2,
    )


T = TypeVar("T", bound="CatalogTypeAttributePayloadV2")


@_attrs_define(kw_only=True)
class CatalogTypeAttributePayloadV2:
    """
    Example:
        {'array': False, 'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': '', 'name': 'tier',
            'path': [{'attribute_id': 'abc123'}], 'type': 'Custom["Service"]'}

    Attributes:
        array (bool): Whether this attribute is an array Example: False.
        name (str): Unique name of this attribute Example: tier.
        type_ (str): Catalog type name for this attribute Example: Custom["Service"].
        backlink_attribute (str | Unset): The attribute to use (if this is a backlink) Example: abc123.
        id (str | Unset): The ID of this attribute Example: 01GW2G3V0S59R238FAHPDS1R66.
        mode (CatalogTypeAttributePayloadV2Mode | Unset): Controls how this attribute is modified
        path (list[CatalogTypeAttributePathItemPayloadV2] | Unset): The path to use (if this is an path) Example:
            [{'attribute_id': 'abc123'}].
    """

    array: bool
    name: str
    type_: str
    backlink_attribute: str | Unset = UNSET
    id: str | Unset = UNSET
    mode: CatalogTypeAttributePayloadV2Mode | Unset = UNSET
    path: list[CatalogTypeAttributePathItemPayloadV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        array = self.array

        name = self.name

        type_ = self.type_

        backlink_attribute = self.backlink_attribute

        id = self.id

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

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
                "name": name,
                "type": type_,
            }
        )
        if backlink_attribute is not UNSET:
            field_dict["backlink_attribute"] = backlink_attribute
        if id is not UNSET:
            field_dict["id"] = id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_type_attribute_path_item_payload_v2 import (
            CatalogTypeAttributePathItemPayloadV2,
        )

        d = dict(src_dict)
        array = d.pop("array")

        name = d.pop("name")

        type_ = d.pop("type")

        backlink_attribute = d.pop("backlink_attribute", UNSET)

        id = d.pop("id", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: CatalogTypeAttributePayloadV2Mode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CatalogTypeAttributePayloadV2Mode(_mode)

        _path = d.pop("path", UNSET)
        path: list[CatalogTypeAttributePathItemPayloadV2] | Unset = UNSET
        if _path is not UNSET:
            path = []
            for path_item_data in _path:
                path_item = CatalogTypeAttributePathItemPayloadV2.from_dict(
                    path_item_data
                )

                path.append(path_item)

        catalog_type_attribute_payload_v2 = cls(
            array=array,
            name=name,
            type_=type_,
            backlink_attribute=backlink_attribute,
            id=id,
            mode=mode,
            path=path,
        )

        catalog_type_attribute_payload_v2.additional_properties = d
        return catalog_type_attribute_payload_v2

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
