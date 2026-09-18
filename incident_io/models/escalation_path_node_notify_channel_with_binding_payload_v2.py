from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_node_notify_channel_with_binding_payload_v2_time_to_ack_interval_condition import (
    EscalationPathNodeNotifyChannelWithBindingPayloadV2TimeToAckIntervalCondition,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_path_target_with_binding_payload_v2 import (
        EscalationPathTargetWithBindingPayloadV2,
    )


T = TypeVar("T", bound="EscalationPathNodeNotifyChannelWithBindingPayloadV2")


@_attrs_define
class EscalationPathNodeNotifyChannelWithBindingPayloadV2:
    """
    Example:
        {'targets': [{'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode':
            'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        targets (list[EscalationPathTargetWithBindingPayloadV2]): The channels to notify, each concrete or a parameter
            binding. Example: [{'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule',
            'urgency': 'high'}].
        time_to_ack_interval_condition (EscalationPathNodeNotifyChannelWithBindingPayloadV2TimeToAckIntervalCondition |
            Unset): If the time to ack is relative to a time window, this defines whether we move when the window is active
            or inactive Example: active.
        time_to_ack_seconds (int | Unset): How long should we wait for this level to acknowledge before moving on to the
            next node in the path? Example: 1800.
        time_to_ack_weekday_interval_config_id (str | Unset): If the time to ack is relative to a time window, this
            identifies which window it is relative to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    targets: list[EscalationPathTargetWithBindingPayloadV2]
    time_to_ack_interval_condition: (
        EscalationPathNodeNotifyChannelWithBindingPayloadV2TimeToAckIntervalCondition
        | Unset
    ) = UNSET
    time_to_ack_seconds: int | Unset = UNSET
    time_to_ack_weekday_interval_config_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        time_to_ack_interval_condition: str | Unset = UNSET
        if not isinstance(self.time_to_ack_interval_condition, Unset):
            time_to_ack_interval_condition = self.time_to_ack_interval_condition.value

        time_to_ack_seconds = self.time_to_ack_seconds

        time_to_ack_weekday_interval_config_id = (
            self.time_to_ack_weekday_interval_config_id
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targets": targets,
            }
        )
        if time_to_ack_interval_condition is not UNSET:
            field_dict["time_to_ack_interval_condition"] = (
                time_to_ack_interval_condition
            )
        if time_to_ack_seconds is not UNSET:
            field_dict["time_to_ack_seconds"] = time_to_ack_seconds
        if time_to_ack_weekday_interval_config_id is not UNSET:
            field_dict["time_to_ack_weekday_interval_config_id"] = (
                time_to_ack_weekday_interval_config_id
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.escalation_path_target_with_binding_payload_v2 import (
            EscalationPathTargetWithBindingPayloadV2,
        )

        d = dict(src_dict)
        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = EscalationPathTargetWithBindingPayloadV2.from_dict(
                targets_item_data
            )

            targets.append(targets_item)

        _time_to_ack_interval_condition = d.pop("time_to_ack_interval_condition", UNSET)
        time_to_ack_interval_condition: (
            EscalationPathNodeNotifyChannelWithBindingPayloadV2TimeToAckIntervalCondition
            | Unset
        )
        if isinstance(_time_to_ack_interval_condition, Unset):
            time_to_ack_interval_condition = UNSET
        else:
            time_to_ack_interval_condition = EscalationPathNodeNotifyChannelWithBindingPayloadV2TimeToAckIntervalCondition(
                _time_to_ack_interval_condition
            )

        time_to_ack_seconds = d.pop("time_to_ack_seconds", UNSET)

        time_to_ack_weekday_interval_config_id = d.pop(
            "time_to_ack_weekday_interval_config_id", UNSET
        )

        escalation_path_node_notify_channel_with_binding_payload_v2 = cls(
            targets=targets,
            time_to_ack_interval_condition=time_to_ack_interval_condition,
            time_to_ack_seconds=time_to_ack_seconds,
            time_to_ack_weekday_interval_config_id=time_to_ack_weekday_interval_config_id,
        )

        escalation_path_node_notify_channel_with_binding_payload_v2.additional_properties = d
        return escalation_path_node_notify_channel_with_binding_payload_v2

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
