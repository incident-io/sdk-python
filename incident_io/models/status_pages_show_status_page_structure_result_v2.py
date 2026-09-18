from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_page_structure_v2 import StatusPageStructureV2


T = TypeVar("T", bound="StatusPagesShowStatusPageStructureResultV2")


@_attrs_define
class StatusPagesShowStatusPageStructureResultV2:
    """
    Example:
        {'current_structure': {'items': [{'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'},
            'group': {'components': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}, 'sub_page': {'id': '01FCNDV6P870EA6S7TK1DSYDG1',
            'items': [{'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}, 'group': {'components':
            [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU
            Data center'}}], 'name': 'United Kingdom'}}]}}

    Attributes:
        current_structure (StatusPageStructureV2):  Example: {'items': [{'component': {'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}, 'group': {'components': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'},
            'sub_page': {'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'items': [{'component': {'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}, 'group': {'components': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}}],
            'name': 'United Kingdom'}}]}.
    """

    current_structure: StatusPageStructureV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_structure = self.current_structure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_structure": current_structure,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_structure_v2 import (
            StatusPageStructureV2,
        )

        d = dict(src_dict)
        current_structure = StatusPageStructureV2.from_dict(d.pop("current_structure"))

        status_pages_show_status_page_structure_result_v2 = cls(
            current_structure=current_structure,
        )

        status_pages_show_status_page_structure_result_v2.additional_properties = d
        return status_pages_show_status_page_structure_result_v2

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
