from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_route_escalation_target_v3 import AlertRouteEscalationTargetV3
    from ..models.alert_route_when_alert_joins_group_v3 import (
        AlertRouteWhenAlertJoinsGroupV3,
    )


T = TypeVar("T", bound="AlertRouteEscalationConfigV3")


@_attrs_define(kw_only=True)
class AlertRouteEscalationConfigV3:
    """
    Example:
        {'auto_cancel_escalations': False, 'escalation_targets': [{'escalation_paths': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'users': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}], 'when_alert_joins_group': {'grace_period_seconds': 60, 'mode':
            'on_each_new_alert'}}

    Attributes:
        auto_cancel_escalations (bool): Should we auto cancel escalations when all alerts are resolved? Example: False.
        escalation_targets (list[AlertRouteEscalationTargetV3]): Targets for escalation Example: [{'escalation_paths':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'users': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}].
        when_alert_joins_group (AlertRouteWhenAlertJoinsGroupV3 | Unset):  Example: {'grace_period_seconds': 60, 'mode':
            'on_each_new_alert'}.
    """

    auto_cancel_escalations: bool
    escalation_targets: list[AlertRouteEscalationTargetV3]
    when_alert_joins_group: AlertRouteWhenAlertJoinsGroupV3 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_cancel_escalations = self.auto_cancel_escalations

        escalation_targets = []
        for escalation_targets_item_data in self.escalation_targets:
            escalation_targets_item = escalation_targets_item_data.to_dict()
            escalation_targets.append(escalation_targets_item)

        when_alert_joins_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.when_alert_joins_group, Unset):
            when_alert_joins_group = self.when_alert_joins_group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auto_cancel_escalations": auto_cancel_escalations,
                "escalation_targets": escalation_targets,
            }
        )
        if when_alert_joins_group is not UNSET:
            field_dict["when_alert_joins_group"] = when_alert_joins_group

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_route_escalation_target_v3 import (
            AlertRouteEscalationTargetV3,
        )
        from ..models.alert_route_when_alert_joins_group_v3 import (
            AlertRouteWhenAlertJoinsGroupV3,
        )

        d = dict(src_dict)
        auto_cancel_escalations = d.pop("auto_cancel_escalations")

        escalation_targets = []
        _escalation_targets = d.pop("escalation_targets")
        for escalation_targets_item_data in _escalation_targets:
            escalation_targets_item = AlertRouteEscalationTargetV3.from_dict(
                escalation_targets_item_data
            )

            escalation_targets.append(escalation_targets_item)

        _when_alert_joins_group = d.pop("when_alert_joins_group", UNSET)
        when_alert_joins_group: AlertRouteWhenAlertJoinsGroupV3 | Unset
        if isinstance(_when_alert_joins_group, Unset):
            when_alert_joins_group = UNSET
        else:
            when_alert_joins_group = AlertRouteWhenAlertJoinsGroupV3.from_dict(
                _when_alert_joins_group
            )

        alert_route_escalation_config_v3 = cls(
            auto_cancel_escalations=auto_cancel_escalations,
            escalation_targets=escalation_targets,
            when_alert_joins_group=when_alert_joins_group,
        )

        alert_route_escalation_config_v3.additional_properties = d
        return alert_route_escalation_config_v3

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
