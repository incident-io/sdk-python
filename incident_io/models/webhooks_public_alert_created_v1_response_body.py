from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_public_alert_created_v1_response_body_event_type import (
    WebhooksPublicAlertCreatedV1ResponseBodyEventType,
)

if TYPE_CHECKING:
    from ..models.alert_v2 import AlertV2


T = TypeVar("T", bound="WebhooksPublicAlertCreatedV1ResponseBody")


@_attrs_define(kw_only=True)
class WebhooksPublicAlertCreatedV1ResponseBody:
    """
    Example:
        {'event_type': 'public_alert.alert_created_v1', 'public_alert.alert_created_v1': {'alert_group_ids':
            ['01GW2G3V0S59R238FAHPDS1R66'], 'alert_source_id': '01GW2G3V0S59R238FAHPDS1R66', 'attributes': [{'array_value':
            [{'catalog_entry': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Primary On-call'}, 'label': 'Payments Team', 'literal': 'SEV123'}], 'attribute': {'array': False, 'emoji':
            'fire', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'service', 'required': False, 'type':
            'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}, 'value': {'catalog_entry': {'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'label': 'Payments
            Team', 'literal': 'SEV123'}}], 'created_at': '2021-08-17T13:28:57.801578Z', 'deduplication_key': '4293868629',
            'description': 'CPU on the payments service has exceeded 75 percent for 5 minutes', 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at': '2021-08-17T14:28:57.801578Z', 'source_url': 'https://www.my-
            alerting-platform.com/alerts/my-alert-123', 'status': 'firing', 'tags': [{'id': '01GW2G3V0S59R238FAHPDS1R66',
            'name': 'noisy'}], 'title': '*errors.withMessage: PG::Error failed to connect', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        event_type (WebhooksPublicAlertCreatedV1ResponseBodyEventType): What type of event is this webhook for? Example:
            public_alert.alert_created_v1.
        public_alert_alert_created_v1 (AlertV2):  Example: {'alert_group_ids': ['01GW2G3V0S59R238FAHPDS1R66'],
            'alert_source_id': '01GW2G3V0S59R238FAHPDS1R66', 'attributes': [{'array_value': [{'catalog_entry':
            {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-
            call'}, 'label': 'Payments Team', 'literal': 'SEV123'}], 'attribute': {'array': False, 'emoji': 'fire', 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'name': 'service', 'required': False, 'type':
            'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}, 'value': {'catalog_entry': {'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'label': 'Payments
            Team', 'literal': 'SEV123'}}], 'created_at': '2021-08-17T13:28:57.801578Z', 'deduplication_key': '4293868629',
            'description': 'CPU on the payments service has exceeded 75 percent for 5 minutes', 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at': '2021-08-17T14:28:57.801578Z', 'source_url': 'https://www.my-
            alerting-platform.com/alerts/my-alert-123', 'status': 'firing', 'tags': [{'id': '01GW2G3V0S59R238FAHPDS1R66',
            'name': 'noisy'}], 'title': '*errors.withMessage: PG::Error failed to connect', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    event_type: WebhooksPublicAlertCreatedV1ResponseBodyEventType
    public_alert_alert_created_v1: AlertV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        public_alert_alert_created_v1 = self.public_alert_alert_created_v1.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "public_alert.alert_created_v1": public_alert_alert_created_v1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_v2 import AlertV2

        d = dict(src_dict)
        event_type = WebhooksPublicAlertCreatedV1ResponseBodyEventType(
            d.pop("event_type")
        )

        public_alert_alert_created_v1 = AlertV2.from_dict(
            d.pop("public_alert.alert_created_v1")
        )

        webhooks_public_alert_created_v1_response_body = cls(
            event_type=event_type,
            public_alert_alert_created_v1=public_alert_alert_created_v1,
        )

        webhooks_public_alert_created_v1_response_body.additional_properties = d
        return webhooks_public_alert_created_v1_response_body

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
