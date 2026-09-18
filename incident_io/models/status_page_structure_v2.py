from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_page_structure_item_v2 import StatusPageStructureItemV2


T = TypeVar("T", bound="StatusPageStructureV2")


@_attrs_define
class StatusPageStructureV2:
    """
    Example:
        {'items': [{'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}, 'group': {'components':
            [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU
            Data center'}, 'sub_page': {'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'items': [{'component': {'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}, 'group': {'components': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}}],
            'name': 'United Kingdom'}}]}

    Attributes:
        items (list[StatusPageStructureItemV2]): Array of components and groups to display in the status page Example:
            [{'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}, 'group': {'components':
            [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU
            Data center'}, 'sub_page': {'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'items': [{'component': {'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}, 'group': {'components': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}}],
            'name': 'United Kingdom'}}].
    """

    items: list[StatusPageStructureItemV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_structure_item_v2 import (
            StatusPageStructureItemV2,
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = StatusPageStructureItemV2.from_dict(items_item_data)

            items.append(items_item)

        status_page_structure_v2 = cls(
            items=items,
        )

        status_page_structure_v2.additional_properties = d
        return status_page_structure_v2

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
