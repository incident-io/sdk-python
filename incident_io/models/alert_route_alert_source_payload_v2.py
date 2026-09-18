from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2


T = TypeVar("T", bound="AlertRouteAlertSourcePayloadV2")


@_attrs_define
class AlertRouteAlertSourcePayloadV2:
    """
    Example:
        {'alert_source_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}]}

    Attributes:
        alert_source_id (str): The alert source ID that will match for the route Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        condition_groups (list[ConditionGroupPayloadV2]): What conditions should alerts from this source meet to be
            included in this alert route? Example: [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}].
    """

    alert_source_id: str
    condition_groups: list[ConditionGroupPayloadV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_source_id = self.alert_source_id

        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_source_id": alert_source_id,
                "condition_groups": condition_groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_group_payload_v2 import (
            ConditionGroupPayloadV2,
        )

        d = dict(src_dict)
        alert_source_id = d.pop("alert_source_id")

        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV2.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        alert_route_alert_source_payload_v2 = cls(
            alert_source_id=alert_source_id,
            condition_groups=condition_groups,
        )

        alert_route_alert_source_payload_v2.additional_properties = d
        return alert_route_alert_source_payload_v2

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
