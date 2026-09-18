from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentUpdatesCreatePayloadV2")


@_attrs_define
class IncidentUpdatesCreatePayloadV2:
    """
    Example:
        {'idempotency_key': 'alert-uuid', 'incident_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'message': "We're working on a
            fix, hoping to ship in the next 30 minutes", 'to_incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'to_severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}

    Attributes:
        idempotency_key (str): Unique string used to de-duplicate incident update requests. Retrying with the same key
            returns the update the first request created, rather than sharing a second one. Example: alert-uuid.
        incident_id (str): The incident you want to update Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        message (str | Unset): Message that explains the context behind the update, in markdown Example: We're working
            on a fix, hoping to ship in the next 30 minutes.
        to_incident_status_id (str | Unset): Move the incident to this status Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        to_severity_id (str | Unset): Move the incident to this severity Example: 01FH5TZRWMNAFB0DZ23FD1TV96.
    """

    idempotency_key: str
    incident_id: str
    message: str | Unset = UNSET
    to_incident_status_id: str | Unset = UNSET
    to_severity_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idempotency_key = self.idempotency_key

        incident_id = self.incident_id

        message = self.message

        to_incident_status_id = self.to_incident_status_id

        to_severity_id = self.to_severity_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idempotency_key": idempotency_key,
                "incident_id": incident_id,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if to_incident_status_id is not UNSET:
            field_dict["to_incident_status_id"] = to_incident_status_id
        if to_severity_id is not UNSET:
            field_dict["to_severity_id"] = to_severity_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        idempotency_key = d.pop("idempotency_key")

        incident_id = d.pop("incident_id")

        message = d.pop("message", UNSET)

        to_incident_status_id = d.pop("to_incident_status_id", UNSET)

        to_severity_id = d.pop("to_severity_id", UNSET)

        incident_updates_create_payload_v2 = cls(
            idempotency_key=idempotency_key,
            incident_id=incident_id,
            message=message,
            to_incident_status_id=to_incident_status_id,
            to_severity_id=to_severity_id,
        )

        incident_updates_create_payload_v2.additional_properties = d
        return incident_updates_create_payload_v2

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
