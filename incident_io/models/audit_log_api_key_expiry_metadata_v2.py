from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogAPIKeyExpiryMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogAPIKeyExpiryMetadataV2:
    """
    Example:
        {'expires_at': '2022-08-17T13:28:57Z'}

    Attributes:
        expires_at (str | Unset): When the key stops working. Absent when the key never expires. Example:
            2022-08-17T13:28:57Z.
    """

    expires_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        expires_at = d.pop("expires_at", UNSET)

        audit_log_api_key_expiry_metadata_v2 = cls(
            expires_at=expires_at,
        )

        audit_log_api_key_expiry_metadata_v2.additional_properties = d
        return audit_log_api_key_expiry_metadata_v2

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
