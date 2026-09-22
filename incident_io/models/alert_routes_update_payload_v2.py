from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_route_alert_source_payload_v2 import (
        AlertRouteAlertSourcePayloadV2,
    )
    from ..models.alert_route_channel_config_payload_v2 import (
        AlertRouteChannelConfigPayloadV2,
    )
    from ..models.alert_route_escalation_config_payload_v2 import (
        AlertRouteEscalationConfigPayloadV2,
    )
    from ..models.alert_route_incident_config_payload_v2 import (
        AlertRouteIncidentConfigPayloadV2,
    )
    from ..models.alert_route_incident_template_payload_v2 import (
        AlertRouteIncidentTemplatePayloadV2,
    )
    from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2
    from ..models.engine_param_binding_payload_v2 import EngineParamBindingPayloadV2
    from ..models.expression_payload_v2 import ExpressionPayloadV2


T = TypeVar("T", bound="AlertRoutesUpdatePayloadV2")


@_attrs_define(kw_only=True)
class AlertRoutesUpdatePayloadV2:
    """
    Example:
        {'alert_sources': [{'alert_source_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}], 'channel_config': [{'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}],
            'ms_teams_targets': {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'channel_visibility': 'abc123'},
            'slack_targets': {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'channel_visibility': 'abc123'}}], 'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'created_at': '2021-08-17T13:28:57.801578Z', 'enabled': False, 'escalation_config':
            {'auto_cancel_escalations': False, 'escalation_targets': [{'escalation_paths': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'users': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}]}, 'expressions': [{'else_branch': {'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
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
            'root_reference': 'incident.status'}], 'incident_config': {'auto_decline_enabled': False,
            'auto_relate_grouped_alerts': False, 'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}],
            'defer_time_seconds': 1, 'enabled': False, 'grouping_keys': [{'reference': 'alert.title'}],
            'grouping_window_seconds': 1}, 'incident_template': {'custom_fields': [{'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'merge_strategy': 'first-wins'}], 'incident_mode': {'binding':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'incident_type': {'binding': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'membership_teams': {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'name': {'autogenerated': False, 'binding':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'severity': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'merge_strategy':
            'first-wins'}, 'start_in_triage': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'summary':
            {'autogenerated': False, 'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'workspace': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}}, 'is_private': False, 'message_template': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'name':
            'Production incidents', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'version': 1}

    Attributes:
        alert_sources (list[AlertRouteAlertSourcePayloadV2]): Which alert sources should this alert route match?
            Example: [{'alert_source_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}]}].
        channel_config (list[AlertRouteChannelConfigPayloadV2]): The channel configuration for this alert route Example:
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'ms_teams_targets': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'channel_visibility': 'abc123'}, 'slack_targets': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'channel_visibility': 'abc123'}}].
        condition_groups (list[ConditionGroupPayloadV2]): What condition groups must be true for this alert route to
            fire? Example: [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}].
        enabled (bool): Whether this alert route is enabled or not Example: False.
        escalation_config (AlertRouteEscalationConfigPayloadV2):  Example: {'auto_cancel_escalations': False,
            'escalation_targets': [{'escalation_paths': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'users':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}]}.
        expressions (list[ExpressionPayloadV2]): The expressions used in this template Example: [{'else_branch':
            {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches':
            {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123',
            'root_reference': 'incident.status'}].
        incident_config (AlertRouteIncidentConfigPayloadV2):  Example: {'auto_decline_enabled': False,
            'auto_relate_grouped_alerts': False, 'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}],
            'defer_time_seconds': 1, 'enabled': False, 'grouping_keys': [{'reference': 'alert.title'}],
            'grouping_window_seconds': 1}.
        incident_template (AlertRouteIncidentTemplatePayloadV2):  Example: {'custom_fields': [{'binding':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'merge_strategy': 'first-
            wins'}], 'incident_mode': {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'incident_type': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'membership_teams': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'name':
            {'autogenerated': False, 'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'severity': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'merge_strategy': 'first-wins'}, 'start_in_triage': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'summary': {'autogenerated': False, 'binding': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'workspace': {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}}.
        is_private (bool): Whether this alert route is private. Private alert routes will only create private incidents
            from alerts. Example: False.
        name (str): The name of this alert route config, for the user's reference Example: Production incidents.
        version (int): The version this update will create. It must be one more than the route's latest version,
            otherwise the update is rejected - guarding against concurrent edits. Example: 1.
        created_at (datetime.datetime | Unset): The time of creation of this alert route Example:
            2021-08-17T13:28:57.801578Z.
        message_template (EngineParamBindingPayloadV2 | Unset):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        owning_team_ids (list[str] | Unset): IDs of teams that own this alert route Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
        updated_at (datetime.datetime | Unset): The time of last update of this alert route Example:
            2021-08-17T13:28:57.801578Z.
    """

    alert_sources: list[AlertRouteAlertSourcePayloadV2]
    channel_config: list[AlertRouteChannelConfigPayloadV2]
    condition_groups: list[ConditionGroupPayloadV2]
    enabled: bool
    escalation_config: AlertRouteEscalationConfigPayloadV2
    expressions: list[ExpressionPayloadV2]
    incident_config: AlertRouteIncidentConfigPayloadV2
    incident_template: AlertRouteIncidentTemplatePayloadV2
    is_private: bool
    name: str
    version: int
    created_at: datetime.datetime | Unset = UNSET
    message_template: EngineParamBindingPayloadV2 | Unset = UNSET
    owning_team_ids: list[str] | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_sources = []
        for alert_sources_item_data in self.alert_sources:
            alert_sources_item = alert_sources_item_data.to_dict()
            alert_sources.append(alert_sources_item)

        channel_config = []
        for channel_config_item_data in self.channel_config:
            channel_config_item = channel_config_item_data.to_dict()
            channel_config.append(channel_config_item)

        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        enabled = self.enabled

        escalation_config = self.escalation_config.to_dict()

        expressions = []
        for expressions_item_data in self.expressions:
            expressions_item = expressions_item_data.to_dict()
            expressions.append(expressions_item)

        incident_config = self.incident_config.to_dict()

        incident_template = self.incident_template.to_dict()

        is_private = self.is_private

        name = self.name

        version = self.version

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        message_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message_template, Unset):
            message_template = self.message_template.to_dict()

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_sources": alert_sources,
                "channel_config": channel_config,
                "condition_groups": condition_groups,
                "enabled": enabled,
                "escalation_config": escalation_config,
                "expressions": expressions,
                "incident_config": incident_config,
                "incident_template": incident_template,
                "is_private": is_private,
                "name": name,
                "version": version,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if message_template is not UNSET:
            field_dict["message_template"] = message_template
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_route_alert_source_payload_v2 import (
            AlertRouteAlertSourcePayloadV2,
        )
        from ..models.alert_route_channel_config_payload_v2 import (
            AlertRouteChannelConfigPayloadV2,
        )
        from ..models.alert_route_escalation_config_payload_v2 import (
            AlertRouteEscalationConfigPayloadV2,
        )
        from ..models.alert_route_incident_config_payload_v2 import (
            AlertRouteIncidentConfigPayloadV2,
        )
        from ..models.alert_route_incident_template_payload_v2 import (
            AlertRouteIncidentTemplatePayloadV2,
        )
        from ..models.condition_group_payload_v2 import (
            ConditionGroupPayloadV2,
        )
        from ..models.engine_param_binding_payload_v2 import (
            EngineParamBindingPayloadV2,
        )
        from ..models.expression_payload_v2 import ExpressionPayloadV2

        d = dict(src_dict)
        alert_sources = []
        _alert_sources = d.pop("alert_sources")
        for alert_sources_item_data in _alert_sources:
            alert_sources_item = AlertRouteAlertSourcePayloadV2.from_dict(
                alert_sources_item_data
            )

            alert_sources.append(alert_sources_item)

        channel_config = []
        _channel_config = d.pop("channel_config")
        for channel_config_item_data in _channel_config:
            channel_config_item = AlertRouteChannelConfigPayloadV2.from_dict(
                channel_config_item_data
            )

            channel_config.append(channel_config_item)

        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV2.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        enabled = d.pop("enabled")

        escalation_config = AlertRouteEscalationConfigPayloadV2.from_dict(
            d.pop("escalation_config")
        )

        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionPayloadV2.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        incident_config = AlertRouteIncidentConfigPayloadV2.from_dict(
            d.pop("incident_config")
        )

        incident_template = AlertRouteIncidentTemplatePayloadV2.from_dict(
            d.pop("incident_template")
        )

        is_private = d.pop("is_private")

        name = d.pop("name")

        version = d.pop("version")

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _message_template = d.pop("message_template", UNSET)
        message_template: EngineParamBindingPayloadV2 | Unset
        if isinstance(_message_template, Unset):
            message_template = UNSET
        else:
            message_template = EngineParamBindingPayloadV2.from_dict(_message_template)

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        alert_routes_update_payload_v2 = cls(
            alert_sources=alert_sources,
            channel_config=channel_config,
            condition_groups=condition_groups,
            enabled=enabled,
            escalation_config=escalation_config,
            expressions=expressions,
            incident_config=incident_config,
            incident_template=incident_template,
            is_private=is_private,
            name=name,
            version=version,
            created_at=created_at,
            message_template=message_template,
            owning_team_ids=owning_team_ids,
            updated_at=updated_at,
        )

        alert_routes_update_payload_v2.additional_properties = d
        return alert_routes_update_payload_v2

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
