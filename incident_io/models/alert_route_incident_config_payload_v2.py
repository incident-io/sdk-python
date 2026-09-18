from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2
    from ..models.grouping_key_v2 import GroupingKeyV2


T = TypeVar("T", bound="AlertRouteIncidentConfigPayloadV2")


@_attrs_define
class AlertRouteIncidentConfigPayloadV2:
    """
    Example:
        {'auto_decline_enabled': False, 'auto_relate_grouped_alerts': False, 'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'defer_time_seconds': 1, 'enabled': False, 'grouping_keys': [{'reference':
            'alert.title'}], 'grouping_window_seconds': 1}

    Attributes:
        auto_decline_enabled (bool): Should triage incidents be declined when alerts are resolved? Example: False.
        condition_groups (list[ConditionGroupPayloadV2]): What condition groups must be true for this alert route to
            create an incident? Example: [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}].
        defer_time_seconds (int): How long should the escalation defer time be? Example: 1.
        enabled (bool): Whether incident creation is enabled for this alert route Example: False.
        grouping_keys (list[GroupingKeyV2]): Which attributes should this alert route use to group alerts? Example:
            [{'reference': 'alert.title'}].
        grouping_window_seconds (int): How large should the grouping window be? Example: 1.
        auto_relate_grouped_alerts (bool | Unset): Should grouped alerts automatically be related to active incidents
            without confirmation? Example: False.
    """

    auto_decline_enabled: bool
    condition_groups: list[ConditionGroupPayloadV2]
    defer_time_seconds: int
    enabled: bool
    grouping_keys: list[GroupingKeyV2]
    grouping_window_seconds: int
    auto_relate_grouped_alerts: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_decline_enabled = self.auto_decline_enabled

        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        defer_time_seconds = self.defer_time_seconds

        enabled = self.enabled

        grouping_keys = []
        for grouping_keys_item_data in self.grouping_keys:
            grouping_keys_item = grouping_keys_item_data.to_dict()
            grouping_keys.append(grouping_keys_item)

        grouping_window_seconds = self.grouping_window_seconds

        auto_relate_grouped_alerts = self.auto_relate_grouped_alerts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auto_decline_enabled": auto_decline_enabled,
                "condition_groups": condition_groups,
                "defer_time_seconds": defer_time_seconds,
                "enabled": enabled,
                "grouping_keys": grouping_keys,
                "grouping_window_seconds": grouping_window_seconds,
            }
        )
        if auto_relate_grouped_alerts is not UNSET:
            field_dict["auto_relate_grouped_alerts"] = auto_relate_grouped_alerts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_group_payload_v2 import (
            ConditionGroupPayloadV2,
        )
        from ..models.grouping_key_v2 import GroupingKeyV2

        d = dict(src_dict)
        auto_decline_enabled = d.pop("auto_decline_enabled")

        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV2.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        defer_time_seconds = d.pop("defer_time_seconds")

        enabled = d.pop("enabled")

        grouping_keys = []
        _grouping_keys = d.pop("grouping_keys")
        for grouping_keys_item_data in _grouping_keys:
            grouping_keys_item = GroupingKeyV2.from_dict(grouping_keys_item_data)

            grouping_keys.append(grouping_keys_item)

        grouping_window_seconds = d.pop("grouping_window_seconds")

        auto_relate_grouped_alerts = d.pop("auto_relate_grouped_alerts", UNSET)

        alert_route_incident_config_payload_v2 = cls(
            auto_decline_enabled=auto_decline_enabled,
            condition_groups=condition_groups,
            defer_time_seconds=defer_time_seconds,
            enabled=enabled,
            grouping_keys=grouping_keys,
            grouping_window_seconds=grouping_window_seconds,
            auto_relate_grouped_alerts=auto_relate_grouped_alerts,
        )

        alert_route_incident_config_payload_v2.additional_properties = d
        return alert_route_incident_config_payload_v2

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
