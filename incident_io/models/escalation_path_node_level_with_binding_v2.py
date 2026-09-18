from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_node_level_with_binding_v2_ack_mode import (
    EscalationPathNodeLevelWithBindingV2AckMode,
)
from ..models.escalation_path_node_level_with_binding_v2_time_to_ack_interval_condition import (
    EscalationPathNodeLevelWithBindingV2TimeToAckIntervalCondition,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_path_retry_config_v2 import EscalationPathRetryConfigV2
    from ..models.escalation_path_round_robin_config_v2 import (
        EscalationPathRoundRobinConfigV2,
    )
    from ..models.escalation_path_target_with_binding_v2 import (
        EscalationPathTargetWithBindingV2,
    )


T = TypeVar("T", bound="EscalationPathNodeLevelWithBindingV2")


@_attrs_define
class EscalationPathNodeLevelWithBindingV2:
    """
    Example:
        {'ack_mode': 'all', 'retry_config': {'attempts': 3, 'interval_seconds': 300}, 'round_robin_config': {'enabled':
            False, 'rotate_after_seconds': 120}, 'targets': [{'binding': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode':
            'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        targets (list[EscalationPathTargetWithBindingV2]): The targets (users or schedules), each concrete or a
            parameter binding. Example: [{'binding': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}].
        ack_mode (EscalationPathNodeLevelWithBindingV2AckMode | Unset): Controls the behaviour of acknowledgements for
            this level, with 'first' cancelling all other escalations on the same level when someone acks Example: all.
        retry_config (EscalationPathRetryConfigV2 | Unset):  Example: {'attempts': 3, 'interval_seconds': 300}.
        round_robin_config (EscalationPathRoundRobinConfigV2 | Unset):  Example: {'enabled': False,
            'rotate_after_seconds': 120}.
        time_to_ack_interval_condition (EscalationPathNodeLevelWithBindingV2TimeToAckIntervalCondition | Unset): If the
            time to ack is relative to a time window, this defines whether we move when the window is active or inactive
            Example: active.
        time_to_ack_seconds (int | Unset): How long should we wait for this level to acknowledge before proceeding to
            the next node in the path? Example: 1800.
        time_to_ack_weekday_interval_config_id (str | Unset): If the time to ack is relative to a time window, this
            identifies which window it is relative to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    targets: list[EscalationPathTargetWithBindingV2]
    ack_mode: EscalationPathNodeLevelWithBindingV2AckMode | Unset = UNSET
    retry_config: EscalationPathRetryConfigV2 | Unset = UNSET
    round_robin_config: EscalationPathRoundRobinConfigV2 | Unset = UNSET
    time_to_ack_interval_condition: (
        EscalationPathNodeLevelWithBindingV2TimeToAckIntervalCondition | Unset
    ) = UNSET
    time_to_ack_seconds: int | Unset = UNSET
    time_to_ack_weekday_interval_config_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        ack_mode: str | Unset = UNSET
        if not isinstance(self.ack_mode, Unset):
            ack_mode = self.ack_mode.value

        retry_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_config, Unset):
            retry_config = self.retry_config.to_dict()

        round_robin_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.round_robin_config, Unset):
            round_robin_config = self.round_robin_config.to_dict()

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
        if ack_mode is not UNSET:
            field_dict["ack_mode"] = ack_mode
        if retry_config is not UNSET:
            field_dict["retry_config"] = retry_config
        if round_robin_config is not UNSET:
            field_dict["round_robin_config"] = round_robin_config
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
        from ..models.escalation_path_retry_config_v2 import (
            EscalationPathRetryConfigV2,
        )
        from ..models.escalation_path_round_robin_config_v2 import (
            EscalationPathRoundRobinConfigV2,
        )
        from ..models.escalation_path_target_with_binding_v2 import (
            EscalationPathTargetWithBindingV2,
        )

        d = dict(src_dict)
        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = EscalationPathTargetWithBindingV2.from_dict(
                targets_item_data
            )

            targets.append(targets_item)

        _ack_mode = d.pop("ack_mode", UNSET)
        ack_mode: EscalationPathNodeLevelWithBindingV2AckMode | Unset
        if isinstance(_ack_mode, Unset):
            ack_mode = UNSET
        else:
            ack_mode = EscalationPathNodeLevelWithBindingV2AckMode(_ack_mode)

        _retry_config = d.pop("retry_config", UNSET)
        retry_config: EscalationPathRetryConfigV2 | Unset
        if isinstance(_retry_config, Unset):
            retry_config = UNSET
        else:
            retry_config = EscalationPathRetryConfigV2.from_dict(_retry_config)

        _round_robin_config = d.pop("round_robin_config", UNSET)
        round_robin_config: EscalationPathRoundRobinConfigV2 | Unset
        if isinstance(_round_robin_config, Unset):
            round_robin_config = UNSET
        else:
            round_robin_config = EscalationPathRoundRobinConfigV2.from_dict(
                _round_robin_config
            )

        _time_to_ack_interval_condition = d.pop("time_to_ack_interval_condition", UNSET)
        time_to_ack_interval_condition: (
            EscalationPathNodeLevelWithBindingV2TimeToAckIntervalCondition | Unset
        )
        if isinstance(_time_to_ack_interval_condition, Unset):
            time_to_ack_interval_condition = UNSET
        else:
            time_to_ack_interval_condition = (
                EscalationPathNodeLevelWithBindingV2TimeToAckIntervalCondition(
                    _time_to_ack_interval_condition
                )
            )

        time_to_ack_seconds = d.pop("time_to_ack_seconds", UNSET)

        time_to_ack_weekday_interval_config_id = d.pop(
            "time_to_ack_weekday_interval_config_id", UNSET
        )

        escalation_path_node_level_with_binding_v2 = cls(
            targets=targets,
            ack_mode=ack_mode,
            retry_config=retry_config,
            round_robin_config=round_robin_config,
            time_to_ack_interval_condition=time_to_ack_interval_condition,
            time_to_ack_seconds=time_to_ack_seconds,
            time_to_ack_weekday_interval_config_id=time_to_ack_weekday_interval_config_id,
        )

        escalation_path_node_level_with_binding_v2.additional_properties = d
        return escalation_path_node_level_with_binding_v2

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
