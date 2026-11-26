from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_rule_action_v3_type import AlertRuleActionV3Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_rule_create_incident_action_v3 import (
        AlertRuleCreateIncidentActionV3,
    )
    from ..models.alert_rule_escalate_action_v3 import AlertRuleEscalateActionV3
    from ..models.alert_rule_post_action_v3 import AlertRulePostActionV3


T = TypeVar("T", bound="AlertRuleActionV3")


@_attrs_define(kw_only=True)
class AlertRuleActionV3:
    """One action a branch takes. Set type, and the object of the same name with the action's parameters. An investigate
    action has no parameters.

        Example:
            {'create_incident': {'auto_decline': False, 'incident_template': {'array_value': [{'literal': 'SEV123',
                'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
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
                {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}, 'type': 'escalate'}

        Attributes:
            type_ (AlertRuleActionV3Type): Which action to take Example: escalate.
            create_incident (AlertRuleCreateIncidentActionV3 | Unset): Create an incident from the alert, or attach it to
                the incident its group already has Example: {'auto_decline': False, 'incident_template': {'array_value':
                [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
                'incident.severity'}}, 'is_private': False, 'membership_teams': {'array_value': [{'literal': 'SEV123',
                'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}.
            escalate (AlertRuleEscalateActionV3 | Unset): Page escalation paths or users about the alert. Set
                escalation_paths, users, or both. Example: {'auto_cancel': True, 'escalation_paths': {'array_value':
                [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
                'incident.severity'}}, 'grace_period_seconds': 120, 'mode': 'on_each_new_alert', 'urgency': {'array_value':
                [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
                'incident.severity'}}, 'users': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
                'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}.
            id (str | Unset): Identifier for this action, unique within the set. The server assigns one when it is omitted.
                Example: page-team.
            post_microsoft_teams (AlertRulePostActionV3 | Unset): Post the alert to chat channels Example:
                {'channel_visibility': 'public', 'channels': {'array_value': [{'literal': 'SEV123', 'reference':
                'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}.
            post_slack (AlertRulePostActionV3 | Unset): Post the alert to chat channels Example: {'channel_visibility':
                'public', 'channels': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
                {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}.
    """

    type_: AlertRuleActionV3Type
    create_incident: AlertRuleCreateIncidentActionV3 | Unset = UNSET
    escalate: AlertRuleEscalateActionV3 | Unset = UNSET
    id: str | Unset = UNSET
    post_microsoft_teams: AlertRulePostActionV3 | Unset = UNSET
    post_slack: AlertRulePostActionV3 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        create_incident: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_incident, Unset):
            create_incident = self.create_incident.to_dict()

        escalate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.escalate, Unset):
            escalate = self.escalate.to_dict()

        id = self.id

        post_microsoft_teams: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post_microsoft_teams, Unset):
            post_microsoft_teams = self.post_microsoft_teams.to_dict()

        post_slack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post_slack, Unset):
            post_slack = self.post_slack.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if create_incident is not UNSET:
            field_dict["create_incident"] = create_incident
        if escalate is not UNSET:
            field_dict["escalate"] = escalate
        if id is not UNSET:
            field_dict["id"] = id
        if post_microsoft_teams is not UNSET:
            field_dict["post_microsoft_teams"] = post_microsoft_teams
        if post_slack is not UNSET:
            field_dict["post_slack"] = post_slack

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_rule_create_incident_action_v3 import (
            AlertRuleCreateIncidentActionV3,
        )
        from ..models.alert_rule_escalate_action_v3 import (
            AlertRuleEscalateActionV3,
        )
        from ..models.alert_rule_post_action_v3 import (
            AlertRulePostActionV3,
        )

        d = dict(src_dict)
        type_ = AlertRuleActionV3Type(d.pop("type"))

        _create_incident = d.pop("create_incident", UNSET)
        create_incident: AlertRuleCreateIncidentActionV3 | Unset
        if isinstance(_create_incident, Unset):
            create_incident = UNSET
        else:
            create_incident = AlertRuleCreateIncidentActionV3.from_dict(
                _create_incident
            )

        _escalate = d.pop("escalate", UNSET)
        escalate: AlertRuleEscalateActionV3 | Unset
        if isinstance(_escalate, Unset):
            escalate = UNSET
        else:
            escalate = AlertRuleEscalateActionV3.from_dict(_escalate)

        id = d.pop("id", UNSET)

        _post_microsoft_teams = d.pop("post_microsoft_teams", UNSET)
        post_microsoft_teams: AlertRulePostActionV3 | Unset
        if isinstance(_post_microsoft_teams, Unset):
            post_microsoft_teams = UNSET
        else:
            post_microsoft_teams = AlertRulePostActionV3.from_dict(
                _post_microsoft_teams
            )

        _post_slack = d.pop("post_slack", UNSET)
        post_slack: AlertRulePostActionV3 | Unset
        if isinstance(_post_slack, Unset):
            post_slack = UNSET
        else:
            post_slack = AlertRulePostActionV3.from_dict(_post_slack)

        alert_rule_action_v3 = cls(
            type_=type_,
            create_incident=create_incident,
            escalate=escalate,
            id=id,
            post_microsoft_teams=post_microsoft_teams,
            post_slack=post_slack,
        )

        alert_rule_action_v3.additional_properties = d
        return alert_rule_action_v3

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
