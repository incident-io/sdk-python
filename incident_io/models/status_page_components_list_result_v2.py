from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_page_component_v2 import StatusPageComponentV2


T = TypeVar("T", bound="StatusPageComponentsListResultV2")


@_attrs_define(kw_only=True)
class StatusPageComponentsListResultV2:
    """
    Example:
        {'status_page_components': [{'description': 'Our iOS app', 'id': '01FCNDV6P870EA6S7TK1DSYDG1',
            'management_meta': {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'managed_by': 'dashboard',
            'source_url': 'https://github.com/my-company/infrastructure'}, 'name': 'App'}]}

    Attributes:
        status_page_components (list[StatusPageComponentV2]):  Example: [{'description': 'Our iOS app', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'management_meta': {'annotations': {'incident.io/terraform/version': '3.0.0'},
            'managed_by': 'dashboard', 'source_url': 'https://github.com/my-company/infrastructure'}, 'name': 'App'}].
    """

    status_page_components: list[StatusPageComponentV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_page_components = []
        for status_page_components_item_data in self.status_page_components:
            status_page_components_item = status_page_components_item_data.to_dict()
            status_page_components.append(status_page_components_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_page_components": status_page_components,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_component_v2 import (
            StatusPageComponentV2,
        )

        d = dict(src_dict)
        status_page_components = []
        _status_page_components = d.pop("status_page_components")
        for status_page_components_item_data in _status_page_components:
            status_page_components_item = StatusPageComponentV2.from_dict(
                status_page_components_item_data
            )

            status_page_components.append(status_page_components_item)

        status_page_components_list_result_v2 = cls(
            status_page_components=status_page_components,
        )

        status_page_components_list_result_v2.additional_properties = d
        return status_page_components_list_result_v2

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
