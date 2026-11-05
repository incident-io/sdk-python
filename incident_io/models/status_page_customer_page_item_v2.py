from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_customer_page_component_v2 import (
        StatusPageCustomerPageComponentV2,
    )
    from ..models.status_page_customer_page_group_v2 import (
        StatusPageCustomerPageGroupV2,
    )


T = TypeVar("T", bound="StatusPageCustomerPageItemV2")


@_attrs_define(kw_only=True)
class StatusPageCustomerPageItemV2:
    """
    Example:
        {'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard',
            'display_uptime': True, 'name': 'App', 'status': 'operational'}, 'group': {'components': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard', 'display_uptime': True, 'name': 'App',
            'status': 'operational'}], 'description': 'Services hosted in our EU data center', 'display_aggregated_uptime':
            True, 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}}

    Attributes:
        component (StatusPageCustomerPageComponentV2 | Unset):  Example: {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1',
            'description': 'The web dashboard', 'display_uptime': True, 'name': 'App', 'status': 'operational'}.
        group (StatusPageCustomerPageGroupV2 | Unset):  Example: {'components': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard', 'display_uptime': True, 'name': 'App',
            'status': 'operational'}], 'description': 'Services hosted in our EU data center', 'display_aggregated_uptime':
            True, 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}.
    """

    component: StatusPageCustomerPageComponentV2 | Unset = UNSET
    group: StatusPageCustomerPageGroupV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component, Unset):
            component = self.component.to_dict()

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component is not UNSET:
            field_dict["component"] = component
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_customer_page_component_v2 import (
            StatusPageCustomerPageComponentV2,
        )
        from ..models.status_page_customer_page_group_v2 import (
            StatusPageCustomerPageGroupV2,
        )

        d = dict(src_dict)
        _component = d.pop("component", UNSET)
        component: StatusPageCustomerPageComponentV2 | Unset
        if isinstance(_component, Unset):
            component = UNSET
        else:
            component = StatusPageCustomerPageComponentV2.from_dict(_component)

        _group = d.pop("group", UNSET)
        group: StatusPageCustomerPageGroupV2 | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = StatusPageCustomerPageGroupV2.from_dict(_group)

        status_page_customer_page_item_v2 = cls(
            component=component,
            group=group,
        )

        status_page_customer_page_item_v2.additional_properties = d
        return status_page_customer_page_item_v2

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
