from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_route_when_alert_joins_group_v3_mode import (
    AlertRouteWhenAlertJoinsGroupV3Mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertRouteWhenAlertJoinsGroupV3")


@_attrs_define(kw_only=True)
class AlertRouteWhenAlertJoinsGroupV3:
    """
    Example:
        {'grace_period_seconds': 60, 'mode': 'on_each_new_alert'}

    Attributes:
        mode (AlertRouteWhenAlertJoinsGroupV3Mode): When a subsequent alert joins an existing group, when should we
            escalate again? Example: on_each_new_alert.
        grace_period_seconds (int | Unset): How long to wait before escalating once an alert joins the group, in
            seconds. Only applies when mode is 'on_each_new_alert'. Example: 60.
    """

    mode: AlertRouteWhenAlertJoinsGroupV3Mode
    grace_period_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        grace_period_seconds = self.grace_period_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if grace_period_seconds is not UNSET:
            field_dict["grace_period_seconds"] = grace_period_seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = AlertRouteWhenAlertJoinsGroupV3Mode(d.pop("mode"))

        grace_period_seconds = d.pop("grace_period_seconds", UNSET)

        alert_route_when_alert_joins_group_v3 = cls(
            mode=mode,
            grace_period_seconds=grace_period_seconds,
        )

        alert_route_when_alert_joins_group_v3.additional_properties = d
        return alert_route_when_alert_joins_group_v3

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
