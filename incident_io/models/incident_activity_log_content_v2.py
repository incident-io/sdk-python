from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_action_ref_v2 import ActivityActionRefV2
    from ..models.activity_action_updated_v2 import ActivityActionUpdatedV2
    from ..models.activity_alert_ref_v2 import ActivityAlertRefV2
    from ..models.activity_custom_field_value_update_v2 import (
        ActivityCustomFieldValueUpdateV2,
    )
    from ..models.activity_escalation_acknowledged_v2 import (
        ActivityEscalationAcknowledgedV2,
    )
    from ..models.activity_escalation_created_v2 import ActivityEscalationCreatedV2
    from ..models.activity_follow_up_ref_v2 import ActivityFollowUpRefV2
    from ..models.activity_follow_up_updated_v2 import ActivityFollowUpUpdatedV2
    from ..models.activity_incident_merged_v2 import ActivityIncidentMergedV2
    from ..models.activity_incident_rename_v2 import ActivityIncidentRenameV2
    from ..models.activity_incident_timestamp_set_v2 import (
        ActivityIncidentTimestampSetV2,
    )
    from ..models.activity_incident_type_changed_v2 import ActivityIncidentTypeChangedV2
    from ..models.activity_incident_update_v2 import ActivityIncidentUpdateV2
    from ..models.activity_incident_visibility_changed_v2 import (
        ActivityIncidentVisibilityChangedV2,
    )
    from ..models.activity_role_update_v2 import ActivityRoleUpdateV2
    from ..models.activity_status_change_v2 import ActivityStatusChangeV2
    from ..models.activity_summary_update_v2 import ActivitySummaryUpdateV2
    from ..models.activity_workflow_ran_v2 import ActivityWorkflowRanV2


T = TypeVar("T", bound="IncidentActivityLogContentV2")


@_attrs_define
class IncidentActivityLogContentV2:
    """Details of an activity log entry.

    At most one key is set, and it matches the entry's type. Types not listed here carry no
    content: the entry's type and title are all there is.

        Example:
            {'action_created': {'action_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'actor': {'alert': {'id':
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
                halted'}}

        Attributes:
            action_created (ActivityActionRefV2 | Unset):  Example: {'action_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'actor':
                {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
                'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}}.
            action_updated (ActivityActionUpdatedV2 | Unset):  Example: {'action_id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'new_assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
                'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'new_status': 'completed', 'previous_assignee': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'previous_status': 'outstanding', 'updater': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}}.
            alert_attached_to_incident (ActivityAlertRefV2 | Unset):  Example: {'actor': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'alert_id':
                '01FCNDV6P870EA6S7TK1DSYDG0'}.
            custom_field_value_update (ActivityCustomFieldValueUpdateV2 | Unset):  Example: {'custom_field': {'description':
                'Which team is impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'Affected Team', 'options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]}, 'new_values': [{'value_catalog_entry':
                {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
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
                workflow'}}}.
            escalation_acknowledged (ActivityEscalationAcknowledgedV2 | Unset):  Example: {'acknowledger': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'escalation_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
            escalation_created (ActivityEscalationCreatedV2 | Unset):  Example: {'creator': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'escalated_to_users':
                [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
                'owner', 'slack_user_id': 'U02AYNF2XJM'}], 'escalation_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'escalation_path_id':
                '01FCNDV6P870EA6S7TK1DSYDG1'}.
            follow_up_created (ActivityFollowUpRefV2 | Unset):  Example: {'actor': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'follow_up_id':
                '01FCNDV6P870EA6S7TK1DSYDG0'}.
            follow_up_updated (ActivityFollowUpUpdatedV2 | Unset):  Example: {'follow_up_id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'new_assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
                'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'new_status': 'completed', 'new_title': 'Add a payments-api
                rollback runbook', 'previous_assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'previous_status':
                'outstanding', 'previous_title': 'Add a runbook', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66',
                'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
                'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}}.
            incident_merged (ActivityIncidentMergedV2 | Unset):  Example: {'incident_update_id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'merger': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}, 'source_incident': {'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91',
                'name': 'Our database is sad', 'reference': 'INC-123', 'status_category': 'triage', 'summary': "Our database is
                really really sad, and we don't know why yet.", 'visibility': 'public'}}.
            incident_rename (ActivityIncidentRenameV2 | Unset):  Example: {'new_name': 'EU checkout failing after 14:02
                deploy', 'previous_name': 'Checkout errors', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}.
            incident_timestamp_set (ActivityIncidentTimestampSetV2 | Unset):  Example: {'incident_timestamp': {'id':
                '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1}, 'new_value': '2026-09-01T13:42:00Z',
                'previous_value': '2026-09-01T14:00:00Z', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}.
            incident_type_changed (ActivityIncidentTypeChangedV2 | Unset):  Example: {'new_incident_type':
                {'create_in_triage': 'always', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing
                production outages', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage',
                'private_incidents_only': False, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'previous_incident_type':
                {'create_in_triage': 'always', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing
                production outages', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage',
                'private_incidents_only': False, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}}.
            incident_update (ActivityIncidentUpdateV2 | Unset):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'message':
                'Rolled back **payments-api** to v411, error rate recovering.', 'new_severity': {'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'new_status': {'category': 'triage',
                'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're
                ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4,
                'updated_at': '2021-08-17T13:28:57.801578Z'}, 'next_update_in_minutes': 30, 'previous_severity': {'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'previous_status': {'category':
                'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and
                we're ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4,
                'updated_at': '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}.
            incident_visibility_changed (ActivityIncidentVisibilityChangedV2 | Unset):  Example: {'new_visibility':
                'private', 'previous_visibility': 'public', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}.
            role_update (ActivityRoleUpdateV2 | Unset):  Example: {'new_assignee': {'email': 'lisa@incident.io', 'id':
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
                workflow'}}}.
            status_change (ActivityStatusChangeV2 | Unset):  Example: {'new_status': {'category': 'triage', 'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
                from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
                '2021-08-17T13:28:57.801578Z'}, 'previous_status': {'category': 'triage', 'created_at':
                '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
                from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
                '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}}.
            summary_update (ActivitySummaryUpdateV2 | Unset):  Example: {'new_summary': 'Checkout is failing for all EU
                customers since the 14:02 deploy.', 'previous_summary': 'Checkout is failing for some customers.', 'updater':
                {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
                'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
                'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
                'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}}.
            workflow_ran (ActivityWorkflowRanV2 | Unset):  Example: {'creator': {'alert': {'id':
                '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
                'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'event_description': 'Stopped
                the synthetic load test in staging.', 'event_title': 'Load test halted'}.
    """

    action_created: ActivityActionRefV2 | Unset = UNSET
    action_updated: ActivityActionUpdatedV2 | Unset = UNSET
    alert_attached_to_incident: ActivityAlertRefV2 | Unset = UNSET
    custom_field_value_update: ActivityCustomFieldValueUpdateV2 | Unset = UNSET
    escalation_acknowledged: ActivityEscalationAcknowledgedV2 | Unset = UNSET
    escalation_created: ActivityEscalationCreatedV2 | Unset = UNSET
    follow_up_created: ActivityFollowUpRefV2 | Unset = UNSET
    follow_up_updated: ActivityFollowUpUpdatedV2 | Unset = UNSET
    incident_merged: ActivityIncidentMergedV2 | Unset = UNSET
    incident_rename: ActivityIncidentRenameV2 | Unset = UNSET
    incident_timestamp_set: ActivityIncidentTimestampSetV2 | Unset = UNSET
    incident_type_changed: ActivityIncidentTypeChangedV2 | Unset = UNSET
    incident_update: ActivityIncidentUpdateV2 | Unset = UNSET
    incident_visibility_changed: ActivityIncidentVisibilityChangedV2 | Unset = UNSET
    role_update: ActivityRoleUpdateV2 | Unset = UNSET
    status_change: ActivityStatusChangeV2 | Unset = UNSET
    summary_update: ActivitySummaryUpdateV2 | Unset = UNSET
    workflow_ran: ActivityWorkflowRanV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_created: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_created, Unset):
            action_created = self.action_created.to_dict()

        action_updated: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_updated, Unset):
            action_updated = self.action_updated.to_dict()

        alert_attached_to_incident: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert_attached_to_incident, Unset):
            alert_attached_to_incident = self.alert_attached_to_incident.to_dict()

        custom_field_value_update: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_field_value_update, Unset):
            custom_field_value_update = self.custom_field_value_update.to_dict()

        escalation_acknowledged: dict[str, Any] | Unset = UNSET
        if not isinstance(self.escalation_acknowledged, Unset):
            escalation_acknowledged = self.escalation_acknowledged.to_dict()

        escalation_created: dict[str, Any] | Unset = UNSET
        if not isinstance(self.escalation_created, Unset):
            escalation_created = self.escalation_created.to_dict()

        follow_up_created: dict[str, Any] | Unset = UNSET
        if not isinstance(self.follow_up_created, Unset):
            follow_up_created = self.follow_up_created.to_dict()

        follow_up_updated: dict[str, Any] | Unset = UNSET
        if not isinstance(self.follow_up_updated, Unset):
            follow_up_updated = self.follow_up_updated.to_dict()

        incident_merged: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident_merged, Unset):
            incident_merged = self.incident_merged.to_dict()

        incident_rename: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident_rename, Unset):
            incident_rename = self.incident_rename.to_dict()

        incident_timestamp_set: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident_timestamp_set, Unset):
            incident_timestamp_set = self.incident_timestamp_set.to_dict()

        incident_type_changed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident_type_changed, Unset):
            incident_type_changed = self.incident_type_changed.to_dict()

        incident_update: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident_update, Unset):
            incident_update = self.incident_update.to_dict()

        incident_visibility_changed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident_visibility_changed, Unset):
            incident_visibility_changed = self.incident_visibility_changed.to_dict()

        role_update: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role_update, Unset):
            role_update = self.role_update.to_dict()

        status_change: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_change, Unset):
            status_change = self.status_change.to_dict()

        summary_update: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary_update, Unset):
            summary_update = self.summary_update.to_dict()

        workflow_ran: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow_ran, Unset):
            workflow_ran = self.workflow_ran.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_created is not UNSET:
            field_dict["action_created"] = action_created
        if action_updated is not UNSET:
            field_dict["action_updated"] = action_updated
        if alert_attached_to_incident is not UNSET:
            field_dict["alert_attached_to_incident"] = alert_attached_to_incident
        if custom_field_value_update is not UNSET:
            field_dict["custom_field_value_update"] = custom_field_value_update
        if escalation_acknowledged is not UNSET:
            field_dict["escalation_acknowledged"] = escalation_acknowledged
        if escalation_created is not UNSET:
            field_dict["escalation_created"] = escalation_created
        if follow_up_created is not UNSET:
            field_dict["follow_up_created"] = follow_up_created
        if follow_up_updated is not UNSET:
            field_dict["follow_up_updated"] = follow_up_updated
        if incident_merged is not UNSET:
            field_dict["incident_merged"] = incident_merged
        if incident_rename is not UNSET:
            field_dict["incident_rename"] = incident_rename
        if incident_timestamp_set is not UNSET:
            field_dict["incident_timestamp_set"] = incident_timestamp_set
        if incident_type_changed is not UNSET:
            field_dict["incident_type_changed"] = incident_type_changed
        if incident_update is not UNSET:
            field_dict["incident_update"] = incident_update
        if incident_visibility_changed is not UNSET:
            field_dict["incident_visibility_changed"] = incident_visibility_changed
        if role_update is not UNSET:
            field_dict["role_update"] = role_update
        if status_change is not UNSET:
            field_dict["status_change"] = status_change
        if summary_update is not UNSET:
            field_dict["summary_update"] = summary_update
        if workflow_ran is not UNSET:
            field_dict["workflow_ran"] = workflow_ran

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.activity_action_ref_v2 import ActivityActionRefV2
        from ..models.activity_action_updated_v2 import (
            ActivityActionUpdatedV2,
        )
        from ..models.activity_alert_ref_v2 import ActivityAlertRefV2
        from ..models.activity_custom_field_value_update_v2 import (
            ActivityCustomFieldValueUpdateV2,
        )
        from ..models.activity_escalation_acknowledged_v2 import (
            ActivityEscalationAcknowledgedV2,
        )
        from ..models.activity_escalation_created_v2 import (
            ActivityEscalationCreatedV2,
        )
        from ..models.activity_follow_up_ref_v2 import (
            ActivityFollowUpRefV2,
        )
        from ..models.activity_follow_up_updated_v2 import (
            ActivityFollowUpUpdatedV2,
        )
        from ..models.activity_incident_merged_v2 import (
            ActivityIncidentMergedV2,
        )
        from ..models.activity_incident_rename_v2 import (
            ActivityIncidentRenameV2,
        )
        from ..models.activity_incident_timestamp_set_v2 import (
            ActivityIncidentTimestampSetV2,
        )
        from ..models.activity_incident_type_changed_v2 import (
            ActivityIncidentTypeChangedV2,
        )
        from ..models.activity_incident_update_v2 import (
            ActivityIncidentUpdateV2,
        )
        from ..models.activity_incident_visibility_changed_v2 import (
            ActivityIncidentVisibilityChangedV2,
        )
        from ..models.activity_role_update_v2 import (
            ActivityRoleUpdateV2,
        )
        from ..models.activity_status_change_v2 import (
            ActivityStatusChangeV2,
        )
        from ..models.activity_summary_update_v2 import (
            ActivitySummaryUpdateV2,
        )
        from ..models.activity_workflow_ran_v2 import (
            ActivityWorkflowRanV2,
        )

        d = dict(src_dict)
        _action_created = d.pop("action_created", UNSET)
        action_created: ActivityActionRefV2 | Unset
        if isinstance(_action_created, Unset):
            action_created = UNSET
        else:
            action_created = ActivityActionRefV2.from_dict(_action_created)

        _action_updated = d.pop("action_updated", UNSET)
        action_updated: ActivityActionUpdatedV2 | Unset
        if isinstance(_action_updated, Unset):
            action_updated = UNSET
        else:
            action_updated = ActivityActionUpdatedV2.from_dict(_action_updated)

        _alert_attached_to_incident = d.pop("alert_attached_to_incident", UNSET)
        alert_attached_to_incident: ActivityAlertRefV2 | Unset
        if isinstance(_alert_attached_to_incident, Unset):
            alert_attached_to_incident = UNSET
        else:
            alert_attached_to_incident = ActivityAlertRefV2.from_dict(
                _alert_attached_to_incident
            )

        _custom_field_value_update = d.pop("custom_field_value_update", UNSET)
        custom_field_value_update: ActivityCustomFieldValueUpdateV2 | Unset
        if isinstance(_custom_field_value_update, Unset):
            custom_field_value_update = UNSET
        else:
            custom_field_value_update = ActivityCustomFieldValueUpdateV2.from_dict(
                _custom_field_value_update
            )

        _escalation_acknowledged = d.pop("escalation_acknowledged", UNSET)
        escalation_acknowledged: ActivityEscalationAcknowledgedV2 | Unset
        if isinstance(_escalation_acknowledged, Unset):
            escalation_acknowledged = UNSET
        else:
            escalation_acknowledged = ActivityEscalationAcknowledgedV2.from_dict(
                _escalation_acknowledged
            )

        _escalation_created = d.pop("escalation_created", UNSET)
        escalation_created: ActivityEscalationCreatedV2 | Unset
        if isinstance(_escalation_created, Unset):
            escalation_created = UNSET
        else:
            escalation_created = ActivityEscalationCreatedV2.from_dict(
                _escalation_created
            )

        _follow_up_created = d.pop("follow_up_created", UNSET)
        follow_up_created: ActivityFollowUpRefV2 | Unset
        if isinstance(_follow_up_created, Unset):
            follow_up_created = UNSET
        else:
            follow_up_created = ActivityFollowUpRefV2.from_dict(_follow_up_created)

        _follow_up_updated = d.pop("follow_up_updated", UNSET)
        follow_up_updated: ActivityFollowUpUpdatedV2 | Unset
        if isinstance(_follow_up_updated, Unset):
            follow_up_updated = UNSET
        else:
            follow_up_updated = ActivityFollowUpUpdatedV2.from_dict(_follow_up_updated)

        _incident_merged = d.pop("incident_merged", UNSET)
        incident_merged: ActivityIncidentMergedV2 | Unset
        if isinstance(_incident_merged, Unset):
            incident_merged = UNSET
        else:
            incident_merged = ActivityIncidentMergedV2.from_dict(_incident_merged)

        _incident_rename = d.pop("incident_rename", UNSET)
        incident_rename: ActivityIncidentRenameV2 | Unset
        if isinstance(_incident_rename, Unset):
            incident_rename = UNSET
        else:
            incident_rename = ActivityIncidentRenameV2.from_dict(_incident_rename)

        _incident_timestamp_set = d.pop("incident_timestamp_set", UNSET)
        incident_timestamp_set: ActivityIncidentTimestampSetV2 | Unset
        if isinstance(_incident_timestamp_set, Unset):
            incident_timestamp_set = UNSET
        else:
            incident_timestamp_set = ActivityIncidentTimestampSetV2.from_dict(
                _incident_timestamp_set
            )

        _incident_type_changed = d.pop("incident_type_changed", UNSET)
        incident_type_changed: ActivityIncidentTypeChangedV2 | Unset
        if isinstance(_incident_type_changed, Unset):
            incident_type_changed = UNSET
        else:
            incident_type_changed = ActivityIncidentTypeChangedV2.from_dict(
                _incident_type_changed
            )

        _incident_update = d.pop("incident_update", UNSET)
        incident_update: ActivityIncidentUpdateV2 | Unset
        if isinstance(_incident_update, Unset):
            incident_update = UNSET
        else:
            incident_update = ActivityIncidentUpdateV2.from_dict(_incident_update)

        _incident_visibility_changed = d.pop("incident_visibility_changed", UNSET)
        incident_visibility_changed: ActivityIncidentVisibilityChangedV2 | Unset
        if isinstance(_incident_visibility_changed, Unset):
            incident_visibility_changed = UNSET
        else:
            incident_visibility_changed = ActivityIncidentVisibilityChangedV2.from_dict(
                _incident_visibility_changed
            )

        _role_update = d.pop("role_update", UNSET)
        role_update: ActivityRoleUpdateV2 | Unset
        if isinstance(_role_update, Unset):
            role_update = UNSET
        else:
            role_update = ActivityRoleUpdateV2.from_dict(_role_update)

        _status_change = d.pop("status_change", UNSET)
        status_change: ActivityStatusChangeV2 | Unset
        if isinstance(_status_change, Unset):
            status_change = UNSET
        else:
            status_change = ActivityStatusChangeV2.from_dict(_status_change)

        _summary_update = d.pop("summary_update", UNSET)
        summary_update: ActivitySummaryUpdateV2 | Unset
        if isinstance(_summary_update, Unset):
            summary_update = UNSET
        else:
            summary_update = ActivitySummaryUpdateV2.from_dict(_summary_update)

        _workflow_ran = d.pop("workflow_ran", UNSET)
        workflow_ran: ActivityWorkflowRanV2 | Unset
        if isinstance(_workflow_ran, Unset):
            workflow_ran = UNSET
        else:
            workflow_ran = ActivityWorkflowRanV2.from_dict(_workflow_ran)

        incident_activity_log_content_v2 = cls(
            action_created=action_created,
            action_updated=action_updated,
            alert_attached_to_incident=alert_attached_to_incident,
            custom_field_value_update=custom_field_value_update,
            escalation_acknowledged=escalation_acknowledged,
            escalation_created=escalation_created,
            follow_up_created=follow_up_created,
            follow_up_updated=follow_up_updated,
            incident_merged=incident_merged,
            incident_rename=incident_rename,
            incident_timestamp_set=incident_timestamp_set,
            incident_type_changed=incident_type_changed,
            incident_update=incident_update,
            incident_visibility_changed=incident_visibility_changed,
            role_update=role_update,
            status_change=status_change,
            summary_update=summary_update,
            workflow_ran=workflow_ran,
        )

        incident_activity_log_content_v2.additional_properties = d
        return incident_activity_log_content_v2

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
