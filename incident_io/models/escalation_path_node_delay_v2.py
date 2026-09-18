from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_node_delay_v2_delay_interval_condition import (
    EscalationPathNodeDelayV2DelayIntervalCondition,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationPathNodeDelayV2")


@_attrs_define
class EscalationPathNodeDelayV2:
    """
    Example:
        {'delay_interval_condition': 'active', 'delay_seconds': 300, 'delay_weekday_interval_config_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        delay_interval_condition (EscalationPathNodeDelayV2DelayIntervalCondition | Unset): If the delay is relative to
            a time window, this defines whether we advance when the window is active or inactive Example: active.
        delay_seconds (int | Unset): How long to delay before advancing to the next node in the path, in seconds
            Example: 300.
        delay_weekday_interval_config_id (str | Unset): If the delay is relative to a time window, this identifies which
            window it is relative to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    delay_interval_condition: (
        EscalationPathNodeDelayV2DelayIntervalCondition | Unset
    ) = UNSET
    delay_seconds: int | Unset = UNSET
    delay_weekday_interval_config_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_interval_condition: str | Unset = UNSET
        if not isinstance(self.delay_interval_condition, Unset):
            delay_interval_condition = self.delay_interval_condition.value

        delay_seconds = self.delay_seconds

        delay_weekday_interval_config_id = self.delay_weekday_interval_config_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delay_interval_condition is not UNSET:
            field_dict["delay_interval_condition"] = delay_interval_condition
        if delay_seconds is not UNSET:
            field_dict["delay_seconds"] = delay_seconds
        if delay_weekday_interval_config_id is not UNSET:
            field_dict["delay_weekday_interval_config_id"] = (
                delay_weekday_interval_config_id
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _delay_interval_condition = d.pop("delay_interval_condition", UNSET)
        delay_interval_condition: (
            EscalationPathNodeDelayV2DelayIntervalCondition | Unset
        )
        if isinstance(_delay_interval_condition, Unset):
            delay_interval_condition = UNSET
        else:
            delay_interval_condition = EscalationPathNodeDelayV2DelayIntervalCondition(
                _delay_interval_condition
            )

        delay_seconds = d.pop("delay_seconds", UNSET)

        delay_weekday_interval_config_id = d.pop(
            "delay_weekday_interval_config_id", UNSET
        )

        escalation_path_node_delay_v2 = cls(
            delay_interval_condition=delay_interval_condition,
            delay_seconds=delay_seconds,
            delay_weekday_interval_config_id=delay_weekday_interval_config_id,
        )

        escalation_path_node_delay_v2.additional_properties = d
        return escalation_path_node_delay_v2

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
