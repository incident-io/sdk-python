from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_entry_payload_v2 import CustomFieldEntryPayloadV2
    from ..models.incident_role_assignment_payload_v2 import (
        IncidentRoleAssignmentPayloadV2,
    )
    from ..models.incident_timestamp_value_payload_v2 import (
        IncidentTimestampValuePayloadV2,
    )


T = TypeVar("T", bound="IncidentEditPayloadV2")


@_attrs_define
class IncidentEditPayloadV2:
    """
    Example:
        {'call_url': 'https://zoom.us/foo', 'custom_field_entries': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it', 'value_timestamp':
            ''}]}], 'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_status_id': 'abc123', 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our database is sad',
            'severity_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_channel_name_override': 'inc-123-database-down', 'summary':
            "Our database is really really sad, and we don't know why yet."}

    Attributes:
        call_url (str | Unset): The call URL attached to this incident Example: https://zoom.us/foo.
        custom_field_entries (list[CustomFieldEntryPayloadV2] | Unset): Set the incident's custom fields to these values
            Example: [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you
            like it', 'value_timestamp': ''}]}].
        incident_role_assignments (list[IncidentRoleAssignmentPayloadV2] | Unset): Assign incident roles to these people
            Example: [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id':
            'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}].
        incident_status_id (str | Unset): Incident status to move the incident to. Allowed transitions are:

            - Moving between statuses within the same category (e.g. between active statuses)
            - Resolving an incident by moving from active/triage to a post-incident or closed status
            - Closing an incident from a post-incident status

            When resolving to a post-incident status, the incident enters the post-incident flow and tasks are created. The
            status must belong to the post-incident flow that applies to this incident based on its severity, incident type,
            and other properties. If you specify a status from a different post-incident flow, the request will fail with a
            validation error.

            When resolving directly to closed, any configured post-incident flow is skipped entirely. This requires the
            'Close incidents by opting out of post-incident flow' permission on the API key, if your incident lifecycle
            normally requires you to run a post-incident flow for this incident.

            Note: Once an incident is in the post-incident flow, its status is managed automatically based on task
            completion. Moving between post-incident statuses via the API is not recommended as the system will recalculate
            the correct status when tasks are updated. Example: abc123.
        incident_timestamp_values (list[IncidentTimestampValuePayloadV2] | Unset): Assign the incident's timestamps to
            these values Example: [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}].
        name (str | Unset): Explanation of the incident Example: Our database is sad.
        severity_id (str | Unset): The ID of the current severity of this incident Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        slack_channel_name_override (str | Unset): Override the name of the incident Slack channel Example:
            inc-123-database-down.
        summary (str | Unset): Detailed description of the incident Example: Our database is really really sad, and we
            don't know why yet..
    """

    call_url: str | Unset = UNSET
    custom_field_entries: list[CustomFieldEntryPayloadV2] | Unset = UNSET
    incident_role_assignments: list[IncidentRoleAssignmentPayloadV2] | Unset = UNSET
    incident_status_id: str | Unset = UNSET
    incident_timestamp_values: list[IncidentTimestampValuePayloadV2] | Unset = UNSET
    name: str | Unset = UNSET
    severity_id: str | Unset = UNSET
    slack_channel_name_override: str | Unset = UNSET
    summary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_url = self.call_url

        custom_field_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_field_entries, Unset):
            custom_field_entries = []
            for custom_field_entries_item_data in self.custom_field_entries:
                custom_field_entries_item = custom_field_entries_item_data.to_dict()
                custom_field_entries.append(custom_field_entries_item)

        incident_role_assignments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.incident_role_assignments, Unset):
            incident_role_assignments = []
            for incident_role_assignments_item_data in self.incident_role_assignments:
                incident_role_assignments_item = (
                    incident_role_assignments_item_data.to_dict()
                )
                incident_role_assignments.append(incident_role_assignments_item)

        incident_status_id = self.incident_status_id

        incident_timestamp_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.incident_timestamp_values, Unset):
            incident_timestamp_values = []
            for incident_timestamp_values_item_data in self.incident_timestamp_values:
                incident_timestamp_values_item = (
                    incident_timestamp_values_item_data.to_dict()
                )
                incident_timestamp_values.append(incident_timestamp_values_item)

        name = self.name

        severity_id = self.severity_id

        slack_channel_name_override = self.slack_channel_name_override

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if call_url is not UNSET:
            field_dict["call_url"] = call_url
        if custom_field_entries is not UNSET:
            field_dict["custom_field_entries"] = custom_field_entries
        if incident_role_assignments is not UNSET:
            field_dict["incident_role_assignments"] = incident_role_assignments
        if incident_status_id is not UNSET:
            field_dict["incident_status_id"] = incident_status_id
        if incident_timestamp_values is not UNSET:
            field_dict["incident_timestamp_values"] = incident_timestamp_values
        if name is not UNSET:
            field_dict["name"] = name
        if severity_id is not UNSET:
            field_dict["severity_id"] = severity_id
        if slack_channel_name_override is not UNSET:
            field_dict["slack_channel_name_override"] = slack_channel_name_override
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_field_entry_payload_v2 import (
            CustomFieldEntryPayloadV2,
        )
        from ..models.incident_role_assignment_payload_v2 import (
            IncidentRoleAssignmentPayloadV2,
        )
        from ..models.incident_timestamp_value_payload_v2 import (
            IncidentTimestampValuePayloadV2,
        )

        d = dict(src_dict)
        call_url = d.pop("call_url", UNSET)

        _custom_field_entries = d.pop("custom_field_entries", UNSET)
        custom_field_entries: list[CustomFieldEntryPayloadV2] | Unset = UNSET
        if _custom_field_entries is not UNSET:
            custom_field_entries = []
            for custom_field_entries_item_data in _custom_field_entries:
                custom_field_entries_item = CustomFieldEntryPayloadV2.from_dict(
                    custom_field_entries_item_data
                )

                custom_field_entries.append(custom_field_entries_item)

        _incident_role_assignments = d.pop("incident_role_assignments", UNSET)
        incident_role_assignments: list[IncidentRoleAssignmentPayloadV2] | Unset = UNSET
        if _incident_role_assignments is not UNSET:
            incident_role_assignments = []
            for incident_role_assignments_item_data in _incident_role_assignments:
                incident_role_assignments_item = (
                    IncidentRoleAssignmentPayloadV2.from_dict(
                        incident_role_assignments_item_data
                    )
                )

                incident_role_assignments.append(incident_role_assignments_item)

        incident_status_id = d.pop("incident_status_id", UNSET)

        _incident_timestamp_values = d.pop("incident_timestamp_values", UNSET)
        incident_timestamp_values: list[IncidentTimestampValuePayloadV2] | Unset = UNSET
        if _incident_timestamp_values is not UNSET:
            incident_timestamp_values = []
            for incident_timestamp_values_item_data in _incident_timestamp_values:
                incident_timestamp_values_item = (
                    IncidentTimestampValuePayloadV2.from_dict(
                        incident_timestamp_values_item_data
                    )
                )

                incident_timestamp_values.append(incident_timestamp_values_item)

        name = d.pop("name", UNSET)

        severity_id = d.pop("severity_id", UNSET)

        slack_channel_name_override = d.pop("slack_channel_name_override", UNSET)

        summary = d.pop("summary", UNSET)

        incident_edit_payload_v2 = cls(
            call_url=call_url,
            custom_field_entries=custom_field_entries,
            incident_role_assignments=incident_role_assignments,
            incident_status_id=incident_status_id,
            incident_timestamp_values=incident_timestamp_values,
            name=name,
            severity_id=severity_id,
            slack_channel_name_override=slack_channel_name_override,
            summary=summary,
        )

        incident_edit_payload_v2.additional_properties = d
        return incident_edit_payload_v2

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
