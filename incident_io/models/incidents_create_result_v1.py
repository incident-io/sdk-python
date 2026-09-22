from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_v1 import IncidentV1


T = TypeVar("T", bound="IncidentsCreateResultV1")


@_attrs_define(kw_only=True)
class IncidentsCreateResultV1:
    """
    Example:
        {'incident': {'call_url': 'https://zoom.us/foo', 'created_at': '2021-08-17T13:28:57.801578Z', 'creator':
            {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}}, 'custom_field_entries': [{'custom_field': {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected
            Team', 'options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}]}, 'values': [{'value_catalog_entry': {'aliases': ['lawrence@incident.io',
            'lawrence'], 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Primary On-call'}, 'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}]}], 'id': '01FDAG4SAP5TYPT98WGR2N7W91',
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
            '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}}

    Attributes:
        incident (IncidentV1):  Example: {'call_url': 'https://zoom.us/foo', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'creator': {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API
            key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}}, 'custom_field_entries': [{'custom_field': {'description':
            'Which team is impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Affected Team', 'options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]}, 'values': [{'value_catalog_entry':
            {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope you like it'}]}], 'id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'incident_role_assignments': [{'assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'},
            'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the
            incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are
            clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'role_type': 'lead', 'shortform':
            'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}], 'incident_type': {'create_in_triage': 'always',
            'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'private_incidents_only': False, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'mode': 'real', 'name': 'Our database is sad', 'permalink': 'https://app.incident.io/incidents/123',
            'postmortem_document_url': 'https://docs.google.com/my_doc_id', 'reference': 'INC-123', 'severity':
            {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'slack_channel_id': 'C02AW36C1M5', 'slack_channel_name': 'inc-165-green-parrot', 'slack_team_id': 'T02A1FSLE8J',
            'status': 'triage', 'summary': "Our database is really really sad, and we don't know why yet.", 'timestamps':
            [{'last_occurred_at': '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'}], 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}.
    """

    incident: IncidentV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident = self.incident.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident": incident,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_v1 import IncidentV1

        d = dict(src_dict)
        incident = IncidentV1.from_dict(d.pop("incident"))

        incidents_create_result_v1 = cls(
            incident=incident,
        )

        incidents_create_result_v1.additional_properties = d
        return incidents_create_result_v1

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
