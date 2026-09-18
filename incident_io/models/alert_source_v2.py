from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_source_v2_source_type import AlertSourceV2SourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_source_azure_devops_options_v2 import (
        AlertSourceAzureDevopsOptionsV2,
    )
    from ..models.alert_source_email_options_v2 import AlertSourceEmailOptionsV2
    from ..models.alert_source_heartbeat_options_v2 import AlertSourceHeartbeatOptionsV2
    from ..models.alert_source_http_custom_options_v2 import (
        AlertSourceHTTPCustomOptionsV2,
    )
    from ..models.alert_source_jira_options_v2 import AlertSourceJiraOptionsV2
    from ..models.alert_source_rate_limit_sharding_v2 import (
        AlertSourceRateLimitShardingV2,
    )
    from ..models.alert_template_v2 import AlertTemplateV2
    from ..models.condition_group_v2 import ConditionGroupV2


T = TypeVar("T", bound="AlertSourceV2")


@_attrs_define
class AlertSourceV2:
    """
    Example:
        {'alert_events_url': 'https://api.incident.io/v2/alert_events/http/01GW2G3V0S59R238FAHPDS1R66',
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
            'incident.severity'}}}}

    Attributes:
        id (str): The ID of this alert source Example: 01GW2G3V0S59R238FAHPDS1R66.
        name (str): Unique name of the alert source Example: Production Web Dashboard Alerts.
        source_type (AlertSourceV2SourceType): Type of alert source Example: alertmanager.
        template (AlertTemplateV2):  Example: {'attributes': [{'alert_attribute_id': 'abc123', 'binding':
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
            'incident.severity'}}}.
        alert_events_url (str | Unset): URL that can be used to send alert events to this source. This is only set for
            sources that accept webhook/HTTP events; email sources use the email_address field, and integration-based
            sources (like Jira) receive events through their native integrations. Example:
            https://api.incident.io/v2/alert_events/http/01GW2G3V0S59R238FAHPDS1R66.
        auto_resolve_incident_alerts (bool | Unset): Whether alerts from this source keep counting down to auto-resolve
            while attached to an incident. Defaults to true. Has no effect without auto_resolve_timeout_minutes. Example:
            False.
        auto_resolve_timeout_minutes (int | Unset): When set, alerts from this source will automatically resolve after
            this many minutes. Example: 1.
        azure_devops_options (AlertSourceAzureDevopsOptionsV2 | Unset):  Example: {'project_ids':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', 'ba038695-f5f7-4490-a9ea-bf4ab3cbf483']}.
        email_options (AlertSourceEmailOptionsV2 | Unset):  Example: {'email_address': 'lawrence@example.com',
            'redactions': ['credit_card_numbers'], 'transform_expression': "return {\\n  title: $.subject,\\n  description:
            $.text,\\n  status: $.subject.startsWith('[RESOLVED]') ? 'resolved' : 'firing',\\n  deduplication_key:
            $.header_message_id,\\n}"}.
        filter_condition_groups (list[ConditionGroupV2] | Unset): Conditions an incoming event must match to be ingested
            from this source, evaluated against the event's payload and this source's expressions. Example: [{'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Incident Severity', 'reference': 'incident.severity'}}]}].
        fixed_team_id (str | Unset): When set, the team every alert from this source is attributed to. The team
            attribute is managed from this field: its binding is not returned in the template and cannot be edited directly.
            Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        heartbeat_options (AlertSourceHeartbeatOptionsV2 | Unset):  Example: {'failure_threshold': 1,
            'grace_period_seconds': 0, 'interval_seconds': 60, 'ping_url':
            'https://api.incident.io/v2/heartbeat/01GW2G3V0S59R238FAHPDS1R66/ping'}.
        http_custom_options (AlertSourceHTTPCustomOptionsV2 | Unset):  Example: {'deduplication_key_path': '$.alert_id',
            'transform_expression': "return {\\n  title: $.title || $.name || 'Unknown Alert',\\n  status: $.status ===
            'resolved' ? 'resolved' : 'firing',\\n  description: $.description || $.message || '',\\n  sourceURL: $.url ||
            $.link || '',\\n  metadata: { team: $.team, severity: $.severity }\\n}"}.
        jira_options (AlertSourceJiraOptionsV2 | Unset):  Example: {'project_ids': ['01GBSQF3FHF7FWZQNWGHAVQ804',
            '10043']}.
        owning_team_ids (list[str] | Unset): IDs of teams that own this alert source Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
        rate_limit_sharding (AlertSourceRateLimitShardingV2 | Unset): Controls how this source's ingest rate limit is
            split into buckets. Example: {'rate_limit_shard_key_path': '$.priority'}.
        secret_token (str | Unset): Secret token used to authenticate this source, if applicable. If applicable, this is
            the token that must be included in either the query string or the 'Authorization' header when sending events to
            this alert source. Example: some-secret-token.
    """

    id: str
    name: str
    source_type: AlertSourceV2SourceType
    template: AlertTemplateV2
    alert_events_url: str | Unset = UNSET
    auto_resolve_incident_alerts: bool | Unset = UNSET
    auto_resolve_timeout_minutes: int | Unset = UNSET
    azure_devops_options: AlertSourceAzureDevopsOptionsV2 | Unset = UNSET
    email_options: AlertSourceEmailOptionsV2 | Unset = UNSET
    filter_condition_groups: list[ConditionGroupV2] | Unset = UNSET
    fixed_team_id: str | Unset = UNSET
    heartbeat_options: AlertSourceHeartbeatOptionsV2 | Unset = UNSET
    http_custom_options: AlertSourceHTTPCustomOptionsV2 | Unset = UNSET
    jira_options: AlertSourceJiraOptionsV2 | Unset = UNSET
    owning_team_ids: list[str] | Unset = UNSET
    rate_limit_sharding: AlertSourceRateLimitShardingV2 | Unset = UNSET
    secret_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        source_type = self.source_type.value

        template = self.template.to_dict()

        alert_events_url = self.alert_events_url

        auto_resolve_incident_alerts = self.auto_resolve_incident_alerts

        auto_resolve_timeout_minutes = self.auto_resolve_timeout_minutes

        azure_devops_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_devops_options, Unset):
            azure_devops_options = self.azure_devops_options.to_dict()

        email_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email_options, Unset):
            email_options = self.email_options.to_dict()

        filter_condition_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_condition_groups, Unset):
            filter_condition_groups = []
            for filter_condition_groups_item_data in self.filter_condition_groups:
                filter_condition_groups_item = (
                    filter_condition_groups_item_data.to_dict()
                )
                filter_condition_groups.append(filter_condition_groups_item)

        fixed_team_id = self.fixed_team_id

        heartbeat_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.heartbeat_options, Unset):
            heartbeat_options = self.heartbeat_options.to_dict()

        http_custom_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.http_custom_options, Unset):
            http_custom_options = self.http_custom_options.to_dict()

        jira_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jira_options, Unset):
            jira_options = self.jira_options.to_dict()

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        rate_limit_sharding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit_sharding, Unset):
            rate_limit_sharding = self.rate_limit_sharding.to_dict()

        secret_token = self.secret_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "source_type": source_type,
                "template": template,
            }
        )
        if alert_events_url is not UNSET:
            field_dict["alert_events_url"] = alert_events_url
        if auto_resolve_incident_alerts is not UNSET:
            field_dict["auto_resolve_incident_alerts"] = auto_resolve_incident_alerts
        if auto_resolve_timeout_minutes is not UNSET:
            field_dict["auto_resolve_timeout_minutes"] = auto_resolve_timeout_minutes
        if azure_devops_options is not UNSET:
            field_dict["azure_devops_options"] = azure_devops_options
        if email_options is not UNSET:
            field_dict["email_options"] = email_options
        if filter_condition_groups is not UNSET:
            field_dict["filter_condition_groups"] = filter_condition_groups
        if fixed_team_id is not UNSET:
            field_dict["fixed_team_id"] = fixed_team_id
        if heartbeat_options is not UNSET:
            field_dict["heartbeat_options"] = heartbeat_options
        if http_custom_options is not UNSET:
            field_dict["http_custom_options"] = http_custom_options
        if jira_options is not UNSET:
            field_dict["jira_options"] = jira_options
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids
        if rate_limit_sharding is not UNSET:
            field_dict["rate_limit_sharding"] = rate_limit_sharding
        if secret_token is not UNSET:
            field_dict["secret_token"] = secret_token

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_source_azure_devops_options_v2 import (
            AlertSourceAzureDevopsOptionsV2,
        )
        from ..models.alert_source_email_options_v2 import (
            AlertSourceEmailOptionsV2,
        )
        from ..models.alert_source_heartbeat_options_v2 import (
            AlertSourceHeartbeatOptionsV2,
        )
        from ..models.alert_source_http_custom_options_v2 import (
            AlertSourceHTTPCustomOptionsV2,
        )
        from ..models.alert_source_jira_options_v2 import (
            AlertSourceJiraOptionsV2,
        )
        from ..models.alert_source_rate_limit_sharding_v2 import (
            AlertSourceRateLimitShardingV2,
        )
        from ..models.alert_template_v2 import AlertTemplateV2
        from ..models.condition_group_v2 import ConditionGroupV2

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        source_type = AlertSourceV2SourceType(d.pop("source_type"))

        template = AlertTemplateV2.from_dict(d.pop("template"))

        alert_events_url = d.pop("alert_events_url", UNSET)

        auto_resolve_incident_alerts = d.pop("auto_resolve_incident_alerts", UNSET)

        auto_resolve_timeout_minutes = d.pop("auto_resolve_timeout_minutes", UNSET)

        _azure_devops_options = d.pop("azure_devops_options", UNSET)
        azure_devops_options: AlertSourceAzureDevopsOptionsV2 | Unset
        if isinstance(_azure_devops_options, Unset):
            azure_devops_options = UNSET
        else:
            azure_devops_options = AlertSourceAzureDevopsOptionsV2.from_dict(
                _azure_devops_options
            )

        _email_options = d.pop("email_options", UNSET)
        email_options: AlertSourceEmailOptionsV2 | Unset
        if isinstance(_email_options, Unset):
            email_options = UNSET
        else:
            email_options = AlertSourceEmailOptionsV2.from_dict(_email_options)

        _filter_condition_groups = d.pop("filter_condition_groups", UNSET)
        filter_condition_groups: list[ConditionGroupV2] | Unset = UNSET
        if _filter_condition_groups is not UNSET:
            filter_condition_groups = []
            for filter_condition_groups_item_data in _filter_condition_groups:
                filter_condition_groups_item = ConditionGroupV2.from_dict(
                    filter_condition_groups_item_data
                )

                filter_condition_groups.append(filter_condition_groups_item)

        fixed_team_id = d.pop("fixed_team_id", UNSET)

        _heartbeat_options = d.pop("heartbeat_options", UNSET)
        heartbeat_options: AlertSourceHeartbeatOptionsV2 | Unset
        if isinstance(_heartbeat_options, Unset):
            heartbeat_options = UNSET
        else:
            heartbeat_options = AlertSourceHeartbeatOptionsV2.from_dict(
                _heartbeat_options
            )

        _http_custom_options = d.pop("http_custom_options", UNSET)
        http_custom_options: AlertSourceHTTPCustomOptionsV2 | Unset
        if isinstance(_http_custom_options, Unset):
            http_custom_options = UNSET
        else:
            http_custom_options = AlertSourceHTTPCustomOptionsV2.from_dict(
                _http_custom_options
            )

        _jira_options = d.pop("jira_options", UNSET)
        jira_options: AlertSourceJiraOptionsV2 | Unset
        if isinstance(_jira_options, Unset):
            jira_options = UNSET
        else:
            jira_options = AlertSourceJiraOptionsV2.from_dict(_jira_options)

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        _rate_limit_sharding = d.pop("rate_limit_sharding", UNSET)
        rate_limit_sharding: AlertSourceRateLimitShardingV2 | Unset
        if isinstance(_rate_limit_sharding, Unset):
            rate_limit_sharding = UNSET
        else:
            rate_limit_sharding = AlertSourceRateLimitShardingV2.from_dict(
                _rate_limit_sharding
            )

        secret_token = d.pop("secret_token", UNSET)

        alert_source_v2 = cls(
            id=id,
            name=name,
            source_type=source_type,
            template=template,
            alert_events_url=alert_events_url,
            auto_resolve_incident_alerts=auto_resolve_incident_alerts,
            auto_resolve_timeout_minutes=auto_resolve_timeout_minutes,
            azure_devops_options=azure_devops_options,
            email_options=email_options,
            filter_condition_groups=filter_condition_groups,
            fixed_team_id=fixed_team_id,
            heartbeat_options=heartbeat_options,
            http_custom_options=http_custom_options,
            jira_options=jira_options,
            owning_team_ids=owning_team_ids,
            rate_limit_sharding=rate_limit_sharding,
            secret_token=secret_token,
        )

        alert_source_v2.additional_properties = d
        return alert_source_v2

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
