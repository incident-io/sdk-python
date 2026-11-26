from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_rule_escalate_action_v3_mode import AlertRuleEscalateActionV3Mode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3


T = TypeVar("T", bound="AlertRuleEscalateActionV3")


@_attrs_define(kw_only=True)
class AlertRuleEscalateActionV3:
    """Page escalation paths or users about the alert. Set escalation_paths, users, or both.

    Example:
        {'auto_cancel': True, 'escalation_paths': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'grace_period_seconds': 120, 'mode': 'on_each_new_alert', 'urgency': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'users':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}

    Attributes:
        auto_cancel (bool | Unset): Cancel the escalation when the alert resolves, or when every alert in its group
            resolves. Defaults to false. Example: True.
        escalation_paths (EngineParamBindingPayloadV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        grace_period_seconds (int | Unset): How long an alert that joins a group with a live page waits before it pages.
            0, the default, pages at once. Only used with on_each_new_alert. Example: 120.
        mode (AlertRuleEscalateActionV3Mode | Unset): How an alert that joins a group pages. on_each_new_alert pages for
            every alert. on_priority_increase pages a target only when the alert's priority is above every live page the
            group already has to that target. Defaults to on_each_new_alert. Example: on_each_new_alert.
        urgency (EngineParamBindingPayloadV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        users (EngineParamBindingPayloadV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    auto_cancel: bool | Unset = UNSET
    escalation_paths: EngineParamBindingPayloadV3 | Unset = UNSET
    grace_period_seconds: int | Unset = UNSET
    mode: AlertRuleEscalateActionV3Mode | Unset = UNSET
    urgency: EngineParamBindingPayloadV3 | Unset = UNSET
    users: EngineParamBindingPayloadV3 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_cancel = self.auto_cancel

        escalation_paths: dict[str, Any] | Unset = UNSET
        if not isinstance(self.escalation_paths, Unset):
            escalation_paths = self.escalation_paths.to_dict()

        grace_period_seconds = self.grace_period_seconds

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        urgency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.urgency, Unset):
            urgency = self.urgency.to_dict()

        users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_cancel is not UNSET:
            field_dict["auto_cancel"] = auto_cancel
        if escalation_paths is not UNSET:
            field_dict["escalation_paths"] = escalation_paths
        if grace_period_seconds is not UNSET:
            field_dict["grace_period_seconds"] = grace_period_seconds
        if mode is not UNSET:
            field_dict["mode"] = mode
        if urgency is not UNSET:
            field_dict["urgency"] = urgency
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_payload_v3 import (
            EngineParamBindingPayloadV3,
        )

        d = dict(src_dict)
        auto_cancel = d.pop("auto_cancel", UNSET)

        _escalation_paths = d.pop("escalation_paths", UNSET)
        escalation_paths: EngineParamBindingPayloadV3 | Unset
        if isinstance(_escalation_paths, Unset):
            escalation_paths = UNSET
        else:
            escalation_paths = EngineParamBindingPayloadV3.from_dict(_escalation_paths)

        grace_period_seconds = d.pop("grace_period_seconds", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: AlertRuleEscalateActionV3Mode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = AlertRuleEscalateActionV3Mode(_mode)

        _urgency = d.pop("urgency", UNSET)
        urgency: EngineParamBindingPayloadV3 | Unset
        if isinstance(_urgency, Unset):
            urgency = UNSET
        else:
            urgency = EngineParamBindingPayloadV3.from_dict(_urgency)

        _users = d.pop("users", UNSET)
        users: EngineParamBindingPayloadV3 | Unset
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = EngineParamBindingPayloadV3.from_dict(_users)

        alert_rule_escalate_action_v3 = cls(
            auto_cancel=auto_cancel,
            escalation_paths=escalation_paths,
            grace_period_seconds=grace_period_seconds,
            mode=mode,
            urgency=urgency,
            users=users,
        )

        alert_rule_escalate_action_v3.additional_properties = d
        return alert_rule_escalate_action_v3

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
