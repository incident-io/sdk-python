from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EscalationPathRetryConfigV2")


@_attrs_define
class EscalationPathRetryConfigV2:
    """
    Example:
        {'attempts': 3, 'interval_seconds': 300}

    Attributes:
        attempts (int): The total number of times we page this level, counting the initial page. For example, 3 means
            three notifications in total. Must be between 2 and 10. Example: 3.
        interval_seconds (int): How long we wait between attempts at this level, in seconds. Must be a whole number of
            minutes (divisible by 60). Example: 300.
    """

    attempts: int
    interval_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        interval_seconds = self.interval_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempts": attempts,
                "interval_seconds": interval_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attempts = d.pop("attempts")

        interval_seconds = d.pop("interval_seconds")

        escalation_path_retry_config_v2 = cls(
            attempts=attempts,
            interval_seconds=interval_seconds,
        )

        escalation_path_retry_config_v2.additional_properties = d
        return escalation_path_retry_config_v2

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
