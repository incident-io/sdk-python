from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_alert_v2 import IncidentAlertV2


T = TypeVar("T", bound="AlertsCreateIncidentAlertResultV2")


@_attrs_define(kw_only=True)
class AlertsCreateIncidentAlertResultV2:
    """
    Example:
        {'incident_alert': {'alert': {'alert_group_ids': ['01GW2G3V0S59R238FAHPDS1R66'], 'alert_source_id':
            '01GW2G3V0S59R238FAHPDS1R66', 'created_at': '2021-08-17T13:28:57.801578Z', 'deduplication_key': '4293868629',
            'description': 'CPU on the payments service has exceeded 75 percent for 5 minutes', 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at': '2021-08-17T14:28:57.801578Z', 'source_url': 'https://www.my-
            alerting-platform.com/alerts/my-alert-123', 'status': 'firing', 'title': '*errors.withMessage: PG::Error failed
            to connect', 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'alert_route_id': '01GW2G3V0S59R238FAHPDS1R67', 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'incident': {'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our
            database is sad', 'reference': 'INC-123', 'status_category': 'triage', 'summary': "Our database is really really
            sad, and we don't know why yet.", 'visibility': 'public'}}}

    Attributes:
        incident_alert (IncidentAlertV2):  Example: {'alert': {'alert_group_ids': ['01GW2G3V0S59R238FAHPDS1R66'],
            'alert_source_id': '01GW2G3V0S59R238FAHPDS1R66', 'created_at': '2021-08-17T13:28:57.801578Z',
            'deduplication_key': '4293868629', 'description': 'CPU on the payments service has exceeded 75 percent for 5
            minutes', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at': '2021-08-17T14:28:57.801578Z', 'source_url':
            'https://www.my-alerting-platform.com/alerts/my-alert-123', 'status': 'firing', 'title': '*errors.withMessage:
            PG::Error failed to connect', 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'alert_route_id':
            '01GW2G3V0S59R238FAHPDS1R67', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'incident': {'external_id': 123, 'id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our database is sad', 'reference': 'INC-123', 'status_category':
            'triage', 'summary': "Our database is really really sad, and we don't know why yet.", 'visibility': 'public'}}.
    """

    incident_alert: IncidentAlertV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_alert = self.incident_alert.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_alert": incident_alert,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_alert_v2 import IncidentAlertV2

        d = dict(src_dict)
        incident_alert = IncidentAlertV2.from_dict(d.pop("incident_alert"))

        alerts_create_incident_alert_result_v2 = cls(
            incident_alert=incident_alert,
        )

        alerts_create_incident_alert_result_v2.additional_properties = d
        return alerts_create_incident_alert_result_v2

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
