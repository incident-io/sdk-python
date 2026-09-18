from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertSourceHeartbeatOptionsPayloadV2")


@_attrs_define
class AlertSourceHeartbeatOptionsPayloadV2:
    """
    Example:
        {'failure_threshold': 1, 'grace_period_seconds': 0, 'interval_seconds': 60}

    Attributes:
        interval_seconds (int): How often a ping is expected, in seconds. Example: 60.
        failure_threshold (int | Unset): Number of consecutive missed pings before an alert fires. Default: 1. Example:
            1.
        grace_period_seconds (int | Unset): How long after a missed ping before the heartbeat is considered late, in
            seconds. If zero, it transitions directly to failing. Default: 0. Example: 0.
    """

    interval_seconds: int
    failure_threshold: int | Unset = 1
    grace_period_seconds: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval_seconds = self.interval_seconds

        failure_threshold = self.failure_threshold

        grace_period_seconds = self.grace_period_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interval_seconds": interval_seconds,
            }
        )
        if failure_threshold is not UNSET:
            field_dict["failure_threshold"] = failure_threshold
        if grace_period_seconds is not UNSET:
            field_dict["grace_period_seconds"] = grace_period_seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        interval_seconds = d.pop("interval_seconds")

        failure_threshold = d.pop("failure_threshold", UNSET)

        grace_period_seconds = d.pop("grace_period_seconds", UNSET)

        alert_source_heartbeat_options_payload_v2 = cls(
            interval_seconds=interval_seconds,
            failure_threshold=failure_threshold,
            grace_period_seconds=grace_period_seconds,
        )

        alert_source_heartbeat_options_payload_v2.additional_properties = d
        return alert_source_heartbeat_options_payload_v2

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
