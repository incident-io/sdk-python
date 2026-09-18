from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_route_channel_target_payload_v2 import (
        AlertRouteChannelTargetPayloadV2,
    )
    from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2


T = TypeVar("T", bound="AlertRouteChannelConfigPayloadV2")


@_attrs_define
class AlertRouteChannelConfigPayloadV2:
    """
    Example:
        {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'ms_teams_targets': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'channel_visibility': 'abc123'}, 'slack_targets': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'channel_visibility': 'abc123'}}

    Attributes:
        condition_groups (list[ConditionGroupPayloadV2]): The conditions that must be met for this channel config to be
            used Example: [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}].
        ms_teams_targets (AlertRouteChannelTargetPayloadV2 | Unset):  Example: {'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'channel_visibility': 'abc123'}.
        slack_targets (AlertRouteChannelTargetPayloadV2 | Unset):  Example: {'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'channel_visibility': 'abc123'}.
    """

    condition_groups: list[ConditionGroupPayloadV2]
    ms_teams_targets: AlertRouteChannelTargetPayloadV2 | Unset = UNSET
    slack_targets: AlertRouteChannelTargetPayloadV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        ms_teams_targets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ms_teams_targets, Unset):
            ms_teams_targets = self.ms_teams_targets.to_dict()

        slack_targets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.slack_targets, Unset):
            slack_targets = self.slack_targets.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_groups": condition_groups,
            }
        )
        if ms_teams_targets is not UNSET:
            field_dict["ms_teams_targets"] = ms_teams_targets
        if slack_targets is not UNSET:
            field_dict["slack_targets"] = slack_targets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_route_channel_target_payload_v2 import (
            AlertRouteChannelTargetPayloadV2,
        )
        from ..models.condition_group_payload_v2 import (
            ConditionGroupPayloadV2,
        )

        d = dict(src_dict)
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV2.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        _ms_teams_targets = d.pop("ms_teams_targets", UNSET)
        ms_teams_targets: AlertRouteChannelTargetPayloadV2 | Unset
        if isinstance(_ms_teams_targets, Unset):
            ms_teams_targets = UNSET
        else:
            ms_teams_targets = AlertRouteChannelTargetPayloadV2.from_dict(
                _ms_teams_targets
            )

        _slack_targets = d.pop("slack_targets", UNSET)
        slack_targets: AlertRouteChannelTargetPayloadV2 | Unset
        if isinstance(_slack_targets, Unset):
            slack_targets = UNSET
        else:
            slack_targets = AlertRouteChannelTargetPayloadV2.from_dict(_slack_targets)

        alert_route_channel_config_payload_v2 = cls(
            condition_groups=condition_groups,
            ms_teams_targets=ms_teams_targets,
            slack_targets=slack_targets,
        )

        alert_route_channel_config_payload_v2.additional_properties = d
        return alert_route_channel_config_payload_v2

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
