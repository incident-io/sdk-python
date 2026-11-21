from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APIKeysRotatePayloadV1")


@_attrs_define(kw_only=True)
class APIKeysRotatePayloadV1:
    """
    Example:
        {'expires_at': '2022-08-17T13:28:57.801578Z', 'grace_period_minutes': 30}

    Attributes:
        grace_period_minutes (int): How many minutes to keep the old access token alive. Default: 30. Example: 30.
        expires_at (datetime.datetime | Unset): A new expiry for the API key. Leave it blank to keep its current expiry.
            It must be in the future and within your organization's maximum lifetime for API keys. Example:
            2022-08-17T13:28:57.801578Z.
    """

    grace_period_minutes: int = 30
    expires_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grace_period_minutes = self.grace_period_minutes

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grace_period_minutes": grace_period_minutes,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        grace_period_minutes = d.pop("grace_period_minutes")

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        api_keys_rotate_payload_v1 = cls(
            grace_period_minutes=grace_period_minutes,
            expires_at=expires_at,
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
