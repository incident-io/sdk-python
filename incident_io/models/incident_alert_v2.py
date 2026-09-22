from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_slim_v2 import AlertSlimV2
    from ..models.incident_slim_v2 import IncidentSlimV2


T = TypeVar("T", bound="IncidentAlertV2")


@_attrs_define(kw_only=True)
class IncidentAlertV2:
    """
    Example:
        {'alert': {'alert_group_ids': ['01GW2G3V0S59R238FAHPDS1R66'], 'alert_source_id': '01GW2G3V0S59R238FAHPDS1R66',
            'created_at': '2021-08-17T13:28:57.801578Z', 'deduplication_key': '4293868629', 'description': 'CPU on the
            payments service has exceeded 75 percent for 5 minutes', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at':
            '2021-08-17T14:28:57.801578Z', 'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123',
            'status': 'firing', 'title': '*errors.withMessage: PG::Error failed to connect', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'alert_route_id': '01GW2G3V0S59R238FAHPDS1R67', 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'incident': {'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our
            database is sad', 'reference': 'INC-123', 'status_category': 'triage', 'summary': "Our database is really really
            sad, and we don't know why yet.", 'visibility': 'public'}}

    Attributes:
        alert (AlertSlimV2):  Example: {'alert_group_ids': ['01GW2G3V0S59R238FAHPDS1R66'], 'alert_source_id':
            '01GW2G3V0S59R238FAHPDS1R66', 'created_at': '2021-08-17T13:28:57.801578Z', 'deduplication_key': '4293868629',
            'description': 'CPU on the payments service has exceeded 75 percent for 5 minutes', 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at': '2021-08-17T14:28:57.801578Z', 'source_url': 'https://www.my-
            alerting-platform.com/alerts/my-alert-123', 'status': 'firing', 'title': '*errors.withMessage: PG::Error failed
            to connect', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
        id (str): The ID of this alert Example: 01GW2G3V0S59R238FAHPDS1R66.
        incident (IncidentSlimV2): Incident slim is a subset of the full incident object, listing key fields. Example:
            {'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our database is sad', 'reference': 'INC-123',
            'status_category': 'triage', 'summary': "Our database is really really sad, and we don't know why yet.",
            'visibility': 'public'}.
        alert_route_id (str | Unset): The ID of the alert route that created this incident alert Example:
            01GW2G3V0S59R238FAHPDS1R67.
    """

    alert: AlertSlimV2
    id: str
    incident: IncidentSlimV2
    alert_route_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert = self.alert.to_dict()

        id = self.id

        incident = self.incident.to_dict()

        alert_route_id = self.alert_route_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert": alert,
                "id": id,
                "incident": incident,
            }
        )
        if alert_route_id is not UNSET:
            field_dict["alert_route_id"] = alert_route_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_slim_v2 import AlertSlimV2
        from ..models.incident_slim_v2 import IncidentSlimV2

        d = dict(src_dict)
        alert = AlertSlimV2.from_dict(d.pop("alert"))

        id = d.pop("id")

        incident = IncidentSlimV2.from_dict(d.pop("incident"))

        alert_route_id = d.pop("alert_route_id", UNSET)

        incident_alert_v2 = cls(
            alert=alert,
            id=id,
            incident=incident,
            alert_route_id=alert_route_id,
        )

        incident_alert_v2.additional_properties = d
        return incident_alert_v2

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
