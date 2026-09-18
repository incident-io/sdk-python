from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_sources_create_payload_v2_source_type import (
    AlertSourcesCreatePayloadV2SourceType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_source_azure_devops_options_v2 import (
        AlertSourceAzureDevopsOptionsV2,
    )
    from ..models.alert_source_email_options_payload_v2 import (
        AlertSourceEmailOptionsPayloadV2,
    )
    from ..models.alert_source_heartbeat_options_payload_v2 import (
        AlertSourceHeartbeatOptionsPayloadV2,
    )
    from ..models.alert_source_http_custom_options_v2 import (
        AlertSourceHTTPCustomOptionsV2,
    )
    from ..models.alert_source_jira_options_v2 import AlertSourceJiraOptionsV2
    from ..models.alert_source_rate_limit_sharding_v2 import (
        AlertSourceRateLimitShardingV2,
    )
    from ..models.alert_template_payload_v2 import AlertTemplatePayloadV2
    from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2


T = TypeVar("T", bound="AlertSourcesCreatePayloadV2")


@_attrs_define
class AlertSourcesCreatePayloadV2:
    """
    Example:
        {'auto_resolve_incident_alerts': False, 'auto_resolve_timeout_minutes': 1, 'azure_devops_options':
            {'project_ids': ['01GBSQF3FHF7FWZQNWGHAVQ804', 'ba038695-f5f7-4490-a9ea-bf4ab3cbf483']}, 'email_options':
            {'redactions': ['credit_card_numbers'], 'transform_expression': "return {\\n  title: $.subject,\\n  description:
            $.text,\\n  status: $.subject.startsWith('[RESOLVED]') ? 'resolved' : 'firing',\\n  deduplication_key:
            $.header_message_id,\\n}"}, 'filter_condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}], 'fixed_team_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'heartbeat_options': {'failure_threshold': 1, 'grace_period_seconds': 0,
            'interval_seconds': 60}, 'http_custom_options': {'deduplication_key_path': '$.alert_id', 'transform_expression':
            "return {\\n  title: $.title || $.name || 'Unknown Alert',\\n  status: $.status === 'resolved' ? 'resolved' :
            'firing',\\n  description: $.description || $.message || '',\\n  sourceURL: $.url || $.link || '',\\n  metadata:
            { team: $.team, severity: $.severity }\\n}"}, 'jira_options': {'project_ids': ['01GBSQF3FHF7FWZQNWGHAVQ804',
            '10043']}, 'name': 'Production Web Dashboard Alerts', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'rate_limit_sharding': {'rate_limit_shard_key_path': '$.priority'}, 'source_type': 'alertmanager', 'template':
            {'attributes': [{'alert_attribute_id': 'abc123', 'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'merge_strategy': 'first_wins', 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'description': {'literal': 'SEV123', 'reference': 'incident.severity'}, 'expressions':
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}],
            'is_private': False, 'title': {'literal': 'SEV123', 'reference': 'incident.severity'}, 'visible_to_teams':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}}

    Attributes:
        name (str): Unique name of the alert source Example: Production Web Dashboard Alerts.
        source_type (AlertSourcesCreatePayloadV2SourceType): Type of alert source Example: alertmanager.
        template (AlertTemplatePayloadV2):  Example: {'attributes': [{'alert_attribute_id': 'abc123', 'binding':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'merge_strategy': 'first_wins',
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'description': {'literal': 'SEV123',
            'reference': 'incident.severity'}, 'expressions': [{'else_branch': {'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123',
            'root_reference': 'incident.status'}], 'is_private': False, 'title': {'literal': 'SEV123', 'reference':
            'incident.severity'}, 'visible_to_teams': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}.
        auto_resolve_incident_alerts (bool | Unset): Whether alerts from this source keep counting down to auto-resolve
            while attached to an incident. Defaults to true. Has no effect without auto_resolve_timeout_minutes. Example:
            False.
        auto_resolve_timeout_minutes (int | Unset): When set, alerts from this source will automatically resolve after
            this many minutes. Example: 1.
        azure_devops_options (AlertSourceAzureDevopsOptionsV2 | Unset):  Example: {'project_ids':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', 'ba038695-f5f7-4490-a9ea-bf4ab3cbf483']}.
        email_options (AlertSourceEmailOptionsPayloadV2 | Unset):  Example: {'redactions': ['credit_card_numbers'],
            'transform_expression': "return {\\n  title: $.subject,\\n  description: $.text,\\n  status:
            $.subject.startsWith('[RESOLVED]') ? 'resolved' : 'firing',\\n  deduplication_key: $.header_message_id,\\n}"}.
        filter_condition_groups (list[ConditionGroupPayloadV2] | Unset): Conditions an incoming event must match to be
            ingested from this source, evaluated against the event's payload and this source's expressions. When empty or
            omitted, everything is ingested; otherwise a firing event that doesn't match is dropped and never creates or
            updates an alert. Resolve events are never filtered. Example: [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}].
        fixed_team_id (str | Unset): Fix the team every alert from this source is attributed to. While set, the team
            attribute is managed from this field: don't send its binding in the template. Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        heartbeat_options (AlertSourceHeartbeatOptionsPayloadV2 | Unset):  Example: {'failure_threshold': 1,
            'grace_period_seconds': 0, 'interval_seconds': 60}.
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
    """

    name: str
    source_type: AlertSourcesCreatePayloadV2SourceType
    template: AlertTemplatePayloadV2
    auto_resolve_incident_alerts: bool | Unset = UNSET
    auto_resolve_timeout_minutes: int | Unset = UNSET
    azure_devops_options: AlertSourceAzureDevopsOptionsV2 | Unset = UNSET
    email_options: AlertSourceEmailOptionsPayloadV2 | Unset = UNSET
    filter_condition_groups: list[ConditionGroupPayloadV2] | Unset = UNSET
    fixed_team_id: str | Unset = UNSET
    heartbeat_options: AlertSourceHeartbeatOptionsPayloadV2 | Unset = UNSET
    http_custom_options: AlertSourceHTTPCustomOptionsV2 | Unset = UNSET
    jira_options: AlertSourceJiraOptionsV2 | Unset = UNSET
    owning_team_ids: list[str] | Unset = UNSET
    rate_limit_sharding: AlertSourceRateLimitShardingV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        source_type = self.source_type.value

        template = self.template.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "source_type": source_type,
                "template": template,
            }
        )
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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_source_azure_devops_options_v2 import (
            AlertSourceAzureDevopsOptionsV2,
        )
        from ..models.alert_source_email_options_payload_v2 import (
            AlertSourceEmailOptionsPayloadV2,
        )
        from ..models.alert_source_heartbeat_options_payload_v2 import (
            AlertSourceHeartbeatOptionsPayloadV2,
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
        from ..models.alert_template_payload_v2 import (
            AlertTemplatePayloadV2,
        )
        from ..models.condition_group_payload_v2 import (
            ConditionGroupPayloadV2,
        )

        d = dict(src_dict)
        name = d.pop("name")

        source_type = AlertSourcesCreatePayloadV2SourceType(d.pop("source_type"))

        template = AlertTemplatePayloadV2.from_dict(d.pop("template"))

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
        email_options: AlertSourceEmailOptionsPayloadV2 | Unset
        if isinstance(_email_options, Unset):
            email_options = UNSET
        else:
            email_options = AlertSourceEmailOptionsPayloadV2.from_dict(_email_options)

        _filter_condition_groups = d.pop("filter_condition_groups", UNSET)
        filter_condition_groups: list[ConditionGroupPayloadV2] | Unset = UNSET
        if _filter_condition_groups is not UNSET:
            filter_condition_groups = []
            for filter_condition_groups_item_data in _filter_condition_groups:
                filter_condition_groups_item = ConditionGroupPayloadV2.from_dict(
                    filter_condition_groups_item_data
                )

                filter_condition_groups.append(filter_condition_groups_item)

        fixed_team_id = d.pop("fixed_team_id", UNSET)

        _heartbeat_options = d.pop("heartbeat_options", UNSET)
        heartbeat_options: AlertSourceHeartbeatOptionsPayloadV2 | Unset
        if isinstance(_heartbeat_options, Unset):
            heartbeat_options = UNSET
        else:
            heartbeat_options = AlertSourceHeartbeatOptionsPayloadV2.from_dict(
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

        alert_sources_create_payload_v2 = cls(
            name=name,
            source_type=source_type,
            template=template,
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
        )

        alert_sources_create_payload_v2.additional_properties = d
        return alert_sources_create_payload_v2

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
