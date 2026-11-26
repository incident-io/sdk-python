from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_rule_set_v3_kind import AlertRuleSetV3Kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_rule_block_v3 import AlertRuleBlockV3
    from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3
    from ..models.expression_payload_v3 import ExpressionPayloadV3


T = TypeVar("T", bound="AlertRuleSetV3")


@_attrs_define(kw_only=True)
class AlertRuleSetV3:
    """One set of alert rules: the organisation's required rules, its default rules, or one team's rules

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
            'incident.severity'}}}], 'created_at': '2021-08-17T13:28:57.801578Z', 'expressions': [{'else_branch': {'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123',
            'root_reference': 'incident.status'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'kind': 'team', 'message_template':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'team_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'version': 3}

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
        created_at (datetime.datetime): When this set of rules was created Example: 2021-08-17T13:28:57.801578Z.
        expressions (list[ExpressionPayloadV3]): Expressions the blocks' conditions and actions reference, such as a
            walk from the alert's team to its escalation path Example: [{'else_branch': {'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123',
            'root_reference': 'incident.status'}].
        id (str): Unique identifier for this set of rules Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        kind (AlertRuleSetV3Kind): Which set this is. Required rules run for every alert. Team rules run for the alert's
            team. Default rules run when no team's rules ran. Example: team.
        updated_at (datetime.datetime): When the current version was written Example: 2021-08-17T13:28:57.801578Z.
        version (int): The current version number. Every update writes the next version. Example: 3.
        message_template (EngineParamBindingPayloadV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        team_id (str | Unset): The catalog entry ID of the team, set only for team rules Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
    """

    blocks: list[AlertRuleBlockV3]
    created_at: datetime.datetime
    expressions: list[ExpressionPayloadV3]
    id: str
    kind: AlertRuleSetV3Kind
    updated_at: datetime.datetime
    version: int
    message_template: EngineParamBindingPayloadV3 | Unset = UNSET
    team_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blocks = []
        for blocks_item_data in self.blocks:
            blocks_item = blocks_item_data.to_dict()
            blocks.append(blocks_item)

        created_at = self.created_at.isoformat()

        expressions = []
        for expressions_item_data in self.expressions:
            expressions_item = expressions_item_data.to_dict()
            expressions.append(expressions_item)

        id = self.id

        kind = self.kind.value

        updated_at = self.updated_at.isoformat()

        version = self.version

        message_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message_template, Unset):
            message_template = self.message_template.to_dict()

        team_id = self.team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blocks": blocks,
                "created_at": created_at,
                "expressions": expressions,
                "id": id,
                "kind": kind,
                "updated_at": updated_at,
                "version": version,
            }
        )
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

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionPayloadV3.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        id = d.pop("id")

        kind = AlertRuleSetV3Kind(d.pop("kind"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        _message_template = d.pop("message_template", UNSET)
        message_template: EngineParamBindingPayloadV3 | Unset
        if isinstance(_message_template, Unset):
            message_template = UNSET
        else:
            message_template = EngineParamBindingPayloadV3.from_dict(_message_template)

        team_id = d.pop("team_id", UNSET)

        alert_rule_set_v3 = cls(
            blocks=blocks,
            created_at=created_at,
            expressions=expressions,
            id=id,
            kind=kind,
            updated_at=updated_at,
            version=version,
            message_template=message_template,
            team_id=team_id,
        )

        alert_rule_set_v3.additional_properties = d
        return alert_rule_set_v3

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
