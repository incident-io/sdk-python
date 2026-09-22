from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_v2 import AlertV2
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2


T = TypeVar("T", bound="AlertsListResultV2")


@_attrs_define(kw_only=True)
class AlertsListResultV2:
    """
    Example:
        {'alerts': [{'alert_group_ids': ['01GW2G3V0S59R238FAHPDS1R66'], 'alert_source_id': '01GW2G3V0S59R238FAHPDS1R66',
            'attributes': [{'array_value': [{'catalog_entry': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'label': 'Payments Team', 'literal': 'SEV123'}],
            'attribute': {'array': False, 'emoji': 'fire', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'service',
            'required': False, 'type': 'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}, 'value': {'catalog_entry':
            {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-
            call'}, 'label': 'Payments Team', 'literal': 'SEV123'}}], 'created_at': '2021-08-17T13:28:57.801578Z',
            'deduplication_key': '4293868629', 'description': 'CPU on the payments service has exceeded 75 percent for 5
            minutes', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at': '2021-08-17T14:28:57.801578Z', 'source_url':
            'https://www.my-alerting-platform.com/alerts/my-alert-123', 'status': 'firing', 'tags': [{'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'name': 'noisy'}], 'title': '*errors.withMessage: PG::Error failed to connect',
            'updated_at': '2021-08-17T13:28:57.801578Z'}], 'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0',
            'page_size': 25}}

    Attributes:
        alerts (list[AlertV2]):  Example: [{'alert_group_ids': ['01GW2G3V0S59R238FAHPDS1R66'], 'alert_source_id':
            '01GW2G3V0S59R238FAHPDS1R66', 'attributes': [{'array_value': [{'catalog_entry': {'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'label': 'Payments
            Team', 'literal': 'SEV123'}], 'attribute': {'array': False, 'emoji': 'fire', 'id': '01GW2G3V0S59R238FAHPDS1R66',
            'name': 'service', 'required': False, 'type': 'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}, 'value':
            {'catalog_entry': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Primary On-call'}, 'label': 'Payments Team', 'literal': 'SEV123'}}], 'created_at':
            '2021-08-17T13:28:57.801578Z', 'deduplication_key': '4293868629', 'description': 'CPU on the payments service
            has exceeded 75 percent for 5 minutes', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at':
            '2021-08-17T14:28:57.801578Z', 'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123',
            'status': 'firing', 'tags': [{'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'noisy'}], 'title':
            '*errors.withMessage: PG::Error failed to connect', 'updated_at': '2021-08-17T13:28:57.801578Z'}].
        pagination_meta (PaginationMetaResultV2):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
    """

    alerts: list[AlertV2]
    pagination_meta: PaginationMetaResultV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alerts = []
        for alerts_item_data in self.alerts:
            alerts_item = alerts_item_data.to_dict()
            alerts.append(alerts_item)

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alerts": alerts,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_v2 import AlertV2
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )

        d = dict(src_dict)
        alerts = []
        _alerts = d.pop("alerts")
        for alerts_item_data in _alerts:
            alerts_item = AlertV2.from_dict(alerts_item_data)

            alerts.append(alerts_item)

        pagination_meta = PaginationMetaResultV2.from_dict(d.pop("pagination_meta"))

        alerts_list_result_v2 = cls(
            alerts=alerts,
            pagination_meta=pagination_meta,
        )

        alerts_list_result_v2.additional_properties = d
        return alerts_list_result_v2

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
