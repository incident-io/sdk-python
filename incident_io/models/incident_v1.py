from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_v1_mode import IncidentV1Mode
from ..models.incident_v1_status import IncidentV1Status
from ..models.incident_v1_visibility import IncidentV1Visibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v1 import ActorV1
    from ..models.custom_field_entry_v1 import CustomFieldEntryV1
    from ..models.incident_role_assignment_v1 import IncidentRoleAssignmentV1
    from ..models.incident_timestamp_value_v1 import IncidentTimestampValueV1
    from ..models.incident_type_v1 import IncidentTypeV1
    from ..models.severity_v1 import SeverityV1


T = TypeVar("T", bound="IncidentV1")


@_attrs_define
class IncidentV1:
    """
    Example:
        {'call_url': 'https://zoom.us/foo', 'created_at': '2021-08-17T13:28:57.801578Z', 'creator': {'api_key': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}},
            'custom_field_entries': [{'custom_field': {'description': 'Which team is impacted by this issue', 'field_type':
            'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]},
            'values': [{'value_catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'},
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}]}], 'id': '01FDAG4SAP5TYPT98WGR2N7W91',
            'incident_role_assignments': [{'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': False, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}], 'incident_type': {'create_in_triage': 'always', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'private_incidents_only': False, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'mode': 'real', 'name': 'Our database is sad', 'permalink': 'https://app.incident.io/incidents/123',
            'postmortem_document_url': 'https://docs.google.com/my_doc_id', 'reference': 'INC-123', 'severity':
            {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'slack_channel_id': 'C02AW36C1M5', 'slack_channel_name': 'inc-165-green-parrot', 'slack_team_id': 'T02A1FSLE8J',
            'status': 'triage', 'summary': "Our database is really really sad, and we don't know why yet.", 'timestamps':
            [{'last_occurred_at': '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'}], 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}

    Attributes:
        created_at (datetime.datetime): When the incident was created Example: 2021-08-17T13:28:57.801578Z.
        creator (ActorV1):  Example: {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'viewer', 'slack_user_id': 'U02AYNF2XJM'}}.
        custom_field_entries (list[CustomFieldEntryV1]): Custom field entries for this incident Example:
            [{'custom_field': {'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]},
            'values': [{'value_catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'},
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}]}].
        id (str): Unique identifier for the incident Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        incident_role_assignments (list[IncidentRoleAssignmentV1]): A list of who is assigned to each role for this
            incident Example: [{'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': False, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}].
        mode (IncidentV1Mode): Whether the incident is real, a test, a tutorial, or importing as a retrospective
            incident Example: real.
        name (str): Explanation of the incident Example: Our database is sad.
        reference (str): Reference to this incident, as displayed across the product Example: INC-123.
        slack_channel_id (str): ID of the Slack channel in the organisation Slack workspace. Note that the channel is
            sometimes created asynchronously, so may not be present when the incident is just created. Example: C02AW36C1M5.
        slack_team_id (str): ID of the Slack team / workspace. This is only required if you are using a Slack Enterprise
            Grid with multiple teams. Example: T02A1FSLE8J.
        status (IncidentV1Status): Current status of the incident Example: triage.
        updated_at (datetime.datetime): When the incident was last updated Example: 2021-08-17T13:28:57.801578Z.
        visibility (IncidentV1Visibility): Whether the incident should be open to anyone in your Slack workspace
            (public), or invite-only (private). For more information on Private Incidents see our
            [docs](https://docs.incident.io/incidents/sensitive-incidents). Example: public.
        call_url (str | Unset): The call URL attached to this incident Example: https://zoom.us/foo.
        incident_type (IncidentTypeV1 | Unset):  Example: {'create_in_triage': 'always', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'private_incidents_only': False, 'updated_at': '2021-08-17T13:28:57.801578Z'}.
        permalink (str | Unset): A permanent link to the homepage for this incident Example:
            https://app.incident.io/incidents/123.
        postmortem_document_url (str | Unset): The URL of the incident post-mortem document Example:
            https://docs.google.com/my_doc_id.
        severity (SeverityV1 | Unset):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues
            with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        slack_channel_name (str | Unset): Name of the slack channel Example: inc-165-green-parrot.
        summary (str | Unset): Detailed description of the incident Example: Our database is really really sad, and we
            don't know why yet..
        timestamps (list[IncidentTimestampValueV1] | Unset): Incident lifecycle events and when they last occurred
            Example: [{'last_occurred_at': '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'}].
    """

    created_at: datetime.datetime
    creator: ActorV1
    custom_field_entries: list[CustomFieldEntryV1]
    id: str
    incident_role_assignments: list[IncidentRoleAssignmentV1]
    mode: IncidentV1Mode
    name: str
    reference: str
    slack_channel_id: str
    slack_team_id: str
    status: IncidentV1Status
    updated_at: datetime.datetime
    visibility: IncidentV1Visibility
    call_url: str | Unset = UNSET
    incident_type: IncidentTypeV1 | Unset = UNSET
    permalink: str | Unset = UNSET
    postmortem_document_url: str | Unset = UNSET
    severity: SeverityV1 | Unset = UNSET
    slack_channel_name: str | Unset = UNSET
    summary: str | Unset = UNSET
    timestamps: list[IncidentTimestampValueV1] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        creator = self.creator.to_dict()

        custom_field_entries = []
        for custom_field_entries_item_data in self.custom_field_entries:
            custom_field_entries_item = custom_field_entries_item_data.to_dict()
            custom_field_entries.append(custom_field_entries_item)

        id = self.id

        incident_role_assignments = []
        for incident_role_assignments_item_data in self.incident_role_assignments:
            incident_role_assignments_item = (
                incident_role_assignments_item_data.to_dict()
            )
            incident_role_assignments.append(incident_role_assignments_item)

        mode = self.mode.value

        name = self.name

        reference = self.reference

        slack_channel_id = self.slack_channel_id

        slack_team_id = self.slack_team_id

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        visibility = self.visibility.value

        call_url = self.call_url

        incident_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident_type, Unset):
            incident_type = self.incident_type.to_dict()

        permalink = self.permalink

        postmortem_document_url = self.postmortem_document_url

        severity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.to_dict()

        slack_channel_name = self.slack_channel_name

        summary = self.summary

        timestamps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = []
            for timestamps_item_data in self.timestamps:
                timestamps_item = timestamps_item_data.to_dict()
                timestamps.append(timestamps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "creator": creator,
                "custom_field_entries": custom_field_entries,
                "id": id,
                "incident_role_assignments": incident_role_assignments,
                "mode": mode,
                "name": name,
                "reference": reference,
                "slack_channel_id": slack_channel_id,
                "slack_team_id": slack_team_id,
                "status": status,
                "updated_at": updated_at,
                "visibility": visibility,
            }
        )
        if call_url is not UNSET:
            field_dict["call_url"] = call_url
        if incident_type is not UNSET:
            field_dict["incident_type"] = incident_type
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if postmortem_document_url is not UNSET:
            field_dict["postmortem_document_url"] = postmortem_document_url
        if severity is not UNSET:
            field_dict["severity"] = severity
        if slack_channel_name is not UNSET:
            field_dict["slack_channel_name"] = slack_channel_name
        if summary is not UNSET:
            field_dict["summary"] = summary
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v1 import ActorV1
        from ..models.custom_field_entry_v1 import CustomFieldEntryV1
        from ..models.incident_role_assignment_v1 import (
            IncidentRoleAssignmentV1,
        )
        from ..models.incident_timestamp_value_v1 import (
            IncidentTimestampValueV1,
        )
        from ..models.incident_type_v1 import IncidentTypeV1
        from ..models.severity_v1 import SeverityV1

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        creator = ActorV1.from_dict(d.pop("creator"))

        custom_field_entries = []
        _custom_field_entries = d.pop("custom_field_entries")
        for custom_field_entries_item_data in _custom_field_entries:
            custom_field_entries_item = CustomFieldEntryV1.from_dict(
                custom_field_entries_item_data
            )

            custom_field_entries.append(custom_field_entries_item)

        id = d.pop("id")

        incident_role_assignments = []
        _incident_role_assignments = d.pop("incident_role_assignments")
        for incident_role_assignments_item_data in _incident_role_assignments:
            incident_role_assignments_item = IncidentRoleAssignmentV1.from_dict(
                incident_role_assignments_item_data
            )

            incident_role_assignments.append(incident_role_assignments_item)

        mode = IncidentV1Mode(d.pop("mode"))

        name = d.pop("name")

        reference = d.pop("reference")

        slack_channel_id = d.pop("slack_channel_id")

        slack_team_id = d.pop("slack_team_id")

        status = IncidentV1Status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        visibility = IncidentV1Visibility(d.pop("visibility"))

        call_url = d.pop("call_url", UNSET)

        _incident_type = d.pop("incident_type", UNSET)
        incident_type: IncidentTypeV1 | Unset
        if isinstance(_incident_type, Unset):
            incident_type = UNSET
        else:
            incident_type = IncidentTypeV1.from_dict(_incident_type)

        permalink = d.pop("permalink", UNSET)

        postmortem_document_url = d.pop("postmortem_document_url", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: SeverityV1 | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = SeverityV1.from_dict(_severity)

        slack_channel_name = d.pop("slack_channel_name", UNSET)

        summary = d.pop("summary", UNSET)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: list[IncidentTimestampValueV1] | Unset = UNSET
        if _timestamps is not UNSET:
            timestamps = []
            for timestamps_item_data in _timestamps:
                timestamps_item = IncidentTimestampValueV1.from_dict(
                    timestamps_item_data
                )

                timestamps.append(timestamps_item)

        incident_v1 = cls(
            created_at=created_at,
            creator=creator,
            custom_field_entries=custom_field_entries,
            id=id,
            incident_role_assignments=incident_role_assignments,
            mode=mode,
            name=name,
            reference=reference,
            slack_channel_id=slack_channel_id,
            slack_team_id=slack_team_id,
            status=status,
            updated_at=updated_at,
            visibility=visibility,
            call_url=call_url,
            incident_type=incident_type,
            permalink=permalink,
            postmortem_document_url=postmortem_document_url,
            severity=severity,
            slack_channel_name=slack_channel_name,
            summary=summary,
            timestamps=timestamps,
        )

        incident_v1.additional_properties = d
        return incident_v1

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
