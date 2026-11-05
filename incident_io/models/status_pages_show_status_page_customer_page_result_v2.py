from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_page_customer_page_v2 import StatusPageCustomerPageV2


T = TypeVar("T", bound="StatusPagesShowStatusPageCustomerPageResultV2")


@_attrs_define(kw_only=True)
class StatusPagesShowStatusPageCustomerPageResultV2:
    """
    Example:
        {'customer_page': {'components': [{'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'description':
            'The web dashboard', 'display_uptime': True, 'name': 'App', 'status': 'operational'}, 'group': {'components':
            [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard', 'display_uptime': True,
            'name': 'App', 'status': 'operational'}], 'description': 'Services hosted in our EU data center',
            'display_aggregated_uptime': True, 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}}],
            'customer_id': 'acme-corp', 'maintenances': [{'automate_maintenance_status': True,
            'component_maintenance_periods': [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN', 'end_at':
            '2021-08-17T13:28:57.801578Z', 'start_at': '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'maintenance_status': 'maintenance_scheduled', 'name': 'Routine infrastructure upgrade', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status': 'maintenance_scheduled', 'message': 'abc123',
            'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_maintenance_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}],
            'name': 'Acme Corp', 'ongoing_incidents': [{'component_impacts': [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN',
            'component_status': 'degraded_performance', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at':
            '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'name':
            'Elevated API latency', 'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'updates': [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2',
            'component_status': 'operational'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating',
            'message': 'abc123', 'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG1'}]}], 'recent_incidents': [{'component_impacts': [{'component_id':
            '01GW7P4ES31Q6V1ZQH321T0GJN', 'component_status': 'degraded_performance', 'end_at':
            '2021-08-17T13:28:57.801578Z', 'start_at': '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_status': 'investigating', 'name': 'Elevated API latency', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'message': 'abc123', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_incident_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}], 'status':
            'degraded_performance'}}

    Attributes:
        customer_page (StatusPageCustomerPageV2): One customer's page on a customer status page: its status, components
            and incidents. Example: {'components': [{'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1',
            'description': 'The web dashboard', 'display_uptime': True, 'name': 'App', 'status': 'operational'}, 'group':
            {'components': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard',
            'display_uptime': True, 'name': 'App', 'status': 'operational'}], 'description': 'Services hosted in our EU data
            center', 'display_aggregated_uptime': True, 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}}],
            'customer_id': 'acme-corp', 'maintenances': [{'automate_maintenance_status': True,
            'component_maintenance_periods': [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN', 'end_at':
            '2021-08-17T13:28:57.801578Z', 'start_at': '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'maintenance_status': 'maintenance_scheduled', 'name': 'Routine infrastructure upgrade', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status': 'maintenance_scheduled', 'message': 'abc123',
            'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_maintenance_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}],
            'name': 'Acme Corp', 'ongoing_incidents': [{'component_impacts': [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN',
            'component_status': 'degraded_performance', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at':
            '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'name':
            'Elevated API latency', 'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'updates': [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2',
            'component_status': 'operational'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating',
            'message': 'abc123', 'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG1'}]}], 'recent_incidents': [{'component_impacts': [{'component_id':
            '01GW7P4ES31Q6V1ZQH321T0GJN', 'component_status': 'degraded_performance', 'end_at':
            '2021-08-17T13:28:57.801578Z', 'start_at': '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_status': 'investigating', 'name': 'Elevated API latency', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'message': 'abc123', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_incident_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}], 'status':
            'degraded_performance'}.
    """

    customer_page: StatusPageCustomerPageV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_page = self.customer_page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_page": customer_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_customer_page_v2 import (
            StatusPageCustomerPageV2,
        )

        d = dict(src_dict)
        customer_page = StatusPageCustomerPageV2.from_dict(d.pop("customer_page"))

        status_pages_show_status_page_customer_page_result_v2 = cls(
            customer_page=customer_page,
        )

        status_pages_show_status_page_customer_page_result_v2.additional_properties = d
        return status_pages_show_status_page_customer_page_result_v2

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
