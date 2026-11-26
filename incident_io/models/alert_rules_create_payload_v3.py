from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_rules_create_payload_v3_kind import AlertRulesCreatePayloadV3Kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_rule_block_v3 import AlertRuleBlockV3
    from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3
    from ..models.expression_payload_v3 import ExpressionPayloadV3


T = TypeVar("T", bound="AlertRulesCreatePayloadV3")


@_attrs_define(kw_only=True)
class AlertRulesCreatePayloadV3:
    """
    Example:
        {'blocks': [{'branches': [{'actions': [{'create_incident': {'auto_decline': False, 'incident_template':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'is_private': False, 'membership_teams': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'escalate': {'auto_cancel': True, 'escalation_paths': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'grace_period_seconds': 120, 'mode': 'on_each_new_alert', 'urgency': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'users':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'id': 'page-team', 'post_microsoft_teams': {'channel_visibility': 'public',
            'channels': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}, 'post_slack': {'channel_visibility':
            'public', 'channels': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}, 'type': 'escalate'}],
            'branches': [{'actions': [{'create_incident': {'auto_decline': False, 'incident_template': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'is_private': False, 'membership_teams': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'escalate': {'auto_cancel': True, 'escalation_paths': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'grace_period_seconds': 120, 'mode': 'on_each_new_alert', 'urgency': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'users':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'id': 'page-team', 'post_microsoft_teams': {'channel_visibility': 'public',
            'channels': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}, 'post_slack': {'channel_visibility':
            'public', 'channels': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}, 'type': 'escalate'}],
            'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'id': 'production-grafana'}], 'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}], 'id': 'production'}], 'id': 'page-owning-team', 'message_template': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'expressions': [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123',
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
            'kind': 'team', 'message_template': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'team_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}

    Attributes:
        blocks (list[AlertRuleBlockV3]): The blocks of rules, in order. Every block runs for an alert. Example:
            [{'branches': [{'actions': [{'create_incident': {'auto_decline': False, 'incident_template': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'is_private': False, 'membership_teams': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'escalate': {'auto_cancel': True, 'escalation_paths': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'grace_period_seconds': 120, 'mode': 'on_each_new_alert', 'urgency': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'users':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'id': 'page-team', 'post_microsoft_teams': {'channel_visibility': 'public',
            'channels': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}, 'post_slack': {'channel_visibility':
            'public', 'channels': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}, 'type': 'escalate'}],
            'branches': [{'actions': [{'create_incident': {'auto_decline': False, 'incident_template': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'is_private': False, 'membership_teams': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'escalate': {'auto_cancel': True, 'escalation_paths': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'grace_period_seconds': 120, 'mode': 'on_each_new_alert', 'urgency': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'users':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'id': 'page-team', 'post_microsoft_teams': {'channel_visibility': 'public',
            'channels': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}, 'post_slack': {'channel_visibility':
            'public', 'channels': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}, 'type': 'escalate'}],
            'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'id': 'production-grafana'}], 'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}], 'id': 'production'}], 'id': 'page-owning-team', 'message_template': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}].
        kind (AlertRulesCreatePayloadV3Kind): Which set to create. Required rules run for every alert. Team rules run
            for the alert's team. Default rules run when no team's rules ran. Example: team.
        expressions (list[ExpressionPayloadV3] | Unset): Expressions the blocks' conditions and actions reference. Omit
            it when the rules use none. Example: [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123',
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
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}].
        message_template (EngineParamBindingPayloadV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        team_id (str | Unset): The catalog entry ID of the team. Set it for team rules only. Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
    """

    blocks: list[AlertRuleBlockV3]
    kind: AlertRulesCreatePayloadV3Kind
    expressions: list[ExpressionPayloadV3] | Unset = UNSET
    message_template: EngineParamBindingPayloadV3 | Unset = UNSET
    team_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blocks = []
        for blocks_item_data in self.blocks:
            blocks_item = blocks_item_data.to_dict()
            blocks.append(blocks_item)

        kind = self.kind.value

        expressions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expressions, Unset):
            expressions = []
            for expressions_item_data in self.expressions:
                expressions_item = expressions_item_data.to_dict()
                expressions.append(expressions_item)

        message_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message_template, Unset):
            message_template = self.message_template.to_dict()

        team_id = self.team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blocks": blocks,
                "kind": kind,
            }
        )
        if expressions is not UNSET:
            field_dict["expressions"] = expressions
        if message_template is not UNSET:
            field_dict["message_template"] = message_template
        if team_id is not UNSET:
            field_dict["team_id"] = team_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_rule_block_v3 import AlertRuleBlockV3
        from ..models.engine_param_binding_payload_v3 import (
            EngineParamBindingPayloadV3,
        )
        from ..models.expression_payload_v3 import ExpressionPayloadV3

        d = dict(src_dict)
        blocks = []
        _blocks = d.pop("blocks")
        for blocks_item_data in _blocks:
            blocks_item = AlertRuleBlockV3.from_dict(blocks_item_data)

            blocks.append(blocks_item)

        kind = AlertRulesCreatePayloadV3Kind(d.pop("kind"))

        _expressions = d.pop("expressions", UNSET)
        expressions: list[ExpressionPayloadV3] | Unset = UNSET
        if _expressions is not UNSET:
            expressions = []
            for expressions_item_data in _expressions:
                expressions_item = ExpressionPayloadV3.from_dict(expressions_item_data)

                expressions.append(expressions_item)

        _message_template = d.pop("message_template", UNSET)
        message_template: EngineParamBindingPayloadV3 | Unset
        if isinstance(_message_template, Unset):
            message_template = UNSET
        else:
            message_template = EngineParamBindingPayloadV3.from_dict(_message_template)

        team_id = d.pop("team_id", UNSET)

        alert_rules_create_payload_v3 = cls(
            blocks=blocks,
            kind=kind,
            expressions=expressions,
            message_template=message_template,
            team_id=team_id,
        )

        alert_rules_create_payload_v3.additional_properties = d
        return alert_rules_create_payload_v3

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
