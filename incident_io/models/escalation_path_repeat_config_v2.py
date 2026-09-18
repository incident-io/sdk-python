from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EscalationPathRepeatConfigV2")


@_attrs_define
class EscalationPathRepeatConfigV2:
    """
    Example:
        {'delay_repeat_on_activity': False, 'repeat_after_seconds': 1800}

    Attributes:
        delay_repeat_on_activity (bool): When true, incident activity resets the repeat timer. Default: False. Example:
            False.
        repeat_after_seconds (int): Number of seconds we'll wait before repeating an escalation. Example: 1800.
    """

    repeat_after_seconds: int
    delay_repeat_on_activity: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_repeat_on_activity = self.delay_repeat_on_activity

        repeat_after_seconds = self.repeat_after_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delay_repeat_on_activity": delay_repeat_on_activity,
                "repeat_after_seconds": repeat_after_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        delay_repeat_on_activity = d.pop("delay_repeat_on_activity")

        repeat_after_seconds = d.pop("repeat_after_seconds")

        escalation_path_repeat_config_v2 = cls(
            delay_repeat_on_activity=delay_repeat_on_activity,
            repeat_after_seconds=repeat_after_seconds,
        )

        escalation_path_repeat_config_v2.additional_properties = d
        return escalation_path_repeat_config_v2

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
