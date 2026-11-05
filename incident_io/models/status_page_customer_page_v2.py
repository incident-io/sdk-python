from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_customer_page_v2_status import StatusPageCustomerPageV2Status

if TYPE_CHECKING:
    from ..models.status_page_customer_page_item_v2 import StatusPageCustomerPageItemV2
    from ..models.status_page_incident_v2 import StatusPageIncidentV2
    from ..models.status_page_maintenance_v2 import StatusPageMaintenanceV2


T = TypeVar("T", bound="StatusPageCustomerPageV2")


@_attrs_define(kw_only=True)
class StatusPageCustomerPageV2:
    """One customer's page on a customer status page: its status, components and incidents.

    Example:
        {'components': [{'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard',
            'display_uptime': True, 'name': 'App', 'status': 'operational'}, 'group': {'components': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard', 'display_uptime': True, 'name': 'App',
            'status': 'operational'}], 'description': 'Services hosted in our EU data center', 'display_aggregated_uptime':
            True, 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}}], 'customer_id': 'acme-corp',
            'maintenances': [{'automate_maintenance_status': True, 'component_maintenance_periods': [{'component_id':
            '01GW7P4ES31Q6V1ZQH321T0GJN', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at':
            '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status':
            'maintenance_scheduled', 'name': 'Routine infrastructure upgrade', 'published_at':
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
            'degraded_performance'}

    Attributes:
        components (list[StatusPageCustomerPageItemV2]): Components and groups shown on this page, in display order
            Example: [{'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard',
            'display_uptime': True, 'name': 'App', 'status': 'operational'}, 'group': {'components': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'description': 'The web dashboard', 'display_uptime': True, 'name': 'App',
            'status': 'operational'}], 'description': 'Services hosted in our EU data center', 'display_aggregated_uptime':
            True, 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}}].
        customer_id (str): The external ID of the catalog entry that defines this customer's page Example: acme-corp.
        maintenances (list[StatusPageMaintenanceV2]): Maintenance windows in progress or scheduled for this customer
            Example: [{'automate_maintenance_status': True, 'component_maintenance_periods': [{'component_id':
            '01GW7P4ES31Q6V1ZQH321T0GJN', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at':
            '2021-08-17T13:28:57.801578Z'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status':
            'maintenance_scheduled', 'name': 'Routine infrastructure upgrade', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'maintenance_status': 'maintenance_scheduled', 'message': 'abc123',
            'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_maintenance_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}].
        name (str): The name of this customer's page Example: Acme Corp.
        ongoing_incidents (list[StatusPageIncidentV2]): Incidents currently affecting this customer Example:
            [{'component_impacts': [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN', 'component_status':
            'degraded_performance', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at': '2021-08-17T13:28:57.801578Z'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'name': 'Elevated API latency',
            'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'message': 'abc123', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_incident_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}].
        recent_incidents (list[StatusPageIncidentV2]): Incidents from this page's history window, including ongoing
            incidents Example: [{'component_impacts': [{'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN', 'component_status':
            'degraded_performance', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at': '2021-08-17T13:28:57.801578Z'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'name': 'Elevated API latency',
            'published_at': '2021-08-17T13:28:57.801578Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'updates':
            [{'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_status': 'investigating', 'message': 'abc123', 'published_at':
            '2021-08-17T13:28:57.801578Z', 'status_page_incident_id': '01FCNDV6P870EA6S7TK1DSYDG1'}]}].
        status (StatusPageCustomerPageV2Status): The worst current status of any component on this page, or operational
            when nothing is affected Example: degraded_performance.
    """

    components: list[StatusPageCustomerPageItemV2]
    customer_id: str
    maintenances: list[StatusPageMaintenanceV2]
    name: str
    ongoing_incidents: list[StatusPageIncidentV2]
    recent_incidents: list[StatusPageIncidentV2]
    status: StatusPageCustomerPageV2Status
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        customer_id = self.customer_id

        maintenances = []
        for maintenances_item_data in self.maintenances:
            maintenances_item = maintenances_item_data.to_dict()
            maintenances.append(maintenances_item)

        name = self.name

        ongoing_incidents = []
        for ongoing_incidents_item_data in self.ongoing_incidents:
            ongoing_incidents_item = ongoing_incidents_item_data.to_dict()
            ongoing_incidents.append(ongoing_incidents_item)

        recent_incidents = []
        for recent_incidents_item_data in self.recent_incidents:
            recent_incidents_item = recent_incidents_item_data.to_dict()
            recent_incidents.append(recent_incidents_item)

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "components": components,
                "customer_id": customer_id,
                "maintenances": maintenances,
                "name": name,
                "ongoing_incidents": ongoing_incidents,
                "recent_incidents": recent_incidents,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_customer_page_item_v2 import (
            StatusPageCustomerPageItemV2,
        )
        from ..models.status_page_incident_v2 import (
            StatusPageIncidentV2,
        )
        from ..models.status_page_maintenance_v2 import (
            StatusPageMaintenanceV2,
        )

        d = dict(src_dict)
        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = StatusPageCustomerPageItemV2.from_dict(
                components_item_data
            )

            components.append(components_item)

        customer_id = d.pop("customer_id")

        maintenances = []
        _maintenances = d.pop("maintenances")
        for maintenances_item_data in _maintenances:
            maintenances_item = StatusPageMaintenanceV2.from_dict(
                maintenances_item_data
            )

            maintenances.append(maintenances_item)

        name = d.pop("name")

        ongoing_incidents = []
        _ongoing_incidents = d.pop("ongoing_incidents")
        for ongoing_incidents_item_data in _ongoing_incidents:
            ongoing_incidents_item = StatusPageIncidentV2.from_dict(
                ongoing_incidents_item_data
            )

            ongoing_incidents.append(ongoing_incidents_item)

        recent_incidents = []
        _recent_incidents = d.pop("recent_incidents")
        for recent_incidents_item_data in _recent_incidents:
            recent_incidents_item = StatusPageIncidentV2.from_dict(
                recent_incidents_item_data
            )

            recent_incidents.append(recent_incidents_item)

        status = StatusPageCustomerPageV2Status(d.pop("status"))

        status_page_customer_page_v2 = cls(
            components=components,
            customer_id=customer_id,
            maintenances=maintenances,
            name=name,
            ongoing_incidents=ongoing_incidents,
            recent_incidents=recent_incidents,
            status=status,
        )

        status_page_customer_page_v2.additional_properties = d
        return status_page_customer_page_v2

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
