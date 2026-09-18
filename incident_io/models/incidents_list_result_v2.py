from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_v2 import IncidentV2
    from ..models.pagination_meta_result_with_total_v2 import (
        PaginationMetaResultWithTotalV2,
    )


T = TypeVar("T", bound="IncidentsListResultV2")


@_attrs_define
class IncidentsListResultV2:
    """
    Example:
        {'incidents': [{'call_url': 'https://zoom.us/foo', 'created_at': '2021-08-17T13:28:57.801578Z', 'creator':
            {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
            'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'custom_field_entries': [{'custom_field': {'description': 'Which team is impacted by this issue',
            'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}]}, 'values': [{'value_catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'],
            'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-
            call'}, 'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}]}], 'duration_metrics': [{'duration_metric': {'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Lasted'}, 'status': 'success', 'value_seconds': 10800}],
            'external_issue_reference': {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-
            io/issue/INC-1609/find-copywriter-to-write-up', 'provider': 'asana'}, 'has_debrief': False, 'id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'incident_role_assignments': [{'assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the
            incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are
            clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'role_type': 'lead', 'shortform':
            'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}], 'incident_status': {'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'incident_timestamp_values': [{'incident_timestamp': {'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1}, 'value': {'value':
            '2021-08-17T13:28:57.801578Z'}}], 'incident_type': {'create_in_triage': 'always', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'last_activity_at': '2021-08-17T13:28:57.801578Z', 'mode':
            'standard', 'ms_teams_channel_url': 'https://teams.microsoft.com/l/channel/19%some-
            hex%40thread.tacv2/inc-123-title?groupId=some-uuid&tenantId=another-uuid', 'name': 'Our database is sad',
            'permalink': 'https://app.incident.io/incidents/123', 'postmortem_document_ids': ['01FCNDV6P870EA6S7TK1DSYD5H'],
            'postmortem_document_url': 'https://docs.google.com/my_doc_id', 'reference': 'INC-123', 'severity':
            {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'slack_channel_id': 'C02AW36C1M5', 'slack_channel_name': 'inc-165-green-parrot', 'slack_channel_url':
            'https://slack.com/app_redirect?team=T1234&channel=C5678', 'slack_team_id': 'T02A1FSLE8J', 'summary': "Our
            database is really really sad, and we don't know why yet.", 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'],
            'updated_at': '2021-08-17T13:28:57.801578Z', 'visibility': 'public', 'workload_minutes_late': 40.7,
            'workload_minutes_sleeping': 0, 'workload_minutes_total': 60.7, 'workload_minutes_working': 20}],
            'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25, 'total_record_count': 238}}

    Attributes:
        incidents (list[IncidentV2]):  Example: [{'call_url': 'https://zoom.us/foo', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}, 'custom_field_entries': [{'custom_field': {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected
            Team', 'options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}]}, 'values': [{'value_catalog_entry': {'aliases': ['lawrence@incident.io',
            'lawrence'], 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Primary On-call'}, 'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}]}], 'duration_metrics':
            [{'duration_metric': {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Lasted'}, 'status': 'success',
            'value_seconds': 10800}], 'external_issue_reference': {'issue_name': 'INC-123', 'issue_permalink':
            'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up', 'provider': 'asana'},
            'has_debrief': False, 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'incident_role_assignments': [{'assignee': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The
            person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on
            the incident; Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': False,
            'role_type': 'lead', 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}], 'incident_status':
            {'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully
            mitigated**, and we're ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name':
            'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'incident_timestamp_values':
            [{'incident_timestamp': {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1}, 'value':
            {'value': '2021-08-17T13:28:57.801578Z'}}], 'incident_type': {'create_in_triage': 'always', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'last_activity_at': '2021-08-17T13:28:57.801578Z', 'mode':
            'standard', 'ms_teams_channel_url': 'https://teams.microsoft.com/l/channel/19%some-
            hex%40thread.tacv2/inc-123-title?groupId=some-uuid&tenantId=another-uuid', 'name': 'Our database is sad',
            'permalink': 'https://app.incident.io/incidents/123', 'postmortem_document_ids': ['01FCNDV6P870EA6S7TK1DSYD5H'],
            'postmortem_document_url': 'https://docs.google.com/my_doc_id', 'reference': 'INC-123', 'severity':
            {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'slack_channel_id': 'C02AW36C1M5', 'slack_channel_name': 'inc-165-green-parrot', 'slack_channel_url':
            'https://slack.com/app_redirect?team=T1234&channel=C5678', 'slack_team_id': 'T02A1FSLE8J', 'summary': "Our
            database is really really sad, and we don't know why yet.", 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'],
            'updated_at': '2021-08-17T13:28:57.801578Z', 'visibility': 'public', 'workload_minutes_late': 40.7,
            'workload_minutes_sleeping': 0, 'workload_minutes_total': 60.7, 'workload_minutes_working': 20}].
        pagination_meta (PaginationMetaResultWithTotalV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0',
            'page_size': 25, 'total_record_count': 238}.
    """

    incidents: list[IncidentV2]
    pagination_meta: PaginationMetaResultWithTotalV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incidents = []
        for incidents_item_data in self.incidents:
            incidents_item = incidents_item_data.to_dict()
            incidents.append(incidents_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incidents": incidents,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_v2 import IncidentV2
        from ..models.pagination_meta_result_with_total_v2 import (
            PaginationMetaResultWithTotalV2,
        )

        d = dict(src_dict)
        incidents = []
        _incidents = d.pop("incidents")
        for incidents_item_data in _incidents:
            incidents_item = IncidentV2.from_dict(incidents_item_data)

            incidents.append(incidents_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultWithTotalV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultWithTotalV2.from_dict(
                _pagination_meta
            )

        incidents_list_result_v2 = cls(
            incidents=incidents,
            pagination_meta=pagination_meta,
        )

        incidents_list_result_v2.additional_properties = d
        return incidents_list_result_v2

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
