from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_activity_log_entry_v2_type import IncidentActivityLogEntryV2Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_activity_log_content_v2 import IncidentActivityLogContentV2


T = TypeVar("T", bound="IncidentActivityLogEntryV2")


@_attrs_define
class IncidentActivityLogEntryV2:
    """One thing that happened on an incident.

    The activity log records everything. The timeline is the narrative, made of the entries
    someone promoted onto it and the items they wrote by hand.

        Example:
            {'content': {'action_created': {'action_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'actor': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}}, 'action_updated':
                {'action_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'new_assignee': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'new_status': 'completed', 'previous_assignee': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'previous_status': 'outstanding', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'alert_attached_to_incident': {'actor': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'alert_id':
                '01FCNDV6P870EA6S7TK1DSYDG0'}, 'custom_field_value_update': {'custom_field': {'description': 'Which team is
                impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected
                Team', 'options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'sort_key': 10, 'value': 'Product'}]}, 'new_values': [{'value_catalog_entry': {'aliases':
                ['lawrence@incident.io', 'lawrence'], 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'value_link': 'https://google.com/', 'value_numeric':
                '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope you like it'}],
                'new_values_count': 4, 'previous_values': [{'value_catalog_entry': {'aliases': ['lawrence@incident.io',
                'lawrence'], 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
                'Primary On-call'}, 'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
                {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
                'Product'}, 'value_text': 'This is my text field, I hope you like it'}], 'previous_values_count': 3, 'updater':
                {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
                'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}}, 'escalation_acknowledged': {'acknowledger': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'escalation_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_created': {'creator': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'escalated_to_users':
                [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
                'owner', 'slack_user_id': 'U02AYNF2XJM'}], 'escalation_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'escalation_path_id':
                '01FCNDV6P870EA6S7TK1DSYDG1'}, 'follow_up_created': {'actor': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66',
                'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
                'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'follow_up_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
                'follow_up_updated': {'follow_up_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'new_assignee': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'new_status': 'completed', 'new_title': 'Add a payments-api rollback runbook',
                'previous_assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'previous_status': 'outstanding', 'previous_title':
                'Add a runbook', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
                PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
                'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
                'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}}, 'incident_merged': {'incident_update_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'merger': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'source_incident':
                {'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our database is sad', 'reference': 'INC-123',
                'status_category': 'triage', 'summary': "Our database is really really sad, and we don't know why yet.",
                'visibility': 'public'}}, 'incident_rename': {'new_name': 'EU checkout failing after 14:02 deploy',
                'previous_name': 'Checkout errors', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'incident_timestamp_set': {'incident_timestamp': {'id':
                '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1}, 'new_value': '2026-09-01T13:42:00Z',
                'previous_value': '2026-09-01T14:00:00Z', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'incident_type_changed': {'new_incident_type': {'create_in_triage': 'always',
                'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
                'updated_at': '2021-08-17T13:28:57.801578Z'}, 'previous_incident_type': {'create_in_triage': 'always',
                'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
                'updated_at': '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'incident_update': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'message': 'Rolled back
                **payments-api** to v411, error rate recovering.', 'new_severity': {'created_at': '2021-08-17T13:28:57.801578Z',
                'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1,
                'updated_at': '2021-08-17T13:28:57.801578Z'}, 'new_status': {'category': 'triage', 'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
                from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
                '2021-08-17T13:28:57.801578Z'}, 'next_update_in_minutes': 30, 'previous_severity': {'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'previous_status': {'category':
                'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and
                we're ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4,
                'updated_at': '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'incident_visibility_changed': {'new_visibility': 'private',
                'previous_visibility': 'public', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'role_update': {'new_assignee': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'previous_assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z',
                'description': 'The person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'instructions': 'Take point on the incident; Make sure people are clear on responsibilities', 'name': 'Incident
                Lead', 'role_type': 'lead', 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'updater':
                {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
                'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}}, 'status_change': {'new_status': {'category': 'triage', 'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
                from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
                '2021-08-17T13:28:57.801578Z'}, 'previous_status': {'category': 'triage', 'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
                from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
                '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'summary_update': {'new_summary': 'Checkout is failing for all EU customers
                since the 14:02 deploy.', 'previous_summary': 'Checkout is failing for some customers.', 'updater': {'alert':
                {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key':
                {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}}, 'workflow_ran': {'creator':
                {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
                'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}, 'event_description': 'Stopped the synthetic load test in staging.', 'event_title': 'Load test
                halted'}}, 'created_at': '2026-09-01T15:30:01Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'occurred_at': '2026-09-01T15:30:00Z', 'title': 'Status changed from Investigating
                to Monitoring', 'type': 'incident_update'}

        Attributes:
            created_at (datetime.datetime): When we recorded the activity Example: 2026-09-01T15:30:01Z.
            id (str): Unique identifier of the activity log entry Example: 01FCNDV6P870EA6S7TK1DSYDG0.
            incident_id (str): ID of the incident this happened on. When the incident has streams, listing the parent also
                returns entries from its streams, and this is the stream's ID for those. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
            occurred_at (datetime.datetime): When the activity happened. This is what the log is ordered by. Example:
                2026-09-01T15:30:00Z.
            title (str): Human-readable summary of what happened Example: Status changed from Investigating to Monitoring.
            type_ (IncidentActivityLogEntryV2Type): What kind of activity this is. Switch on this rather than title, which
                is display copy we reword. Example: incident_update.
            content (IncidentActivityLogContentV2 | Unset): Details of an activity log entry.

                At most one key is set, and it matches the entry's type. Types not listed here carry no
                content: the entry's type and title are all there is. Example: {'action_created': {'action_id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'actor': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'action_updated': {'action_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'new_assignee':
                {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'new_status': 'completed', 'previous_assignee': {'email': 'lisa@incident.io',
                'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
                'U02AYNF2XJM'}, 'previous_status': 'outstanding', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66',
                'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
                'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}}, 'alert_attached_to_incident': {'actor': {'alert':
                {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key':
                {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'alert_id':
                '01FCNDV6P870EA6S7TK1DSYDG0'}, 'custom_field_value_update': {'custom_field': {'description': 'Which team is
                impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected
                Team', 'options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'sort_key': 10, 'value': 'Product'}]}, 'new_values': [{'value_catalog_entry': {'aliases':
                ['lawrence@incident.io', 'lawrence'], 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'value_link': 'https://google.com/', 'value_numeric':
                '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope you like it'}],
                'new_values_count': 4, 'previous_values': [{'value_catalog_entry': {'aliases': ['lawrence@incident.io',
                'lawrence'], 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
                'Primary On-call'}, 'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
                {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
                'Product'}, 'value_text': 'This is my text field, I hope you like it'}], 'previous_values_count': 3, 'updater':
                {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
                'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}}, 'escalation_acknowledged': {'acknowledger': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'escalation_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_created': {'creator': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'escalated_to_users':
                [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
                'owner', 'slack_user_id': 'U02AYNF2XJM'}], 'escalation_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'escalation_path_id':
                '01FCNDV6P870EA6S7TK1DSYDG1'}, 'follow_up_created': {'actor': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66',
                'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
                'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'follow_up_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
                'follow_up_updated': {'follow_up_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'new_assignee': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'new_status': 'completed', 'new_title': 'Add a payments-api rollback runbook',
                'previous_assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'previous_status': 'outstanding', 'previous_title':
                'Add a runbook', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
                PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
                'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
                'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}}, 'incident_merged': {'incident_update_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'merger': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'source_incident':
                {'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our database is sad', 'reference': 'INC-123',
                'status_category': 'triage', 'summary': "Our database is really really sad, and we don't know why yet.",
                'visibility': 'public'}}, 'incident_rename': {'new_name': 'EU checkout failing after 14:02 deploy',
                'previous_name': 'Checkout errors', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'incident_timestamp_set': {'incident_timestamp': {'id':
                '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1}, 'new_value': '2026-09-01T13:42:00Z',
                'previous_value': '2026-09-01T14:00:00Z', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'incident_type_changed': {'new_incident_type': {'create_in_triage': 'always',
                'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
                'updated_at': '2021-08-17T13:28:57.801578Z'}, 'previous_incident_type': {'create_in_triage': 'always',
                'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
                'updated_at': '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'incident_update': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'message': 'Rolled back
                **payments-api** to v411, error rate recovering.', 'new_severity': {'created_at': '2021-08-17T13:28:57.801578Z',
                'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1,
                'updated_at': '2021-08-17T13:28:57.801578Z'}, 'new_status': {'category': 'triage', 'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
                from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
                '2021-08-17T13:28:57.801578Z'}, 'next_update_in_minutes': 30, 'previous_severity': {'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'previous_status': {'category':
                'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and
                we're ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4,
                'updated_at': '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'incident_visibility_changed': {'new_visibility': 'private',
                'previous_visibility': 'public', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'role_update': {'new_assignee': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'previous_assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z',
                'description': 'The person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'instructions': 'Take point on the incident; Make sure people are clear on responsibilities', 'name': 'Incident
                Lead', 'role_type': 'lead', 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'updater':
                {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
                'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}}, 'status_change': {'new_status': {'category': 'triage', 'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
                from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
                '2021-08-17T13:28:57.801578Z'}, 'previous_status': {'category': 'triage', 'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
                from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
                '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}, 'summary_update': {'new_summary': 'Checkout is failing for all EU customers
                since the 14:02 deploy.', 'previous_summary': 'Checkout is failing for some customers.', 'updater': {'alert':
                {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key':
                {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}}, 'workflow_ran': {'creator':
                {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
                'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}, 'event_description': 'Stopped the synthetic load test in staging.', 'event_title': 'Load test
                halted'}}.
    """

    created_at: datetime.datetime
    id: str
    incident_id: str
    occurred_at: datetime.datetime
    title: str
    type_: IncidentActivityLogEntryV2Type
    content: IncidentActivityLogContentV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        incident_id = self.incident_id

        occurred_at = self.occurred_at.isoformat()

        title = self.title

        type_ = self.type_.value

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "incident_id": incident_id,
                "occurred_at": occurred_at,
                "title": title,
                "type": type_,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_activity_log_content_v2 import (
            IncidentActivityLogContentV2,
        )

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        title = d.pop("title")

        type_ = IncidentActivityLogEntryV2Type(d.pop("type"))

        _content = d.pop("content", UNSET)
        content: IncidentActivityLogContentV2 | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = IncidentActivityLogContentV2.from_dict(_content)

        incident_activity_log_entry_v2 = cls(
            created_at=created_at,
            id=id,
            incident_id=incident_id,
            occurred_at=occurred_at,
            title=title,
            type_=type_,
            content=content,
        )

        incident_activity_log_entry_v2.additional_properties = d
        return incident_activity_log_entry_v2

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
