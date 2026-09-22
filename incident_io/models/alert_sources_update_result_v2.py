from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_source_v2 import AlertSourceV2


T = TypeVar("T", bound="AlertSourcesUpdateResultV2")


@_attrs_define(kw_only=True)
class AlertSourcesUpdateResultV2:
    """
    Example:
        {'alert_source': {'alert_events_url': 'https://api.incident.io/v2/alert_events/http/01GW2G3V0S59R238FAHPDS1R66',
            'auto_resolve_incident_alerts': False, 'auto_resolve_timeout_minutes': 1, 'azure_devops_options':
            {'project_ids': ['01GBSQF3FHF7FWZQNWGHAVQ804', 'ba038695-f5f7-4490-a9ea-bf4ab3cbf483']}, 'email_options':
            {'email_address': 'lawrence@example.com', 'redactions': ['credit_card_numbers'], 'transform_expression': "return
            {\\n  title: $.subject,\\n  description: $.text,\\n  status: $.subject.startsWith('[RESOLVED]') ? 'resolved' :
            'firing',\\n  deduplication_key: $.header_message_id,\\n}"}, 'filter_condition_groups': [{'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Incident Severity', 'reference': 'incident.severity'}}]}], 'fixed_team_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'heartbeat_options': {'failure_threshold': 1, 'grace_period_seconds': 0, 'interval_seconds': 60, 'ping_url':
            'https://api.incident.io/v2/heartbeat/01GW2G3V0S59R238FAHPDS1R66/ping'}, 'http_custom_options':
            {'deduplication_key_path': '$.alert_id', 'transform_expression': "return {\\n  title: $.title || $.name ||
            'Unknown Alert',\\n  status: $.status === 'resolved' ? 'resolved' : 'firing',\\n  description: $.description ||
            $.message || '',\\n  sourceURL: $.url || $.link || '',\\n  metadata: { team: $.team, severity: $.severity
            }\\n}"}, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'jira_options': {'project_ids': ['01GBSQF3FHF7FWZQNWGHAVQ804',
            '10043']}, 'name': 'Production Web Dashboard Alerts', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'rate_limit_sharding': {'rate_limit_shard_key_path': '$.priority'}, 'secret_token': 'some-secret-token',
            'source_type': 'alertmanager', 'template': {'attributes': [{'alert_attribute_id': 'abc123', 'binding':
            {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}],
            'merge_strategy': 'first_wins', 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'description': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}, 'expressions': [{'else_branch': {'result': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches':
            {'branches': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference': '1235', 'reference_label': 'Teams'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}]}, 'navigate': {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type':
            'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}, 'returns': {'array': True, 'type': 'IncidentStatus'}}], 'reference':
            'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}],
            'is_private': False, 'title': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}, 'visible_to_teams': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}}}

    Attributes:
        alert_source (AlertSourceV2):  Example: {'alert_events_url':
            'https://api.incident.io/v2/alert_events/http/01GW2G3V0S59R238FAHPDS1R66', 'auto_resolve_incident_alerts':
            False, 'auto_resolve_timeout_minutes': 1, 'azure_devops_options': {'project_ids': ['01GBSQF3FHF7FWZQNWGHAVQ804',
            'ba038695-f5f7-4490-a9ea-bf4ab3cbf483']}, 'email_options': {'email_address': 'lawrence@example.com',
            'redactions': ['credit_card_numbers'], 'transform_expression': "return {\\n  title: $.subject,\\n  description:
            $.text,\\n  status: $.subject.startsWith('[RESOLVED]') ? 'resolved' : 'firing',\\n  deduplication_key:
            $.header_message_id,\\n}"}, 'filter_condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence
            Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'fixed_team_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'heartbeat_options':
            {'failure_threshold': 1, 'grace_period_seconds': 0, 'interval_seconds': 60, 'ping_url':
            'https://api.incident.io/v2/heartbeat/01GW2G3V0S59R238FAHPDS1R66/ping'}, 'http_custom_options':
            {'deduplication_key_path': '$.alert_id', 'transform_expression': "return {\\n  title: $.title || $.name ||
            'Unknown Alert',\\n  status: $.status === 'resolved' ? 'resolved' : 'firing',\\n  description: $.description ||
            $.message || '',\\n  sourceURL: $.url || $.link || '',\\n  metadata: { team: $.team, severity: $.severity
            }\\n}"}, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'jira_options': {'project_ids': ['01GBSQF3FHF7FWZQNWGHAVQ804',
            '10043']}, 'name': 'Production Web Dashboard Alerts', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'rate_limit_sharding': {'rate_limit_shard_key_path': '$.priority'}, 'secret_token': 'some-secret-token',
            'source_type': 'alertmanager', 'template': {'attributes': [{'alert_attribute_id': 'abc123', 'binding':
            {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}],
            'merge_strategy': 'first_wins', 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'description': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}, 'expressions': [{'else_branch': {'result': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches':
            {'branches': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference': '1235', 'reference_label': 'Teams'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}]}, 'navigate': {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type':
            'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}, 'returns': {'array': True, 'type': 'IncidentStatus'}}], 'reference':
            'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}],
            'is_private': False, 'title': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}, 'visible_to_teams': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}}.
    """

    alert_source: AlertSourceV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_source = self.alert_source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_source": alert_source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_source_v2 import AlertSourceV2

        d = dict(src_dict)
        alert_source = AlertSourceV2.from_dict(d.pop("alert_source"))

        alert_sources_update_result_v2 = cls(
            alert_source=alert_source,
        )

        alert_sources_update_result_v2.additional_properties = d
        return alert_sources_update_result_v2

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
