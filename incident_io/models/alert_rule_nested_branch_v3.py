from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_rule_action_v3 import AlertRuleActionV3
    from ..models.condition_group_payload_v3 import ConditionGroupPayloadV3


T = TypeVar("T", bound="AlertRuleNestedBranchV3")


@_attrs_define(kw_only=True)
class AlertRuleNestedBranchV3:
    """A branch nested inside another, with its own conditions and actions

    Example:
        {'actions': [{'create_incident': {'auto_decline': False, 'incident_template': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'is_private': False, 'membership_teams': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'escalate':
            {'auto_cancel': True, 'escalation_paths': {'array_value': [{'literal': 'SEV123', 'reference':
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
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'id': 'production-grafana'}

    Attributes:
        actions (list[AlertRuleActionV3]): The actions to take when the branch holds Example: [{'create_incident':
            {'auto_decline': False, 'incident_template': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'is_private': False,
            'membership_teams': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'escalate': {'auto_cancel': True, 'escalation_paths':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'grace_period_seconds': 120, 'mode': 'on_each_new_alert', 'urgency':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'users': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'id': 'page-team',
            'post_microsoft_teams': {'channel_visibility': 'public', 'channels': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'mode':
            'per_alert'}, 'post_slack': {'channel_visibility': 'public', 'channels': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'mode':
            'per_alert'}, 'type': 'escalate'}].
        condition_groups (list[ConditionGroupPayloadV3]): The branch holds when every condition in any one group holds.
            A branch with no groups always holds. Example: [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}].
        id (str): Identifier for this branch, unique within the set Example: production-grafana.
    """

    actions: list[AlertRuleActionV3]
    condition_groups: list[ConditionGroupPayloadV3]
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
                "condition_groups": condition_groups,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_rule_action_v3 import AlertRuleActionV3
        from ..models.condition_group_payload_v3 import (
            ConditionGroupPayloadV3,
        )

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = AlertRuleActionV3.from_dict(actions_item_data)

            actions.append(actions_item)

        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV3.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        id = d.pop("id")

        alert_rule_nested_branch_v3 = cls(
            actions=actions,
            condition_groups=condition_groups,
            id=id,
        )

        alert_rule_nested_branch_v3.additional_properties = d
        return alert_rule_nested_branch_v3

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
