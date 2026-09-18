from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationPathRoundRobinConfigV2")


@_attrs_define
class EscalationPathRoundRobinConfigV2:
    """
    Example:
        {'enabled': False, 'rotate_after_seconds': 120}

    Attributes:
        enabled (bool): Whether round robin is enabled for this level Example: False.
        rotate_after_seconds (int | Unset): How long should we wait before rotating to the next target in a round robin,
            if not set will stick with a single target per level. Example: 120.
    """

    enabled: bool
    rotate_after_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        rotate_after_seconds = self.rotate_after_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if rotate_after_seconds is not UNSET:
            field_dict["rotate_after_seconds"] = rotate_after_seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        rotate_after_seconds = d.pop("rotate_after_seconds", UNSET)

        escalation_path_round_robin_config_v2 = cls(
            enabled=enabled,
            rotate_after_seconds=rotate_after_seconds,
        )

        escalation_path_round_robin_config_v2.additional_properties = d
        return escalation_path_round_robin_config_v2

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
