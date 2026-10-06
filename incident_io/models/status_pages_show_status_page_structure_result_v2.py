from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_pages_show_status_page_structure_result_v2_display_uptime_mode import (
    StatusPagesShowStatusPageStructureResultV2DisplayUptimeMode,
)

if TYPE_CHECKING:
    from ..models.management_meta_v2 import ManagementMetaV2
    from ..models.status_page_structure_v2 import StatusPageStructureV2


T = TypeVar("T", bound="StatusPagesShowStatusPageStructureResultV2")


@_attrs_define(kw_only=True)
class StatusPagesShowStatusPageStructureResultV2:
    """
    Example:
        {'current_structure': {'items': [{'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'display_uptime':
            True, 'hidden': False, 'name': 'App'}, 'group': {'components': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1',
            'display_uptime': True, 'hidden': False, 'name': 'App'}], 'description': 'Services hosted in our EU data
            center', 'display_aggregated_uptime': True, 'hidden': False, 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU
            Data center'}, 'sub_page': {'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'items': [{'component': {'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'display_uptime': True, 'hidden': False, 'name': 'App'}, 'group': {'components':
            [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'display_uptime': True, 'hidden': False, 'name': 'App'}],
            'description': 'Services hosted in our EU data center', 'display_aggregated_uptime': True, 'hidden': False,
            'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}}], 'name': 'United Kingdom'}}]},
            'display_uptime_mode': 'chart_and_percentage', 'management_meta': {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'managed_by': 'dashboard', 'source_url': 'https://github.com/my-
            company/infrastructure'}}

    Attributes:
        current_structure (StatusPageStructureV2):  Example: {'items': [{'component': {'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'display_uptime': True, 'hidden': False, 'name': 'App'}, 'group': {'components':
            [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'display_uptime': True, 'hidden': False, 'name': 'App'}],
            'description': 'Services hosted in our EU data center', 'display_aggregated_uptime': True, 'hidden': False,
            'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}, 'sub_page': {'id': '01FCNDV6P870EA6S7TK1DSYDG1',
            'items': [{'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'display_uptime': True, 'hidden': False,
            'name': 'App'}, 'group': {'components': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'display_uptime': True,
            'hidden': False, 'name': 'App'}], 'description': 'Services hosted in our EU data center',
            'display_aggregated_uptime': True, 'hidden': False, 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data
            center'}}], 'name': 'United Kingdom'}}]}.
        display_uptime_mode (StatusPagesShowStatusPageStructureResultV2DisplayUptimeMode): How the page shows uptime
            against its components Example: chart_and_percentage.
        management_meta (ManagementMetaV2):  Example: {'annotations': {'incident.io/terraform/version': '3.0.0'},
            'managed_by': 'dashboard', 'source_url': 'https://github.com/my-company/infrastructure'}.
    """

    current_structure: StatusPageStructureV2
    display_uptime_mode: StatusPagesShowStatusPageStructureResultV2DisplayUptimeMode
    management_meta: ManagementMetaV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_structure = self.current_structure.to_dict()

        display_uptime_mode = self.display_uptime_mode.value

        management_meta = self.management_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_structure": current_structure,
                "display_uptime_mode": display_uptime_mode,
                "management_meta": management_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.management_meta_v2 import ManagementMetaV2
        from ..models.status_page_structure_v2 import (
            StatusPageStructureV2,
        )

        d = dict(src_dict)
        current_structure = StatusPageStructureV2.from_dict(d.pop("current_structure"))

        display_uptime_mode = (
            StatusPagesShowStatusPageStructureResultV2DisplayUptimeMode(
                d.pop("display_uptime_mode")
            )
        )

        management_meta = ManagementMetaV2.from_dict(d.pop("management_meta"))

        status_pages_show_status_page_structure_result_v2 = cls(
            current_structure=current_structure,
            display_uptime_mode=display_uptime_mode,
            management_meta=management_meta,
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
