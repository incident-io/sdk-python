from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_structure_component_v2 import (
        StatusPageStructureComponentV2,
    )
    from ..models.status_page_structure_group_v2 import StatusPageStructureGroupV2
    from ..models.status_page_structure_sub_page_v2 import StatusPageStructureSubPageV2


T = TypeVar("T", bound="StatusPageStructureItemV2")


@_attrs_define(kw_only=True)
class StatusPageStructureItemV2:
    """
    Example:
        {'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}, 'group': {'components':
            [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU
            Data center'}, 'sub_page': {'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'items': [{'component': {'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}, 'group': {'components': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}}],
            'name': 'United Kingdom'}}

    Attributes:
        component (StatusPageStructureComponentV2 | Unset):  Example: {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1',
            'name': 'App'}.
        group (StatusPageStructureGroupV2 | Unset):  Example: {'components': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}.
        sub_page (StatusPageStructureSubPageV2 | Unset):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'items':
            [{'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}, 'group': {'components':
            [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU
            Data center'}}], 'name': 'United Kingdom'}.
    """

    component: StatusPageStructureComponentV2 | Unset = UNSET
    group: StatusPageStructureGroupV2 | Unset = UNSET
    sub_page: StatusPageStructureSubPageV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component, Unset):
            component = self.component.to_dict()

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        sub_page: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sub_page, Unset):
            sub_page = self.sub_page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component is not UNSET:
            field_dict["component"] = component
        if group is not UNSET:
            field_dict["group"] = group
        if sub_page is not UNSET:
            field_dict["sub_page"] = sub_page

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_structure_component_v2 import (
            StatusPageStructureComponentV2,
        )
        from ..models.status_page_structure_group_v2 import (
            StatusPageStructureGroupV2,
        )
        from ..models.status_page_structure_sub_page_v2 import (
            StatusPageStructureSubPageV2,
        )

        d = dict(src_dict)
        _component = d.pop("component", UNSET)
        component: StatusPageStructureComponentV2 | Unset
        if isinstance(_component, Unset):
            component = UNSET
        else:
            component = StatusPageStructureComponentV2.from_dict(_component)

        _group = d.pop("group", UNSET)
        group: StatusPageStructureGroupV2 | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = StatusPageStructureGroupV2.from_dict(_group)

        _sub_page = d.pop("sub_page", UNSET)
        sub_page: StatusPageStructureSubPageV2 | Unset
        if isinstance(_sub_page, Unset):
            sub_page = UNSET
        else:
            sub_page = StatusPageStructureSubPageV2.from_dict(_sub_page)

        status_page_structure_item_v2 = cls(
            component=component,
            group=group,
            sub_page=sub_page,
        )

        status_page_structure_item_v2.additional_properties = d
        return status_page_structure_item_v2

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
