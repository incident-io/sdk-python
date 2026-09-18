from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="APIKeysRotatePayloadV1")


@_attrs_define
class APIKeysRotatePayloadV1:
    """
    Example:
        {'grace_period_minutes': 30}

    Attributes:
        grace_period_minutes (int): How many minutes to keep the old access token alive. Default: 30. Example: 30.
    """

    grace_period_minutes: int = 30
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grace_period_minutes = self.grace_period_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grace_period_minutes": grace_period_minutes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        grace_period_minutes = d.pop("grace_period_minutes")

        api_keys_rotate_payload_v1 = cls(
            grace_period_minutes=grace_period_minutes,
        )

        api_keys_rotate_payload_v1.additional_properties = d
        return api_keys_rotate_payload_v1

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
