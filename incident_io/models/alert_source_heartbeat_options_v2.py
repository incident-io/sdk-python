from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertSourceHeartbeatOptionsV2")


@_attrs_define
class AlertSourceHeartbeatOptionsV2:
    """
    Example:
        {'failure_threshold': 1, 'grace_period_seconds': 0, 'interval_seconds': 60, 'ping_url':
            'https://api.incident.io/v2/heartbeat/01GW2G3V0S59R238FAHPDS1R66/ping'}

    Attributes:
        failure_threshold (int): Number of consecutive missed pings before an alert fires. Example: 1.
        grace_period_seconds (int): How long after a missed ping before the heartbeat is considered late, in seconds. If
            zero, it transitions directly to failing. Example: 0.
        interval_seconds (int): How often a ping is expected, in seconds. Example: 60.
        ping_url (str): The URL to POST to in order to send a heartbeat ping. Example:
            https://api.incident.io/v2/heartbeat/01GW2G3V0S59R238FAHPDS1R66/ping.
    """

    failure_threshold: int
    grace_period_seconds: int
    interval_seconds: int
    ping_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failure_threshold = self.failure_threshold

        grace_period_seconds = self.grace_period_seconds

        interval_seconds = self.interval_seconds

        ping_url = self.ping_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "failure_threshold": failure_threshold,
                "grace_period_seconds": grace_period_seconds,
                "interval_seconds": interval_seconds,
                "ping_url": ping_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        failure_threshold = d.pop("failure_threshold")

        grace_period_seconds = d.pop("grace_period_seconds")

        interval_seconds = d.pop("interval_seconds")

        ping_url = d.pop("ping_url")

        alert_source_heartbeat_options_v2 = cls(
            failure_threshold=failure_threshold,
            grace_period_seconds=grace_period_seconds,
            interval_seconds=interval_seconds,
            ping_url=ping_url,
        )

        alert_source_heartbeat_options_v2.additional_properties = d
        return alert_source_heartbeat_options_v2

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
