from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2
    from ..models.status_page_maintenance_v2 import StatusPageMaintenanceV2


T = TypeVar("T", bound="StatusPagesListStatusPageMaintenancesResultV2")


@_attrs_define
class StatusPagesListStatusPageMaintenancesResultV2:
    """
    Example:
        {'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}, 'status_page_maintenances':
            [{'automate_maintenance_status': True, 'component_maintenance_periods': [{'component_id':
            '01GW7P4ES31Q6V1ZQH321T0GJN', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at':
            '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status':
            'maintenance_scheduled', 'name': 'Routine infrastructure upgrade', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status': 'maintenance_scheduled', 'message': 'abc123',
            'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_maintenance_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}]}

    Attributes:
        pagination_meta (PaginationMetaResultV2):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
        status_page_maintenances (list[StatusPageMaintenanceV2]):  Example: [{'automate_maintenance_status': True,
            'component_maintenance_periods': [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN', 'end_at':
            '2021-08-17T13:28:57.801578Z', 'start_at': '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'maintenance_status': 'maintenance_scheduled', 'name': 'Routine infrastructure upgrade', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status': 'maintenance_scheduled', 'message': 'abc123',
            'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_maintenance_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}].
    """

    pagination_meta: PaginationMetaResultV2
    status_page_maintenances: list[StatusPageMaintenanceV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination_meta = self.pagination_meta.to_dict()

        status_page_maintenances = []
        for status_page_maintenances_item_data in self.status_page_maintenances:
            status_page_maintenances_item = status_page_maintenances_item_data.to_dict()
            status_page_maintenances.append(status_page_maintenances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination_meta": pagination_meta,
                "status_page_maintenances": status_page_maintenances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )
        from ..models.status_page_maintenance_v2 import (
            StatusPageMaintenanceV2,
        )

        d = dict(src_dict)
        pagination_meta = PaginationMetaResultV2.from_dict(d.pop("pagination_meta"))

        status_page_maintenances = []
        _status_page_maintenances = d.pop("status_page_maintenances")
        for status_page_maintenances_item_data in _status_page_maintenances:
            status_page_maintenances_item = StatusPageMaintenanceV2.from_dict(
                status_page_maintenances_item_data
            )

            status_page_maintenances.append(status_page_maintenances_item)

        status_pages_list_status_page_maintenances_result_v2 = cls(
            pagination_meta=pagination_meta,
            status_page_maintenances=status_page_maintenances,
        )

        status_pages_list_status_page_maintenances_result_v2.additional_properties = d
        return status_pages_list_status_page_maintenances_result_v2

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
