from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertsCreateIncidentAlertPayloadV2")


@_attrs_define
class AlertsCreateIncidentAlertPayloadV2:
    """
    Example:
        {'alert_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 're_relate': False}

    Attributes:
        alert_id (str): Alert to attach to the incident Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        incident_id (str): Incident to attach the alert to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        re_relate (bool | Unset): Relate the alert again even though someone previously marked it unrelated to this
            incident. Defaults to false, which preserves that decision and returns a 422 Default: False. Example: False.
    """

    alert_id: str
    incident_id: str
    re_relate: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_id = self.alert_id

        incident_id = self.incident_id

        re_relate = self.re_relate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_id": alert_id,
                "incident_id": incident_id,
            }
        )
        if re_relate is not UNSET:
            field_dict["re_relate"] = re_relate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alert_id = d.pop("alert_id")

        incident_id = d.pop("incident_id")

        re_relate = d.pop("re_relate", UNSET)

        alerts_create_incident_alert_payload_v2 = cls(
            alert_id=alert_id,
            incident_id=incident_id,
            re_relate=re_relate,
        )

        alerts_create_incident_alert_payload_v2.additional_properties = d
        return alerts_create_incident_alert_payload_v2

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
