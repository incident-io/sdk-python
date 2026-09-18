from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_grouping_config_v3 import AlertGroupingConfigV3
    from ..models.alert_message_config_payload_v3 import AlertMessageConfigPayloadV3
    from ..models.alert_route_alert_source_payload_v3 import (
        AlertRouteAlertSourcePayloadV3,
    )
    from ..models.alert_route_escalation_config_payload_v3 import (
        AlertRouteEscalationConfigPayloadV3,
    )
    from ..models.alert_route_incident_config_payload_v3 import (
        AlertRouteIncidentConfigPayloadV3,
    )
    from ..models.condition_group_payload_v3 import ConditionGroupPayloadV3
    from ..models.expression_payload_v3 import ExpressionPayloadV3


T = TypeVar("T", bound="AlertRoutesCreatePayloadV3")


@_attrs_define
class AlertRoutesCreatePayloadV3:
    """
    Example:
        {'alert_sources': [{'alert_source_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}], 'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'enabled': False, 'escalation_config':
            {'auto_cancel_escalations': False, 'escalation_targets': [{'escalation_paths': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'users': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}], 'when_alert_joins_group': {'grace_period_seconds': 60, 'mode':
            'on_each_new_alert'}}, 'expressions': [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label':
            'Team Slack channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}],
            'grouping_config': {'default': {'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}],
            'window_seconds': 1800, 'window_type': 'rolling'}}, 'incident_config': {'auto_decline_enabled': False,
            'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'enabled': False, 'incident_template': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'membership_teams': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'template':
            {'custom_fields': [{'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'merge_strategy': 'first-wins'}], 'incident_mode': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'incident_type': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'membership_teams':
            {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}, 'name': {'autogenerated': False, 'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'severity': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'merge_strategy':
            'first-wins'}, 'start_in_triage': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'summary':
            {'autogenerated': False, 'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}}}, 'is_private': False, 'message_config':
            {'destinations': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'ms_teams_targets': {'binding':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'channel_visibility': 'public', 'group_alerts_summary': False},
            'slack_targets': {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'channel_visibility': 'public',
            'group_alerts_summary': False}}], 'template': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'name': 'Production
            incidents', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH']}

    Attributes:
        alert_sources (list[AlertRouteAlertSourcePayloadV3]): Which alert sources this route matches Example:
            [{'alert_source_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}]}].
        condition_groups (list[ConditionGroupPayloadV3]): Filter: the condition groups that must be true for this route
            to fire Example: [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}].
        enabled (bool): Whether this alert route is enabled Example: False.
        escalation_config (AlertRouteEscalationConfigPayloadV3):  Example: {'auto_cancel_escalations': False,
            'escalation_targets': [{'escalation_paths': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'users':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'when_alert_joins_group': {'grace_period_seconds': 60, 'mode':
            'on_each_new_alert'}}.
        expressions (list[ExpressionPayloadV3]): The expressions used by bindings in this route Example:
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}].
        grouping_config (AlertGroupingConfigV3):  Example: {'default': {'enabled': True, 'grouping_keys': [{'reference':
            'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}.
        incident_config (AlertRouteIncidentConfigPayloadV3):  Example: {'auto_decline_enabled': False,
            'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'enabled': False, 'incident_template': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'membership_teams': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'template':
            {'custom_fields': [{'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'merge_strategy': 'first-wins'}], 'incident_mode': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'incident_type': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'membership_teams':
            {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}, 'name': {'autogenerated': False, 'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'severity': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'merge_strategy':
            'first-wins'}, 'start_in_triage': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'summary':
            {'autogenerated': False, 'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}}}.
        is_private (bool): Whether this alert route is private. Private alert routes only create private incidents from
            alerts. Example: False.
        message_config (AlertMessageConfigPayloadV3):  Example: {'destinations': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}], 'ms_teams_targets': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'channel_visibility':
            'public', 'group_alerts_summary': False}, 'slack_targets': {'binding': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'channel_visibility': 'public', 'group_alerts_summary': False}}], 'template': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}.
        name (str): The name of this alert route, for the user's reference Example: Production incidents.
        owning_team_ids (list[str] | Unset): IDs of teams that own this alert route Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
    """

    alert_sources: list[AlertRouteAlertSourcePayloadV3]
    condition_groups: list[ConditionGroupPayloadV3]
    enabled: bool
    escalation_config: AlertRouteEscalationConfigPayloadV3
    expressions: list[ExpressionPayloadV3]
    grouping_config: AlertGroupingConfigV3
    incident_config: AlertRouteIncidentConfigPayloadV3
    is_private: bool
    message_config: AlertMessageConfigPayloadV3
    name: str
    owning_team_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_sources = []
        for alert_sources_item_data in self.alert_sources:
            alert_sources_item = alert_sources_item_data.to_dict()
            alert_sources.append(alert_sources_item)

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

        grouping_config = self.grouping_config.to_dict()

        incident_config = self.incident_config.to_dict()

        is_private = self.is_private

        message_config = self.message_config.to_dict()

        name = self.name

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_sources": alert_sources,
                "condition_groups": condition_groups,
                "enabled": enabled,
                "escalation_config": escalation_config,
                "expressions": expressions,
                "grouping_config": grouping_config,
                "incident_config": incident_config,
                "is_private": is_private,
                "message_config": message_config,
                "name": name,
            }
        )
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_grouping_config_v3 import (
            AlertGroupingConfigV3,
        )
        from ..models.alert_message_config_payload_v3 import (
            AlertMessageConfigPayloadV3,
        )
        from ..models.alert_route_alert_source_payload_v3 import (
            AlertRouteAlertSourcePayloadV3,
        )
        from ..models.alert_route_escalation_config_payload_v3 import (
            AlertRouteEscalationConfigPayloadV3,
        )
        from ..models.alert_route_incident_config_payload_v3 import (
            AlertRouteIncidentConfigPayloadV3,
        )
        from ..models.condition_group_payload_v3 import (
            ConditionGroupPayloadV3,
        )
        from ..models.expression_payload_v3 import ExpressionPayloadV3

        d = dict(src_dict)
        alert_sources = []
        _alert_sources = d.pop("alert_sources")
        for alert_sources_item_data in _alert_sources:
            alert_sources_item = AlertRouteAlertSourcePayloadV3.from_dict(
                alert_sources_item_data
            )

            alert_sources.append(alert_sources_item)

        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV3.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        enabled = d.pop("enabled")

        escalation_config = AlertRouteEscalationConfigPayloadV3.from_dict(
            d.pop("escalation_config")
        )

        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionPayloadV3.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        grouping_config = AlertGroupingConfigV3.from_dict(d.pop("grouping_config"))

        incident_config = AlertRouteIncidentConfigPayloadV3.from_dict(
            d.pop("incident_config")
        )

        is_private = d.pop("is_private")

        message_config = AlertMessageConfigPayloadV3.from_dict(d.pop("message_config"))

        name = d.pop("name")

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        alert_routes_create_payload_v3 = cls(
            alert_sources=alert_sources,
            condition_groups=condition_groups,
            enabled=enabled,
            escalation_config=escalation_config,
            expressions=expressions,
            grouping_config=grouping_config,
            incident_config=incident_config,
            is_private=is_private,
            message_config=message_config,
            name=name,
            owning_team_ids=owning_team_ids,
        )

        alert_routes_create_payload_v3.additional_properties = d
        return alert_routes_create_payload_v3

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
