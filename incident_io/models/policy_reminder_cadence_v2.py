from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_reminder_cadence_v2_interval import PolicyReminderCadenceV2Interval

T = TypeVar("T", bound="PolicyReminderCadenceV2")


@_attrs_define(kw_only=True)
class PolicyReminderCadenceV2:
    """A recurring reminder, which repeats once per interval until the finding is resolved.

    Example:
        {'interval': 'daily'}

    Attributes:
        interval (PolicyReminderCadenceV2Interval): How often to send the reminder, stepping in fixed durations from the
            due date. Example: daily.
    """

    interval: PolicyReminderCadenceV2Interval
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval = self.interval.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interval": interval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        interval = PolicyReminderCadenceV2Interval(d.pop("interval"))

        policy_reminder_cadence_v2 = cls(
            interval=interval,
        )

        policy_reminder_cadence_v2.additional_properties = d
        return policy_reminder_cadence_v2

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
