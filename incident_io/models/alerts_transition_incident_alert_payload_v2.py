from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alerts_transition_incident_alert_payload_v2_state import (
    AlertsTransitionIncidentAlertPayloadV2State,
)

T = TypeVar("T", bound="AlertsTransitionIncidentAlertPayloadV2")


@_attrs_define(kw_only=True)
class AlertsTransitionIncidentAlertPayloadV2:
    """
    Example:
        {'state': 'related'}

    Attributes:
        state (AlertsTransitionIncidentAlertPayloadV2State): What state to move the connection to Example: related.
    """

    state: AlertsTransitionIncidentAlertPayloadV2State
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        state = AlertsTransitionIncidentAlertPayloadV2State(d.pop("state"))

        alerts_transition_incident_alert_payload_v2 = cls(
            state=state,
        )

        alerts_transition_incident_alert_payload_v2.additional_properties = d
        return alerts_transition_incident_alert_payload_v2

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
