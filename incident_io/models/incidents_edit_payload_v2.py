from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_edit_payload_v2 import IncidentEditPayloadV2


T = TypeVar("T", bound="IncidentsEditPayloadV2")


@_attrs_define
class IncidentsEditPayloadV2:
    """
    Example:
        {'incident': {'call_url': 'https://zoom.us/foo', 'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_status_id': 'abc123', 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our database is sad',
            'severity_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_channel_name_override': 'inc-123-database-down', 'summary':
            "Our database is really really sad, and we don't know why yet."}, 'notify_incident_channel': True}

    Attributes:
        incident (IncidentEditPayloadV2):  Example: {'call_url': 'https://zoom.us/foo', 'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you
            like it', 'value_timestamp': ''}]}], 'incident_role_assignments': [{'assignee': {'email': 'bob@example.com',
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id': 'abc123', 'incident_timestamp_values':
            [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_channel_name_override': 'inc-123-database-
            down', 'summary': "Our database is really really sad, and we don't know why yet."}.
        notify_incident_channel (bool): Should we send Slack channel notifications to inform responders of this update?
            Note that this won't work if the Slack channel has already been archived. Example: True.
    """

    incident: IncidentEditPayloadV2
    notify_incident_channel: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident = self.incident.to_dict()

        notify_incident_channel = self.notify_incident_channel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident": incident,
                "notify_incident_channel": notify_incident_channel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_edit_payload_v2 import (
            IncidentEditPayloadV2,
        )

        d = dict(src_dict)
        incident = IncidentEditPayloadV2.from_dict(d.pop("incident"))

        notify_incident_channel = d.pop("notify_incident_channel")

        incidents_edit_payload_v2 = cls(
            incident=incident,
            notify_incident_channel=notify_incident_channel,
        )

        incidents_edit_payload_v2.additional_properties = d
        return incidents_edit_payload_v2

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
