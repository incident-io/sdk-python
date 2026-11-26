from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_grouping_settings_v3 import AlertGroupingSettingsV3
    from ..models.condition_group_payload_v3 import ConditionGroupPayloadV3


T = TypeVar("T", bound="AlertGroupingConditionalBranchV3")


@_attrs_define(kw_only=True)
class AlertGroupingConditionalBranchV3:
    """A grouping branch: the grouping settings for the alerts that match its conditions

    Example:
        {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'settings':
            {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe the same outage, so
            group them together.', 'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800,
            'window_type': 'rolling'}}

    Attributes:
        condition_groups (list[ConditionGroupPayloadV3]): The branch matches an alert when every condition in any one
            group holds Example: [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}].
        settings (AlertGroupingSettingsV3): How alerts are grouped together Example: {'ai_enabled': False,
            'ai_instructions': 'Alerts from the old and new clusters describe the same outage, so group them together.',
            'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type':
            'rolling'}.
        id (str | Unset): Identifier for this branch, a ULID. Omit it on a new branch and one is assigned. Send the ID
            you read back on every update: alert groups are keyed on it. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    condition_groups: list[ConditionGroupPayloadV3]
    settings: AlertGroupingSettingsV3
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        settings = self.settings.to_dict()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_groups": condition_groups,
                "settings": settings,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_grouping_settings_v3 import (
            AlertGroupingSettingsV3,
        )
        from ..models.condition_group_payload_v3 import (
            ConditionGroupPayloadV3,
        )

        d = dict(src_dict)
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV3.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        settings = AlertGroupingSettingsV3.from_dict(d.pop("settings"))

        id = d.pop("id", UNSET)

        alert_grouping_conditional_branch_v3 = cls(
            condition_groups=condition_groups,
            settings=settings,
            id=id,
        )

        alert_grouping_conditional_branch_v3.additional_properties = d
        return alert_grouping_conditional_branch_v3

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
